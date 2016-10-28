import requests

def parse_runners(runners_list):
    runners = (1 if "1B" in runners_list else 0,
               1 if "2B" in runners_list else 0,
               1 if "3B" in runners_list else 0)
    if runners == (0,0,0):
        return 1
    elif runners == (1,0,0):
        return 2
    elif runners == (0,1,0):
        return 3
    elif runners == (1,1,0):
        return 4
    elif runners == (0,0,1):
        return 5
    elif runners == (1,0,1):
        return 6
    elif runners == (0,1,1):
        return 7
    elif runners == (1,1,1):
        return 8

#win p is normalized to describe home team
def win_p_and_li(state):
    s = state.copy()
    if int(s['count']['outs']) == 3:
        if s['half'] == 'bottom':
            s['inning'] += 1
            s['half'] == 'top'
        else:
            s['half'] == 'bottom'
        s['count']['outs'] = 0

    state_array = []

    state_array.append('"V"' if s['half'] == 'top' else 'H')
    state_array.append(s['inning'])
    state_array.append(max(int(s['count']['outs']), 2))
    state_array.append(parse_runners(s['runners']))
    scorediff = s['homeScore']-s['awayScore']
    scorediff = -scorediff if s['half'] == 'top' else scorediff
    state_array.append(scorediff)

    state_string = state_array.join(",")

    url = "https://gregstoll.dyndns.org/~gregstoll/baseball/getcumulativestats.cgi"
    payload = {'stateString': state_string, 'startYear': 1957, 'endYear': 2015}
    r = requests.get(url, params=payload)
    result = json.loads(r.json())
    win_p = result['wins']/result['total']
    win_p = 1 - win_p if s['half'] == 'top' else win_p
    return win_p, result['leverage']
