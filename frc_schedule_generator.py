import tbapy
from IPython.display import display
from tabulate import tabulate
import pandas as pd
import json
from operator import itemgetter
import time
import TBA_data_functions
# import TBA_data_functions as t

tba = tbapy.TBA('dZURQZdsSGuLmOC8lHnCnpPvjUqVpQ2qXxdObgcLS75cT7jNAfUxxvkOusgsd30e')

# event_key = '2022gal'

def tbapy_to_pandas_df(json_data):
    s1 = json.dumps(json_data)
    data = json.loads(s1)
    df = pd.DataFrame(data)
    df = df.fillna("")

    return df

def season_event_keys(team_key, year):
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
    print(tba.team_events('frc401', 2022, True))
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
    events = season_event_keys(team_key, 2022)
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


event_key = '2022chcmp'
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
start = time.time()
# print(get_team_list(event_key))
print(get_team_season_matches('frc254'))
end = time.time()
print(f'time of execution: {(end-start) * 10**3} ms')

# data = get_qm_schedule(event_key)
# out = pd.DataFrame.from_dict(data)

# top = out.columns.values

# print(top)
# github update?

