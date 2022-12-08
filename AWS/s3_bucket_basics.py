import boto3
from boto3 import client, resource
import uuid

s3_client = client('s3')
s3_resource = resource('s3')

#Create bucket
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

first_bucket_name, first_response = create_bucket(
    bucket_prefix='firstbucket', 
    s3_connection=s3_resource.meta.client)

print("Bucket name:", first_bucket_name)
print(first_response)

second_bucket_name, second_response = create_bucket(
    bucket_prefix='secondbucket', s3_connection=s3_resource)

print("Bucket name:", second_bucket_name)
print(second_response)

#Create a file
def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content) * size)
    return random_file_name

first_file_name = create_temp_file(300, 'firstfile.txt', 'f')
second_file_name = create_temp_file(300, 'secondfile.txt', 'f')

#Create Bucket Instances
first_bucket = s3_resource.Bucket(name=first_bucket_name)

#Create Object Instance
first_object = s3_resource.Object(
    bucket_name=first_bucket_name, key=first_file_name)

#Upload a file 
##using Object Instance version
s3_resource.Object(first_bucket_name, first_file_name).upload_file(
    Filename=first_file_name)

##using a Bucket Instance version
s3_resource.meta.client.upload_file(
    Filename=second_file_name, Bucket=first_bucket_name,
    Key=second_file_name)

#Download a file
s3_resource.Object(first_bucket_name, first_file_name).download_file(
    f'/tmp/{first_file_name}')

#Copy an Object between buckets
def copy_to_bucket(bucket_from_name, bucket_to_name, file_name):
    copy_source = {
        'Bucket': bucket_from_name,
        'Key': file_name
    }
    s3_resource.Object(bucket_to_name, file_name).copy(copy_source)

copy_to_bucket(first_bucket_name, second_bucket_name, first_file_name)

#Delete an Object
s3_resource.Object(second_bucket_name, first_file_name).delete()

#List buckets
for bucket_dict in s3_resource.meta.client.list_buckets().get('Buckets'):
    print(bucket_dict['Name'])

#List objects in bucket
for obj in first_bucket.objects.all():
    subsrc = obj.Object()
    print(obj.key, obj.storage_class, obj.last_modified,
        subsrc.version_id, subsrc.metadata)

#Delete objects in bucket whether or not is enabled versioning
def delete_all_objects(bucket_name):
    res = []
    bucket = s3_resource.Bucket(bucket_name)
    for obj_version in bucket.object_versions.all():
        res.append({'Key': obj_version.object_key,
                    'VersionId': obj_version.id})
    print(res)
    bucket.delete_objects(Delete={'Objects': res})

delete_all_objects(first_bucket_name)

# Delete empty bucket
s3_resource.Bucket(first_bucket_name).delete()
s3_resource.meta.client.delete_bucket(Bucket=second_bucket_name)
#BucketNotEmpty log