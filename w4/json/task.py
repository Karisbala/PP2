import json

print('''
Interface Status
======================================================================================
#    DN                                           Description           Speed    MTU  
--- -------------------------------------------- --------------------  -------- ------
''', end = '')

num = 0

data = json.loads(open('sample_data.json').read())
imdata = data["imdata"]

for i in imdata:

    dn = i["l1PhysIf"]["attributes"]["dn"]
    descr = i["l1PhysIf"]["attributes"]["descr"]
    speed = i["l1PhysIf"]["attributes"]["speed"]
    mtu = i["l1PhysIf"]["attributes"]["mtu"]
    num += 1    

    print("{0:3} {1:44} {2:21} {3:8} {4:7}".format(num, dn, descr, speed, mtu))