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
states = ['Accepted', 'Delivered', 'Finished', 'Started']

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
            print "[" + p_name + "]"
            for state in states:
                headers = {'X-TrackerToken': ''+token}
                hit_url = "https://www.pivotaltracker.com/services/v5/projects/" + p_id + "/search?"
                req_date = int(sys.argv[1])
                query_date = datetime.today() - timedelta(days=req_date)
                query = hit_url + 'query=owner:"'+u_name+'" and state:' + state
                # Accepted Stories GET req to API
                if state is 'Accepted':
                    query = hit_url+'query=accepted_since:"'+str(query_date.day)+'-'+str(query_date.month)+\
                            '-' +str(query_date.year) +'" and owner:"'+u_name+'" and state:' + state

                response = requests.get(query, headers=headers)
                res_json = ast.literal_eval(response.text).get('stories').get('stories')
                lt = len(res_json)

                print state
                for x in range(lt):
                    result = res_json[x]
                    story = result.get('name')
                    story_type = result.get('story_type')
                    estimate = str(result.get('estimate'))
                    # Change Date Format
                    created_date = datetime.strptime((result.get('created_at').split('T')[0]), "%Y-%m-%d")
                    created_at = datetime.strftime(created_date, "%d-%b-%Y")
                    accepted_date = result.get('accepted_at')
                    if accepted_date is not None:
                        accepted_date = datetime.strptime((result.get('accepted_at').split('T')[0]), "%Y-%m-%d")
                        accepted_at = datetime.strftime(accepted_date, "%d-%b-%Y")
                    else:
                        accepted_at = "NA"
                    table = story + " - " + story_type + " Estimate:[" + estimate + "] Created:[" \
                            + created_at + "] Accepted:[" + accepted_at + "]"
                    print table
                print ""
