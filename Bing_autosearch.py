#############################################################################
##     This program searches bing 30 times by opening, searching and closing
##  chrome.
#############################################################################

import subprocess
import time

#   To use chrome, I had to update the path environment variable to have chrome.exe.
# The following line can be used to see if Google Chrome will open when called.
#subprocess.Popen(["chrome.exe",'E://Users//Purple//desktop//Google_Chrome.lnk'])

#The command to open the CMD prompt goes first because the chrome window needs to be open for it to work.
subprocess.Popen(['E://Users//Purple//Desktop//Bing_Rewards_autosearcher//Bing_search_with_large_word_bank2.exe'])
time.sleep(1)#delay 1 second
subprocess.call(["chrome.exe"])

