# thanks to https://docs.python.org/3/library/csv.html
# thanks to https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
import csv
import json

import pandas as pd
from pandas import DataFrame


def get_agent_time(filename:str) -> DataFrame:
    # define storage dicts/lists
    agent_names = []
    active_days = []
    hold_days = []

    # retrieve agent names, active days, and hold days from the csv file
    with open('data/FY20-25.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            agent_names.append(row[1] if row[1] != "" else "unknown")
            active_days.append(float(row[3]))
            hold_days.append(float(row[4]))

    # sort and average with pandas
    dataframe = pd.DataFrame({"agent_name": agent_names, "active_days": active_days, "hold_days": hold_days})
    sorted_data = dataframe.groupby(["agent_name"]).mean()
    return sorted_data.reset_index()

get_agent_time('data/FY20-25.csv')