import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--path","-p")
parser.add_argument("--target", "-t")

parsed = parser.parse_args()


le = LabelEncoder()
scaler = StandardScaler()

path = parsed.path
target_name = parsed.target

def read_dataset(path):
    return pd.read_csv(path)

def inspect_column(df):
    columns = list(df.columns)
    columns.remove(target_name)

    columns_to_drop = []
    columns_to_encode = []

    for column in columns:
        if df[column].unique() == 1:
            columns_to_drop.append(column)

        elif (df[column].unique <= 5 ) and (df[column].unique >= 1):
            columns_to_encode.append(column)

        else:
            df[column] = le.fit_transform(df[column])

    print("columns_to_encode" , columns_to_encode)
    print("columns_to_drop" , columns_to_drop)

    df.drop(labels = columns , axis = 1 , inplace = True)
    df = pd.get_dummies(df , columns = columns_to_encode ,prefix_sep="__" , drop_first=True)

    return df


def do_scale(df):
    columns = list(df.columns)
    columns.remove(target_name)

    for column in columns:
        df[column] = scaler.fit_transform(df[[column]])
    return df

def save_df(df):
    df.to_csv("output.csv")
    print("saved")

def main():
    df = read_dataset(path)
    df = inspect_column(df)
    df = do_scale(df)
    save_df(df)

if __name__ == "__main__":
    main()



