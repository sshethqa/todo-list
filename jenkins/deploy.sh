#!/bin/bash

# Install apt Dependencies
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv -y

# Create todo list working directory and make working directory
sudo chown -R jenkins /opt
install_dir=/opt/todo-list
rm -rf $install_dir
mkdir $install_dir
cp -r . $install_dir
cd $install_dir

# Create and source virtual environment
python3 -m venv venv
source venv/bin/activate

# Install pip requirements
pip3 install -r requirements.txt

# Create service script
cat << EOF > /opt/todo-list/todo-list.service
    [Unit]
    Description=Todo List

    [Service]
    User=jenkins
    WorkingDirectory=/opt/todo-list
    Environment="DATABASE_URI=$DATABASE_URI"
    Environment="SECRET_KEY=$SECRET_KEY"
    ExecStart=/bin/bash ${install_dir}/jenkins/run.sh

    [Install]
    WantedBy=multi-user.target
EOF

# Install the app service script
sudo cp /opt/todo-list/todo-list.service /etc/systemd/system/

# Start the systemd service
sudo systemctl daemon-reload
sudo systemctl stop todo-list
sudo systemctl start todo-list
