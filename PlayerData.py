import json
import requests
from lxml import html

class PlayerData(self,player_id,team_id,season,league_id):

    def __init__(self,player_id,team_id,season,league_id):
        self.player_id = player_id
        self.league_id = league_id
        self.team_id = team_id
        self.season = season
        url = 'http://mlb.mlb.com/lookup/named.stats_player_hitting_default.bam?game_type=%27R%27&season=%27'+season+'%27&sort_order=%27desc%27&league_id=%27'+league_id+'%27&sort_column=%27hr%27&team_id=%27'+team_id+'%27'
        name_xml = requests.get(url)
        self.tree = html.fromstring(name_xml.content)


    def return_player_data(self,player):



    def return_agg_data(self,player,):
