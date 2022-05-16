import requests
from loguru import logger
from retrying import retry

from .errors import ServiceUnavailable


@retry(stop_max_attempt_number=5, wait_random_min=2000, wait_random_max=5000)
def send_post_request(url, headers: dict, json_body):
    logger.info("Fetching answer from model")
    r = requests.post(url, headers=headers, json=json_body)
    if r.status_code in [503, 502]:
        logger.error("Service Unavailable. Retrying....")
        raise ServiceUnavailable
    return r
