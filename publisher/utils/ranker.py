import datetime

def ranker(
        data: list,
        threshold: int = 75,
) -> list:
    """
    Reads list of json publications and returns
    data filtered by threshold and actual date.
    Input:
    data: list with json publications
    threshold: minimum value for score
    Returns:
    filtered data
    """
    data = [
        publication
        for publication in data
        if publication['date'] == str(datetime.date.today())
    ]

    data = [
        publication
        for publication in data
        if publication['score'] >= threshold
    ]

    return data