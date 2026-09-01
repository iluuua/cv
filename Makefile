ML  = Mikhailovsky_Ilya_ML_NLP_CV_RU.pdf
BE  = Mikhailovsky_Ilya_Python_Backend_CV_RU.pdf

all: $(ML) $(BE)

$(ML): src/cv.tex
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(basename $(ML)) src/cv.tex
	@rm -f *.aux *.log *.out

$(BE): src/cv-backend.tex
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(basename $(BE)) src/cv-backend.tex
	@rm -f *.aux *.log *.out

clean:
	rm -f *.aux *.log *.out $(ML) $(BE)

.PHONY: all clean
