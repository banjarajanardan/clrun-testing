from typing import List

def ensemble_answer(answers: List[dict]) -> List[dict]:
    """Collapse the overlapping lines in list by merging them
    Args:
        lines (List[dict]): input answers
    Returns:
        List[dict]: merged answers
    """
    to_be_overlaped = answers[:1]
    for answer in answers:
        overlapped = False
        for i in range(len(to_be_overlaped)):
            if not is_overlapped(answer, to_be_overlaped[i]):
                continue
            to_be_overlaped[i] = merge_lines(to_be_overlaped[i], answer)
            overlapped = True
            break
        if not overlapped:
            to_be_overlaped.append(answer)

    return to_be_overlaped


def is_overlapped(answer1: dict, answer2: dict) -> bool:
    """Check if two 1 dimensional lines overlap or not
    Args:
        answer1 (dict): first answer with start and end point in 1d
        answer2 (dict): second answer with start and end point in 1d
    Returns:
        bool: If overlaps or not
    """
    start = max(answer1.get("start",0), answer2.get("start",0))
    end = min(answer1.get("end", 0), answer2.get("end", 0))
    d = end - start

    if d < 1:
        return False
    else:
        return True


def merge_lines(answer1: dict, answer2: dict) -> dict:
    """Merge two answers
    Args:
        answer1 (dict]): answer start and end point
        answer2 (dict]): answer start and end point
    Returns:
        dict: new answer with start and end point for merged answer
    """
    if not is_overlapped(answer1, answer2):
        raise Exception("Answers are different")
    
    answer1, answer2 = (answer1, answer2) if answer1.get("start", 0) <= answer2.get("start", 0) else (answer2, answer1)
    
    overlap = answer1.get("end", 0) - answer2.get("start", 0)
    answer = {
        "answer": answer1.get("answer", "") + answer2.get("answer", "")[overlap:],
        "score": (answer1.get("score", 0.5) + answer2.get("score", 0.5))/2,
        "start": answer1.get("start", 0),
        "end": max(answer1.get("end", 0), answer2.get("end", 0))
    }
    return answer