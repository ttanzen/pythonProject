import subprocess

ip_list = ['1.1.1.1', '192.168.10.10', '1.1.1.2', '192.168.10.12', '1.1.1.14']

def ping_ip_addresses(ip_addr_list):
    reach = []
    unreach = []
    for ip in ip_addr_list:
        result = subprocess.run(['ping', '-c', '3', ip], stderr=subprocess.PIPE, encoding='utf-8')
        if result.returncode == 0:
           reach.append(ip)
        else:
           unreach.append(ip)
    return (reach, unreach,)


if __name__ == "__main__":
   print(ping_ip_addresses(ip_list))