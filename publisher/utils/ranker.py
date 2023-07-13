def ranker(
        data: list,
        threshold: int = 75,
) -> list:
    data = [
        publication
        for publication in data
        if publication['score'] >= threshold
    ]

    return data