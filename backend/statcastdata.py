#Functions Used in Stepping through events
import json
import requests


class StatCastData():

    def __init__(self):
        game_pk  = 487609
        url = 'http://statsapi.mlb.com/api/v1/game/'+str(game_pk)+'/feed/live'
        game_page = requests.get(url)
        game = json.loads(game_page.text)
        game_schema = []
        item_number = 0
        for x in range(len(game['liveData']['plays']['allPlays'])):
            play_num = x
            for y in range(len(game['liveData']['plays']['allPlays'][play_num]['playEvents'])):
                event_num = y
                game_schema.append({'item': item_number,'play_num': play_num,'event_num': event_num})
                item_number +=1
        self.game_schema = game_schema
        self.game_pk = game_pk
        self.item_return = 0
        self.game = game

    def get_total_items(self):
        return len(self.game_schema)

    def number_of_plays(self):
        play_count = len(self.game['liveData']['plays']['allPlays'])
        return play_count

    def current_play(self,play_num):
        currentPlay = self.game['liveData']['plays']['allPlays'][play_num]
        return currentPlay

    def get_play_data_before(self,play_num):
        currentPlay = self.current_play(play_num)
        batter = currentPlay['matchup']['batter']
        pitcher = currentPlay['matchup']['pitcher']
        return {'batter': batter,'pitcher': pitcher}

    def get_play_data_after(self,play_num):
        currentPlay = self.current_play(play_num)
        batter = currentPlay['matchup']['batter']
        pitcher = currentPlay['matchup']['pitcher']
        return {'batter': batter,'pitcher': pitcher}

    def get_play_data_after_last_event(self,play_num):
        currentPlay = self.current_play(play_num)
        result = currentPlay['after']
        return result

    def number_of_events(self,play_num):
        currentPlay = self.current_play(play_num)
        event_count = len(currentPlay['playEvents'])
        return event_count

    def current_event(self,play_num,event_num):
        currentPlay = self.current_play(play_num)
        currentEvent = currentPlay['playEvents'][event_num]
        return currentEvent

    def get_event_data(self,play_num,event_num):
        currentEvent = self.current_event(play_num,event_num)
        if 'count' in currentEvent.keys():
            output_dict = currentEvent['details']
            if 'details' in currentEvent.keys():
                output_dict.update(currentEvent['count'])
        else:
            output_dict = {}
        return output_dict

    def get_score(self,play_num,event_num):
        currentEvent = current_event(play_num,event_num)

    def get_pitch_count(self,pitcher,pitch_count):
        pitch_count += 1
        return {'pitcher': pitcher, 'pitch_count': pitch_count}


    def return_update(self):
        item_val = [(x['play_num'], x['event_num']) for x in self.game_schema if x['item'] == self.item_return]
        self.item_return += 1
        state_before = self.get_play_data_before(item_val[0][0])
        event = self.get_event_data(item_val[0][0],item_val[0][1])
        state_after = self.get_play_data_before(item_val[0][0])
        return (state_before,event,state_after)
