import json
import pandas as pd
import os

cfg = json.load(open('data-params.json'))

def get_data(outpath, teams, years):
    
    path = outpath

    if not os.path.exists(path):
        os.mkdir(path)
        
    for team in teams:
    
        for year in years:
            
            table = get_table(team, year)[0] # get rid of this indexing?
            
            table.to_csv('data/%s_%s.csv' %(team, year))
            
def get_table(team, year):
    
    dfs = pd.read_html("https://www.pro-football-reference.com/teams/%s/%s.htm" %(team, year), match='Schedule & Game Results')
    
    return dfs
        
get_data(**cfg)