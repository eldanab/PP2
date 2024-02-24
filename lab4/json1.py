import json
j = open('sample-data.json').read()
i = json.loads(j)
print(
    "=======================================================================================" "\n"
    "DN                                                 Description           Speed    MTU" "\n" 
    "-------------------------------------------------- --------------------  ------  ------")
data = i["imdata"]
for i in data:
        dn = i["l1PhysIf"]["attributes"]["dn"]
        des = i["l1PhysIf"]["attributes"]["descr"]
        sp = i["l1PhysIf"]["attributes"]["speed"]
        mtu = i["l1PhysIf"]["attributes"]["mtu"]
        print("{0:50} {1:20} {2:7} {3:6}".format(dn,des,sp,mtu))