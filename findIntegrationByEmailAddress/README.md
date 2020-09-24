# Find Integration by Email Address
This script helps searches through all configured integration in your Dynatrace tenant and returns direct links to those integrations, where the provided Email address is either a receiver, a CC receiver, or a BCC receiver.

## Prerequisites
You need to know your environment ID and you need to have an API token that has the access scope "Read configuration".

## Get Started
Replace the placeholders in the script with the actual values of your environment ID and API token. Then execute the script and pass the Email address you're looking for as an argument, e.g.

```
$ python findIntegrationByEmail.py my@email.com
```

If the Email address is found in an integration a direct link to that integration will be printed to the console, e.g.

```
$ python findIntegrationByEmail.py my@email.com
Found my@email.com as receiver in integration https://ENV_ID.live.dynatrace.com/#settings/integration/notification/integrationemail;id=ID;gf=all
$
```