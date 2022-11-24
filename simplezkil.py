import websocket
from discord import SyncWebhook
from websocket import create_connection
import json
from bs4 import BeautifulSoup
import time

# Add your Corp or Alliance ID
allianceID = 99001105
corporationID = 98512964
allalliancekillswebhookurl = "https://discord.com/api/webhooks/1040550494185209948/t6cmlErFvq95y61g-hClAFAADiZWMdMKtwIxQ7M1qaLPjqUM42vdAaAnG_9GYzoCm14v"

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


