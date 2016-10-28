from statcastdata import StatCastData
game = StatCastData()

for x in range(game.get_total_items()):
    print(game.return_update())
