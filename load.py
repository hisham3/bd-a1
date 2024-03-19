import sys
import pandas as pd
import subprocess

if __name__ == "__main__":
    # get arg from terminal
    df_path = sys.argv[1]

    try:
        # read dataset from path specified
        df = pd.read_excel(df_path)

    except FileNotFoundError:
        print("This dataset does not exist in the provided path.")
    else:
        print("The dataset has been read successfully and redirected to next step.")
        print(subprocess.run(["python3", "dpre.py", df_path], capture_output=True).stdout.decode("utf-8"))