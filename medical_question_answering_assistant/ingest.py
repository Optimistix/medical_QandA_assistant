import os
import pandas as pd

import minsearch


DATA_PATH = os.getenv("DATA_PATH", "../data/medquad.csv")


def load_index(data_path=DATA_PATH):
    df = pd.read_csv(data_path)
    df = df[0:1028] # The subset used in the project to save time and money; comment this line out if you want to use all 16000-odd records

    documents = df.to_dict(orient="records")

    index = minsearch.Index(
        text_fields=['question','answer','source','focus_area'],
        keyword_fields=['id']
    )

    index.fit(documents)
    return index
