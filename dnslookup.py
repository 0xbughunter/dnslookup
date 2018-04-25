from dns import resolver, reversename
import requests
import json


dns_query = ['A', 'NS', 'MX', 'SOA', 'PTR', 'CNAME', 'AAAA', 'SPF']

class dnslookup:

    address = []

    def __init__(self, host):
        self.host = host

    def dns_resolver(self):
        print '\n'
        for q in dns_query:
            try:
                print "checking for {0} records".format(q)
                print "====================================="
                data = resolver.query(self.host, q)
                for cap in data:
                    print cap
                    if q == 'A':
                        self.address.append(str(cap))
                print "\n"
            except:
                print "{0} record doesn't exists".format(q)
                print "\n"

    def reverse_lookup(self):
        for adr in self.address:
            print "reverse iplookup data for {0}".format(adr)
            print "==========================================="
            try:
                data = reversename.from_address(adr)
                rdns = resolver.query(data, 'PTR')[0]
                print rdns
                print "\n"
            except:
                print "no host(s) found for {0}".format(adr)
                print "\n"
        self.ip_location()

    def ip_location(self):
        for ipadr in self.address:
            print "Geo Location of {0}".format(ipadr)
            print "==========================================="
            data = requests.get("http://api.db-ip.com/v2/free/{0}".format(ipadr))
            content = json.loads(data.content)
            for key in content:
                print key +" ==> "+ content[key]
            print "\n"


if __name__ == '__main__':
    hostname = raw_input('Enter the host name: ')
    dnslup = dnslookup(hostname)
    dnslup.dns_resolver()
    dnslup.reverse_lookup()