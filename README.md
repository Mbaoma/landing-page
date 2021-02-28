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
*   Next, we check if our project runs with uwsgi
    ```
    uwsgi dev.ini
    ```
    In your browser type:
    ```
    127.0.0.1:9090/
    ```

ssh into a vm
sudo apt update
install python
clone the repo into your VM
create a virtual environment
    sudo apt-get install python3-venv
    python -m venv <venvname>
pip install -r requirements.txt

