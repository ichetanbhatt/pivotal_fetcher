import requests, json, ast, sys, os
from beautifultable import BeautifulTable
from datetime import datetime, timedelta

# Extract PT_APIKEY and PROJECT_ID from .bashrc
token = (os.environ.get('PT_APIKEY'))
p_id = (os.environ.get('PROJECT_ID'))
headers = {'X-TrackerToken': 'dc5dc9390121b6fe507c4347021ed007'}
hit_url = "https://www.pivotaltracker.com/services/v5/projects/"+p_id+"/search?"

# Accepted Stories
def accepted():

    req_date = int(sys.argv[1])
    query_date = datetime.today() - timedelta(days=req_date)
    table = BeautifulTable()
    table.column_headers = ["Story", "Type", "Estimate"]
    table.row_seperator_char = ''
    table.column_alignments['Story'] = BeautifulTable.ALIGN_LEFT
    # GET req to API
    r = requests.get(hit_url+'query=created_since:""'+str(query_date.day)+'-'+str(query_date.month)+'-'+str(query_date.year)+
                     ' -state:accepted', headers=headers)
    res_json = ast.literal_eval(r.text).get('stories').get('stories')
    lt = len(res_json)
    print ("Accepted Stories: ")
    for x in range(lt):
        result = res_json[x]
        story = result.get('name')
        story_type = result.get('story_type')
        estimate = result.get('estimate')
        table.append_row([story, story_type, estimate])
    print table

accepted()