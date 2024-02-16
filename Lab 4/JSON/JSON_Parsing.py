import json

with open('C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 4\JSON\sample-data.json') as f:
    data = json.load(f)

interfaces = data['imdata']

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU   ")
print("-------------------------------------------------- --------------------  ------  ------")

for iface in interfaces:
    dn = iface['l1PhysIf']['attributes']['dn']
    descr = iface['l1PhysIf']['attributes'].get('descr', '')
    speed = iface['l1PhysIf']['attributes']['speed']
    mtu = iface['l1PhysIf']['attributes']['mtu']
    print(f"{dn:58} {descr:<13} {speed:<8} {mtu}")