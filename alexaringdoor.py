from ring_doorbell import Ring
import simpleaudio as sa
from time import sleep
import configparser

ringUsername=None
ringPassword=None

# Read PropertiesFile
try:
    config = configparser.ConfigParser()
    config.read("alexaringdoor.ini")
    ringUsername=config.get('AlexaRing','ringUsername')
    ringPassword=config.get('AlexaRing','ringPassword')
    goHomeMessageTimeout=60 
except configparser.NoOptionError as err:
    print('Error : Getting section from alexaringdoor.ini ')
    print("Error : {0}".format(err))
    exit()

if ringUsername is None or ringPassword is None:
    print('Error : Either ringUsername or ringPassword not defined')

# Read PropertiesFile
print('Settings from alexaringdoor.ini file read')
print('ringUsermame = %s' % ringUsername)

myring = Ring(ringUsername,ringPassword)

if myring.is_connected==False:
    print ("Ring Connection Not Successful".format(myring.is_connected))
    sleep(30)
    quit()
else:
    print("Ring Connection Successful")
# Now loop infinitely
while(1):
    print ("scanning")
    data = myring.doorbells[0].check_alerts()
    print (data)
    if data==True:
        # Doorbell rang play sound file
        lastEvent=myring.doorbells[0].history(limit=100)[0]
        print('ID:       %s' % lastEvent['id'])
        print('Kind:     %s' % lastEvent['kind'])
        print('Answered: %s' % lastEvent['answered'])
        print('When:     %s' % lastEvent['created_at'])
        if lastEvent['kind']=='ding':
            wave_obj = sa.WaveObject.from_wave_file('AlexaShowFrontDoorSound.wav')                 
            play_obj = wave_obj.play()
            play_obj.wait_done()
            # Sleep 60 Seconds waiting for video etc, then go back home
            sleep(goHomeMessageTimeout)
            print ("{0} Seconds up , go Home".format(goHomeMessageTimeout))
            wave_obj = sa.WaveObject.from_wave_file('AlexaHomeSound.wav')
            play_obj = wave_obj.play()
            play_obj.wait_done()
    # Loop around
    sleep(1)
