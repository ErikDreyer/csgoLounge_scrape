#!/usr/bin/env python3
"""
Script to take the json file and write all the data that isn't in the SQL databse already to the SQL database
"""

import pymysql
import sys
from apiParser import *


class SqlWriter:
    """Class for writing data from a json file with the match data to a sql database"""

    def __init__(self, json_input_file, sql_host_ip, username, password, database_name, table_name='csgo_matches',
                 port=3306):
        """
        1. Initialize a SqlWriter object, table name and port number is set as defaults, the table is a normal generic
            name and the port nummer is the standard sql number
        2. connect to database
        """
        self.json_input_file = json_input_file
        self.sql_host_ip = sql_host_ip
        self.username = username
        self.password = password
        self.database_name = database_name
        self.table_name = table_name
        self.port = port
        self.connection = None
        # self.__connect_to_database()

    def __connect_to_database(self):
        """Make a connection to the database"""
        try:
            self.connection = pymysql.connect(host=self.sql_host_ip, port=self.port, user=self.username,
                                              passwd=self.password, db=self.database_name)
            print("> Connection to database successful...")
        except RuntimeError:
                print("> Connection failed, quitting")
                sys.exit()

    def load_data_from_file(self):
        """Load the data from the json file"""
        with open(self.json_input_file) as f_obj:
            matches = json.load(f_obj)

        return matches


def main():
    """The main function is for testing purposes, instead of making a query and writing to q sql server, it prints the
    output for testing when you can't connect to the server"""

    # create a SqlWriter object
    input_file_name = 'parsedData.json'
    sql_host_ip = '127.0.0.1'
    username = 'admin'
    password = 'password'
    database_name = 'csgoData'
    sql_writer = SqlWriter(input_file_name, sql_host_ip, username, password, database_name)

    # get the last known match's id to know which matches to write to the sql database
    with open("settings.txt", "+r") as settings_file:
        prev_match = settings_file.readline()

    # all the matches as one string from the json file and store it in var text
    text = sql_writer.load_data_from_file()
    matches = text.split(';') # split all the matches at the ';' in to a list
    # cursor = sql_writer.connection.cursor()

    # get single matches, and split the matches' attributes into var match_attribute
    # match_object is created as an instance of the Match class
    # the match is printed back as a string for testing purposes
    # the match is written to the sql database if it is not yet in the table
    for match in matches:
        if match:
            match_attribute = match.split(',')
            match_obj = Match(match_attribute[0][1:], match_attribute[1], match_attribute[2], match_attribute[3],
                              match_attribute[4], match_attribute[5], match_attribute[6], match_attribute[7])

            print(match_obj.match_to_str())

    # close the settings text file
    settings_file.close()

if __name__ == "__main__":
        main()
