import json
from statcastdata import StatCastData
game = StatCastData()

for x in range(game.get_total_items()):
    d = game.return_update()
    json.dump(d, open("data_output.txt",'w'))
    print(d)
