import sys
import subprocess
import pandas as pd
import numpy as np
#from handle_outliers import OutliersTreatment
from sklearn.preprocessing import StandardScaler

class ProcessStep:
    def __init__(self, path):
        self.df = pd.read_excel(path)

    def clean(self):
        # drop any row that has more than 5 nan values
        num_nan_rows = self.df.isna().sum(axis=1).iloc[self.df[self.df.isna().any(axis=1)].index]
        self.df.drop(index=num_nan_rows[num_nan_rows > 5].index, inplace=True)

        # impute the remaining nan values with the median value
        self.df[self.df.select_dtypes(include="number").columns] = self.df.select_dtypes(include="number").fillna(self.df.select_dtypes(include="number").median())

        # convert object type to quantity types
        self.df["Population (Millions)"]    = self.df["Population (Millions)"].astype("float")
        self.df["GDP (Billions, PPP)"]      = self.df["GDP (Billions, PPP)"].astype("float")
        self.df["GDP per Capita (PPP)"]     = self.df["GDP per Capita (PPP)"].astype("int")
        self.df["Unemployment (%)"]         = self.df["Unemployment (%)"].astype("float")

        # # deal with outliers
        # outlier_model = OutliersTreatment(self.df, columns=self.df.columns[1:], quantile=[0.05, 0.95])
        # outlier_model.fit()
        # outlier_model.transform()

    def reduce(self):
        correlated_columns = self.find_correlated_columns(self.df)

        # Drop one of the correlated columns
        for column1, column2 in correlated_columns:
            self.df.drop(column2, axis=1)

    def discretize(self):
        self.df["Income Tax Rate (%)"].groupby(pd.qcut(self.df["Income Tax Rate (%)"], 5)).transform("mean")
        self.df["Population (Millions)"].groupby(pd.qcut(self.df["Population (Millions)"], 7)).transform("median")

    def transform(self):
        scaler = StandardScaler()
        scaler.fit(self.df.select_dtypes(include="number"))
        self.df[self.df.select_dtypes(include="number").columns] = scaler.transform(self.df.select_dtypes(include="number"))

    def save(self):
        self.df.to_csv("res_dpre.csv")

    @staticmethod
    def find_correlated_columns(df, threshold=0.9):

        columns = df.select_dtypes(include="number").columns
        correlated_columns = []

        for i in range(len(columns)):
            for j in range(i + 1, len(columns)):
                correlation = df[columns[i]].corr(df[columns[j]])
                if abs(correlation) >= threshold:
                    correlated_columns.append((columns[i], columns[j]))

        return correlated_columns


if __name__ == "__main__":
    # get arg from terminal
    df_path = sys.argv[1]

    try:
        process = ProcessStep(df_path)
        process.clean()
        process.reduce()
        process.discretize()
        process.transform()
        process.save()

    except:
        print("One of the steps has failed.")
    else:
        print("The dataset has been preprocessed successfully and redirected to next step.")
        print(subprocess.run(["python3", "eda.py"], capture_output=True).stdout.decode("utf-8"))