# Installation

1. [Install pip](https://pip.pypa.io/en/latest/installing.html) somehow. You can first try `sudo easy_install pip`
2. Install virtualenv `sudo pip install virtualenv`
3. Clone this repo
4. In the repo folder run `virtualenv venv`
5. Run `. venv/bin/activate`. Your shell will be prefixed like this `(venv)Computer:dir user$`
6. Finally run `pip install -r requirements.txt`

# App commands

- `. venv/bin/activate` starts the virtual env. You need this running to start the app
- `python app.py` starts the server