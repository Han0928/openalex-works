"""
Test module for the Works class in the s23openalex package.
"""

from s23openalex.works import Works


def test_ris_format():
    """
    Test the RIS formatted citation for a Works instance.
    """
    works = Works("https://doi.org/10.1021/acscatal.5b00538")
    expected_ris = (
        "TY  - JOUR\nAU  - John R. Kitchin\nPY  - 2015\nTI  - Examples of "
        "Effective Data Sharing in Scientific Publishing\nJO  - ACS "
        "Catalysis\nVL  - 5\nIS  - 6\nSP  - 3894\nEP  - 3899\nDO  - "
        "10.1021/acscatal.5b00538\nER  -"
    )
    assert works.ris == expected_ris


def test_bibtex_format():
    """
    Test the BibTeX formatted citation for a Works instance.
    """
    works = Works("https://doi.org/10.1021/acscatal.5b00538")
    expected_bibtex = (
        "@article{https://doi.org/10.1021/acscatal.5b00538,\n  author = {John "
        "R. Kitchin},\n  title = {Examples of Effective Data Sharing in "
        "Scientific Publishing},\n  journal = {ACS Catalysis},\n  "
        "volume = {5},\n  number = {6},\n  pages = {3894-3899},\n  "
        "year = {2015},\n  doi = {10.1021/acscatal.5b00538},\n}"
    )
    assert works.bibtex_entry == expected_bibtex
