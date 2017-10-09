import requests, json, ast, sys, os
from datetime import datetime, timedelta

file_path = os.path.expanduser('~/.pt_config')
# Read config file
with open(file_path, "r") as ins:
    array = []
    for line in ins:
        array.append(line)

# Extract APIKEY and Owner
token = (array[0].split('=', 1)[1])[0:-1]
u_name = array[2].split('=', 1)[1]


# Accepted Stories
def accepted():
    # Extract ID
    project_ids_str = array[1].split('=', 1)[1]
    project_ids = json.loads(project_ids_str)
    for key in project_ids:
        p_id = str(project_ids[key])
        p_name = key
        if not len(sys.argv) > 1:
            print "Please define how old data you want!"
            return
        else:
            headers = {'X-TrackerToken': ''+token}
            hit_url = "https://www.pivotaltracker.com/services/v5/projects/" + p_id + "/search?"
            req_date = int(sys.argv[1])
            query_date = datetime.today() - timedelta(days=req_date)
            # Accepted Stories GET req to API
            r = requests.get(hit_url+'query=created_since:"'+str(query_date.day)+'-'+str(query_date.month)+'-' +
                             str(query_date.year) +
                             '" and owner:"'+u_name+'" and state:accepted', headers=headers)
            res_json = ast.literal_eval(r.text).get('stories').get('stories')
            a_lt = len(res_json)
            print "[" + p_name + "]"
            print "Accepted"
            for x in range(a_lt):
                a_result = res_json[x]
                story = a_result.get('name')
                story_type = a_result.get('story_type')
                state = a_result.get('current_state')
                estimate = str(a_result.get('estimate'))
                # Change Date Format
                created_date = datetime.strptime((a_result.get('created_at').split('T')[0]), "%Y-%m-%d")
                created_at = datetime.strftime(created_date, "%d-%b-%Y")
                accepted_date = datetime.strptime((a_result.get('accepted_at').split('T')[0]), "%Y-%m-%d")
                accepted_at = datetime.strftime(accepted_date, "%d-%b-%Y")

                owners = str(a_result.get('owner_ids'))
                table = "Story:[" + story + "] Type:[" + story_type + "] Estimate:[" + estimate + "] Created:[" + \
                        created_at + "] Accepted:[" + accepted_at + "] Owners:" + owners
                print table
            # Other Stories
            o = requests.get(hit_url + 'query=-state:accepted AND owner:"'+u_name+'"', headers=headers)
            o_res_json = ast.literal_eval(o.text).get('stories').get('stories')
            o_lt = len(o_res_json)
            print ""
            print "Started"
            for x in range(o_lt):
                result = o_res_json[x]
                story = result.get('name')
                story_type = result.get('story_type')
                created_date = datetime.strptime((result.get('created_at').split('T')[0]), "%Y-%m-%d")
                created_at = datetime.strftime(created_date, "%d-%b-%Y")
                owners = str(result.get('owner_ids'))
                table = "Story:[" + story + "] Type:[" + story_type + "] Created:[" + created_at + "] Owners:" + owners
                print table
            print ""

