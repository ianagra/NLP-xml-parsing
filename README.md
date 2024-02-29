[![author](https://img.shields.io/badge/author-ianagra-red.svg)](https://github.com/ianagra) [![](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/release/python-3118/) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

# XML parsing

This was my first assignment for my Master's degree in AI, as part of a Natural Language Processing course.

Many of the documents we encounter today are of the XML type. In this short and simple project, I used two XML parsers for Python, DOM and SAX, in order to compare their use and the results obtained.

The database used was The Cystic Fibrosis Database (CF)*, available [here](https://people.ischool.berkeley.edu/~hearst/irbook/cfc.html). 

The names of all the authors were extracted from one of the database files using the DOM processor, saving them one by one in the `authors.xml` file. The SAX processor was used to do the same with the article titles, saving them in the `titles.xml` file. The database and results files are not in the repository.

*Shaw, W.M. & Wood, J.B. & Wood, R.E. & Tibbo, H.R. The Cystic Fibrosis Database: Content and Research Opportunities. LISR 13, pp. 347-366, 1991.
