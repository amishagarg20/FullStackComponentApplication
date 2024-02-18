# config.py

# AWS credentials
AWS_ACCESS_KEY_ID = 'AKIAISQKWDO5XV4IJH5Q'
AWS_SECRET_ACCESS_KEY = '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'
AWS_REGION = 'us-east-2'  # Specify the desired region

# Key pair information
KEY_PAIR_NAME = 'amgarg01'
KEY_PAIR_PATH = './amgarg01.pem'

# Security group information
SECURITY_GROUP_NAME = 'Amisha-Project'

# EC2 instance information
INSTANCE_NAME = 'Amisha-trial'
IMAGE_ID = 'ami-036f5574583e16426'
INSTANCE_TYPE = 't2.micro'
USER_DATA = 'echo "Hello, World!"'

#Paths
LOCAL_FOLDER_PATH = 'C:/Users/amgarg/Desktop/aws'
REMOTE_FOLDER_PATH = '/home/ec2-user/aws'

# EC2 Configuration
EC2_PUBLIC_IP = '18.220.254.59'
SSH_KEY_PATH = 'c:/Users/amgarg/.ssh/amgarg01.pem'

# AWS session parameters
#def get_aws_session_params():
#   return AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION
