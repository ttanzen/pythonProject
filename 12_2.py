import ipaddress
list1 = ["10.1.1.1", "10.4.10.10-13", "192.168.1.12-192.168.1.15"]


def convert_ranges_to_ip_list(ip_range_list):
    result = []
    for ip_range in ip_range_list:
        try:
           ipaddress.ip_address(ip_range)
        except ValueError:
            try:
               ipaddress.ip_address(ip_range.split('-')[-1])
            except ValueError:
                last_num = ip_range.split('-')[-1]
                first_ip = ipaddress.ip_address(ip_range.split('-')[0])
                last_ip =  '.'.join(str(first_ip).split('.')[:-1] + [last_num])
                last_ip = ipaddress.ip_address(last_ip)
                for ip in range(int(first_ip),int(last_ip)+1):
                    result.append(str(ipaddress.ip_address(ip)))
            else:
                ip1 = ipaddress.ip_address(ip_range.split('-')[0])
                ip2 = ipaddress.ip_address(ip_range.split('-')[-1])
                for ip in range(int(ip1),int(ip2)+1):
                    result.append(str(ipaddress.ip_address(ip)))



        else:
            result.append(ip_range)
    return result


print(convert_ranges_to_ip_list(list1))