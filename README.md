## MerakiTimelapse
If you need to create timelapse for one or five years using Meraki Camere, this code can help you to take snapshot each few minutes,hours or even dayes.
This script will create folder foreach camera to save snapshots inside, the folder name will use camera serialnumber.

**How to use it?**
It's recommended to use env, follow below steps:

 1. run command `pip3 install meraki`
 2. run command `pip3 install install apscheduler` for schadule 
 3. Edit main.py `API_KEY` 
 4. Edit main.py `scheduler_minutes`
 5. Edit main.py `serialNumbers` add list of cameras serialnumbers 

**Special Thanks!**
[@malshaer-meraki](https://github.com/malshaer-meraki) 