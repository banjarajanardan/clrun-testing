FROM python:3.8-slim-buster
WORKDIR /app
COPY . .

RUN pip3 install -r /app/weAnswer/app/requirements.txt


EXPOSE $PORT

CMD [ "./weAnswer/runserver.sh" ]