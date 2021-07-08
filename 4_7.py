mac = "AAAA:BBBB:CCCC"
mac1 = int(mac.replace(":", ""), 16)
mac2 = "{:b}".format(mac1)
print(mac2)
