# Loanding Page hosted on a Nginx

Steps to take in running this project:

*   Clone the project
  
*   Create a virtual environment by running:
    ```
    python -m venv <name of virtual environment>
    ```
    Example:
    ```
    python -m venv venv
    ```

*   Activate your virtual environment:
    ```
    source <venvname/bin/activate>
    ```
    Example:
    ```
    source venv/bin/activate
    ```

*   Install the requirements
    ```
    pip install -r requirements.txt
    ```

*   Run the project by typing the following in your terminal:
    ```
    export FLASK_APP=run.py
    export FLASK_ENV=development
    flask run
    ```

*   Type in your browser:
    ```
    127.0.0.1:5000/
    ```

*   Next, we check if our project runs on uWSGI
    ```
    uwsgi dev.ini
    ```

*   In your browser type:
    ```
    127.0.0.1:9090/
    ```
![image](https://user-images.githubusercontent.com/49791498/109414697-81948300-79b4-11eb-81e1-539470434b3b.png)

*To stop the uWSGI server, run ```Ctrl + C```

## In your VM

*   ssh into a vm
*   Run the following:
```
sudo apt update
```
*   Install [python](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)
  
*   Clone the repo into your VM
```
sudo apt update
git clone <repo-url>
```

* Change your directory's name to app
```
mv <repo-name>/ app
```
*   cd into your file and create a virtual environment and activate it
```
sudo apt-get install python3-venv
python3 -m venv <virtual-environment-name>
source <virtual-environment-name>/bin/activate
```
    
*   Install the requirements in your requirements.txt file
```
    pip3 install -r requirements.txt
```
*run ```pip3 list``` to see a list of all installed dependencies*

*If uWSGI does not install, run the following:*
```
sudo apt-get install build-essential python3-dev
pip3 install uwsgi
```
    
*   Set ufw to allow for connections on port 9090  
```
sudo ufw enable
sudo ufw allow 9090
```

*   Run 
```
uwsgi dev.ini
```
*   In your browser type 
```
<vmipaddress>:9090/
```

*   Delete firewall
```
sudo ufw delete allow 9090
```
*   Deactivate virtual environment
```
deactivate
```

*   Install nginx
```
sudo apt install nginx
```

*   Allow ufw connections to http
```
sudo ufw allow 'Nginx HTTP'
```

*   In your browser, type your VM's IP address
Expected result:
![image](https://user-images.githubusercontent.com/49791498/109413045-c1a33800-79ab-11eb-900f-8de337b31f7d.png)

*   Create systemd unit file
```
sudo nano /etc/systemd/system/app.service
```
File contents:
```
[Unit]
Description=A simple Flask uWSGI application
After=network.target

[Service]
User=<yourusername>
Group=www-data
WorkingDirectory=/home/<yourusername>/app
Environment="PATH=/home/<yourusername>/app/venv/bin"
ExecStart=/home/<yourusername>/app/venv/bin/uwsgi --ini app.ini

[Install]
WantedBy=multi-user.target
```

*   To enable the service file just created, run
```
sudo systemctl start app
sudo systemctl enable app app
```
expected output:

![image](https://user-images.githubusercontent.com/49791498/109413425-93bef300-79ad-11eb-81cd-36a0b6c4d644.png)

*   To check if the file is running,
```
sudo systemctl status app
```

*   Configure nginx
```
sudo nano /etc/nginx/sites-available/app
```
File contents:
```
server {
    listen 80;
    server_name <your_ip_address> <your_domain_name>;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/<username>/app/app.sock;
    }
}
```
*To heck if there are any errors in your nginx configuration file, run ```
sudo nginx -t```*

![image](https://user-images.githubusercontent.com/49791498/109413763-6ecb7f80-79af-11eb-8d01-3c64664d7dfe.png)

*   Link app file to sites available
```
sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/
```

*You can run a sytax check again, to be sure there are no errors.*

*   Restart nginx for changes to take place
```
sudo systemctl restart nginx
```

*   In your browser, type in your VM IP address without adding a port becase in nginx config file, we have defined a port for nginx to listen on


![image](https://user-images.githubusercontent.com/49791498/109413975-9ec75280-79b0-11eb-8859-0fa7096da98a.png)
*IP address*

![image](https://user-images.githubusercontent.com/49791498/109420276-d1357780-79d1-11eb-870a-4ee7a331b278.png)
*Azure custom domain name*


*cool thing is, anyone with your public IP address can access your webpage*

Tutorial article can be accessed [here]()


    