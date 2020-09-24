import requests, sys, json

YOUR_DT_API_URL = 'https://ENV_ID.live.dynatrace.com';
YOUR_DT_API_TOKEN = 'TOKEN';

if not len(sys.argv) == 2:
  print("Please provide Email address to look for as argument")
  exit(1)

EMAIL = sys.argv[1]
found = False

r1 = requests.get(YOUR_DT_API_URL + '/api/config/v1/notifications?Api-Token=' + YOUR_DT_API_TOKEN)
data1 = r1.json()

for integration in data1['values']:
  if integration['type'] == "EMAIL":
    r2 = requests.get(YOUR_DT_API_URL + '/api/config/v1/notifications/{}?Api-Token='.format(integration['id']) + YOUR_DT_API_TOKEN)
    data2 = r2.json()
    id = integration['id']

    if EMAIL in data2['receivers']:
      found = True
      print("Found {} as receiver in integration {}/#settings/integration/notification/integrationemail;id={};gf=all".format(EMAIL, YOUR_DT_API_URL, id))
    if EMAIL in data2['ccReceivers']:
      found = True
      print("Found {} as cc-receiver in integration {}/#settings/integration/notification/integrationemail;id={};gf=all".format(EMAIL, YOUR_DT_API_URL, id))
    if EMAIL in data2['bccReceivers']:
      found = True
      print("Found {} as bcc-receiver in integration {}/#settings/integration/notification/integrationemail;id={};gf=all".format(EMAIL, YOUR_DT_API_URL, id))

if not found:
  print("Couldn't find {} in any Email integration.".format(EMAIL))