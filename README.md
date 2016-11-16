# Pixation
## Setup Instructions

### Installing virtualenv
* Install `virtualenv` using your package manager for `python3.5`, for example in ubuntu run:
    ```shell
    sudo apt-get install python3.5-virtualenv
    ```
* Now run the following to complete virtual environment Setup
    ```shell
    virtualenv -p python3 venv
    source venv/bin/activate
    # move to the pixation directory
    pip install -r requirements.txt
    ```
### Setting up private settings

* Run `cp pixation/settings_secret.py.template pixation/settings_secret.py`
* Add correct database and other settings in `settings_secret.py`

### Deploying the Server

* Build the database, assuming your settings are correct
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

* Run the server by using the following shell command
    ```shell
    python manage.py runserver
    ```