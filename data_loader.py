# https://pysus.readthedocs.io/en/latest/Analyzing%20SIA.html


import pandas as pd
from pysus.online_data.SIA import download
from pysus.online_data import parquets_to_dataframe
from config import groups, states, years, months


def load_data_path():
    d = dict()
    for group in groups:
        files = download(states=states, years=years, months=months, group=group)
        d[group] = files
    return d


def split_file_name(file_name):
    fname = file_name.split('/')[-1].split('.')[0]
    infos = {
        'APAC': fname[:2],
        'UF': fname[2:4],
        'ANO': int('20' + fname[4:6]),
        'MES': int(fname[6:8]),}
    return infos


def get_dataframe(files_path, columns, filtro_max_cid):
    df_list = list()
    for _, files in files_path.items():
        for f in files:
            try:
                df = parquets_to_dataframe(f)[columns]
                filtro_cid = df['AP_CIDPRI'].apply(
                    lambda x: int(x[1:]) <= filtro_max_cid)
                df = df[filtro_cid]
                infos = split_file_name(f)
                for k, v in infos.items():
                    df[k] = v
                df_list.append(df)
            except:
                print(f)
    df = pd.concat(df_list)
    return df