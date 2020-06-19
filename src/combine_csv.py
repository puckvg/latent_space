#!/usr/bin/env python3
import pandas as pd 

if __name__ == "__main__":
    stable_df = pd.read_csv("../data/stable.csv")
    unstable_df = pd.read_csv("../data/unstable.csv")
    df = pd.concat([stable_df, unstable_df], ignore_index=True)

    df.to_csv("../stability.csv", index=False)
