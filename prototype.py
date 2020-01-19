import sys
import random
from pprint import pprint


def make_node(key, unique=False):
    if unique:
        # allow equal keys in dict
        second_item = random.random()
    else:
        second_item = None

    return key, second_item


def insert_ip_as_list(ip_as_list, ip_tree):
    prefix = ip_as_list.pop(0)
    if not ip_as_list:   # terminate tree
        ip_tree[prefix] = None
        return

    # init branch in tree
    if prefix not in ip_tree:
        ip_tree[prefix] = {}

    insert_ip_as_list(ip_as_list, ip_tree[prefix])


def load_data(file_path):
    ip_tree = {}

    with open(file_path) as f:
        for line in f:
            line = line.rstrip()
            ip, _, _ = line.split()
            ip_as_list = [int(part) for part in ip.split('.')]
            ip_as_nodes_list = [make_node(addr_part) for addr_part in ip_as_list]
            ip_as_nodes_list[3] = make_node(ip_as_list[3], unique=True) # allow dups
            insert_ip_as_list(ip_as_nodes_list, ip_tree)

    return ip_tree


def print_addr(addr_parts):
    print('.'.join(str(part[0]) for part in addr_parts))


def print_tree_sorted(accumulated_prefixes, ip_tree):
    if not ip_tree:   # leave case
        print_addr(accumulated_prefixes)
        return

    for prefix, subtree in sorted(ip_tree.items(), reverse=True):
        print_tree_sorted(accumulated_prefixes + [prefix], subtree)


ip_tree = load_data(sys.argv[1])
print_tree_sorted([], ip_tree)
print_tree_sorted(
    [(1, None)],
    ip_tree[(1, None)]
)

print_tree_sorted(
    [(46, None), (70, None)],
    ip_tree[(46, None)][(70, None)]
)
