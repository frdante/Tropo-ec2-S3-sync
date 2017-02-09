from itty import *
from datetime import datetime
import json
import urllib , urllib2
import os
import boto3

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)

# You Amazon credentials
s3 = boto3.client(
    's3',
    aws_access_key_id ='YOUR_S3_KEY',
    aws_secret_access_key ='YOUR_S3_SECRET_KEY'
)

@post('/')
def index(request):
    response =  request.body
    headers = request.headers
    data = json.loads(response)
    print "incoming data", data
    with open("json.txt","w+") as filetest:
        json.dump(data, filetest)

    with open("json.txt", "rb") as f:
        s3.upload_fileobj(f, "YOUR_BUCKET_NAME_HERE", "cdr_{0}.txt".format(datetime.utcnow()))

    filepath = dname + "/json.txt"
    os.remove(filepath)

    return 'Ok'

run_itty(host=os.getenv('IP', '0.0.0.0') , port=int(os.getenv('PORT', 8888)))
