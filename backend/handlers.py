from winpercent import win_p_and_li

handlers = []

def register(f):
    handlers.append(f)
    return f


@register
def in_play(before, event, after, index):
    if event and 'isInPlay' in event and event['isInPlay']:
        print("returning from in_play")
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
    print("LI: {}".format(li))
    if li > 2.5:
        print("HIGH LEVERAGE")
        return {"title": "Big Opportunity", "index": index, "text": "Head's up, this could be big. With a hit, this game could change."}

# @register
# def new_batter(before, event, after):
#     pass
#
# @register
# def new_runner(before, event, after):
#     pass
#
# @register
# def new_pitcher(before, event, after):
#     pass

# @register
# def starter_high_pitch_count(before, event, after):
#     pass
#
# @register
# def starter_low_pitch_count(before, event, after):
#     pass
#
# @register
# def bunt_situation(before, event, after):
#     pass
#
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
#
# @register
# def hit_and_run_situation(before, event, after):
#     pass
