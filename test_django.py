import json
input_file = 'parsedData.json'
with open(input_file, "r") as f_obj:
    input_data = json.load(f_obj)

matches = input_data.split(';')

for match in matches:
    # get single attributes of the match as an array
    match_data = match.split(',')

    # get all the attributes
    match_id = int(match_data[0][1:])
    match_date = match_data[1]
    match_time = match_data[2]
    match_date_time = match_date + ' ' + match_time
    team_a = match_data[3]
    team_b = match_data[4]
    winner = match_data[5]
    event = match_data[7][:-1]

    if match_data[6] == 'TRUE':
        closed = True
    else:
        closed = False

    print(str(match_id), match_date_time, team_a, team_b, winner, event, closed)
