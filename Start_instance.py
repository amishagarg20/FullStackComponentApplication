from aws_session import create_aws_session

# Start EC2 instance
def start_ec2_instance(instance_id):
    session = create_aws_session()
    ec2_client = session.client('ec2')
    
    response = ec2_client.start_instances(
        InstanceIds=[instance_id]
    )
    
    print('Started instance with ID:', instance_id)

# Usage
if __name__ == '__main__':
    instance_id = 'i-03b8e4dc9482c2145'  # Replace with the actual instance ID
    start_ec2_instance(instance_id)
