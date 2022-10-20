# pull python base image
FROM python:3.9

# install pipenv
RUN pip install pipenv

# set working derictory
WORKDIR /app/

# install dependencies
COPY ../Pipfile ./Pipfile.lock /usr/src/app/docker_conf/
RUN pipenv  install --system

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/docker_conf/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY /. /app

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/docker_conf/entrypoint.sh"]