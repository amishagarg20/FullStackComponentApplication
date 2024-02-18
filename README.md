# Full-Stack-Component-Application
 Capstone Project


# Introduction 
A comprehensive guide to streamline the process of setting up and configuring an AWS EC2 instance using automation scripts. This infrastructure Automation Documentation will be a resource for effortless setting up and configuring AWS infrastructure using Automation Script.
In a world where rapid and consistent deployment is key, this documentation serves as a guide to a seamless and reproducible infrastructure setup.

# Purpose
The main objectives of this documentation are:

**Streamline Setup Processes:** We understand the challenges users face when configuring AWS environments. This documentation aims to simplify the setup process through automation, reducing the time and effort required.

**Ensure Reliability and Consistency:** Achieve a reliable and consistent infrastructure environment by automating key tasks such as key pair creation, security group setup, and software installations. Say goodbye to manual errors and variations in setups.

**Facilitate Dockerized Deployments:** Embrace the power of Docker for containerized application deployments. The provided scripts are designed to seamlessly integrate Docker into the workflow, making application deployment a breeze.

**GitHub Integration Made Easy:** Collaborate effortlessly by automating GitHub repository creation and SSH key configuration. Enhance version control workflow with automation, ensuring a smooth development process.

# Why we use this documentation

**AWS Enthusiasts:** Individuals familiar with AWS services seeking a simplified and automated approach to setting up EC2 instances.

**Developers and DevOps Professionals:** Those looking to streamline their development and deployment workflows with Dockerized applications and GitHub integration.

**Testing and Development Environments:** Users who require quick and consistent setups for testing or development purposes.

# Learnings 
**Effortlessly Create an AWS EC2 Instance:** The provided scripts guide you through the creation and configuration of an EC2 instance, minimizing manual intervention.

**Seamlessly Configure Docker and GitHub Integration:** Streamline the setup of essential software, Docker containers, and GitHub repositories, ensuring a standardized and efficient development environment.

**Verify Environment:** Confirm the success of infrastructure setup by checking the versions of installed software on the EC2 instance.

# Key Components
In this infrastructure automation solution, several key components work together seamlessly to create and configure an AWS environment. Understanding these components is crucial for a successful setup:

# Configuration File
### 1) Config.py :
   **Purpose:**
   Stores user-specific configurations, including AWS credentials, key pair information, and EC2 instance details.
   
   **Usage:** 
   Modify this file to match the AWS environment and preferences.
   
### 2) Aws_session.py:
   **Purpose:** 
   Establishes an AWS session using the provided credentials.
   
   **Usage:** 
   Typically requires no direct modification, as it is used internally by other scripts.
   

# Main Automation Script (Creating Instance.py)
### 1) Creating Instance.py :
   **Purpose:**
   - Creates or verifies the existence of a key pair.
   - Retrieves the security group ID.
   - Launches an EC2 instance with specified configurations.
 
  **Usage:**
   Run this script to initiate the creation and setup of an AWS EC2 instance.
  

# Aws Initialization Script (BashScript.sh) 
### 1) BashScript.sh :
   **Purpose:**
    - Updates package lists and installs essential utilities on the EC2 instance.
    - Installs Python, Jupyter Lab, AWS CLI, Git, Docker, and Docker Compose.
    - Configures Docker containers for MySQL and phpMyAdmin.
    - Set up a new GitHub repository.
    - Generates and adds an SSH key for GitHub authentication.
    
   **Usage:**
   - Execute this script on the EC2 instance after connecting via SSH. 
   - It prepares the environment for development and builds infrastructure.
   
# User Interaction Script (ec2-user.py)
### 1) Ec2-user.py :
   **Purpose:**
  - Copies a local folder to the EC2 instance.
   - Executes the initialization script remotely on the EC2 instance.
   
   **Usage:**
   Run this script to automate the transfer of local files to the EC2 instance and execute scripts remotely.
   
# Start EC2 Instance Script (start_instance.py):
### 1) Start_Instance.py :
   **Purpose:**
   Starts an existing EC2 instance using its instance ID
   
   **Usage:**
   The script is executed with a specific instance ID as an argument to start the corresponding EC2 instance.
   
# Stop EC2 Instance Script(Stoping_Instance.py)
### 1) Stopping_Instance:
   **Purpose:**
   Stops an existing EC2 instance using its instance ID.
   
   **Usage:**
   The script is executed with a specific instance ID as an argument to stop the corresponding EC2 instance.

# Prerequisites:

Before begin using the infrastructure automation scripts, ensure that you have the following prerequisites in place:

### 1) Aws Account :
 **Instruction:** Ensure to have an Amazon Web Service account with the necessary permission to create EC2 instances, Key Pairs, Security Groups, and other required resources.

# Getting Started:
Proceeding for the next steps for setting up the AWS environment using Automation Script.

## a. Configuration:
### 1) Update Config.py:
     Open the Config.py in the text editor.
**a) AWS credentials:**

AWS credentials 

AWS_ACCESS_KEY_ID = ''

AWS_SECRET_ACCESS_KEY = ''

AWS_REGION = 'us-east-2'  # Specify the desired region

**Purpose:** 
     Contains the AWS access key ID, secret access key, and the desired AWS region
     
### Instructions:
     - Replace the placeholder values with  actual AWS credentials.
     - Set the desired AWS region.
     
## b) KeyPair Information:
### Key pair information

KEY_PAIR_NAME = ''

KEY_PAIR_PATH = ''
 
  **Purpose:**
     Specifies the name of the SSH key pair and the path to the corresponding private key file.
     
### Instructions:
     
    - Set the key pair name to match the requirements.
    - Ensure the private key file path is accurate. 

## c) EC2 Instance Information:

### EC2 Instance Information:

INSTANCE_NAME = ''

IMAGE_ID = ''

INSTANCE_TYPE = 't2.micro'

USER_DATA = 'echo "Hello, World!"'

  **Purpose:**
     Specifies details about the EC2 instance, such as its name, Amazon Machine Image (AMI) ID, instance type, and user data.
     
### Instructions:

     - Set the instance name according to preference.
     - Choose the appropriate AMI ID and instance type.
     - Modify user data as needed.
     
## d) Paths

### paths:

LOCAL_FOLDER_PATH = ''

REMOTE_FOLDER_PATH = ''

 **Purpose:**
     Defines the local and remote paths for file transfer between the local machine and the EC2 instance.
     
### Instructions:
     Set the local and remote folder paths based on the file transfer requirements.
     
## e) Ec2 Configuration

### Ec2 Configuration:

EC2_PUBLIC_IP = ''

SSH_KEY_PATH = ''

 **Purpose:**
      Specifies the public IP address of the EC2 instance and the path to the local SSH key file.
      
### Instructions:
      - Set the public IP address to match the EC2 instance.
      - Provide the correct path to the local SSH key file.

## b. AWS Session Script (aws_session.py)
The aws_session.py script is responsible for creating an AWS session using the AWS SDK for Python (boto3). Here's an overview of the script:

### a) Import Statements: 

import boto3

from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION

 **Purpose:**
 
 - Imports the necessary modules and AWS credentials from the config.py file.
 - **boto3:** The AWS SDK for Python, allowing interaction with AWS services.

### b) Create AWS Session Function (create_aws_session):

def create_aws_session():
    
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )
    return session
    
 **Purpose:**
 - Defines a function named create_aws_session responsible for creating an AWS session.
 - Utilizes the boto3.Session class to create a session with specified credentials and region.
 - Returns the created session object.

### c) Explanation:
- The create_aws_session function encapsulates the process of establishing an AWS session, abstracting away the details of credential management.
- The boto3.Session class is instantiated with the provided AWS access key ID, secret access key, and region.
- The function returns the created session object, which is used to interact with various AWS services.

### d) Usage Example:

if __name__ == '__main__':
    # Create an AWS session
    session = create_aws_session()
    
    # Now 'session' can be used to create clients or resources for specific AWS services.
    # Example:
    ec2_client = session.client('ec2')
    s3_resource = session.resource('s3')

**Purpose:**
 - Demonstrates how the create_aws_session function can be used to create a session.
 - The resulting session object can then be utilized to create clients or resources for specific AWS services (e.g., EC2, S3).
 - 
This script provides a modular way to create an AWS session, enhancing the reusability and maintainability of AWS-related automation scripts. It allows users to manage AWS credentials centrally in the config.py file and easily create sessions for interacting with AWS services.

## c. Initial EC2 instance Setup

### 1) Run Creating_Instance:

     Execute the creating_Instance.py script to create and start an EC2 instance. This script may also create a key pair if one does not exist. This script is the core automation script responsible for creating, starting, and configuring an Amazon EC2 instance. Below is an overview of each section:

### a) Import Statements:

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

**Purpose:**

 - Imports necessary modules and functions required for the script's functionality.
 - os: Provides a way to interact with the operating system.
 - time: Introduces time-related functionality (e.g., sleep).
 - create_aws_session: Function for creating an AWS session.
 - config: Importing configuration parameters from the config.py file.

### b) Creating EC2 Instance Function (create EC2 Instance)

**Purpose:**

 - Check if the specified SSH key pair exists; if not, create one.
- Retrieves the security group ID for 'Amisha-Project.'
 - Runs an EC2 instance with specified configurations (image, instance type, key pair, security group).
 - Tags the instance with the name 'Amisha-trial.'
 - Prints the instance ID and returns it.

### c) Start EC2 Instance Function (Start Ec2 Instance)

**Purpose:**

 - Modifies the security groups of the specified EC2 instance.
 - Starts the specified EC2 instance.
 - Prints a confirmation message.

### d) Get Public IP Address Function (get_instance_public_ip)

def get_instance_public_ip(session, instance_id):

    ec2_client = session.client('ec2')
    
    response = ec2_client.describe_instances(
    
        InstanceIds=[instance_id]
    )
    public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
    
    return public_ip

**Purpose:**

 Retrieves the public IP address of the specified EC2 instance.

### e) Main Execution (__main__ Block):

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
    
**Purpose:**

 - Initiates the script when executed as the main program.
 - Creates an AWS session.
 - Calls the create_ec2_instance function to create and configure an EC2 instance.
 - Waits for 30 seconds for the instance to be ready.
 - Calls the start_ec2_instance function to start the EC2 instance.
 - Waits for the instance to be in the 'running' state.
 - Retrieves and prints the public IP address of the EC2 instance.

This script automates the process of creating and configuring an EC2 instance, making it suitable for a variety of deployment scenarios. It utilizes AWS Boto3 and demonstrates best practices for EC2 instance setup and initialization.

## d. Initialization Bash Script:

The provided bash script is designed to set up a development environment on an EC2 instance. Below is an overview of the script's functionality:

### a) Update and Installation:

**Purpose:** 

 - Updates the package list on the EC2 instance to ensure access to the latest software versions.
 - Installs Python 3 and pip for Python package management.
 - Installs Jupyter Lab, a web-based interactive development environment for Python.
 - Installs AWS CLI, Git, and Docker to facilitate AWS interaction, version control, and containerization.
 - Starts the Docker service on the EC2 instance.
 - Adds the user to the Docker group to run Docker commands without sudo
 - Displays information about the Docker installation.
 - Installs Docker Compose, a tool for defining and running multi-container Docker applications.
 - Adds Docker Compose to the user's PATH for easy execution.
 - Prints Docker Compose configuration to a file.
 - Runs the Docker container defined in the docker-compose.yml file in detached mode.
 - Defines a function to print the installed software versions.
 - Executes the function to display the versions.
 - Indicates the successful completion of the setup process.
 - 
The script automates the setup of a development environment on an EC2 instance, including Python, Jupyter Lab, AWS CLI, Git, and Docker. Docker Compose is used to configure and run Docker containers for MySQL and PHPMyAdmin. Software versions are printed for verification. The script provides a streamlined process for initializing a development environment on an EC2 instance, facilitating efficient software development and testing.

## e. File Transfer and Execution Script :
This Python script facilitates the transfer of a local folder to an EC2 instance and the subsequent execution of a remote script on that EC2 instance. Below is an overview of the script's functionality:

### a) Copy to EC2 Function:

def copy_to_ec2(local_path, remote_path, ec2_ip, ssh_key_path):

    # Construct SCP command
    
    scp_command = [
    
        'scp',
        '-r',  # Recursive copy
        '-o', 'StrictHostKeyChecking=no',  # Disable strict host key checking
        '-i', ssh_key_path,
        local_path,
        f'ec2-user@{ec2_ip}:{remote_path}'
    ]

    try:
        # Execute SCP command
        subprocess.run(scp_command, check=True)
        print(f"Folder copied successfully to the EC2 instance at {ec2_ip}:{remote_path}.")
    except subprocess.CalledProcessError as e:
        print("Error copying the folder to the EC2 instance: ", str(e))
        
**Purpose:**

 - Copies a local folder to a specified path on the target EC2 instance,
 - Utilizes the SCP (Secure Copy) command for secure file transfer.

### b) Execute on EC2 Function:

def execute_on_ec2(ec2_ip, ssh_key_path, remote_script_path):

    # Construct SSH command
    
    ssh_command = [
        'ssh',
        '-o', 'StrictHostKeyChecking=no',  # Disable strict host key checking
        '-i', ssh_key_path,
        f'ec2-user@{ec2_ip}',
        f'bash {remote_script_path}'
    ]

    try:
        # Execute SSH command
        subprocess.run(ssh_command, check=True)
        print(f"Script executed successfully on the EC2 instance at {ec2_ip}.")
    except subprocess.CalledProcessError as e:
        print("Error executing the script on the EC2 instance: ", str(e))
        
**Purpose:**

 - Executes a remote script on a specified EC2 instance using SSH.
 - Uses the SSH command to establish a secure connection and execute the specified script.

### c)  Main Script Execution:

if __name__ == "__main__":

    # Copy folder to EC2
    
    copy_to_ec2(LOCAL_FOLDER_PATH, REMOTE_FOLDER_PATH, EC2_PUBLIC_IP, SSH_KEY_PATH)

    # Execute script on EC2
    
    script_path = f'{REMOTE_FOLDER_PATH}/Bashscript.sh'
    
    print(f"Attempting to execute script at {EC2_PUBLIC_IP}:{script_path}")
    
    execute_on_ec2(EC2_PUBLIC_IP, SSH_KEY_PATH, script_path)

**Purpose:**

- If this script is executed directly (not imported), it performs the following:
- Copies the local folder specified by LOCAL_FOLDER_PATH to the remote path specified by REMOTE_FOLDER_PATH on the EC2 instance.
- Executes the script located at REMOTE_FOLDER_PATH/Bashscript.sh on the EC2 instance.
  
The script is designed to automate the process of transferring files and executing a script on an EC2 instance. It relies on the subprocess module to execute system commands (SCP and SSH) from within the Python script. The copy_to_ec2 function transfers a local folder to a specified path on the EC2 instance using SCP. The execute_on_ec2 function executes a remote script on the EC2 instance using SSH. The main script section demonstrates the usage of these functions by copying a local folder and executing a script on the specified EC2 instance. This script is useful for automating deployment and execution tasks on remote servers, facilitating a seamless development and deployment workflow.

## f. Start and stop Instance

### a) Start Instance:

- This script is designed to start an EC2 instance using the AWS SDK (Boto3) in Python.
- It imports the create_aws_session function from aws_session.py to establish an AWS session.
- The start_ec2_instance function takes an instance_id as an argument and uses it to start the specified EC2 instance.
- The if __name__ == '__main__': block is used to execute the script when run directly, and it starts the EC2 instance with the specified ID.

## b ) Stop Instance:

- This script is designed to stop an EC2 instance using the AWS SDK (Boto3) in Python.
- It also imports the create_aws_session function from aws_session.py to establish an AWS session.
- The stop_ec2_instance function takes an instance_id as an argument and uses it to stop the specified EC2 instance.
- The if __name__ == '__main__': block is used to execute the script when run directly, and it stops the EC2 instance with the specified ID.


# Customization

### 1. Updating Instance IDs:

**Where to Find Instance ID:**
Users should locate the EC2 instance ID(s) they want to manage. This information is available in the AWS Management Console or through the AWS CLI.

**Update in the Script:**
In the script, look for the variable or parameter where the instance ID is specified. It's usually explicitly mentioned in the script, often at the beginning or where the script interacts with EC2 instances.

**Example:**
 In my script, you might have a line like instance_id = 'i-03b8e4dc9482c2145'. Users should replace this with their actual EC2 instance ID.

### 2. Updating AWS Credentials:

**Where to Find AWS Credentials:**
Users need their AWS Access Key ID, AWS Secret Access Key, and AWS Region. These credentials are obtained through the AWS Management Console.

**Update in the Script:**
Locate the section of the script where AWS credentials are set. This is usually in a separate configuration file or directly in the script. Update the values with the user's AWS credentials.

**Example (from my script):**
In my config.py file, update the following:

AWS_ACCESS_KEY_ID = 'your_access_key_id'

AWS_SECRET_ACCESS_KEY = 'your_secret_access_key'

AWS_REGION = 'your_region'

### 3. Other Parameters:
**Review Configuration Options:**
Check for other parameters or configuration options in the script that might need customization. This could include security group names, key pair information, instance types, etc.

**Update as Needed:**
Modify these parameters in the script or configuration file according to the user's environment and requirements.

### 4. Script Execution:

**Running the Script:**
Provide instructions on how to run the script. Users might execute the script through a terminal or command prompt, depending on the scripting language.

**Passing Arguments:**
If the script accepts command-line arguments, document how users can pass these arguments during script execution.

### 5. Testing:
**Test with Sample Data:**

Encourage users to test the customized script with a sample or non-production environment first to ensure it behaves as expected.

# Customization Guide

**1. Updating Instance IDs**

Locate the variable `instance_id` in the script (e.g., `start_instance.py`) and replace the placeholder with your EC2 instance ID.

**2. Updating AWS Credentials**

Edit the `config.py` file and update the AWS credentials (Access Key ID, Secret Access Key, and Region) with your own. This file is where AWS configuration details are stored.

**3. Other Parameters**

Review the script for any additional parameters that might need customization, such as security group names, key pair information, etc. Update these according to your environment.

 **4. Script Execution**

To run the script, open a terminal or command prompt, navigate to the script's directory, and execute it. If the script accepts arguments, provide them as needed.

 **5. Testing**

Before using the script in a production environment, test it with sample data or in a non-production environment to ensure it behaves as expected.


# Execution
The "Execution" section in this documentation should provide clear instructions on how users can execute the scripts. Here's a guide on how to structure this section:

## Execution Guide
Follow these steps to execute the provided automation scripts:

### Prerequisites:

**Clone the GitHub Repository:**

- Download the complete folder by cloning the GitHub repository:
- git clone https://github.com/your-username/your-repo.git
- Open the Project in Visual Studio: Open the downloaded folder in Visual Studio or your preferred integrated development environment (IDE).
- Setup Configuration: Locate the config.py file in the project folder and update it with your AWS credentials, instance details, and other required parameters.

## 3 Steps to Execute:

- Create an EC2 Instance: Run the Creating_instance.py file to create an EC2 instance:
- python Creating_instance.py
- Once the instance is started, note the public IP address and update it in your config.py file.
- Prepare Bash Script: Prepare a Bash script (Bashscript.sh) with the required software installations. Customize the script according to your project needs.
- Set Up Local and Destination Paths: Update the local and destination paths in the config.py file:
   
LOCAL_FOLDER_PATH = '/path/to/local/folder'

REMOTE_FOLDER_PATH = '/path/on/ec2/instance'

 - Transfer Files to EC2 Instance: Run the ec2_user.py script to transfer folders from the local machine to the EC2 instance and set up the infrastructure:
 python ec2_user.py

**Check Services:**
- Once the script execution is complete, check the following services:
- **MySQL:** MySQL should be running on the EC2 instance.
- **PHPMyAdmin:** PHPMyAdmin should be accessible via the public IP address of the EC2 instance.


### 1)  Development and Testing Environments:

 **Scenario:**
 
You are a developer or tester working on a project that involves multiple instances for testing different features or configurations.

**How These Scripts Help:**
 Automate the process of creating, starting, and stopping EC2 instances, streamlining the workflow for development and testing.

**Example Usage:**
- Use the provided scripts to create instances with specific configurations, start them for testing, and then stop them to optimize costs when not in use.

### 2)  Cost Optimization in Production:

**Scenario:**
- In a production environment, you have instances running certain processes periodically, and you want to optimize costs during idle periods.

**How These Scripts Help:**
- Schedule the start and stop of instances using these scripts, ensuring resources are only active when needed, leading to cost savings.

**Example Usage:**
- Set up a cron job to automatically start instances during peak hours and stop them during off-peak hours, optimizing resource utilization and reducing operational costs.

### 3)  Project Infrastructure Setup:

**Scenario:**
- You want to quickly set up a project infrastructure with specific software configurations on EC2 instances.

**How These Scripts Help:**
- Automate the creation of EC2 instances, software installations, and infrastructure setup with a single execution.

**Example Usage:**
- Customize the provided Bash script ('Bash script.sh') with the required software installations, and use the ec2_user.py script to transfer files and execute the setup on the EC2 instance.


# Conclusion

In conclusion, the provided automation scripts offer a robust and efficient solution for managing AWS EC2 instances, particularly in scenarios where repetitive tasks, cost optimization, and infrastructure setup are critical. By utilizing these scripts, users can experience enhanced productivity, reduced manual intervention, and improved resource utilization. Here's a summary of the key takeaways:

### Key Benefits:

**1) Automation for Efficiency:**
The scripts automate key processes such as instance creation, starting, stopping, and file transfer, streamlining workflows for development, testing, and project setup.

**2) Cost Optimization:**
Users can schedule the start and stop of instances, contributing to cost savings by ensuring resources are active only when necessary.

**3) Customization for Flexibility:**
The scripts are designed with customization in mind, allowing users to adapt configurations, AWS credentials, and scripts to suit their specific use cases.

### Example Use Cases:
Demonstrated scenarios such as development and testing environments, cost optimization in production, project infrastructure setup, educational environments, and temporary work environments showcase the versatility of the scripts.

### Next Steps for Users:
Users are encouraged to review and customize the scripts based on their requirements, ensuring that AWS credentials, instance IDs, and other parameters are configured appropriately.

### Execution Guidelines:
The documentation provides clear instructions on executing the scripts, including prerequisites, customization steps, and a step-by-step guide for users to follow.

### Versatility and Accessibility:
These scripts cater to a broad range of users, from developers and testers to educators and project managers, making AWS resource management more accessible and efficient.
Incorporating these scripts into AWS workflow not only simplifies routine tasks but also empowers users to make the most of their AWS resources while minimizing operational overhead. As technology and user requirements evolve, these scripts can serve as a foundation for further enhancements and optimizations in AWS resource management.





