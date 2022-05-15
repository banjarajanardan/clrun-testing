FROM python:3.8-slim-buster
# WORKDIR /weAnswer
# COPY . /weAnswer

RUN pip3 install -r weAnswer/app/requirements.txt


EXPOSE $PORT

CMD [ "./weAnswer/runserver.sh" ]