#thanks to https://docs.python.org/3/library/csv.html
import csv

def get_agent_time(filename:str) -> list[dict[str, str|float]]:
    # define storage dicts/lists
    agent_counts = {}
    total_active_days = {}
    total_hold_days = {}
    data = []

    # organize data into counts, active time, hold time by agent name
    with open('data/FY20-25.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            agent = row[1]
            active_days = row[3]
            hold_days = row[4]
            if agent == "":
                agent = "Unknown"
            if agent not in agent_counts:
                agent_counts[agent] = 1
                total_active_days[agent] = float(active_days)
                total_hold_days[agent] = float(hold_days)
            else:
                agent_counts[agent] += 1
                total_active_days[agent] += float(active_days)
                total_hold_days[agent] += float(hold_days)

    # get averages and create dicts from the data
    for agent, count in list(agent_counts.items())[:16]:
        avg_active_days = total_active_days[agent] / count
        avg_hold_days = total_hold_days[agent] / count
        datum = {"agent": agent, "avg_active_days": avg_active_days, "avg_hold_days": avg_hold_days}
        data.append(datum)
    return data