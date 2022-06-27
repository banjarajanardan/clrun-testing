from flask import Blueprint, request

from ..services.qna_service import find_answers
from ..utils.auth import abort_json, login_required, make_response

qna_blueprint = Blueprint("qna", __name__)


@qna_blueprint.route("/find/answers/", methods=["POST"])
@login_required
def get_answer():
    if "application/json" in request.headers.get("Content-Type", ""):
        text = request.json.get("text", "")
        questions = request.json.get("query", "")
        delimiter = request.json.get("delimiter", "\n")

        if not (text and questions):
            abort_json(400, "MISSING_INPUT", "text and query are required in json body")
        answers = find_answers(questions, text, delimiter)
    else:
        abort_json(
            400,
            "INVALID_REQUEST",
            "content type can be mulipart/form-data or application/json only",
        )

    res = make_response(answers)
    return res, 200

@qna_blueprint.route("/health/", methods=["GET"])
def health():
    return make_response("Welcome to WeAnswer v2.0")