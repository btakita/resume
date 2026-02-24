.PHONY: pdf clean

PDF = BrianTakita.pdf
MD = BrianTakita.md
CSS = resume.css
HTML_TMP = /tmp/resume.html

pdf: $(PDF)

$(PDF): $(MD) $(CSS)
	pandoc $(MD) -o $(HTML_TMP) --standalone --metadata title="Brian Takita"
	weasyprint $(HTML_TMP) $(PDF) --stylesheet $(CSS)
	@rm -f $(HTML_TMP)

clean:
	rm -f $(PDF) $(HTML_TMP)