import pandas as pd

def reviews(filepath = '/Users/will/Desktop/COSC 4397/reviews_segment.pkl'):
    df = pd.read_pickle(filepath)
    return df

if __name__ == "__main__":
    df = reviews()
    print('Columns of the data: ', df.columns.tolist())
    print(df.head(5))