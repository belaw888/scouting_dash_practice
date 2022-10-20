import json
import time
import pandas as pd
import plotly.express as px
from operator import itemgetter
import time
import tbapy 

tba = tbapy.TBA('dZURQZdsSGuLmOC8lHnCnpPvjUqVpQ2qXxdObgcLS75cT7jNAfUxxvkOusgsd30e')

start = time.time()

event_key = '2022vabrb'
team_key = 'frc5724'
year = 2022

def new_team_season_data_json(event_key):
    """
    Creates a json file of teams at a given event. 
    Includes data from every event and match the team has participated in this season.
    Saves file as 'event_teams_season_data.json' in current directory

    Args:
        event_key (String): The Blue Alliance database format, eg. '2022chcmp'
    """    
    list = get_event_teams_list(event_key)
    dict = team_list_season_matches(list)

    with open('event_teams_season_data.json', 'w') as outfile:
        json.dump(dict, outfile, indent=4)

def open_team_season_data_json():
    """
    enables read and write to 'event_teams_season_data.json' in current directory

     Returns:
        Dictionary: deserialized contents of json file
    """    
    with open('event_teams_season_data.json', 'r') as infile:
        data = json.load(infile)

    return data

def team_endgame_results(match_keys, team_key):  
    """
    generates list of endgame results ('climbs' for 2022 season) achieved by a team during a given set of matches

    Args:
        match_keys (List): The Blue Alliance database format, eg. '2022chcmp_qm1'
        team_key (String): The Blue Alliance database format, eg. '2022chcmp'

    Returns:
        List: List of strings eg. [Mid, Low, None], Built in order of match_keys argument
    """    
    data = open_team_season_data_json()
    team_match_stations = []
    endgames = []
    for key in match_keys:
                matches_list = data[team_key][key.split('_')[0]]
                for match in matches_list:
                    if match['key'] == key:
            
                        try:
                            station_index = match['alliances']['blue']['team_keys'].index(team_key) + 1
                            alliance_color = 'blue'
                        except ValueError:
                            station_index = match['alliances']['red']['team_keys'].index(team_key) + 1
                            alliance_color = 'red'
                        
                        team_match_stations.append((alliance_color + ' ' + str(station_index))) 
                        station = alliance_color + ' ' + str(station_index)
                        split = station.split()
    
                        if match['score_breakdown'] != None:
                            endgame = match['score_breakdown'][split[0]]['endgameRobot' + split[1]]
                            endgames.append(endgame)

                                
                
    return endgames

def team_season_matches(team_key, year):
    """
    get a list of match keys for all matches played by a team in a given year

    Args:
        team_key (String): The Blue Alliance database format, eg. 'frc401'
        year (int): year of competition

    Returns:
        List: The Blue Alliance database format, eg. '2022chcmp_qm1'; All matches over whole season
    """    

    data = open_team_season_data_json()
    season_event_keys = season_events(team_key, year)
    team_data = data[team_key]

    season_match_keys = []
    for i in season_event_keys:
        events = team_data[i]

        for x in events:
            season_match_keys.append(x['key'])

    return season_match_keys

def team_event_matches(event_key, team_key):
    """
    get a list of match keys for all matches played by a team at a given event

    Args:
        event_key (String): The Blue Alliance database format, eg. '2022chcmp'
        team_key (String): The Blue Alliance database format, eg. 'frc401'

    Returns:
        List: The Blue Alliance database format, eg. '2022chcmp_qm1'; All matches at an event
    """        
    open_team_season_data_json()
    team_event_data = data[team_key][event_key]

    event_match_keys = []

    for x in team_event_data:
        event_match_keys.append(x['key'])

    return event_match_keys

# functions previously in 'frc_schedule_generator.py'
def tbapy_to_pandas_df(json_data):
    """
    Converts the json string returned by tbapy functions into a pandas dataframe 

    Args:
        json_data (String): String format of json data

    Returns:
        pandas.DataFrame: all n/a values replaced with "" 
    """    
    s1 = json.dumps(json_data)
    data = json.loads(s1)
    df = pd.DataFrame(data)
    df = df.fillna("")

    return df

def season_events(team_key, year):
    """
    generates list of events attended by a team during a given year

    Args:
        team_key (String): The Blue Alliance database format, eg. 'frc401'
        year (int): the year of competition

    Returns:
        List: event keys in The Blue Alliance database format, eg. '2022chcmp'
    """    
    json_data = tba.team_events(team_key, year)
    s1 = json.dumps(json_data)
    data = json.loads(s1)
    # Sorting here triples the execution time
    # data = sorted(data, key=itemgetter('start_date'))
    output = []
    for i in data:
        output.append(i['key'])
    return output

def get_qm_schedule(event_key):
    # print(tba.team_events('frc401', 2022, True))
    json_data = tba.event_matches(event_key)
    df = tbapy_to_pandas_df(json_data)

    try:
        output = df.sort_values(by=['predicted_time'])  
        output = output.reset_index(drop=True)

        output = output[output['comp_level'] == 'qm']
        newdf = output['alliances']

        match_schedule_dict = {}

        for index, items in newdf.items():
            blue_alliance = items['blue']['team_keys']
            red_alliance = items['red']['team_keys']
            b1,b2,b3 = blue_alliance
            r1,r2,r3 = red_alliance
            synced_match_code = output.iloc[index]['key']

            match_label = ''
            flag = False

            # print(synced_match_code)

            # print(type(synced_match_code))

            for character in range(4, len(synced_match_code)):
                # print(character)
                if flag == True:
                    match_label += synced_match_code[character]

                if synced_match_code[character] == '_':
                    flag = True

            # print(match_label)

            match_schedule_dict[synced_match_code] = {
                'b1' : b1,
                'b2' : b2,
                'b3' : b3,
                'r1' : r1,
                'r2' : r2,
                'r3' : r3,
                'match_labels' : match_label
            } 
            
        return match_schedule_dict
    
    except KeyError:
        return 'Schedule Has Not Been Released'

def get_team_season_matches(team_key):
    events = season_events(team_key, 2022)
    # print(events)
    season_event_matches = {}
    for i in events:
        # print(i)
        season_event_matches[i] = tba.team_matches(team_key, i, 2022)

    return season_event_matches

def team_list_season_matches(team_key_list):
    team_list_season_matches = {}
    for i in team_key_list:
        team_list_season_matches[i] = get_team_season_matches(i)

    return team_list_season_matches

def get_event_teams_list(event_key):
     json_data = tba.event_teams(event_key, keys=True)
     return json_data

def get_team_list(event_key):
    json_data = tba.event_teams(event_key)
    df = tbapy_to_pandas_df(json_data)
    # print(df.head())
    # print(df.loc[df['key'] == 'frc1262'])

    event_teams_dict = {}
    # event_teams_dict = dict(df['key'])

    # print(event_teams_dict)

    for items in df['key']:
        team_profile_df = df.loc[df['key'] == items]
        # print(type(team_profile_dict))
        # event_teams_dict[items]['profile']['team_number'] = team_profile_dict['team_number']
        # event_teams_dict[items]['profile']['team_name'] = team_profile_dict['nickname']
        team_number = team_profile_df['team_number'].values[0]
        nickname = team_profile_df['nickname'].values[0]
        city = team_profile_df['city'].values[0]
        state_prov = team_profile_df['state_prov'].values[0]
        country = team_profile_df['country'].values[0]

        events_and_matches = get_team_season_matches(items)
        # events = [0]
        #to save time:
        #store data for first event
        #if event data has been called already, use that
        event_data_dict = {}

        # TBA_data_functions.

        for i in events:
            event_data_dict[i] = {
                'win_loss_tie' : 'x',
                'endgame_points' : 'y'
            }
        
        
        # print(events)
        # print(team_profile_df.columns)
        event_teams_dict[items] = {
            'profile' : {
                'team_number' : team_number, 
                'nickname' : nickname,
                'state_prov' : state_prov,
                'country' : country },
                #robot image
            'season_data' : {
                'events' : event_data_dict }
        }

    # print(event_teams_dict)
    return event_teams_dict

    # return df

#video keys like H-zSTqt0SHE should be used
#after 'youtube.com/watch?v=' in the url
#ie: 'youtube.com/watch?v=H-zSTqt0SHE'

climbs = team_endgame_results(team_season_matches(team_key, year), team_key)
df3 = pd.DataFrame({'climbs': climbs})
fig = px.pie(df3, names='climbs')
fig.show()

end = time.time()
print(f'time of execution: {(end-start) * 10**3} ms')
