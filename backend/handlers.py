from winpercent import win_p_and_li
from NameLookup import NameLookup

name = NameLookup()
handlers = []

def register(f):
    handlers.append(f)
    return f


@register
def in_play(before, event, after, index):
    if event and 'isInPlay' in event and event['isInPlay'] and before['pitch_count'] % 6 == 0:
        print("IN PLAY")
        return {"title": "In Play", "text": "The ball is in play", "index": index}

@register
def big_play(before, event, after, index):
    win_p_before, _ = win_p_and_li(before)
    win_p_after, _ = win_p_and_li(after)

    if win_p_after-win_p_before > .10:
        print("BIG PLAY HOME")
        return {
            "title": "Big Play",
            "index": index,
            "text": "That play was huge, the home team has improved from a "
            "{:.3}% to a {:.3}% chance of winning.".format(100*win_p_before, 100*win_p_after)}
    if win_p_after-win_p_before < -.10:
        print("BIG PLAY AWAY")
        return {
            "title": "Big Play",
            "index": index,
            "text": "That play was huge, the away team has improved from a "
            "{:.3}% to a {:.3}% chance of winning.".format(100*(1-win_p_before), 100*(1-win_p_after))
        }

@register
def high_leverage(before, event, after, index):
    _, li = win_p_and_li(after)
    if li > 2.5:
        print("HIGH LEVERAGE")
        return {
            "title": "Big Opportunity",
            "index": index,
            "text": "Head's up, this could be big. With a hit, this game could change."}

@register
def new_batter(before, event, after, index):
    if 'new_batter' in before and before['new_batter'] == 1 and before['pitch_count'] % 4 == 0:
        print('New Batter')
        return({"title":"New Batter","text": "{} strides up to the plate.".format(name.return_name(before['batter']))})


@register
def new_pitcher(before, event, after, index):
    if 'new_pitcher' in before and before['new_pitcher'] == 1:
        print('New Pitcher')
        return({"title":"New Batter","text":"{} trots in from the bullpen.".format(name.return_name(before['pitcher']))})

@register
def starter_high_pitch_count(before, event, after, index):
    if after['pitch_count'] > 0:
        pitch_yield = ((int(after['inning'])-int(after['pitcher_first_inning']))*3 + (int(after['count']['outs'])-int(after['pitcher_first_out'])))/int(after['pitch_count'])
    else:
        pitch_yield = 0
    if pitch_yield < .16 and after['pitch_count']>15 and after['count']['strikes'] == 0 and after['count']['balls'] == 0:
        print('High Pitch Count')
        return({"title":"High Pitch Count","text": "{} better be careful, he is running up the pitch count".format(name.return_name(before['pitcher']))})

@register
def starter_low_pitch_count(before, event, after, index):
    if after['pitch_count'] > 0:
        pitch_yield = ((int(after['inning'])-int(after['pitcher_first_inning']))*3 + (int(after['count']['outs'])-int(after['pitcher_first_out'])))/int(after['pitch_count'])
    else:
        pitch_yield = 0
    if pitch_yield > .19 and after['pitch_count']>15 and after['count']['strikes'] == 0 and after['count']['balls'] == 0:
        print('Low Pitch Count')
        return({"title":"Low Pitch Count","text": "{} has been very efficient. He has retired batters quickly".format(name.return_name(before['pitcher']))})

@register
def bunt_situation(before, event, after, index):
    runners_list = after['runners']
    runners = (1 if "1B" in runners_list else 0,
               1 if "2B" in runners_list else 0,
               1 if "3B" in runners_list else 0)
    if (runners == (1,1,0) or runners ==(1,0,0)) and (abs(int(before['score']['homeScore'])-int(before['score']['awayScore'])) <=2 and int(before['count']['strikes'])<2 and int(before['count']['outs'])<2):
        print('Bunt Situation')
        return({"title":"Possible Bunt Situation","text":"Heads up on the hot corners - this could be a good time to bunt!"})

#@register
def squeze_situation(before, event, after, index):
    runners_list = after['runners']
    runners = (1 if "1B" in runners_list else 0,
               1 if "2B" in runners_list else 0,
               1 if "3B" in runners_list else 0)
    if (runners == (0,0,1) or runners ==(1,0,1)) and (abs(int(before['score']['homeScore'])-int(before['score']['awayScore'])) <=2 and int(before['count']['strikes'])<2 and int(before['count']['outs'])<2):
        print('Squeze Situation')
        return({"title":"Possible Squeze Situation","text":"Close game, it might be worth the risk two squeze this runner in!"})

#@register
def hit_and_run_situation(before, event, after, index):
    runners_list = after['runners']
    runners = (1 if "1B" in runners_list else 0,
               1 if "2B" in runners_list else 0,
               1 if "3B" in runners_list else 0)
    if (runners == (1,1,0) or runners ==(1,0,0)) and (abs(int(before['score']['homeScore'])-int(before['score']['awayScore'])) <=2):
        print('Hit and Run Situation')
        return({"title":"Possible Hit and Run Situation","text":"Speed and OBP might indicate a good time to hit and run!"})

# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def steal_situation(before, event, after):
#     pass
#
# @register
# def intentional_walk_situation(before, event, after):
#     pass
#
# @register
# def pinch_hitter_situation(before, event, after):
#     pass
# #
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
