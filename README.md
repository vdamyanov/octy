# Installation

1. [Install pip](https://pip.pypa.io/en/latest/installing.html) somehow. You can first try `sudo easy_install pip`
2. Install virtualenv `sudo pip install virtualenv`
3. Clone this repo
4. In the repo folder run `virtualenv venv`
5. Run `. venv/bin/activate`. Your shell will be prefixed like this `(venv)Computer:dir user$`
6. Finally run `pip install -r requirements.txt`

# App commands

- `. venv/bin/activate` starts the virtual env. You need this running to start the app
- `export APP_CONFIG="config.Dev"` sets the app environment to Dev. There is also `config.Prod`, `config.Stage` and `config.Test`
- `python runserver.py` starts the server

# Setting up the database

You need to be in the root of the app when you run these commands. You also need to have the environment variable set and be in the venv

- open up postgres in terminal `psql`
- create a new db `CREATE DATABASE octy_dev;`
- select the db. you can user `\c octy_dev;`
- in another tab open up python with `python`
- import the db using `from octy.models import db`
- run `db.create_all()` and you are done

# Running migrations

You need to be in the root of the app when you run these commands. You also need to have the environment variable set and be in the venv

Migrations should be used to update databases and not to create them from scratch. They are ideally suited for keeping existing databases up to date with schema changes. If you need a new database it is faster and more efficient to use `db.create_all()`. See the __Setting up the database__ section for details. [Alembic Reference](https://alembic.readthedocs.org/en/latest/cookbook.html)

- run `alembic upgrade head` to run migrations forward up until the most recent migration i.e. run all migrations
- run `alembic downgrade base` to go all the way back to nothing
- there's also other things like +1, -2, etc. [here](https://alembic.readthedocs.org/en/latest/tutorial.html#partial-revision-identifiers)