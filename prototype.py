import sys
from pprint import pprint


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
            insert_ip_as_list(ip_as_list, ip_tree)

    return ip_tree


def print_tree_sorted(ip_tree):
    for byte1, subtrees1 in sorted(ip_tree.items(), reverse=True):
        for byte2, subtrees2 in sorted(subtrees1.items(), reverse=True):
            for byte3, subtrees3 in sorted(subtrees2.items(), reverse=True):
                for byte4, _ in sorted(subtrees3.items(), reverse=True):
                    print(byte1, byte2, byte3, byte4)


ip_tree = load_data(sys.argv[1])
print_tree_sorted(ip_tree)
