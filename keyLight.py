import requests
import json

elGatoIp = "x.x.x.x"

lightSetup = {
    "on" : 1, # '0' for off, '1' for on
    "brightness" : 50, # from 2 to 100 (%)
    "temperature" : 178 # notYetIdentified the relation between °kelvin and the passed value XD !!! from 143 (7000°K) to 343 (2900°K)
}

if (lightSetup.get("on", 0) == 0):
    bodyContent = '{"numberOfLights": 1,"lights": [{"on": 0}]}'
else:
    bodyContent = '{"numberOfLights": 1,"lights": [' + json.dumps(lightSetup) + ']}'

response = requests.put("http://{}:9123/elgato/lights".format(elGatoIp), bodyContent)
