PDF = Mikhailovsky_Ilya_ML_NLP_CV_RU.pdf

$(PDF): src/cv.tex
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(basename $(PDF)) src/cv.tex
	@rm -f *.aux *.log *.out

clean:
	rm -f *.aux *.log *.out $(PDF)

.PHONY: clean
