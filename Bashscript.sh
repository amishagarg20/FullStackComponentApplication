#!/bin/bash

# Load credentials from the configuration file
CONFIG_FILE="/home/ec2-user/aws/config.sh"

if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
    echo "Configuration file sourced successfully."
else
    echo "Error: Configuration file ($CONFIG_FILE) not found."
    exit 1
fi
# Update the package list and install essential utilities
sudo yum update

# Install Python (adjust version as needed)
echo "Installing Python..."
sudo yum install -y python3
sudo yum install python3-pip

# Install Jupyter Lab
echo "Installing Jupyter Lab..."
pip3 install jupyterlab

# Install AWS CLI
echo "Installing AWS CLI..."
sudo yum install -y awscli

# Add this line for Git installation
sudo yum install -y git

# Installing Docker
echo "Installing Docker"
sudo yum install docker
echo "Docker Service start"
sudo docker service start
groups $USER

sudo usermod -a -G docker $USER 
sudo chown root:docker /var/run/docker.sock
sudo systemctl restart docker

docker info

# Install Docker Compose (if not already installed)
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Add Docker Compose path to user's PATH
export PATH=$PATH:/usr/local/bin

# Create docker-compose.yml file (if needed)
echo "Creating docker-compose.yml..."
docker_compose=$(cat <<EOL
version: "3.8"
services:
  mysql:
    image: mysql
    container_name: mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: password
    ports:
      - "3306:3306"
    volumes:
      - ${PWD}/mysql_data:/var/lib/mysql

  phpmyadmin:
    image: phpmyadmin
    container_name: myadmin
    restart: always
    ports:
      - "8080:80"
    links:
      - mysql:db
    environment:
      PMA_HOST: db
      MYSQL_ROOT_PASSWORD: password
EOL
)

echo "$docker_compose" | sudo tee /home/ec2-user/docker-compose.yml > /dev/null

# Run the Docker container
echo "Running Docker container..."
docker-compose up -d

# Source the config file
source "/home/ec2-user/aws/config.sh"

# Create a new GitHub repository
echo "Creating a new GitHub repository..."
response=$(curl -s -H "Authorization: token $GITHUB_TOKEN" -d '{"name":"'$REPOSITORY_NAME'"}' https://api.github.com/user/repos)

# Check if there are any errors in the response
if [[ $response == *"Problems parsing JSON"* ]]; then
    echo "Error creating repository. Check your GitHub token and repository name."
    echo "Response from GitHub API:"
    echo "$response"
    exit 1
else
    echo "Repository created successfully!"
fi
# Generate SSH Key Pair
echo "Generating SSH key pair..."
ssh-keygen -t rsa -b 4096 -C "amishagarg828@gmail.com" -f ~/.ssh/id_rsa -N "" -q

# Add SSH Key to SSH Agent
echo "Adding SSH key to SSH agent..."
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub


# Change to the directory where your AWS project is located
cd /home/ec2-user/aws

# Initialize a new Git repository (if not already initialized)
git init

# Add all files to the Git repository
git add .

# Commit changes
git commit -m "Initial commit"



# Add the GitHub repository as a remote using SSH

GITHUB_REPO_URL="git@github.com:${GITHUB_USERNAME}/${REPOSITORY_NAME}.git"
git remote add origin $GITHUB_REPO_URL

# Check if the SSH key is correctly configured
ssh -T git@github.com

# Add the GitHub repository as a remote using SSH, only if the remote doesn't exist
if ! git remote | grep -q "origin"; then
    git remote add origin $GITHUB_REPO_URL
fi



# Push changes to GitHub (assuming you are pushing to the main branch)
git push -u origin master






# Software versions
SOFTWARE_VERSIONS=(
    "Docker: docker --version"
    "Docker Compose: docker-compose --version"
    "aws: aws --version"
    "jupyter lab: jupyter lab --version"
    "git: git --version"
    "Python3: python3 --version"
    "pip: pip --version"
)

# Function to print software versions
print_versions() {
    for software in "${SOFTWARE_VERSIONS[@]}"; do
        IFS=':' read -r -a software_info <<< "$software"
        name="${software_info[0]}"
        version_command="${software_info[1]}"

        echo -n "$name version: "
        eval $version_command 2>/dev/null || echo "Not installed"
    done
}

# Print the versions
print_versions
echo "Setup completed!"
