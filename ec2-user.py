import os
import subprocess
from config import LOCAL_FOLDER_PATH, REMOTE_FOLDER_PATH, EC2_PUBLIC_IP, SSH_KEY_PATH

def copy_to_ec2(local_path, remote_path, ec2_ip, ssh_key_path):
    scp_command = [
        'scp',
        '-r',  # Recursive copy
        '-o', 'StrictHostKeyChecking=no',  # Disable strict host key checking
        '-i', ssh_key_path,
        local_path,
        f'ec2-user@{ec2_ip}:{remote_path}'
    ]

    try:
        subprocess.run(scp_command, check=True)
        print(f"Folder copied successfully to the EC2 instance at {ec2_ip}:{remote_path}.")
    except subprocess.CalledProcessError as e:
        print("Error copying the folder to the EC2 instance: ", str(e))

def execute_on_ec2(ec2_ip, ssh_key_path, remote_script_path):
    ssh_command = [
        'ssh',
        '-o', 'StrictHostKeyChecking=no',  # Disable strict host key checking
        '-i', ssh_key_path,
        f'ec2-user@{ec2_ip}',
        f'bash {remote_script_path}'
    ]

    try:
        subprocess.run(ssh_command, check=True)
        print(f"Script executed successfully on the EC2 instance at {ec2_ip}.")
    except subprocess.CalledProcessError as e:
        print("Error executing the script on the EC2 instance: ", str(e))

if __name__ == "__main__":
    # Copy folder to EC2
    copy_to_ec2(LOCAL_FOLDER_PATH, REMOTE_FOLDER_PATH, EC2_PUBLIC_IP, SSH_KEY_PATH)

    # Execute script on EC2
    script_path = f'{REMOTE_FOLDER_PATH}/Bashscript.sh'
    print(f"Attempting to execute script at {EC2_PUBLIC_IP}:{script_path}")
    execute_on_ec2(EC2_PUBLIC_IP, SSH_KEY_PATH, script_path)
