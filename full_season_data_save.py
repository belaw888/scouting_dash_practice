import frc_schedule_generator as sched
import json
import time
start = time.time()

event_key = '2022vabrb'

def update_team_season_data_json(event_key):
    list = sched.get_event_teams_list(event_key)
    dict = sched.team_list_season_matches(list)

    with open('event_teams_season_data.json', 'w') as outfile:
        json.dump(dict, outfile, indent=4)

team_key = 'frc5724'


with open('event_teams_season_data.json', 'r') as infile:
    data = json.load(infile)

def team_climbs(match_keys, team_key):  
        team_match_stations = []
        climbs = []
        for key in match_keys:
                matches_list = data[team_key][key.split('_')[0]]
                for match in matches_list:
                    if match['key'] == key:
                        # match_json_data = matches_list['key']
                        # print(match)

                        try:
                            station_index = match['alliances']['blue']['team_keys'].index(team_key) + 1
                            alliance_color = 'blue'
                        except ValueError:
                            station_index = match['alliances']['red']['team_keys'].index(team_key) + 1
                            alliance_color = 'red'
                        
                        team_match_stations.append((alliance_color + ' ' + str(station_index))) 

                        station = alliance_color + ' ' + str(station_index)

                        split = station.split()
                        # print(type(match['score_breakdown']))
                        # print(team_key)
                        # print(data[team_key]['2022varr'])
                        # print(match['score_breakdown']['blue'])
                        if match['score_breakdown'] != None:
                            climb = match['score_breakdown'][split[0]]['endgameRobot' + split[1]]
                            climbs.append(climb)

                                
                
        return climbs

def team_season_match_keys(team_key):

    season_event_keys = sched.season_event_keys(team_key, 2022)
    team_data = data[team_key]

    season_match_keys = []
    for i in season_event_keys:
        events = team_data[i]

        for x in events:
            season_match_keys.append(x['key'])

    return season_match_keys

# def team_event_match_keys(event_key, team_key):

#     team_event_data = data[team_key][event_key]

#     event_match_keys = []

#     for x in team_event_data:
#         season_match_keys.append(x['key'])

#     return season_match_keys



print(team_climbs(team_season_match_keys(team_key), team_key))

end = time.time()
print(f'time of execution: {(end-start) * 10**3} ms')
#video keys like H-zSTqt0SHE should be used
#after 'youtube.com/watch?v=' in the url
#ie: 'youtube.com/watch?v=H-zSTqt0SHE'

