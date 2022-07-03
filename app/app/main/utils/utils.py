import joblib
import requests

from typing import List, Callable

from loguru import logger
from retrying import retry

from .errors import ServiceUnavailable


@retry(stop_max_attempt_number=5, wait_random_min=2000, wait_random_max=5000)
def send_post_request(url:str, headers: dict, json_body: dict):
    """
        Send request to any API
        Args:
            url: `str`
                api/url to make request
            headers: `dict`
                authetication params required for api call
            json_body: `dict`
                params to be sent on request
        Returns:
            r: `Response`
                response of the api call
    """
    logger.info("Fetching answer from model")
    r = requests.post(url, headers=headers, json=json_body)
    if r.status_code in [503, 502]:
        logger.error(f"Service Unavailable. Retrying....")
        raise ServiceUnavailable
    return r


def parallelize(n_jobs: int, func: Callable, params: List[dict]):
    """
        Parallelize any operations
        Args:
            n_jobs: `int`
                number of jobs to run in parallel
                dynamically set between 1 and 8
            func: `Callable`
                function to parallelize
            parmams: `List[dict]`
                each dict is args to the function
        Returns:
            res: `list`
                accumulated result of each function call
    """
    n_jobs = max(n_jobs, 1)
    n_jobs = min(n_jobs, len(params))
    n_jobs = min(n_jobs, 8)
    job = joblib.Parallel(n_jobs=n_jobs, prefer="threads", require="sharedmem")
    res = job(joblib.delayed(func)(**param) for param in params)
    return res


def str_to_bool(string: str) -> bool:
    """
        check if value can be converted to boolean type
    """
    true_values = ["1", "y", "yes", "true"]
    if str(string).lower() in true_values:
        return True
    else:
        return False