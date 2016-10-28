#Functions Used in Stepping through events
import json
import requests
import newrelic.agent


class StatCastData():

    def __init__(self):
        game_pk  = 487610
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
        self.score = {'awayScore':0,'homeScore':0}
        self.count = {'balls':0,'strikes':0,'outs':0}
        self.pitch_count = 0
        self.pitcher_first_inning = 1
        self.pitcher_first_out = 0




    def get_total_items(self):
        return len(self.game_schema)

    def number_of_plays(self):
        play_count = len(self.game['liveData']['plays']['allPlays'])
        return play_count

    def current_play(self,play_num):
        currentPlay = self.game['liveData']['plays']['allPlays'][play_num]
        return currentPlay

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

    def get_data(self,play_num,event_num,play_num_prev,event_num_prev):
        currentPlay = self.current_play(play_num)
        previousPlay = self.current_play(play_num_prev)
        currentEvent = self.current_event(play_num,event_num)
        previousEvent = self.current_event(play_num_prev,event_num_prev)
        batter = currentPlay['matchup']['batter']
        pitcher = currentPlay['matchup']['pitcher']
        runners_before = []
        for x in range(len(currentPlay['runners'])):
            runners_before.extend([currentPlay['runners'][x]['movement']['start']])
        runners_after = []
        for x in range(len(currentPlay['runners'])):
            runners_after.extend([currentPlay['runners'][x]['movement']['end']])

        ##Determine Count for Before
        if (currentPlay['about']['halfInning'] == previousPlay['about']['halfInning'] and
            currentPlay['about']['inning'] == previousPlay['about']['inning'] and
            currentPlay['matchup']['batter'] != previousPlay['matchup']['batter']):
            self.count.update({'balls':0,'strikes':0})
            self.count.update({'outs':previousPlay['count']['outs']})
        elif 'count' in previousEvent:
            self.count.update(previousEvent['count'])

        count_before = self.count

        #Determine Count After
        if ('count' in currentEvent):
            if 'outs' in currentEvent['count']:
                self.count.update(currentEvent['count'])
            elif 'count' in previousEvent:
                if 'outs' in previousEvent['count']:
                    self.count.update(currentEvent['count'])
                    self.count.update({'outs':previousEvent['count']['outs']})
                else:
                    self.count.update(previousEvent['count'])
        count_after = self.count

        # Determine the Score
        score_before = self.score
        if 'homeScore' in currentEvent['details']:
            self.score.update({'awayScore':currentEvent['details']['awayScore'],'homeScore':currentEvent['details']['homeScore']})
        score_after = self.score

        inning = currentPlay['about']['inning']
        half = currentPlay['about']['halfInning']

        #Search of Umpire Review
        if ('result' in currentPlay and 'description' in currentPlay['result']):
            if 'challenge' in currentPlay['result']['description']:
                play_challenge = 1
            else:
                play_challenge = 0
            if 'confirm' in currentPlay['result']['description']:
                challenge_confirm = 1
            else:
                challenge_confirm = 0
        challenge = {'challenge':play_challenge,'confirm':challenge_confirm}

        ## Calculate Pitch Count
        pitch_count_before = self.pitch_count
        if currentPlay['matchup']['pitcher'] == previousPlay['matchup']['pitcher']:
            if currentEvent['isPitch']:
                self.pitch_count += 1
                pitch_count_after = self.pitch_count
            else:
                pitch_count_after = self.pitch_count
        else:
            if currentEvent['isPitch']:
                self.pitch_count = 1
                pitch_count_after = self.pitch_count
            else:
                pitch_count_after = 0

        ## Check for new Batter
        if previousPlay['matchup']['batter'] != currentPlay['matchup']['batter']:
            new_batter = 1
        else:
            new_batter = 0

        ## Check for new pitcher
        if previousPlay['matchup']['pitcher'] != currentPlay['matchup']['pitcher']:
            new_pitcher = 1
            self.pitcher_first_inning = int(currentPlay['about']['inning'])
            self.pitcher_first_out = int(self.count['outs'])
        else:
            new_pitcher = 0

        # Build output dictionaries
        state_before = {'batter': batter,'pitcher': pitcher,'runners':runners_before,'count':count_before,
                        'inning':inning,'half':half,'score':score_before,'pitch_count':pitch_count_before,
                        'new_batter':new_batter,'new_pitcher':new_pitcher}
        state_after = {'batter': batter,'pitcher': pitcher,'runners':runners_after,'count':count_after,
                        'inning':inning,'half':half,'score':score_after,'pitch_count':pitch_count_after,
                        'pitcher_first_inning':self.pitcher_first_inning,'pitcher_first_out':self.pitcher_first_out}
        event = self.get_event_data(play_num,event_num)

        if event_num == self.number_of_events(play_num):
            event.update(challenge)


        return (state_before,event,state_after,self.item_return)

    @newrelic.agent.background_task()
    def return_update(self):
        if self.item_return > 0:
            self.item_return -= 1
            item_val_prev = [(x['play_num'], x['event_num']) for x in self.game_schema if x['item'] == self.item_return]
            self.item_return += 1
            item_val = [(x['play_num'], x['event_num']) for x in self.game_schema if x['item'] == self.item_return]
            self.item_return += 1
        else:
            item_val_prev = [(x['play_num'], x['event_num']) for x in self.game_schema if x['item'] == self.item_return]
            item_val = [(x['play_num'], x['event_num']) for x in self.game_schema if x['item'] == self.item_return]
            self.item_return += 1


        return self.get_data(item_val[0][0],item_val[0][1],item_val_prev[0][0],item_val_prev[0][1])
