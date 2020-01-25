import sys


def load_data(stream):
    ips_list = []

    for line in stream:
        line = line.rstrip()
        ip, _, _ = line.split()
        ip_as_list = [int(part) for part in ip.split('.')]
        ips_list.append(ip_as_list)

    return ips_list


def print_addr(ip_parts):
    print('.'.join(str(part) for part in ip_parts))


def print_sorted(ips_list, filter_):
    for ip_as_list in sorted(ips_list, reverse=True):
        if filter_(ip_as_list):
            print_addr(ip_as_list)


ips_list = load_data(sys.stdin)

print_sorted(ips_list, lambda ip_as_list: True)   # print all addresses
print_sorted(ips_list, lambda ip_as_list: ip_as_list[0] == 1)
print_sorted(ips_list,
             lambda ip_as_list:
             ip_as_list[0] == 46 and
             ip_as_list[1] == 70)

print_sorted(ips_list, lambda ip_as_list: any(i == 46 for i in ip_as_list))
