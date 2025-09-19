import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores_only = scores[["score"]]
    scores_only["rank"] = scores_only.rank(method="dense", ascending=False)
    scores_only = scores_only.sort_values(by="rank")
    return scores_only