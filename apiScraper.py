#!/usr/bin/env python3

"""
Scraper for the website www.csgolounge.com
The website has an api(https://csgolounge.com/api/matches.php) that has a file with all the matches on the site,
this file seems to be a json format, this module scrapes all the data from the site, then it is parsed and sent to
a sql server.
"""

import urllib.request
# from apiParser import parse_api
import sys
import json


class Scrape:
    """Simple class to be used to scrape the source from a webpage in a json file"""

    def __init__(self, page_url, json_file_name, encoding='utf-8'):
        """Initialize the object for the Scrape class, an instance has a url and an output file name"""

        self.page_url = page_url
        self.json_file_name = json_file_name
        self.encoding = encoding

    def print_url_for_testing(self):
        """
        For testing purposes:

        Function for getting the plain html source from a webpage and dumping it to a json,
        the webpage sees that a bot is trying to scrape the data, so a header is used to hide this and to allow
        the bot to get the data.
        """
        try:
            user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
            headers = {'User-Agent': user_agent, }
            request = urllib.request.Request(self.page_url, None, headers)
            response = urllib.request.urlopen(request)
            data = response.read().decode(self.encoding)

            print(data)
            print('\n> Match data scraped and print')
        except UnicodeError:
            print('Error: ' + str(UnicodeError))
            sys.exit()

    def write_url_to_json(self):
        """
        Function for getting the plain html source from a webpage and dumping it to a json,
        the webpage sees that a bot is trying to scrape the data, so a header is used to hide this and to allow
        the bot to get the data.
        """
        try:
            user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
            headers = {'User-Agent': user_agent, }
            request = urllib.request.Request(self.page_url, None, headers)
            response = urllib.request.urlopen(request)
            data = response.read().decode(self.encoding)

            with open(self.json_file_name, 'w') as f_obj:
                json.dump(data, f_obj)

            print('> Match data scraped to:', self.json_file_name)
        except UnicodeError:
            print('Error: ' + str(UnicodeError))
            sys.exit()


def main():
    url = 'https://csgolounge.com/api/matches'
    file_name = 'rawData.json'
    scrape = Scrape(url, file_name)
    scrape.print_url_for_testing()


if __name__ == "__main__":
    main()