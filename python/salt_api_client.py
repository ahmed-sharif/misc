import requests

args = [{
            'client': 'local',
            'tgt': 'hostname-1',
            'fun': 'test.ping',
}]

headless_username = "user"
headless_user_password = "password"
salt_master = "ela4.master.salt.linkedin.com"
port = 1234
payload = {'username': headless_username, 'password': headless_user_password, 'eauth': 'ldap'}
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
root_url = 'https://{master}:{port}'.format(master=salt_master, port=port)
minion_url = 'https://{master}:{port}/minions'.format(master=salt_master, port=port)
response = requests.post(url='{0}/login'.format(self.root_url), data=json.dumps(payload), headers=headers, verify=False)
token = response.headers.get('X-Auth-Token')
headers = {'X-Auth-Token': token, 'Content-type': 'application/json', 'Accept': 'application/json'}
response = requests.post(url='{0}'.format(minion_url), data=json.dumps(payload), headers=headers, verify=False)
print response.content