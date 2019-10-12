############# REquest the REST structure from URL ##########
import urllib.request

def get_stuff():
    with urllib.request.urlopen('http://localhost:5000/todo/api/v1.0/tasks') as response:
       html = response.read()
       #print(html)
       return html


def analyze_stuff(stuff):
    import json
    stuff = stuff.decode('utf8').replace("'", '"')
    y = json.loads(stuff)
    s = json.dumps(y, indent=4, sort_keys=True)
    print('##########')
    subitem = y['tasks']
    for item in subitem:
        for  key in item.keys():
            print(str(key) + ":"+ str(item[key]))
        print ('#########')
    #print(s)



if __name__ == "__main__":
    stuff = get_stuff()
    analyze_stuff(stuff)
    print("DONE")
