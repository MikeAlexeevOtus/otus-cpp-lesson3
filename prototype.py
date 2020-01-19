import sys
import random
from pprint import pprint


def make_node(key):
    # make node uniq
    # to allow equal keys in dict
    return key, random.random()


def insert_ip_as_list(ip_as_list, ip_tree):
    prefix = ip_as_list.pop(0)
    node = make_node(prefix)
    if not ip_as_list:   # terminate tree
        ip_tree[node] = None
        return

    # init branch in tree
    if prefix not in ip_tree:
        ip_tree[node] = {}

    insert_ip_as_list(ip_as_list, ip_tree[node])


def load_data(file_path):
    ip_tree = {}

    with open(file_path) as f:
        for line in f:
            line = line.rstrip()
            ip, _, _ = line.split()
            ip_as_list = [int(part) for part in ip.split('.')]
            insert_ip_as_list(ip_as_list, ip_tree)

    return ip_tree


def print_tree_sorted(accumulated_prefixes, ip_tree):
    if not ip_tree:   # leave case
        print('.'.join(str(b) for b in accumulated_prefixes))
        return

    for node, subtree in sorted(ip_tree.items(), reverse=True):
        print_tree_sorted(accumulated_prefixes + [node[0]], subtree)


ip_tree = load_data(sys.argv[1])
print_tree_sorted([], ip_tree)
