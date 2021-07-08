ip = "192.168.3.1"
i1 = ip.replace('.','          ')
print(i1)
i3 = i1.split()
i2 = int(i3[0], 10)
i4 = int(i3[1], 10)
i5 = int(i3[2], 10)
i6 = int(i3[3], 10)
print("{:b}     {:b}     {:b}         {:b}".format(i2, i4, i5, i6))


