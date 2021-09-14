## MerakiTimelapse
If you need to create timelapse for one or five years using Meraki Camere, this code can help you to take snapshot each few minutes,hours or even dayes.
This script will create folder foreach camera to save snapshots inside, the folder name will use camera serialnumber.

**How to use it?**
It's recommended to use env, follow below steps:

 1. run command `pip3 install meraki`
 2. run command `pip3 install install apscheduler` for schadule 
 3. Edit main.py `API_KEY` 
 4. Edit main.py `scheduler_minutes` how many minutes between each snapshot 
 5. Edit main.py `serialNumbers` add list of cameras serialnumbers 
 6. Incase create folder `cameras` , where will we save images. 
 7. Run main.py `python3 main.py`  

**How to create a vide?**
just run `python3 create_video.py` 
@ the terminal will ask for which camera serialnumber, and how many frames per second, this will create file mp4 at cameras folder


**Special Thanks!**
[@malshaer-meraki](https://github.com/malshaer-meraki) 