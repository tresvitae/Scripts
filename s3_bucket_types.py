import boto3
from boto3 import client, resource
import uuid

s3_client = client('s3')
s3_resource = resource('s3')

#Create bucket methods
def create_bucket_name(bucket_prefix):
    return ''.join([bucket_prefix, str(uuid.uuid4())])

def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
        'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response


#ACL

#versioning

#encryption

#storage type
#tagi ec2 a nie ma szyfrowania ssl
#glupia nawzwa - zla konwencja