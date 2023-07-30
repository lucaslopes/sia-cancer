import pandas as pd
from data_loader import load_data_path, get_dataframe
from config import groups, years, columns, filtro_max_cid


def main():
    files_path = load_data_path()
    out_path = '~/Databases/sia/SIA'
    df = get_dataframe(files_path, columns, filtro_max_cid)
    df.to_parquet(f'{out_path}.parquet', index=False)
    # for group in groups:
    #     for year in years:
    #         df[(df['APAC'] == group) & (df['ANO'] == year)].to_excel(
    #             f'{out_path}_{group}_{year}.xlsx', index=False)
# ERROR:root:No objects to concatenate
# /Users/lucas/pysus/AQRR1806.parquet
# /Users/lucas/pysus/AQTO1910.parquet
# /Users/lucas/pysus/ARRS1806.parquet
# /Users/lucas/pysus/ARMG1911.parquet


__name__ == '__main__' and main()