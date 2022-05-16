# We Answer Documentation

#### Contents
- [Environment Setup](#1-environment-setup)
- [Overview](#2-overview)

## 1. Environment Setup

Recommended Linux, python 3.8.10

### 1.1 Setting Up Environment
* create virtual environment
    * virtualenv venv --python=python3.8
* activate virtual environment
    * . ./venv/bin/activate (linux)
    * . ./venv/Scripts/activate (windows)
* pip install -r app/requirements.txt

### 1.2 Running Server
* . ./runserver.sh (linux)
    * runs gunicorn server
* . ./runserver_windows.sh (windows/linux)
    * runs flask development server

### 1.3 Testing
* import `WeWrite.postman_collection.json` to postman
* send request to `answer_extract` to get answer for any given text

## 2. Overview
### 2.1 Find Answer In Passage
Api: ` POST http://127.0.0.1:8000/api/v1/find/answers/`
```
POST /api/v1/find/answers/
Content-Type: application/json
Header: {token: <TOKEN>}
Body: {text:<PASSAGE>, query:<QUERY>}
```
| Parameter       | Type     | Required?  | Description  |
| -------------   |----------|------------|--------------|
| `TOKEN`         | string   | required   | Static token to authorize the request |
| `TEXT`          | string   | required   | Passage in which answer is to be searched |
| `QUERY`         | string   | required   | Question to search in the passage. In case of multiple questions, separate each question by `\n`|

Request Example

Header:
```
{
    token: <TOKEN>
}
```
Json Body:
```
{
    "query": "Which name is also used to describe the Amazon rainforest in English? \n What is amazon rainforest called in French?",
    "text": "The Amazon rainforest (Portuguese: Floresta Amazônica or Amazônia; Spanish: Selva Amazónica, Amazonía or usually Amazonia; French: Forêt amazonienne; Dutch: Amazoneregenwoud), also known in English as Amazonia or the Amazon Jungle, is a moist broadleaf forest that covers most of the Amazon basin of South America. This basin encompasses 7,000,000 square kilometres (2,700,000 sq mi), of which 5,500,000 square kilometres (2,100,000 sq mi) are covered by the rainforest. This region includes territory belonging to nine nations. The majority of the forest is contained within Brazil, with 60% of the rainforest, followed by Peru with 13%, Colombia with 10%, and with minor amounts in Venezuela, Ecuador, Bolivia, Guyana, Suriname and French Guiana. States or departments in four nations contain \"Amazonas\" in their names. The Amazon represents over half of the planet's remaining rainforests, and comprises the largest and most biodiverse tract of tropical rainforest in the world, with an estimated 390 billion individual trees divided into 16,000 species."
}
```
Response of a successful request
```
{
    "data": [
        {
            "answer": "Amazonia or the Amazon Jungle",
            "end": 230,
            "score": 0.567615807056427,
            "start": 201
        },
        {
            "answer": "Forêt amazonienne",
            "end": 148,
            "score": 0.9856641888618469,
            "start": 131
        }
    ],
    "error": "",
    "message": "",
    "status": "success",
    "status_code": 200
}
```

| Parameter       | Type     | Description  |
| -------------   |----------|--------------|
| `DATA`          | list     | Each object in a list has `answer`, starting position of answer in position `start`, end position of answer `end` and confidence by which answer is extracted `score` |
| `ERROR`         | string   | Error code in case request is unsuccessful |
| `MESSAGE`       | string   | Description of error in case request is unsuccessful |
| `STATUS`        | string   | `success` if request is successful else `fail` |
| `STATUS_CODE`   | int      | HTTP response status code. Eg: 200 for success, 401 for unauthorized. |

