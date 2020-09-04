# Deprecated

This repo is now deprecated given the Amazon now added the functionality OOTB to the echo show devices. This script does offer some more flexibility and may be useful to someone in the future


# Alexa Ring Doorbell add on for Alexa Show

I like that on my alexa show I can say "Alexa Show me the front door" and see the video feed from the front door, but Im surprised that Alexa/Ring dont have a skill which allows this. I think its because Alexa skills cant execute anything on the alexa WITHOUT a human asking it.. 

My workaround is to have a small program polling for the doorbell ding and when it occurs then play a sound file , on a small speaker, near the alexashow. When this happens the echo show , shows the doorbell video. 

After 60 seconds (configurable) the Pi will tell the echo show to stop showing the doorbell video.


## Hardware

1. Any device which can run python 3 . e.g. RaspberryPi or C.H.I.P
2. Speaker connected to Linux device
3. Echo Show , (may work on a echo spot but I havent tested this)

## Installation

1. Clone the git repository
```
git clone https://github.com/asantaga/alexashowRing
```
2. Create a file called alexaringdoor.ini, within this file add the following modifying the username/password to your values
e.g.

```
[AlexaRing]
ringUsername=someusername@gmail.com
ringPassword=YourPassword
goHomeMessageTimeout=30
```
The goHomeMessageTimeout dictates the timeout before the Pi asks the alexashow show to go home

3. Record your own versions of *AlexaShowFrontDoorSound.wav* and *AlexaHomeSound.wav* , or if you like you can keep my dulcit tones!
4. Modify *alexaringdoor.service* file to match your system paths
5. Execute the following commands, this enables the app run on boot
```
sudo systemctl enable alexaringdoor.service
sudo systemctl start  alexaringdoor.service
```

Enjoy!, let me know if this is useful
