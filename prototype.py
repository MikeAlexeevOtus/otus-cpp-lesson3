import sys
import random


def make_node(value, unique=False):
    if unique:
        # allow equal values as individual keys in dict
        second_item = random.random()
    else:
        second_item = None

    return value, second_item


def insert_ip_parts(ip_parts, ip_tree):
    prefix = ip_parts.pop(0)
    if not ip_parts:   # terminate tree
        ip_tree[prefix] = None
        return

    # init branch in tree
    if prefix not in ip_tree:
        ip_tree[prefix] = {}

    insert_ip_parts(ip_parts, ip_tree[prefix])


def load_data(stream):
    ip_tree = {}

    for line in stream:
        line = line.rstrip()
        ip, _, _ = line.split()
        ip_as_list = [int(part) for part in ip.split('.')]
        ip_as_nodes_list = [make_node(addr_part) for addr_part in ip_as_list]

        # make 3 element unique to allow dups
        ip_as_nodes_list[3] = make_node(ip_as_list[3], unique=True)
        insert_ip_parts(ip_as_nodes_list, ip_tree)

    return ip_tree


def print_addr(ip_parts, filter_):
    # drop unique part of nodes
    ip_parts = [part[0] for part in ip_parts]
    if filter_(ip_parts):
        print('.'.join(str(part) for part in ip_parts))


def print_tree_sorted(ip_tree, filter_, accumulated_ip_parts=None):
    accumulated_ip_parts = accumulated_ip_parts or []

    if not ip_tree:   # leave case
        print_addr(accumulated_ip_parts, filter_)
        return

    for ip_part, subtree in sorted(ip_tree.items(), reverse=True):
        print_tree_sorted(subtree, filter_, accumulated_ip_parts + [ip_part])


ip_tree = load_data(sys.stdin)

print_tree_sorted(ip_tree, lambda ip_parts: True)   # print all addresses
print_tree_sorted(ip_tree, lambda ip_parts: ip_parts[0] == 1)
print_tree_sorted(ip_tree,
                  lambda ip_parts:
                  ip_parts[0] == 46 and
                  ip_parts[1] == 70)

print_tree_sorted(ip_tree, lambda ip_parts: any(i == 46 for i in ip_parts))
