# Here you can define/import your db connection and return it to the caller
from v1.config import Settings, get_config

_config: Settings = get_config()

class DynamoDBClient:
    def __init__(self):
        #TODO Use the AWS SDK for Python (Boto3) with DynamoDB to get the client
        self.db = ""
        
 

def get_dynamodb_client() -> DynamoDBClient:
    return DynamoDBClient()