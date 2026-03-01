PDF = BrianTakita.pdf
MD = BrianTakita.md
CSS = resume.css
HTML_TMP = /tmp/resume.html
BODY_TMP = /tmp/resume-body.html

$(PDF): $(MD) $(CSS)
	pandoc $(MD) -o $(BODY_TMP)
	printf '<!DOCTYPE html>\n<html>\n<head><meta charset="utf-8"></head>\n<body>\n' > $(HTML_TMP)
	cat $(BODY_TMP) >> $(HTML_TMP)
	printf '</body>\n</html>\n' >> $(HTML_TMP)
	weasyprint $(HTML_TMP) $(PDF) --stylesheet $(CSS)
	@rm -f $(BODY_TMP)

.PHONY: clean
clean:
	rm -f $(PDF) $(HTML_TMP)
