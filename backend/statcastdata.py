import json
import requests

class StatCastData:


    game_pk = 487629
    item_return = 0

    def __init__(self,game_pk):
        url = 'http://statsapi.mlb.com/api/v1/game/'+str(game_pk)+'/feed/live'
        self.game = json.loads(game_page.text)
        self.game_schema = []
        item_number = 0
        for x in range(number_of_plays(game_pk)):
            play_num = x
            for y in range(number_of_events(game_pk,play_num)):
                event_num = y
                self.game_schema.append({'item': item_number,'play_num': play_num,'event_num': event_num})
                item_number +=1
        self.item_return = item_return

    def get_game_json(game_pk):
        url = 'http://statsapi.mlb.com/api/v1/game/'+str(game_pk)+'/feed/live'
        game = json.loads(game_page.text)
        return game

    def number_of_plays(game_pk):
        game = get_game_json(game_pk)
        play_count = len(game['liveData']['plays']['allPlays'])
        return play_count

    def current_play(game_pk,play_num):
        game = get_game_json(game_pk)
        currentPlay = game['liveData']['plays']['allPlays'][play_num]
        return currentPlay

    def get_play_data(game_pk,play_num):
        currentPlay = current_play(game_pk,play_num)
        batter = currentPlay['matchup']['batter']
        pitcher = currentPlay['matchup']['pitcher']
        return {'batter': batter,'pitcher': pitcher}

    def number_of_events(game_pk,play_num):
        currentPlay = current_play(game_pk,play_num)
        event_count = len(currentPlay['playEvents'])
        return event_count

    def current_event(game_pk,play_num,event_num):
        currentPlay = current_play(game_pk,play_num)
        currentEvent = currentPlay['playEvents'][event_num]
        return currentEvent

    def get_event_data(game_pk,play_num,event_num):
        currentEvent = current_event(game_pk,play_num,event_num)
        if 'count' in currentEvent.keys():
            output_dict = currentEvent['count']
            if 'details' in currentEvent.keys():
                output_dict.update(currentEvent['details'])
        else:
            output_dict = {}
        return output_dict

    def get_pitch_count(pitcher,pitch_count):
        pitch_count += 1
        return {'pitcher': pitcher, 'pitch_count': pitch_count}


    def return_update(self):
        item_val = [(x['play_num'], x['event_num']) for x in game_schema if x['item'] == self.item_return]
        self.item_return += 1
        state = get_play_data(game_pk,item_val[0][0])
        event = get_event_data(game_pk,item_val[0][0],item_val[0][1])
        return (state,event)
