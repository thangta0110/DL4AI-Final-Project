import pandas as pd



def rank_stocks(predictions_df):
    return predictions_df.sort_values(
        by='Predicted_Return',
        ascending=False
    )