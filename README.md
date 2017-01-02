# csgoLoungerAPI
Small python script that scrapes, and parses all the match data from a website (csgolounge.com). This website has a sort of API, a link(csgolounge.com/api/mathces.php) with a page that has all the match data in a soirt of json file. This script scrapes the data from the website and writes the raw data, as it is on this link, to a textfile, then it is parsed into the seperate match data and written to a sql database, for easier processing and reading.

The script uses a textfile to keep track of how many matches are in the sql database, to only write new matches to the sql databse, that aren't already there. Currently I am using textfiles, but would like to use json files in a future version.

HOW TO USE:
Run the apiScraper file, this will output 2 files: rawData.txt and matchData.txt

What you do with this is your own responsibility, I accept no repsonsibility for your actions with this code.


** If you are the owner of the website, I have emailed you previously asking permission to do this, if you have change your mind and would like me to remove this, please let me know!
