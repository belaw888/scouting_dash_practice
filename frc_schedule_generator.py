import tbapy
from IPython.display import display
from tabulate import tabulate
import pandas as pd
import json
from operator import itemgetter
import TBA_data_functions as t

tba = tbapy.TBA('dZURQZdsSGuLmOC8lHnCnpPvjUqVpQ2qXxdObgcLS75cT7jNAfUxxvkOusgsd30e')

# event_key = '2022gal'

def get_qm_schedule(event_key):
    json_data = tba.event_matches(event_key)
    s1 = json.dumps(json_data)
    data = json.loads(s1)
    df = pd.DataFrame(data)
    df = df.fillna("")

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


# data = get_qm_schedule(event_key)
# out = pd.DataFrame.from_dict(data)

# top = out.columns.values

# print(top)
# github update?

