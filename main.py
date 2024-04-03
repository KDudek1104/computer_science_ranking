import pandas as pd


df = pd.read_csv('graduates-major-data.csv', sep=';', low_memory=False)

additional_columns = [
    # 'P_E_ZAR_STUD', 'P_E_ZAR_NSTUD', 'P_E_ZAR', 'P_E_ZAR_NSTUD_P1', 'P_E_ZAR_P1',
    # 'P_E_ZAR_NSTUD_P2', 'P_E_ZAR_P2', 'P_E_ZAR_NSTUD_P3', 'P_E_ZAR_P3',
    # 'P_E_ZAR_NSTUD_P4', 'P_E_ZAR_P4',
    # 'P_E_ZAR_DOSW', 'P_E_ZAR_NDOSW', 'P_E_ZAR_DOSW_P1', 'P_E_ZAR_NDOSW_P1', 'P_E_ZAR_DOSW_P2', 'P_E_ZAR_NDOSW_P2',
    # 'P_E_ZAR_DOSW_P3', 'P_E_ZAR_NDOSW_P3', 'P_E_ZAR_DOSW_P4', 'P_E_ZAR_NDOSW_P4',
    # 'P_ME_ZAR_STUD', 'P_ME_ZAR_NSTUD', 'P_ME_ZAR', 'P_ZAR_Q1', 'P_ZAR_Q2', 'P_ZAR_Q3', 'P_ZAR_Q4',
    # 'P_ME_ZAR_STUD_P1', 'P_ME_ZAR_NSTUD_P1', 'P_ME_ZAR_P1', 'P_ME_ZAR_STUD_P2', 'P_ME_ZAR_NSTUD_P2', 'P_ME_ZAR_P2',
    # 'P_ME_ZAR_STUD_P3', 'P_ME_ZAR_NSTUD_P3', 'P_ME_ZAR_P3', 'P_ME_ZAR_STUD_P4', 'P_ME_ZAR_NSTUD_P4', 'P_ME_ZAR_P4',
    # 'P_ME_ZAR_DOSW', 'P_ME_ZAR_NDOSW', 'P_ME_ZAR_DOSW_P1',
    # 'P_ME_ZAR_NDOSW_P1', 'P_ME_ZAR_DOSW_P2', 'P_ME_ZAR_NDOSW_P2', 'P_ME_ZAR_DOSW_P3', 'P_ME_ZAR_NDOSW_P3',
    # 'P_ME_ZAR_DOSW_P4', 'P_ME_ZAR_NDOSW_P4',
    'P_CZY_BEZR_P1', 'P_CZY_BEZR_P4', 'P_ME_ZAR_STUD_P1', 'P_ME_ZAR_STUD_P4', 'P_IF_2st', 'P_IF_2st_ucz', 'P_ME_ZAR_ETAT_DOSW_P4', 'P_ME_ZAR_ETAT_NDOSW_P4'
]

needed_columns = [
    'P_KIERUNEK_NAZWA', 'P_NAZWA_UCZELNI', 'P_NAZWA_JEDN', 'P_POZIOM_TEKST_PL', 'P_ROKDYP',
] + additional_columns

df_selected = df[needed_columns]

df_selected = df_selected[df_selected['P_KIERUNEK_NAZWA'].str.contains('Informatyka', na=False)]
df_selected = df_selected[df_selected['P_ROKDYP'] == 2016]
df_selected = df_selected[df_selected['P_POZIOM_TEKST_PL'].str.contains('pierwszego', na=False)]
columns_to_exclude = ['P_ROKDYP', 'P_POZIOM_TEKST_PL']
df_selected = df_selected.drop(columns=columns_to_exclude)
df_selected.to_excel('dane_uczelni.xlsx', index=False)
