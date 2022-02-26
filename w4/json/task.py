
'''
Using data file sample-data.json, create output that resembles the following by parsing the included JSON file.

Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 
'''

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