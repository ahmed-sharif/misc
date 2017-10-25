import requests
import json
import time
import pprint


headless_username = "svc-netops-nurse"
headless_user_password = ""
salt_master = "lca1-netops01.corp.linkedin.com"
port = 8080

root_url = 'http://{master}:{port}'.format(master=salt_master, port=port)
minion_url = 'http://{master}:{port}/minions'.format(master=salt_master, port=port)
jobs_url = 'http://{master}:{port}/jobs'.format(master=salt_master, port=port)


def print_all(res):
    
    print "###############"
    print res.content
    print res.headers
    print res.status_code
    data = res.json()
    pprint.pprint(data)
    print
    print "###############"


def login_failure():
    #############################
    print "Check login failure"
    payload = {'username': "headless_username", 'password': "headless_user_password", 'eauth': 'auto'}
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(url='{0}/login'.format(root_url), data=json.dumps(payload), headers=headers, verify=False)
    print_all(response)

def login_success():
    ############################
    print "Check login success"
    payload = {'username': headless_username, 'password': headless_user_password, 'eauth': 'auto'}
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(url='{0}/login'.format(root_url), data=json.dumps(payload), headers=headers, verify=False)
    print_all(response)
    data = response.json()
    token = data['return'][0]['token']
    return token


def successful_commmand_testping(token):
    print "Check test.ping"
    headers = {'X-Auth-Token': token, 'Content-type': 'application/json', 'Accept': 'application/json'}
    # payload = {'fun': 'test.ping', 'tgt': '*'}
    # payload = {'fun': 'disk.inodeusage', 'tgt': "*"}
    # response = requests.post(url='{0}'.format(minion_url), data=json.dumps(payload), headers=headers, verify=False)
    tgt = "*"
    job_args = {}
    payload ={
      'tgt': tgt,
      'fun': "test.ping",
      'arg': ['='.join([k, str(v)]) for (k, v) in job_args.items()],
    }
    response = requests.post(url='{0}'.format(minion_url), data=json.dumps(payload), headers=headers, verify=False)
    print_all(response)
    data = response.json()
    jid = data['return'][0]['jid']
    response = requests.get(url='{0}/{1}'.format(jobs_url, jid), headers=headers, verify=False)
    print_all(response)


def successful_commmand_inode(token):
    print "Check disk.inodeusage"
    headers = {'X-Auth-Token': token, 'Content-type': 'application/json', 'Accept': 'application/json'}
    # payload = {'fun': 'test.ping', 'tgt': '*'}
    # payload = {'fun': 'disk.inodeusage', 'tgt': "*"}
    # response = requests.post(url='{0}'.format(minion_url), data=json.dumps(payload), headers=headers, verify=False)
    tgt = "*"
    job_args = {}
    payload ={
      'tgt': tgt,
      'fun': "disk.inodeusage",
      'arg': ['='.join([k, str(v)]) for (k, v) in job_args.items()],
    }
    response = requests.post(url='{0}'.format(minion_url), data=json.dumps(payload), headers=headers, verify=False)
    print_all(response)
    data = response.json()
    jid = data['return'][0]['jid']
    response = requests.get(url='{0}/{1}'.format(jobs_url, jid), headers=headers, verify=False)
    print_all(response)


def invalid_commmand(token):
    print "Check diskinodeusage"
    headers = {'X-Auth-Token': token, 'Content-type': 'application/json', 'Accept': 'application/json'}
    # payload = {'fun': 'test.ping', 'tgt': '*'}
    # payload = {'fun': 'disk.inodeusage', 'tgt': "*"}
    # response = requests.post(url='{0}'.format(minion_url), data=json.dumps(payload), headers=headers, verify=False)
    tgt = "*"
    job_args = {}
    payload ={
      'tgt': tgt,
      'fun': "diskinodeusage",
      'arg': ['='.join([k, str(v)]) for (k, v) in job_args.items()],
    }
    response = requests.post(url='{0}'.format(minion_url), data=json.dumps(payload), headers=headers, verify=False)
    print_all(response)
    data = response.json()
    jid = data['return'][0]['jid']
    response = requests.get(url='{0}/{1}'.format(jobs_url, jid), headers=headers, verify=False)
    print_all(response)


def invalid_minion(token):
    print "Check invalid minion"
    headers = {'X-Auth-Token': token, 'Content-type': 'application/json', 'Accept': 'application/json'}
    # payload = {'fun': 'test.ping', 'tgt': '*'}
    # payload = {'fun': 'disk.inodeusage', 'tgt': "*"}
    # response = requests.post(url='{0}'.format(minion_url), data=json.dumps(payload), headers=headers, verify=False)
    tgt = "asdfasd"
    job_args = {}
    payload ={
      'tgt': tgt,
      'fun': "test.ping",
      'arg': ['='.join([k, str(v)]) for (k, v) in job_args.items()],
    }
    response = requests.post(url='{0}'.format(minion_url), data=json.dumps(payload), headers=headers, verify=False)
    print_all(response)
    data = response.json()
    jid = data['return'][0]['jid']
    response = requests.get(url='{0}/{1}'.format(jobs_url, jid), headers=headers, verify=False)
    print_all(response)



def test_time_minion(token):
    print "Check time.sleep"
    headers = {'X-Auth-Token': token, 'Content-type': 'application/json', 'Accept': 'application/json'}
    # payload = {'fun': 'test.ping', 'tgt': '*'}
    # payload = {'fun': 'disk.inodeusage', 'tgt': "*"}
    # response = requests.post(url='{0}'.format(minion_url), data=json.dumps(payload), headers=headers, verify=False)
    tgt = "*"
    job_args = {}
    job_args = {"length": 60}
    payload ={
      'tgt': tgt,
      'fun': "test.sleep",
      'arg': ['='.join([k, str(v)]) for (k, v) in job_args.items()],
    }
    response = requests.post(url='{0}'.format(minion_url), data=json.dumps(payload), headers=headers, verify=False)
    print_all(response)
    data = response.json()
    jid = data['return'][0]['jid']
    response = requests.get(url='{0}/{1}'.format(jobs_url, jid), headers=headers, verify=False)
    print_all(response)
    print "############### waiting for 60 ########"
    import time
    time.sleep(60)
    response = requests.get(url='{0}/{1}'.format(jobs_url, jid), headers=headers, verify=False)
    print_all(response)


"""
try:
    login_failure()
except Exception, e:
    print (str(e))
"""
token = login_success()
# successful_commmand_testping(token)
# successful_commmand_inode(token)
#invalid_commmand(token)
#invalid_minion(token)
test_time_minion(token)




