access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
template = {"access": access_template, "trunk": trunk_template}
variant = {"access": "Введите номер VLAN: ", "trunk": "Введите разрешенные VLANы: "}
inter = input('Выберите интерфейс (access/trunk): ')
tn = input('Выберите тип и номер интерфейса: ')
vl = input(variant[inter])
print(f"tn{tn}")
print("\n".join(template[inter]).format(vl))