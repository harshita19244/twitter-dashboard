from sqlalchemy import false
import matplotlib.pyplot as plt
from models.hsol import caller as cl1
from models.fakeddit_2 import caller as cl2
from models.fakeddit_6 import caller as cl3
from models.implicit_3 import caller as cl4
from models.implicit_6 import caller as cl5
import pandas as pd

predictions = []
def classify_input_tweet(tweet):
    df = pd.DataFrame(columns = ['Tweet'])
    row = []
    row.append(tweet)
    df.loc[len(df.index)] = row
    predictions.append(cl1(df)['Category'].iloc[0])
    predictions.append(cl2(df)['Category'].iloc[0])
    predictions.append(cl3(df)['Category'].iloc[0])
    predictions.append(cl4(df)['Category'].iloc[0])
    predictions.append(cl5(df)['Category'].iloc[0])
    print(predictions)
    return predictions