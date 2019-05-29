# csgoLoungerAPI
Small python script that pulls the match data form the csgolounge.com API

This is just a small script that pulls the match data form the csgolounge.com API (csgolounge.com/api/mathces.php). The raw data will be written and saved to the rawData.txt file, and the parsed match data will be written and saved to the matchData.txt file.

In the API file, some data is incomplete or mixed up, my script removes all these matches and outputs the rest.

HOW TO USE:
Run the apiScraper file, this will output 2 files: rawData.txt and matchData.txt

What you do with this is your own responsibility, I accept no repsonsibility for your actions with this code.

# csgoLoungeAPI

A small python script that pulls and scrapes the csgo e-sports match data from the popular betting website:
www.csgolounge.com. The website has an "API". A page @ www.csgolounge.com/api/matches, the page is a jason file will all
the matches ever recorded on the website and is open to the public.

This small python app scrapes the website's data, the data is the parsed and then it is possible to write all the data
to a SQL or MySQL database, or any database(just change the SQL queries, to your liking).