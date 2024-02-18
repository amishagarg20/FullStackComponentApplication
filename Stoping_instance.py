from aws_session import create_aws_session

# Stop EC2 instance
def stop_ec2_instance(instance_id):
    session = create_aws_session()
    ec2_client = session.client('ec2')
    
    response = ec2_client.stop_instances(
        InstanceIds=[instance_id]
    )
    
    print('Stopped instance with ID:', instance_id)

# Usage
if __name__ == '__main__':
    instance_id = 'i-062bc937118bca398'  # Replace with the actual instance ID
    stop_ec2_instance(instance_id)
