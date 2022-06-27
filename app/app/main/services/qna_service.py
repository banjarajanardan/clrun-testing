from json.decoder import JSONDecodeError
from typing import List

from ..config import CONFIG
from ..utils.utils import send_post_request, parallelize
from ..utils.errors import ServiceUnavailable
from .ensembler import ensemble_answer


api_urls = CONFIG.QNA_APIs


def _find_answer(json_body: dict):
    headers = {}
    params = []
    for api_url in api_urls:
        params.append({"url":api_url, "headers":headers, "json_body": json_body})
    res = parallelize(4, send_post_request, params)
    return res


def find_answers(questions: str, text: str, delimiter:str="\n") -> List[List[dict]]:
    """
    find answer of questions from given text
    Args:
        questions: `str`
            questions for which answer is to be found from text
        text: `str`
            refrence text to find answers
        delimiter: `str`
            separator in case of multiple questions
    Returns:
        answers: `List[List[dict]]
            each list inside the list is answers predicted by different model
            each dict is answer to a question
    """
    questions = questions.split(delimiter)
    json_body = {"inputs": {"context": text}}
    answers = []
    for question in questions:
        json_body["inputs"]["question"] = question
        _answers = []
        try:
            responses = _find_answer(json_body)
            for response in responses:
                _answers.append(response.json())
        except (ServiceUnavailable, JSONDecodeError):
            _answers.append({"answer": "", "start": 0, "end": 0, "score": 0})
        # _answers = ensemble_answer(_answers)
        answers.append(_answers)
    return answers