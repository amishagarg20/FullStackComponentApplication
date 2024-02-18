import os

import subprocess

local_script_path = 'C:/Users/amgarg/Desktop/aws/Bashscript.sh'

remote_script_path = '/home/ubuntu/script.sh'



# Public IP address or DNS name of your EC2 instance
ec2_public_ip = '3.22.171.74'

# SSH private key file
ssh_key_path = 'c:/Users/amgarg/.ssh/amgarg01.pem'

# Construct the scp command to copy from local directory to the EC2 instance
scp_command = [
    'scp',
    '-o', 'StrictHostKeyChecking=no',  # Disable strict host key checking
    '-i', ssh_key_path,
    local_script_path,  # Use the local path to your script
    f'ubuntu@{ec2_public_ip}:{remote_script_path}'
]

# Copy the script from your local machine to the EC2 instance
try:
    subprocess.run(scp_command, check=True)
    print("Script copied successfully to the EC2 instance.")
except subprocess.CalledProcessError as e:
    print("Error copying the script to the EC2 instance: ", str(e))