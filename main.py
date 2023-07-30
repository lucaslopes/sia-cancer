from pysus.online_data.SIA import download, show_datatypes
from pysus.online_data import parquets_to_dataframe


# Sobre a coleta de dados no SIA:
# Vamos analisar as APACs (Autorização de Procedimentos Ambulatoriais de Alta Complexidade)
# Filtrar por
# - Quimioterapia: códigos 03.04.02 até 03.04.08
# - Radioterapia: código 03.04.01
# Ano: 2018 e 2019
# CID: C00 até C75


# show_datatypes()
# AQ - APAC de Quimioterapia
# AR - APAC de Radioterapia
groups = ['AQ', 'AR']
states = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
years = [2018, 2019]
months = list(range(1, 13))


files_aq = download(states=states, years=years, months=months, group=groups[0])
files_ar = download(states=states, years=years, months=months, group=groups[1])


df = parquets_to_dataframe(files_aq[0])
print(df.head())