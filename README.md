# Greenhouse Report

## Installation

## Linux 

Clone the repository and install latex packages:

```bash
https://github.com/srad/Greenhouse-Report.git
sudo apt install texlive-full
chmod +x compile.sh
sudo chown -R <your-user> .
```

## Windows

On windows you should be able to just use your favourite Latex environment.

## Configuration

You must rename all `authors.tex.default` to `authors.tex` and define the author name in the file (or leave the default).

## Build the document

```bash
./compile.sh
```

or just compile `main.tex` in your IDE on Windows.

This will generate the final document `main.pdf`.
