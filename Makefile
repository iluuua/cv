ML  = Mikhailovsky_Ilya_ML_NLP_CV_RU.pdf
ML_DOWNLOAD = Ilya_Mikhailovsky_Resume.pdf
BE  = Mikhailovsky_Ilya_Python_Backend_CV_RU.pdf

all: $(ML_DOWNLOAD) $(BE)

$(ML_DOWNLOAD): $(ML)
	cp $< $@

$(ML): src/cv.tex
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(basename $(ML)) src/cv.tex
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(basename $(ML)) src/cv.tex
	@rm -f *.aux *.log *.out

$(BE): src/cv-backend.tex
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(basename $(BE)) src/cv-backend.tex
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(basename $(BE)) src/cv-backend.tex
	@rm -f *.aux *.log *.out

clean:
	rm -f *.aux *.log *.out $(ML) $(ML_DOWNLOAD) $(BE)

.PHONY: all clean
