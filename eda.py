import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import subprocess

if __name__ == "__main__":
    try:
        # read dataset from path specified
        df = pd.read_csv("res_dpre.csv")

        # First insight
        with open("eda-in-1.txt", "w") as file:
            stats = df.describe()
            mode_stats = df.mode().loc[0]
            stats.loc['mode'] = mode_stats

            file.write("> Insight: GDP Growth Rate and Inflation can have a negative value that means decreasing in the Rate or Percentage.")

        # Second insight
        with open("eda-in-2.txt", "w") as file:
            # using the following plot between `GDP Growth Rate (%)` and `Unemployment (%)` we have insighted that
            # sns.jointplot(x=df["GDP Growth Rate (%)"], y=df["Unemployment (%)"], kind="hex")

            file.write("> Insight: Countries that have lower unemployment rate most likely have a higher GDP growth rate.")

        # Third insight
        with open("eda-in-3.txt", "w") as file:
            # using the following plot between `GDP Growth Rate (%)` and `Unemployment (%)` we have insighted that
            # g = sns.JointGrid(data=df, x="Trade Freedom", y="Business Freedom", space=0, ratio=17)
            # g.plot_joint(sns.scatterplot, sizes=(30, 120), color="g", alpha=.6, legend=False)
            # g.plot_marginals(sns.rugplot, height=1, color="g", alpha=.6)

            file.write("> Insight: Countries that have more trade freedom are more likley to have higher bussiness freedom score.")

    except FileNotFoundError:
        print("This dataset does not exist in the provided path.")
    except:
        print("There is an error in one of the insights.")
    else:
        print("The dataset has been explored successfully and redirected to next step.")
        print(subprocess.run(["python3", "vis.py"], capture_output=True).stdout.decode("utf-8"))