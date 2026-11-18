ML  = Mikhailovsky_Ilya_ML_NLP_CV_RU.pdf
ML_DOWNLOAD = Ilya_Mikhailovsky_Resume.pdf
BE  = Mikhailovsky_Ilya_Python_Backend_CV_RU.pdf
DS  = Mikhailovsky_Ilya_DS_NLP_CV_RU.pdf
OPS = Mikhailovsky_Ilya_DevOps_CV_RU.pdf

all: $(ML_DOWNLOAD) $(BE) $(DS) $(OPS)

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

$(DS): src/cv-nlp.tex
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(basename $(DS)) src/cv-nlp.tex
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(basename $(DS)) src/cv-nlp.tex
	@rm -f *.aux *.log *.out

$(OPS): src/cv-devops.tex
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(basename $(OPS)) src/cv-devops.tex
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(basename $(OPS)) src/cv-devops.tex
	@rm -f *.aux *.log *.out

clean:
	rm -f *.aux *.log *.out $(ML) $(ML_DOWNLOAD) $(BE) $(DS) $(OPS)

.PHONY: all clean
