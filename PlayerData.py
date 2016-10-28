import json
import requests
from lxml import html

class PlayerData(object):

    def __init__(self):
        url = 'http://mlb.mlb.com/lookup/named.stats_player_hitting_default.bam?game_type=%27R%27&season=%272014%27&sort_order=%27desc%27&league_id=%27103%27&sort_column=%27hr%27&team_id=%27120%27'
        name_xml = requests.get(url)
        self.tree = html.fromstring(name_xml.content)


    def return_player_data(self,player):



    def return_agg_data(self,player,):
        
