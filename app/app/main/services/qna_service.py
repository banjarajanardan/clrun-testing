from email import header
from wsgiref import headers
from ..config import CONFIG
from ..utils.utils import send_post_request, parallelize

api_urls = CONFIG.QNA_APIs

def find_answer(json_body: dict):
    headers = {}
    params = []
    for api_url in api_urls:
        params.append({"url":api_url, "headers":headers, "json_body": json_body})
    res = parallelize(4, send_post_request, params)
    return res