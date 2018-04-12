#a bitbucket api-val leszedett json filet dolgozza fel
# fontos hogy pagelen is legyen a GET-ben: https://api.bitbucket.org/2.0/repositories/#{repo neve}?pagelen=100

import csv
import json

with open('bitbucket_repos_all.json', 'r') as bb_file:    
    adat = json.load(bb_file)
    val=adat["values"]

    with open('bb_adatok_.csv', 'w', newline='') as f:
        fieldnames = ["name","project","language","mainbranch","full_name","owner","updated_on","type","slug","is_private","description"]
        #fieldnames = ["name", "language"]
        wr = csv.DictWriter(f, fieldnames=fieldnames)
        wr.writeheader()
        
        for x in val:
            tiszta={}
            for k, v in x.items():
                t=''
                if k in fieldnames:
                    if k=="project" or k=="mainbranch":
                        try:
                            t=v["name"] 
                        except(TypeError):
                            pass
                    elif k=="owner":
                        try:
                            t=v["username"] 
                        except(TypeError):
                            pass
                    else:
                        t=v
                    tiszta.update({k:t})
            wr.writerow(tiszta)
                
