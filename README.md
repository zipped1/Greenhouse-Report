# Greenhouse Report

## Installation

### Linux 

Clone the repository and install latex packages:

```bash
https://github.com/srad/Greenhouse-Report.git
sudo apt install texlive-full
chmod +x compile.sh
sudo chown -R <your-user> .
```

### Windows

On windows you should be able to just use your favourite Latex environment.

## Configuration

You must rename all `authors.tex.default` to `authors.tex` and define the author name in the file (or leave the default).

## Build the document

```bash
./compile.sh
```

or just compile `main.tex` in your IDE on Windows.

This will generate the final document `main.pdf`.

## Include Graphics and Code

### Images / Graphics

Since at the top of every member directory `\graphicspath{{members/<name>/figures/}}` is set,
you can just put your graphics in each folder's `figures` folder and include them via `\includegraphics{filename.ext}`.

### Code

Including code requires the define the whole path, i.e.:

```latex
\lstinputlisting[language=Python, linerange={12-14}, frame=single, caption = Given a folder \textit{directory\_im} containing obj files a specific number of plants are randomly selected ]{members/cm/import_plants.py}\vspace{5pt}
```