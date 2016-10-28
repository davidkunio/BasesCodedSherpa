# import winpercent

handlers = []

def register(f):
    handlers.append(f)
    return f


@register
def runs_scored(before, event, after):
    if event['isScoringPlay']:
        return {"title": "Runs Scored", "text": "Runs were scored"}

@register
def big_play(before, event, after):
    pass

@register
def high_leverage(before, event, after):
    pass

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
