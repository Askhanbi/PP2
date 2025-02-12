# JSON   Task 1
import json

data = open('sample-data.json').read()
object = json.loads(data) 
print (
    "================================================================================" "\n"
    "DN                                                 Description           Speed    MTU" "\n" 
    "-------------------------------------------------- --------------------  ------  ------"
)
data2 = object["imdata"]
for i in data2:
     a = i['l1PhysIf']['attributes']
     print("{0:42} {1:28} {2:10} {3:4}".format(a["dn"],a["descr"],a["speed"],a["mtu"])) 





# l1PhysIf     attributes