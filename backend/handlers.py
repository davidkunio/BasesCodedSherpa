from winpercent import win_p_and_li

handlers = []

def register(f):
    handlers.append(f)
    return f


@register
def in_play(before, event, after):
    if 'isInPlay' in event and event['isInPlay']:
        print("returning from in_play")
        return {"title": "In Play", "text": "The ball is in play"}

@register
def big_play(before, event, after):
    pass

@register
def high_leverage(before, event, after):
    win_p, li = win_p_and_li(after)
    if li > 2.5:
        return {"title": "Big Opportunity", "text": "Head's up, this could be big. With a hit, this game could change."}

@register
def new_batter(before, event, after):
    pass

@register
def new_runner(before, event, after):
    pass

@register
def new_pitcher(before, event, after):
    pass

@register
def starter_high_pitch_count(before, event, after):
    pass

@register
def starter_low_pitch_count(before, event, after):
    pass

@register
def bunt_situation(before, event, after):
    pass

@register
def hit_and_run_situation(before, event, after):
    pass

@register
def steal_situation(before, event, after):
    pass

@register
def intentional_walk_situation(before, event, after):
    pass

@register
def pinch_hitter_situation(before, event, after):
    pass
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
