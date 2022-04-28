import pandas as pd
UvI_UP = pd.read_csv('DATA/Raw/U_vs_I_UP.csv')
UvI_DO = pd.read_csv('DATA/Raw/U_vs_I_DOWN.csv')
UvEDU_UP = pd.read_csv('DATA/Raw/U_vs_EDU_UP.csv')
UvEDU_DO = pd.read_csv('DATA/Raw/U_vs_EDU_DOWN.csv')
IvEDU_UP = pd.read_csv('DATA/Raw/I_vs_EDU_UP.csv')
IvEDU_DO = pd.read_csv('DATA/Raw/I_vs_EDU_DOWN.csv')


def UP_LOG_U_EDU(df1, df2):
    output = pd.merge(df1, df2[['Protein', 'Log FC ([A3A_U] vs [EDU]) : Normalized']], how="inner", on='Protein')
    return output


def UP_LOG_I_EDU(df1, df2):
    output = pd.merge(df1, df2[['Protein', 'Log FC ([A3A_I] vs [EDU]) : Normalized']], how="inner", on='Protein')
    return output


def DOWN(df1, df2):
    output = pd.merge(df1, df2[['Protein']], how="left", on='Protein')
    output = output.reset_index(drop=True)
    return output


if __name__ == '__main__':

    U_UP_EDU_UP = UP_LOG_U_EDU(UvI_UP, UvEDU_UP).rename(columns={'Log FC ([A3A_U] vs [EDU]) : Normalized':'Log FC EDU'})
    I_UP_EDU_UP = UP_LOG_I_EDU(UvI_UP, IvEDU_UP).rename(columns={'Log FC ([A3A_I] vs [EDU]) : Normalized':'Log FC EDU'})
    pd.set_option('display.max_rows', U_UP_EDU_UP.shape[0]+1)

    merged_UP = U_UP_EDU_UP.append(I_UP_EDU_UP)
    merged_UP = merged_UP.drop_duplicates(subset=['Protein'])


    # !!!
    I_DO_EDU_UP = UP_LOG_I_EDU(UvI_DO, IvEDU_UP).rename(columns={'Log FC ([A3A_I] vs [EDU]) : Normalized':'Log FC EDU'})
    U_DO_EDU_UP = UP_LOG_U_EDU(UvI_DO, UvEDU_UP).rename(columns={'Log FC ([A3A_U] vs [EDU]) : Normalized':'Log FC EDU'})

    merged_DO = U_DO_EDU_UP.append(I_DO_EDU_UP)
    merged_DO = merged_DO.drop_duplicates(subset=['Protein'])
    # print(merged_UP)



    # EXCLUDED VALUES OF [U v I] & [U v EDU]
    U_UP_EDU_DO = DOWN(UvI_UP, UvEDU_DO)
    I_UP_EDU_DO = DOWN(UvI_UP, IvEDU_DO)
    exclude_UP = U_UP_EDU_DO.append(I_UP_EDU_DO)
    exclude_UP = exclude_UP.drop_duplicates(subset='Protein')




    I_DO_EDU_DO = DOWN(UvI_DO, IvEDU_DO)
    U_DO_EDU_DO = DOWN(UvI_DO, UvEDU_DO)
    exclude_DO = I_DO_EDU_DO.append(U_DO_EDU_DO)
    exclude_DO = exclude_DO.drop_duplicates(subset='Protein')

    exclude_DO.to_csv('C:/Users/micha/PycharmProjects/UpDownProtein/DATA/Manipulated_Data/Exclude_down.csv',index = False, header=True)
    exclude_UP.to_csv('C:/Users/micha/PycharmProjects/UpDownProtein/DATA/Manipulated_Data/Exclude_up.csv',index = False, header=True)

    # print(exclude_UP)

