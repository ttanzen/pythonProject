import re
import yaml
from z17_3 import parse_sh_cdp_neighbors


files = ['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt', 'sh_cdp_n_r4.txt', 'sh_cdp_n_r5.txt', 'sh_cdp_n_r6.txt']

def generate_topology_from_cdp(list_of_files, save_to_filename=None):
   result = {}
   for file in list_of_files:
       with open (file) as f:
           result.update(parse_sh_cdp_neighbors(f.read()))
   if save_to_filename:
       with open(save_to_filename, 'w') as y:
           yaml.dump(result, y, default_flow_style=False)
   return result

if __name__ == "__main__":
    print(generate_topology_from_cdp(files, 'topology.yaml'))