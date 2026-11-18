ML  = Mikhailovsky_Ilya_ML_NLP_CV_RU.pdf
ML_DOWNLOAD = Ilya_Mikhailovsky_Resume.pdf
ML_EN = Ilya_Mikhailovskiy_Resume_EN.pdf
ML_EN_LEGACY = Ilya_Mikhailovsky_Resume_EN.pdf
BE  = Mikhailovsky_Ilya_Python_Backend_CV_RU.pdf

all: $(ML_DOWNLOAD) $(ML_EN_LEGACY) $(BE)

$(ML_DOWNLOAD): $(ML)
	cp $< $@

$(ML): src/cv.tex
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(basename $(ML)) src/cv.tex
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(basename $(ML)) src/cv.tex
	@rm -f $(addprefix $(basename $@).,aux log out)

$(ML_EN_LEGACY): $(ML_EN)
	cp $< $@

$(ML_EN): src/cv-en.tex
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(basename $@) $<
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(basename $@) $<
	@rm -f $(addprefix $(basename $@).,aux log out)

$(BE): src/cv-backend.tex
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(basename $(BE)) src/cv-backend.tex
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(basename $(BE)) src/cv-backend.tex
	@rm -f $(addprefix $(basename $@).,aux log out)

clean:
	rm -f *.aux *.log *.out $(ML) $(ML_DOWNLOAD) $(ML_EN) $(ML_EN_LEGACY) $(BE)

.PHONY: all clean
