#!/bin/bash
export FLASK_APP="app:create_app('development')"
export FLASK_ENV=development
export FLASK_RUN_EXTRA_FILES=.env
flask run
