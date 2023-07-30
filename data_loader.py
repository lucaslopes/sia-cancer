from pysus.online_data.SIA import download
from config import groups, states, years, months


def load_data_path():
    d = dict()
    for group in groups:
        files = download(states=states, years=years, months=months, group=group)
        d[group] = files
    return d