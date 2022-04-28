import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn2, venn2_circles, venn3_circles, venn3_unweighted
df_I = pd.read_csv('Pared_data/I.csv')
df_U = pd.read_csv('Pared_data/U.csv')
df_EDU = pd.read_csv('Pared_data/EDU.csv')

def RightCompare(df1, df2):
    return pd.merge(df1, df2, on=['UniProt','Gene symbol'], how="outer", indicator=True).query('_merge=="right_only"')

# def rightCompare(df1, df2):
#     return pd.merge(df1, df2, on='UniProt')
#
# def midCompare(df1, df2):
#     return pd.merge(df1, df2, on='UniProt')


if __name__ == "__main__":
    # print(RightCompare(df_I, df_U))

    # Solo U
    print("U")
    print(RightCompare( df_EDU,RightCompare(df_I, df_U)[['UniProt', 'Gene symbol']])[['UniProt', 'Gene symbol']])
    iso1 = RightCompare(df_EDU, RightCompare(df_I, df_U)[['UniProt', 'Gene symbol']])[['UniProt', 'Gene symbol']].rename(columns={'UniProt':'UniProt_U', "Gene symbol":"Gene symbol_U"})
    # Solo I

    print("------------------")
    print("I")
    print(RightCompare( df_EDU,RightCompare(df_U, df_I)[['UniProt', 'Gene symbol']])[['UniProt', 'Gene symbol']])
    iso2 = RightCompare(df_EDU, RightCompare(df_U, df_I)[['UniProt', 'Gene symbol']])[['UniProt', 'Gene symbol']].rename(columns={'UniProt':'UniProt_I', "Gene symbol":"Gene symbol_I"})
    # Solo -Edu

    print("------------------")
    print("-EdU")
    print(RightCompare( df_I,RightCompare(df_U, df_EDU)[['UniProt', 'Gene symbol']])[['UniProt', 'Gene symbol']])
    iso3 = RightCompare(df_I, RightCompare(df_U, df_EDU)[['UniProt', 'Gene symbol']])[['UniProt', 'Gene symbol']].rename(columns={'UniProt':'UniProt_EdU', "Gene symbol":"Gene symbol_EdU"})

    iso_data = pd.concat([iso1, iso2,iso3],axis=0, ignore_index=True)
    # iso_data = pd.merge([iso1, iso2,iso3],axis=0,how='outer',ignore_index=True)

    iso_data.to_csv(r'C:/Users/micha/PycharmProjects/Protien_Data/Pared_data/Isolate_data.csv', index=False, header=True)


    a = venn3_unweighted([set(df_I["UniProt"]),
                          set(df_U["UniProt"]),
                          set(df_EDU["UniProt"])],
                         subset_areas=(5,5,1,5,1,1,1),
                         set_labels=("Induced", "Uninduced","-EdU"))

    for label in a.set_labels:
        label.set_family('arial')
        label.set_fontsize(16)
    for label in a.subset_labels:
        label.set_family('arial')
        label.set_fontsize(14)
    venn3_circles(((5,5,1,5,1,1,1)),linewidth=1)
    # plt.show()
#
