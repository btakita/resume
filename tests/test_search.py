"""Test suite for resume search page using LightPanda and a local HTTP server."""

import json
import subprocess
import threading
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

import pytest

RESUME_DIR = Path(__file__).parent.parent
PORT = 18923  # High port to avoid conflicts


class QuietHandler(SimpleHTTPRequestHandler):
    """HTTP handler that suppresses request logging."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(RESUME_DIR), **kwargs)

    def log_message(self, format, *args):
        pass  # Suppress output


@pytest.fixture(scope="module")
def http_server():
    """Start a local HTTP server serving the resume directory."""
    server = HTTPServer(("127.0.0.1", PORT), QuietHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    # Wait for server to be ready
    for _ in range(20):
        try:
            subprocess.run(
                ["curl", "-s", "-o", "/dev/null", f"http://127.0.0.1:{PORT}/search.html"],
                check=True,
                timeout=2,
            )
            break
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            time.sleep(0.1)
    yield f"http://127.0.0.1:{PORT}"
    server.shutdown()


@pytest.fixture(scope="module")
def search_index():
    """Load and return the search-index.json data."""
    index_path = RESUME_DIR / "search-index.json"
    assert index_path.exists(), "search-index.json not found — run: agent-resume search-index -d data.toml > search-index.json"
    with open(index_path) as f:
        return json.load(f)


def lightpanda_fetch(url: str) -> str:
    """Fetch a URL via LightPanda and return the rendered HTML."""
    result = subprocess.run(
        ["lightpanda", "fetch", "--dump", "html", url],
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0, f"LightPanda failed: {result.stderr}"
    return result.stdout


class TestSearchIndex:
    """Tests for search-index.json validity."""

    def test_index_has_experiences(self, search_index):
        assert "experiences" in search_index
        assert len(search_index["experiences"]) > 0

    def test_experience_schema(self, search_index):
        required_fields = {"company", "title", "start", "tags", "accomplishments"}
        for exp in search_index["experiences"]:
            missing = required_fields - set(exp.keys())
            assert not missing, f"{exp.get('company', '?')}: missing fields {missing}"

    def test_accomplishments_have_text(self, search_index):
        for exp in search_index["experiences"]:
            for acc in exp["accomplishments"]:
                assert "text" in acc, f"{exp['company']}: accomplishment missing 'text'"

    def test_no_empty_tags(self, search_index):
        for exp in search_index["experiences"]:
            assert all(t.strip() for t in exp["tags"]), f"{exp['company']}: empty tag found"

    def test_valid_json_no_cargo_output(self):
        """Ensure search-index.json is clean JSON (no cargo build output)."""
        index_path = RESUME_DIR / "search-index.json"
        content = index_path.read_text()
        assert content.lstrip().startswith("{"), "search-index.json has non-JSON prefix (cargo output?)"


class TestSearchPage:
    """Tests for search.html rendering via LightPanda."""

    def test_page_loads(self, http_server):
        html = lightpanda_fetch(f"{http_server}/search.html")
        assert "Brian Takita" in html

    def test_experiences_rendered(self, http_server, search_index):
        html = lightpanda_fetch(f"{http_server}/search.html")
        # All experiences should appear in the rendered DOM
        for exp in search_index["experiences"]:
            assert exp["company"] in html, f"Experience '{exp['company']}' not found in rendered page"

    def test_search_input_exists(self, http_server):
        html = lightpanda_fetch(f"{http_server}/search.html")
        assert 'id="search"' in html

    def test_tags_rendered(self, http_server):
        html = lightpanda_fetch(f"{http_server}/search.html")
        assert 'class="tag"' in html or "data-tag=" in html

    def test_results_count_shown(self, http_server, search_index):
        html = lightpanda_fetch(f"{http_server}/search.html")
        expected_count = len(search_index["experiences"])
        assert f"{expected_count} of {expected_count}" in html

    def test_pdf_link_present(self, http_server):
        html = lightpanda_fetch(f"{http_server}/search.html")
        assert "BrianTakita.pdf" in html

    def test_linkedin_link_present(self, http_server):
        html = lightpanda_fetch(f"{http_server}/search.html")
        assert "linkedin.com/in/briantakita" in html
