# 06682_final_project

## Introduction
This package was created as the final project for course 06682. Its main task is to provide an OpenAlexWorks class that can be used to get 
RIS and BibTeX entries for a given Digital Object Identifier (DOI).

## Purpose

The folder contains a package called:s23openalex

- Installation
  You can install the package via pip: pip install openalex-works
- Usage
  Command Line Interface
- After installing the package, you can use the command line interface (CLI) to get RIS or BibTeX entries for a DOI. To get an RIS entry, run:
  openalexworks get-ris <doi>
  
  To get a BibTeX entry, run:
  openalexworks get-bibtex <doi>
  Replace <doi> with the DOI for which you want to get the entry.


- Testing
  This package includes tests to ensure that it works correctly. You can run the tests with:
  python -m unittest discover tests
  Make sure to run this command from the root of the package.

- Code Quality
  The code in this package has been formatted and checked for quality using black and pylint. You should ensure that your repo passes both of these before submitting a pull request.

- License
  This package is licensed under the MIT License. See the LICENSE file for more information.

