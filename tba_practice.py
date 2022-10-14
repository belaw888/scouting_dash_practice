import tbapy 
# import gspread
import json
import pandas as pd
from operator import itemgetter
import TBA_data_functions as t
import time

# sa = gspread.service_account(filename=
#     r'C:\Users\Team401\Desktop\Python_Projects\TBA_Test\%APPDATA%\gspread\service_account.json')
# sh = sa.open('TBA API Practice')

# wks = sh.worksheet('Sheet1')
# wks2 = sh.worksheet('Sheet2')

tba = tbapy.TBA('dZURQZdsSGuLmOC8lHnCnpPvjUqVpQ2qXxdObgcLS75cT7jNAfUxxvkOusgsd30e')
start = time.time()

team401 = t.team(422, 2022) 
team401_schedule = team401.simple_season_schedule()
team401_events = team401.season_event_keys()
# print(team401_events)


# wks.clear()
# wks.update('a1', [team401_schedule.columns.values.tolist()] + team401_schedule.values.tolist())

# team401_match_keys_va305 = team401.team_event_match_keys([team401_events[0]])
# team401_climbs_va305 = team401.team_match_climbs(team401_match_keys_va305)

# team401_match_keys_va320 = team401.team_event_match_keys([team401_events[1]])
# team401_climbs_va320 = team401.team_match_climbs(team401_match_keys_va320)

# team401_match_keys_chcmp = team401.team_event_match_keys([team401_events[2]])
# team401_climbs_chcmp = team401.team_match_climbs(team401_match_keys_chcmp)

# team401_match_keys_gal = team401.team_event_match_keys([team401_events[3]])
# team401_climbs_gal = team401.team_match_climbs(team401_match_keys_gal)

# titles = ['va305', 'va320', 'chcmp', 'galileo']
# team401_climbs_list = [team401_climbs_va305, 
#                        team401_climbs_va320, 
#                        team401_climbs_chcmp, 
#                        team401_climbs_gal]

# new = team401.to_data_frame(titles, team401_climbs_list)

# # wks2.clear()
# # wks2.update('a1', [new.columns.values.tolist()] + new.values.tolist())

import plotly.express as px

# team_numbers = [401, 254, 422, 2363, 364, 1511]

# for num in team_numbers:
#     team = t.team(num, 2022)
#     event_keys = team.season_event_keys()
#     match_keys = team.team_event_match_keys(event_keys)
#     climbs = team.team_match_climbs(match_keys)
#     titles = ['climbs']
#     data = [climbs]
#     dataframe = team.to_data_frame(titles, data)
#     fig = px.pie(dataframe, names='climbs')
#     fig.show

team401_match_keys_season = team401.team_event_match_keys(team401_events[:3])
print(team401_match_keys_season)
# print(team401_match_keys_season)
team401_climbs_season = team401.team_match_climbs(team401_match_keys_season)
df3 = pd.DataFrame({'climbs': team401_climbs_season})
fig = px.pie(df3, names='climbs')
fig.show()
end = time.time()
print(f'time of execution: {(end-start) * 10**3} ms')