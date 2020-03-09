# Greenhouse Report

[![Build Status](http://sedrad.com:8080/buildStatus/icon?job=Greenhouse-Report)](http://sedrad.com:8080/job/Greenhouse-Report/)

## Compiling the document

First install the required latex packages:

```bash
sudo apt install texlive-base texlive-bibtex-extra texlive-latex-extra -y
```
Then clone the repository:

```bash
git clone https://github.com/srad/Greenhouse-Report.git
cd Greenhouse-Report
```
The authors are not checked in for privacy reasons, but are stored in `authors.tex` locally.

You must rename all `authors.tex.default` to `authors.tex` and define the author name in the file (or leave the default).

To get quickly running just rename the default files:

```bash
cp authors.tex.default authors.tex
cp members/cm/authors.tex.default members/cm/authors.tex
cp members/kh/authors.tex.default members/kh/authors.tex
cp members/nh/authors.tex.default members/nh/authors.tex
cp members/paz/authors.tex.default members/paz/authors.tex
cp members/ssr/authors.tex.default members/ssr/authors.tex
cp members/tf/authors.tex.default members/tf/authors.tex
```

Then compile the document:

```bash
chmod +x compile.sh
./compile.sh
```

On windows you should be able to just use your favourite Latex environment, just compile `main.tex` in your IDE on Windows.

Both will generate the final document `main.pdf`.

## Include Graphics and Code

### Images / Graphics

Since at the top of every member directory `\graphicspath{{members/<name>/figures/}}` is set,
you can just put your graphics in each folder's `figures` folder and include them via `\includegraphics{filename.ext}`.

### Code

Including code requires to define the whole path, i.e.:

```latex
\lstinputlisting[language=Python, linerange={12-14}, frame=single, caption = Given a folder \textit{directory\_im} containing obj files a specific number of plants are randomly selected ]{members/cm/import_plants.py}\vspace{5pt}
```
