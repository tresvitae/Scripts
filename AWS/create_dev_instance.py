import boto3
import requests

ec2 = boto3.resource("ec2")

security_group_id = 'sg-x' # YOUR SG ID
key_pairs_name = 'x' # YOUR Key Pairs name
subnet_id = 'subnet-x' # YOUR SUBNET ID

#Create Ubuntu Server 20.04 LTS
def create_instance():
    instances = ec2.create_instances(
        ImageId='ami-0a8e758f5e873d1c1', # for eu-west-1
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1,
        Monitoring={
            'Enabled': False
        },
        KeyName=key_pairs_name,
        #UserData='starter.sh',
        NetworkInterfaces=[
            {
                'AssociatePublicIpAddress': True,
                'DeleteOnTermination': True,
                'DeviceIndex': 0,
                'SubnetId': subnet_id,
                'Groups': [
                    security_group_id
                ]
            }
        ]
    )
create_instance()