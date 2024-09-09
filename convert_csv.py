import pandas as pd

def ler_salvar(solana_csv, solananew):
    df = pd.read_csv(solana_csv)

    df.to_csv(solananew, sep=';', index=False )

    print(f'O arquivo foi salvo em {solananew}. ')
    print(df.head())

solana_csv = 'C:/Users/Nicolas/Desktop/Projeto Crypto/data/solana.csv'
solananew = 'data/solananew.csv'

ler_salvar(solana_csv, solananew)







