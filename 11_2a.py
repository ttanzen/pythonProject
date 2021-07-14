from z11_2 import create_network_map
from draw_network_graph import draw_topology

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

def unique_network_map(topology_dict):
    dubs = []
    dct = topology_dict.copy()
    for key, value in dct.items():
        if key in dct.values() and value not in dubs:
            dubs.append(key)
    for d in dubs:
        del dct[d]


    return dct

if __name__ == "__main__":
   draw_topology(unique_network_map(create_network_map(infiles)), output_filename="z11_2aa")
#  print (unique_network_map(create_network_map(infiles)))