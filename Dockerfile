FROM python:3.12

# Update apt package list
RUN apt-get update
RUN apt-get -y install net-tools

# Upgrade pip
RUN pip install --upgrade pip

# Install pipenv
RUN pip install pipenv

# Set up the project directory
WORKDIR /srv
COPY . /srv/flask_best_practices
RUN mkdir logs

# Install project dependencies
# --system: Installs packages into the system Python instead of a virtualenv (since virtualenvs are unnecessary in Docker containers)
# --deploy: Fails the build if Pipfile.lock is outdated
# --ignore-pipfile: Ensures it doesn't interfere with the settings
WORKDIR /srv/flask_best_practices
RUN pipenv install --system --deploy --ignore-pipfile

# Install uWSGI
RUN apt-get install libpcre3
RUN apt-get install libpcre3-dev -y
RUN pip install uwsgi --no-cache-dir

# Set timezone
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

# Start the application
CMD export FLASK_ENV='production' && uwsgi --ini uwsgi_for_docker.ini
