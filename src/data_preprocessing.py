import pandas as pd

def load_data(path):
    df = pd.read_csv(path, parse_dates=['date'])
    df.fillna(0, inplace=True)
    return df

if __name__ == "__main__":
    df = load_data("../data/sample_weather.csv")
    print(df.head())
