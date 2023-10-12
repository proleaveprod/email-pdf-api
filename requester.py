import requests

CANTEST_STARLINE_IP        = '10.100.9.11'
FRM01_PROD_CAN_RD_NETLO_IP = '10.50.28.238'
#frm01-prod-can.rd.netlo

host_ip   = 'frm01-prod-can.rd.netlo'
host_port = 5252

url = f'http://{host_ip}:{host_port}/yandex_request'

# myobj = {'somekey': 'somevalue'}
# x = requests.post(url, json = myobj)

x = requests.post(url)

print(x.text)