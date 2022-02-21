import requests
from receive import retrive_messages


message = retrive_messages('832396513367687183')


channelid = '945008964628774995'

payload = {
    'content': message
}
header = {
    'authorization': 'authtoken here'
}


r = requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', data = payload , headers = header )
