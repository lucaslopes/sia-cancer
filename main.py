from data_loader import load_data_path
from pysus.online_data import parquets_to_dataframe


files_path = load_data_path()


df = parquets_to_dataframe(files_path['AQ'][0])
print(df.head())