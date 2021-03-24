import json
import requests

def get_activity(username, password, token):
    if password:
        headers ={
            'Password': password,
            }
    else:
        headers ={
            'Authorization': token,
            }

    url = 'https://api.github.com/users/' + username + '/received_events'
    response = requests.get(url, headers=headers) 
    data = response.json()
    event_actions = {'WatchEvent': 'starred', 'PushEvent': 'pushed to'}

    for event in data:
        if event['type'] in event_actions:
            name = event['actor']
            name = name['display_login']
            action = event_actions[event['type']] 
            repo = event['repo']['name'] 
            print (name + ' ' + action + repo)

    if event['type'] == 'ForkEvent':
        name = event['actor']
        name = name['display_login']
        repo = event['repo']['name']  
        forked_repo = event['payload']['forkee']['full_name'] 
        print (name + ' forked ' + forked_repo + ' from ' + repo)

if __name__=='__main__':
    githubUsername = input('Enter Github username: ')
    tokenRequired = input('Do you have a personal access token (PAT)? (Y/n)')
    authToken = githubPassword = None
    if tokenRequired in 'Yy':
        authToken = input('Enter your personal access token: ')
        authToken = 'token ' + authToken
    else:
        githubPassword = input('Enter your password: ')
        githubPassword = 'password ' + githubPassword
    get_activity(githubUsername, githubPassword, authToken)
    