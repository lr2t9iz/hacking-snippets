import requests
import sys

domain = sys.argv([1])
sub_file = sys.argv([2])

sub_list = open(sub_file).read()
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{domain}"
    try:
        requests.get(sub_domains)
    except requests.ConnectionError:
        pass
    else:
        print("Valid Domain: ",sub_domains)
