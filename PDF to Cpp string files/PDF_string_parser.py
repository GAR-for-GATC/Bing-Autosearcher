################################################################
##
##  This code prints the data stored in the pickle storage unit 
## and outputs it in a way that can be cut and pasted into a C++
## file.
##
################################################################
import pickle
import re
purple = open("E://Users//Purple//Desktop//Bing_Rewards_autosearcher//pdf_stuff//large_pdf_pickle.pkl",'rb')
b = pickle.load(purple)
print len(b)

#Change extracted list to a string
new_string = ""
for i in b:
    new_string = new_string + "\""
    new_string = new_string + i
    new_string = new_string + "\""
    new_string = new_string + ","

## This code gets rid of parens in the string
new_string = re.sub(r'\(',"",new_string)
new_string = re.sub(r'\)',"",new_string)
print new_string
