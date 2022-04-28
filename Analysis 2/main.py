import pandas as pd

df_I = pd.read_csv('raw_data/A3A_I.csv')
df_U = pd.read_csv('raw_data/A3A_U.csv')
df_EDU = pd.read_csv('raw_data/No_EDU.csv')

df_raw_dun = pd.read_csv('published_data/Dungrawala_raw.csv')
df_raw_lec = pd.read_csv('published_data/Lecona_raw.csv')
df_raw_loi = pd.read_csv('published_data/Loissant_raw_filter.csv')

# filters data for Accession Number and Protein name while dropping duplicates
def filterSelf(df):
    return df[["UniProt", "Gene symbol"]].drop_duplicates()

def compare(df1, df2_raw, df3_raw, df4_raw):
    a = pd.merge(df1, df2_raw, on='UniProt')
    b = pd.merge(df1, df3_raw, on='UniProt')
    c = pd.merge(df1, df4_raw, on='UniProt')

    d = pd.merge(a, b, on='UniProt')
    e = pd.merge(c, d, on='UniProt')
    return e

if __name__ == '__main__':
    compare(filterSelf(df_I), filterSelf(df_raw_dun), filterSelf(df_raw_lec), filterSelf(df_raw_loi))[["UniProt", "Gene symbol_y_y"]].to_csv(r'C:/Users/micha/PycharmProjects/Protien_Data/Pared_data/I.csv', index=False, header=True)
    compare(filterSelf(df_U), filterSelf(df_raw_dun), filterSelf(df_raw_lec), filterSelf(df_raw_loi))[["UniProt", "Gene symbol_y_y"]].to_csv(r'C:/Users/micha/PycharmProjects/Protien_Data/Pared_data/U.csv',index = False, header=True)
    compare(filterSelf(df_EDU), filterSelf(df_raw_dun), filterSelf(df_raw_lec), filterSelf(df_raw_loi))[["UniProt", "Gene symbol_y_y"]].to_csv(r'C:/Users/micha/PycharmProjects/Protien_Data/Pared_data/EDU.csv',index = False, header=True)
