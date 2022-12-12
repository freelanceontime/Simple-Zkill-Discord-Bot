from discord import SyncWebhook
from websocket import create_connection
import json

# Add your Corp or Alliance ID
allianceID = 99001105
corporationID = 98512964
allalliancekillswebhookurl = ""

global toggle
toggle = False

def getkill():

    print("New Connection Established")
    ws = create_connection("wss://zkillboard.com/websocket/")

    # Comment Out Either the Alliance or Corp
    ws.send('{"action":"sub","channel":"alliance:' + str(allianceID) + '"}')
    #ws.send('{"action":"sub","channel":"corporation:' + str(corporationID) + '"}')

    while True:
        urls = []
        result =  ws.recv()
        data = json.loads(result)
        urls.append(data['url'])

        for i in range(len(urls)): 
          
            killid = (str(urls[i]))
            webhook = SyncWebhook.from_url(allalliancekillswebhookurl) 
            webhook.send(killid)

while True:
    try:
        getkill()
    except:
        print("Connection Lost")
        pass


