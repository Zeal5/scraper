
import requests
import json



def retrive_messages(channelid):
    message_id = 'message_id_here'
    headers = {'authorization' : 'authtoken here'
            }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers = headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        if value['id'] == message_id:
            return(value['content'],'\n')
        
retrive_messages('channelid')
    