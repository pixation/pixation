# Pixation
## Setup Instructions

### Installing virtualenv
* Install `virtualenv` using your package manager for `python3.5`, for example in ubuntu run:
    ```shell
    sudo apt-get install python3.5-virtualenv
    ```
* Now run the following to complete virtual environment Setup
    ```shell
    virtualenv -p python3.5 venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
### Setting up private settings

* Run `cp pixation/settings_secret.py.template pixation/settings_secret.py`
* Add correct database and other settings in `settings_secret.py`

