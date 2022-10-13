import tbapy
from IPython.display import display
from tabulate import tabulate
import pandas as pd
import json
from operator import itemgetter
import TBA_data_functions as t

tba = tbapy.TBA('dZURQZdsSGuLmOC8lHnCnpPvjUqVpQ2qXxdObgcLS75cT7jNAfUxxvkOusgsd30e')

# +

event_key = '2022varr'
json_data = tba.event_matches(event_key)
# schedule = tba.team_events(401, 2022)
team401 = t.team(401, 2022) 
schedule = team401.simple_season_schedule()
# print(schedule)
s1 = json.dumps(json_data)
data = json.loads(s1)
print(data)
df = pd.DataFrame(data)
df = df.fillna("")

# output = df[['key', 'start_date', 'name']]
output = df.sort_values(by=['predicted_time'])  
output = output.reset_index(drop=True)

# print(output)

# print(df)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 2)

# output = output[output['key'] == f'{event_key}_qm89']
# display(output)
newdf = output['alliances']
# print(type(newdf))

match_schedule_dict = {}

for index, items in newdf.items():
    # index = row()
    blue_alliance = items['blue']['team_keys']
    red_alliance = items['red']['team_keys']
    b1,b2,b3 = blue_alliance
    r1,r2,r3 = red_alliance
    # print(index, items)
    synced_match_code = output.iloc[index]['key']
    # print(synced_match_code)
    match_schedule_dict[synced_match_code] = {
        'b1' : b1,
        'b2' : b2,
        'b3' : b3,
        'r1' : r1,
        'r2' : r2,
        'r3' : r3,
    } 
    
# print(match_schedule_dict)

print(match_schedule_dict['2022chcmp_qm102'])
# display(output['alliances'])

# json_data = newdf
# s1 = json.dumps(json_data)
# data = json.loads(s1)
# print(type(newdf))



# for key in (newdf.keys()).iteritems():
#     print(key)
# blue = newdf['blue']['team_keys']
# print(blue)
#is update?

# +
# print(tabulate(df, tablefmt="pretty"))
