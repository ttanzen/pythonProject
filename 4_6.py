ospf_route = "10.0.24.0/24 [110/41] via 10.0.13.3 3d18h FastEthernet0/0"

n2 =ospf_route.split()
print('Prefix:  ' + n2[0])
print('AD/Metric:  '+n2[1])
print('Next-Hop:  ' + n2[3])
print('Last update:  ' + n2[4])
print('Outbound Interface:  ' + n2[5])