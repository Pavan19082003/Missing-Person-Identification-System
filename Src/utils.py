from encoding import Encode
from recognition import Recognition
import numpy as np
import json
from urllib.request import urlopen
        
        
def encode_folder():
    enc = Encode('./database/missing_persons/')
    enc.names()
    enc.findEncodings()
    enc.save()
    
    
def detect():
    with open('./database/encodings.json') as f:
        data = json.load(f)
        
    eList = []
    cNames = data['classNames']
    for i in range(len(cNames)):
        eList.append(np.array(data['encodeList'][i]))
            
    
    rec = Recognition(eList, cNames)
    status, name = rec.recog()
    return status, name
    
    
def get_coordinates():
    # urlopen("http://ipinfo.io/json")
    # data = json.load(urlopen("http://ipinfo.io/json"))
    lat = 24.456
    lon = 27.342

    return lat, lon
    
    
    
    
    
