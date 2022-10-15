import frc_schedule_generator as sched
import json
import time
start = time.time()
list = sched.get_event_teams_list('2022vabrb')
# print(list)
dict = sched.team_list_season_matches(list)

with open('event_teams_season_data.json', 'w') as outfile:
    json.dump(dict, outfile, indent=4)

end = time.time()
print(f'time of execution: {(end-start) * 10**3} ms')

#video keys like H-zSTqt0SHE should be used
#after 'youtube.com/watch?v=' in the url
#ie: 'youtube.com/watch?v=H-zSTqt0SHE'