FROM python:3.8-slim-buster
WORKDIR /weAnswer
COPY . .

RUN pip3 install -r /app/requirements.txt


EXPOSE $PORT

CMD [ "./weAnswer/runserver.sh" ]