command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

c1 = command1.split()[-1].split(',')
c2 = command2.split()[-1].split(',')
r1 = set(c1)
r2 = set(c2)
result = sorted(r1 & r2)
print(result)