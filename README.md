# landing-page
Login Page hosted on a linux server

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
    pip install requirements.txt
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
*   Next, we check if our project runs with uwsgi
    ```
    uwsgi dev.ini
    ```
    In your browser type:
    ```
    127.0.0.1:9090/
    ```
    
    in your VM:
    clone the project into your vm by:
    ```
    sudo apt update
    git clone <repo-url>
    ```
    
    then cd into your file and create a virtual environment and activate it
    ```
    python3 -m venv <virtual-environment-name>
    source <virtual-environment-name>/bin/activate
    ```
    
    install the requirements in your requirements.txt file
    ```
    pip3 install -r requirements.txt
    ```
    run ```pip list``` to see a list of all installed dependencies
    
    check if your app runs on uwsgi, but first we have to set our ufw to allow for connections on port 9090
  
    ```
    sudo ufw enable
    sudo fw allow 9090
    ```
    expected result:
    
    running ```sudo ufw status``` shows us the crrent state of our firewall. if it is active or not and the ports our firewall gives us access to.
    
    go ahead and run 
    ```uwsgi dev.ini```andin your browser type ```<vmipaddress>:9090/```
    
    
