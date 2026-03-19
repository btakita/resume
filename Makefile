PROFILE ?= default
MD = BrianTakita.md
CSS = resume.css

ifeq ($(PROFILE),default)
  PDF = BrianTakita.pdf
else
  PDF = BrianTakita-$(PROFILE).pdf
endif

$(PDF): $(MD) $(CSS) profiles/$(PROFILE).toml build.py
	python3 build.py --profile $(PROFILE) --output $(PDF)

.PHONY: test clean
test:
	mise exec -- pytest tests/ -v

clean:
	rm -f BrianTakita*.pdf /tmp/resume.html
