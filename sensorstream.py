import json
import datetime
import random
import boto3
from botocore.config import Config

my_config = Config(
    region_name = 'us-west-2',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

kinesis = boto3.client('kinesis', config=my_config)

def getData(iotName, lowVal, highVal):
   data = {}
   data["iotName"] = iotName
   data["iotValue"] = random.randint(lowVal, highVal) 
   return data

while 1:
   rnd = random.random()
   if (rnd < 0.01):
      data = json.dumps(getData("DemoSensor", 100, 120))  
      kinesis.put_record(StreamName="RawStreamData", Data=data, PartitionKey="DemoSensor")
      print('***************************** anomaly ************************* ' + data)
   else:
      data = json.dumps(getData("DemoSensor", 10, 20))  
      kinesis.put_record(StreamName="RawStreamData", Data=data, PartitionKey="DemoSensor")
      print(data)
