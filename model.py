import sys
import pandas as pd
from sklearn.cluster import KMeans
import subprocess

if __name__ == "__main__":
    try:
        # read dataset from path specified
        df = pd.read_csv("res_dpre.csv")

        k_means = KMeans(n_clusters=3)

        k_means.fit(df.select_dtypes(include="number"))

        with open("k.txt", "w") as file:
            for k, count in pd.Series(k_means.labels_).value_counts().items():
                file.write(f"cluster {k} -> {count}\n")

    except FileNotFoundError:
        print("This dataset does not exist in the provided path.")
    except:
        print("There is an error in the model.")
    else:
        print("The model step has been done successfully and redirected to next step.")
        #print(subprocess.run(["python3", "model.py"], capture_output=True).stdout.decode("utf-8"))