import requests, json, ast
from beautifultable import BeautifulTable

# TOKEN = '0ac691cc97828aed54e8cfd30e0488b2'
headers = {'X-TrackerToken': '0ac691cc97828aed54e8cfd30e0488b2'}
hit_url = "https://www.pivotaltracker.com/services/v5/projects/2112896/search?"


# Accepted Stories
def accepted():
    table = BeautifulTable()
    table.column_headers = ["Story", "Type", "Estimate"]
    table.row_seperator_char = ''
    table.column_alignments['Story'] = BeautifulTable.ALIGN_LEFT
    # GET req to API
    r = requests.get(hit_url+'query=created_since:"22 Sep 2017"'
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

