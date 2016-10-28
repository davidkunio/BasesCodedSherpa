import json
from statcastdata import StatCastData
game = StatCastData()

with open("data_output.txt",'w') as f:
    for x in range(game.get_total_items()):
        d = str(game.return_update())+'\n'
        f.write(d)
        print(d)
