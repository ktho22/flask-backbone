import requests
import itertools
import time

s = requests.session()

ip_address = 'http://0.0.0.0:8081'

aa = time.time()
ss = 'sentence example'
r = s.post(ip_address, data={'sentence': ss})
print('It takes {}s'.format(time.time() - aa))
