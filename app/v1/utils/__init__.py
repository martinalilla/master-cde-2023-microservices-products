import base64
import json



def decode_base64(data: str):
    return base64.b64decode(data + '==').decode('utf8')

def decode_base64_dict(data: str):
    return json.loads(decode_base64(data))

def to_dict(self):
    return json.loads(json.dumps(self, default=lambda o: o.__dict__))