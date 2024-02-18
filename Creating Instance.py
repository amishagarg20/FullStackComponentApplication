# main_script.py

import os
import time
from aws_session import create_aws_session
from config import (
    KEY_PAIR_NAME,
    KEY_PAIR_PATH,
    SECURITY_GROUP_NAME,
    INSTANCE_NAME,
    IMAGE_ID,
    INSTANCE_TYPE,
    USER_DATA
)

# Create EC2 instance
def create_ec2_instance(session):
    ec2_client = session.client('ec2')

    # Check if key pair exists
    if not os.path.isfile(KEY_PAIR_PATH):
        # Create key pair
        key_pair_response = ec2_client.create_key_pair(KeyName=KEY_PAIR_NAME)
        key_material = key_pair_response['KeyMaterial']

        # Save key pair to a file
        with open(KEY_PAIR_PATH, 'w') as key_file:
             key_file.write(key_material)
        os.chmod(KEY_PAIR_PATH, 0o400)
        print('Created key pair:', KEY_PAIR_NAME)

    # Get the security group id for 'Amisha-Project'
    security_groups = ec2_client.describe_security_groups(GroupNames=[SECURITY_GROUP_NAME])
    security_group_ids = [group['GroupId'] for group in security_groups['SecurityGroups']]

    response = ec2_client.run_instances(
        ImageId=IMAGE_ID,
        MinCount=1,
        MaxCount=1,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_PAIR_NAME,
        SecurityGroupIds=security_group_ids,  # Attach to 'Amisha-Project'
        SubnetId='',
        UserData=USER_DATA,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': INSTANCE_NAME
                    },
                ]
            },
        ]
    )

    instance_id = response['Instances'][0]['InstanceId']
    print('Created instance with ID:', instance_id)
    return instance_id



# Start EC2 instance
def start_ec2_instance(session, instance_id):
    ec2_client = session.client('ec2')

    # Get the security group id for 'Amisha-Project'
    security_groups = ec2_client.describe_security_groups(GroupNames=[SECURITY_GROUP_NAME])
    security_group_ids = [group['GroupId'] for group in security_groups['SecurityGroups']]

    # Update the instance's security groups
    ec2_client.modify_instance_attribute(
        InstanceId=instance_id,
        Groups=security_group_ids
    )

    # Start the instance
    response = ec2_client.start_instances(
        InstanceIds=[instance_id]
    )

    print('Started instance with ID:', instance_id)


# Get public IP address of EC2 instance
def get_instance_public_ip(session, instance_id):
    ec2_client = session.client('ec2')

    response = ec2_client.describe_instances(
        InstanceIds=[instance_id]
    )

    public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
    return public_ip

if __name__ == '__main__':
    # Create AWS session
    session = create_aws_session()

    # Create and start EC2 instance
    instance_id = create_ec2_instance(session)
    print('Waiting for instance to be ready...')
    time.sleep(30)  # Wait for 30 seconds
    start_ec2_instance(session, instance_id)
    
    # Wait for the instance to start running
    print('Waiting for instance to start running...')
    ec2 = session.resource('ec2', region_name='us-east-2')  # Specify the desired region
    instance = ec2.Instance(instance_id)
    instance.wait_until_running()
    
    public_ip = instance.public_ip_address
    print('Public IP of the instance:', public_ip)
