import tbapy 
import json
import pandas as pd
from operator import itemgetter

tba = tbapy.TBA('dZURQZdsSGuLmOC8lHnCnpPvjUqVpQ2qXxdObgcLS75cT7jNAfUxxvkOusgsd30e')

class team:
    def __init__(self, team_number, year):
        self.team_number = team_number
        self.year = year
        
    def season_event_keys(self):
        json_data = tba.team_events(self.team_number, self.year)
        s1 = json.dumps(json_data)
        data = json.loads(s1)
        data = sorted(data, key=itemgetter('start_date'))
        output = []
        for i in data:
            output.append(i['key'])
        return output

    def team_event_match_keys(self, event_keys):
        json_data = []
        for event in event_keys:
            json_data += tba.team_matches(self.team_number, event)
            
        s1 = json.dumps(json_data)
        data = json.loads(s1)
        try:
            # data = sorted(data, key=itemgetter('actual_time'))
            match_keys = []
            
            for i in data:
                match_keys.append(i['key'])
                
            return match_keys
        except TypeError:
            return[]
        

    def team_match_stations(self, match_keys):  
        team_match_stations = []
            
        for i in match_keys:     
            match_data = tba.match(i)

            try:
                station_index = match_data['alliances']['blue']['team_keys'].index('frc'+ str(self.team_number)) + 1
                alliance_color = 'blue'
            except ValueError:
                station_index = match_data['alliances']['red']['team_keys'].index('frc'+ str(self.team_number)) + 1
                alliance_color = 'red'
            
            team_match_stations.append(alliance_color + ' ' + str(station_index)) 
            
            
        return team_match_stations

    def team_match_climbs(self, match_keys):
        index = 0
        climbs = []
        stations = self.team_match_stations(match_keys)
        for i in match_keys:
            json_data = tba.match(i)
            s1 = json.dumps(json_data)
            data = json.loads(s1)
            
            split = stations[index].split()
            climb = data['score_breakdown'][split[0]]['endgameRobot' + split[1]]
            climbs.append(climb)
            index += 1 
        return climbs
    
    #Returns data frame unlike other functions
    def simple_season_schedule(self):
        json_data = tba.team_events(self.team_number, self.year)
        s1 = json.dumps(json_data)
        data = json.loads(s1)

        df = pd.DataFrame(data)
        df = df.fillna("")
        output = df[['key', 'start_date', 'name']]
        output = output.sort_values(by=['start_date'])  
        
        return output

    def to_data_frame(self, column_titles, column_data):
        table = []
        for i in range(len(column_titles)):
            table.append(pd.DataFrame({column_titles[i]: column_data[i]}))
  
        data_frame = pd.concat(table, axis=1)
        data_frame = data_frame.fillna("")
        
        return data_frame