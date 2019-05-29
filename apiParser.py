#!/usr/bin/env python3
"""
Parser for the website www.csgolounge.com
The website has an api(https://csgolounge.com/api/matches.php) that has a file with all the matches on the site,
this file seems to be a json format
"""

import json
from collections import OrderedDict
import sys


class Parse:
    """Simple class to parse a json file with data from csgolounge.com/api/matches"""

    def __init__(self, json_input_name, json_output_name):
        """Initialize an object with and input and output file in json format"""
        self.input_file = json_input_name
        self.output_file = json_output_name

    def parse_file(self):

        # get the input from the input_file
        print('> Starting api parser...')
        with open(self.input_file, "r") as f_obj:
            input_data = json.load(f_obj)

        # get rid of the first block parentheses and curly bracket
        input_data = input_data[2:]

        # string to hold all parsed matches
        parsed_data = ''

        # while there are still matches in input
        while input_data:
            end_pos = input_data.find('}')

            match = input_data[:end_pos]
            input_data = input_data[end_pos + 2:]

            match = match[match.find('"match"') + 9:]
            match_id = match[:match.find('"')]

            # date and time
            match = match[match.find('"when"') + 8:]
            date = match[:10]
            time = match[11: match.find('"')]

            # team A
            match = match[match.find('"a"') + 5:]
            team_a = match[:match.find('"')]

            # team B
            match = match[match.find('"b"') + 5:]
            team_b = match[:match.find('"')]

            # winner
            match = match[match.find('"winner"') + 10:]
            winner = match[:match.find('"')]

            if winner == 'a':
                winner = team_a
            if winner == 'b':
                winner = team_b
            if winner == 'c':
                winner = 'draw'

            # closed
            match = match[match.find('"closed"') + 10:]
            closed = match[:match.find('"')]

            if closed == '1':
                closed = 'TRUE'
            if closed == '0':
                closed = 'FALSE'

            # event
            match = match[match.find('"event"') + 9:]
            event = match[:match.find('"')]

            match = Match(match_id, date, time, team_a, team_b, winner, closed, event)

            # get values from orddict()
            match_info = ''
            for key, values in match.match_to_dict().items():
                if key != 'event_name':
                    match_info += values + ','
                else:
                    match_info += values

            parsed_data += '[' + match_info + '];'

        with open(self.output_file, 'w') as f_obj:
            json.dump(parsed_data, f_obj)

        print('> Match data parsed and written to: ' + self.output_file)
        sys.exit()


class Match:
    """Parse the data of a match from a line out of the matchData file"""

    def __init__(self, match_id, date, time, team_a, team_b, winner, closed, event):
        self.match_id = match_id
        self.date = date
        self.time = time
        self.team_a = team_a
        self.team_b = team_b
        self.winner = winner
        self.closed = closed
        self.event = event

    def match_to_str(self):
        match_data = 'ID: ' + self.match_id + ' Date: ' + self.date + ' ' + self.time + ' Team A: ' + self.team_a + ' Team B: ' + self.team_b + ' Winner: ' + self.winner + ' Event: ' + self.event + ' Closed: ' + str(self.closed)
        return match_data

    def match_to_dict(self):
        match_dict = OrderedDict()
        match_dict['id'] = self.match_id
        match_dict['match_date'] = self.date
        match_dict['match_time'] = self.time
        match_dict['team_a_name'] = self.team_a
        match_dict['team_b_name'] = self.team_b
        match_dict['match_winner'] = self.winner
        match_dict['match_closed'] = self.closed
        match_dict['event_name'] = self.event
        return match_dict


def main():
    parse = Parse('rawData.json', 'parsedData.json')
    parse.parse_file()

if __name__ == "__main__":
    main()
