# Sobre a coleta de dados no SIA:
# Vamos analisar as APACs (Autorização de Procedimentos Ambulatoriais de Alta Complexidade)
# Filtrar por
# - Quimioterapia: códigos 03.04.02 até 03.04.08
# - Radioterapia: código 03.04.01
# - Ano: 2018 e 2019
# - CID: C00 até C75


# AQ - APAC de Quimioterapia
# AR - APAC de Radioterapia
groups = ['AQ', 'AR']
states = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
years = [2018, 2019]
months = list(range(1, 13))

filtro_max_cid = 75

columns = [
    'AP_CODUNI',
    'AP_CMP',
    'AP_PRIPAL',
    'AP_VL_AP',
    'AP_UFMUN',
    'AP_TPUPS',
    'AP_NUIDADE',
    'AP_SEXO',
    'AP_RACACOR',
    'AP_MUNPCN',
    'AP_UFDIF',
    'AP_MNDIF',
    'AP_OBITO',
    'AP_UNISOL',
    'AP_CIDCAS',
    'AP_CIDPRI',
    'AP_CIDSEC',
    'AP_ETNIA',   
]