################################################################
##
##  This code takes the unique words in a PDF file and outputs
## it into a pickle file for later use.  In this case it's
## parsed into a usable format by the "pickle open.py" script.
##
################################################################

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import pickle

import re

#This function was cut and pasted from stackexchange
## http://stackoverflow.com/questions/26748788/extraction-of-text-from-pdf-with-pdfminer-gives-multiple-copies
def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,password=password,caching=caching, check_extractable=True):

        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text


a = convert_pdf_to_txt("E://Users//Purple//Desktop//Bing_Rewards_autosearcher//PDF_stuff//1984.pdf")
## Remove everything except letters and spaces
b = re.sub(r'[^(\s)(A-Z)(a-z)]',"",a)
b=b.lower() #change all letters to lowercase
print len(b)

##Change word string to list
counter = 0
list_of_words = []
while len(b)>0:
    #remove whitespace
    b = re.sub(r'^((\s)+)',"",b)
    #take first word from string, and put it into a list    
    chop_string = re.match(r'^([(A-Z)(a-z)]+)',b)
    list_of_words.append(chop_string.group())
    #remove the first word
    b = re.sub(r'^([(A-Z)(a-z)]+)',"",b)
    #remove whitespace
    b = re.sub(r'^((\s)+)',"",b)
    if (counter%1000)==0:
        print counter
    counter=counter+1
    
#remove duplicate items from the list
list_counter = 0
unique_list = []
for i in list_of_words:
    if (counter%1000)==0:
        print "unique  %d"%list_counter
    if i not in unique_list:
        unique_list.append(i)
    list_counter = list_counter+1

print len(unique_list)
print unique_list

purple = open("E://Users//Purple//Desktop//Bing_Rewards_autosearcher//pdf_stuff//large_pdf_pickle.pkl",'wb')
pickle.dump(unique_list, purple,0)
purple.close()
       
        




