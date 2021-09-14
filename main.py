import meraki
import time
import os
import requests
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

API_KEY = 'e225e5c727d6107b15b89b0bae02aba45e106176'
#cameras 
serialNumbers= ['Q2NV-6XBT-YECK']
dashboard = None

#Ask Meraki API to generate Snapshot
def getSnip(serial):
    return dashboard.camera.generateDeviceCameraSnapshot(serial)

#Check if this link is downloadable
def is_downloadable(url):
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

#download Image
def download(url,device):
    #creat folder foreach camera
    if not os.path.exists('cameras/'+device):
        os.makedirs('cameras/'+device)
    ts=time.time()
    localFile='cameras/'+device+"/"+str(ts)+ ".jpeg"
    response = requests.get(url)
    file = open(localFile, "wb")
    file.write(response.content)
    file.close()
    print("downloaded: "+localFile)

#startApp
scheduler = BlockingScheduler()
@scheduler.scheduled_job(IntervalTrigger(minutes=2))
def startApp():
    global dashboard
    dashboard = meraki.DashboardAPI(API_KEY,print_console=False,suppress_logging=True)
    for device in serialNumbers:
        response = getSnip(device)
        if(is_downloadable(response['url'])):
            print("Yes You can download.")
            download(response['url'],device)


#run scaduler 
scheduler.start()