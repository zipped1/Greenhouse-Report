build: clean
	pdflatex main.tex
	biber main
	pdflatex main.tex
	
view: build
	xdg-open main.pdf

install:
	sudo apt install texlive-base texlive-bibtex-extra texlive-latex-extra biber -y

setup:
	cp authors.tex.default authors.tex
	cp members/cm/authors.tex.default members/cm/authors.tex
	cp members/kh/authors.tex.default members/kh/authors.tex
	cp members/nh/authors.tex.default members/nh/authors.tex
	cp members/paz/authors.tex.default members/paz/authors.tex
	cp members/ssr/authors.tex.default members/ssr/authors.tex
	cp members/tf/authors.tex.default members/tf/authors.tex

clean:
	find . -name "*.aux" -type f -delete
	rm *.bbl *.blg *.bcf *.toc *.aux *.log main.pdf -f
