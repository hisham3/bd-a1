import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import subprocess

if __name__ == "__main__":
    try:
        # read dataset from path specified
        df = pd.read_csv("res_dpre.csv")

        f, ax = plt.subplots(figsize=(15, 10))

        sns.boxplot(x="Region", y="Income Tax Rate (%)", data=df)

        ax.set(title="Income Tax Rate for Regions")

        plt.savefig('vis.png', format='png', dpi=250)

    except FileNotFoundError:
        print("This dataset does not exist in the provided path.")
    else:
        print("The visualization step has been done successfully and redirected to next step.")
        print(subprocess.run(["python3", "model.py"], capture_output=True).stdout.decode("utf-8"))