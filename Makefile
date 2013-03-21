PDF=aide_scilab.pdf

all: $(PDF)

%.pdf : %.tex
	xelatex $<
clean:
	rm -rf *.log
	rm -rf *.aux

mrproper: clean
	rm -rf $(EXEC)
