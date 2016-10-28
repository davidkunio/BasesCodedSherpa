import requests
from lxml import html

class NameLookup():

    def __init__(self):
        url = 'http://mlb.mlb.com/lookup/named.player_list.bam?active_sw=%27Y%27&sport_code=%27mlb%27'
        name_xml = requests.get(url)
        self.tree = html.fromstring(name_xml.content)


    def return_name(self,player_id):
        return([x.attrib['name_display_first_last'] for x in self.tree[0].getchildren() if x.attrib['player_id']==player_id][0])
