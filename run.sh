#!/bin/bash
export FLASK_DEBUG=true
export FLASK_APP=app
export FLASK_ENV=development
export VIRTUALENVWRAPPER_PYTHON=$(command \which python3)
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Projects
source /usr/local/bin/virtualenvwrapper.sh
workon WayOutWest
flask run
deactivate
