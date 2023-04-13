import json

with open('1.json', 'r') as f:
    data = json.load(f)
    w = data['result']['hits']
    ips = ['http://' + hit['ip'] for hit in w]
    # print (ips)
ip='\n'.join(ips)
print(str(ip))
