import threading



lock = threading.Lock()
scores = {}


def set_ethical_score(scores_):
    global scores
    global lock
    with lock : scores = scores_


def get_ethical_score(behavior_id,scheme_id=scheme_id):
    global scores
    global lock
    if not scheme_id :
        with lock : return scores[behavior_id]
    else :
        with lock : return scores[scheme_id][behavior_id]
