import glob
import csv
import re

def parse_sh_version(sh_vers):
    regex1 = re.compile(r'^Cisco IOS Software, .*Version (?P<ios>\S+)')
    regex2 = re.compile(r'System image file is "(?P<image>\S+)"')
    regex3 = re.compile(r'uptime is (?P<uptime>.*$)')

    result = []
    for i in sh_vers.split('\n'):
        match1 = regex1.search(i)
        match2 = regex2.search(i)
        match3 = regex3.search(i)
        if match1:
            result.append(match1.group('ios').rstrip(','))
        elif match2:
            result.insert(1,match2.group('image'))
        elif match3:
            result.append(match3.group('uptime'))
    return tuple(result)


sh_version_files = glob.glob("sh_vers*")
# print(sh_version_files)


def write_inventory_to_csv(data_filenames, csv_filename):
 headers = ["hostname", "ios", "image", "uptime"]
 with open (csv_filename, 'w') as dest:
  result = []

  for file in  data_filenames:
    host = re.search('sh_version_([^/]+).txt', file).group(1)
    with open (file) as f:
        sh_vers = f.read()
        result.append([host] + list(parse_sh_version(sh_vers)))

  result.insert(0, headers)
  print (result)
  writer = csv.writer(dest)
  writer.writerows(result)


if __name__ == "__main__":
#    files = ['sh_version_r1.txt', 'sh_version_r2.txt', 'sh_version_r3.txt']
    write_inventory_to_csv(sh_version_files, '17_2.csv')