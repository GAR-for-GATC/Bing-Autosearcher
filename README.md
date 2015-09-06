# Bing-Autosearch

This script will search Bing using text from the book 1984.  The program is only tested with Windows 7 and when 
it's used, you need to update the path variables in each of the code sections that you use as well as the 
Windows path environment variable.

The code in "pdf_cut_and_paste.py" and "PDF_string_parser.py" can be used to take the unique words from a PDF 
file and parse them in such a way that it can be used in C++ code as a string.  The Bing_autosearch script is 
used to run the Bing search C++ script that can be compiled from the Bing_search.cpp file.  

This code has gone through several revisions since its inception:

Version 1 used a small word bank containing around 15 words.

Version 2 used a large word bank generated from the PDF file 1984.

Version 2.1 fixed the C++ random number generator in order to generate more random numbers.

Only version 2.1 is included on the GitHub.  This code was made some time in late 2014 - early 2015.

