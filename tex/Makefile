####
#  Makefile

TARGET    = Fundamentals
TEXMACS   = macros.tex
TOP       = ..

TEXFILE  = $(TARGET).tex
PDFFILE  = $(TARGET).pdf
BBLFILE  = $(TARGET).bbl
AUXFILE  = $(TARGET).aux

PDFLATEX = pdflatex
BIBTEX   = bibtex

.PHONY: !  pdf clean bib

pdf:
	$(PDFLATEX) $(TEXFILE)

bib:
	$(BIBTEX) $(TARGET)

clean:
	rm -f *.aux *.log *.toc *.blg *.out $(PDFFILE)

