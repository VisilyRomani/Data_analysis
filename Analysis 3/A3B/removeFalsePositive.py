# imports panda library into python (panda is used for data analysis in Python)
import pandas as pd
"""
 NOTE:
   Within the csv files I renamed the column containing the Log FC data into "Log FC"
   because for each file that is being compared the column name is different
       eg. 'Log FC ([I_A3A] vs [U_A3A]) : Normalized' --> 'Log FC'
"""

# imports files into python
DOWNI_v_EDU = pd.read_csv('Raw/DOWN I vs EdU.csv')
DOWNU_v_EDU = pd.read_csv('Raw/DOWN U vs EdU.csv')

UPI_v_U = pd.read_csv('Raw/UP I vs U.csv')
DOWNI_v_U = pd.read_csv('Raw/DOWN I vs U.csv')


def compareLeft(df1, df2):
    """
    :param df1: represents the first dataframe (dataset)
    :param df2: represents the second dataframe (dataset)
    :return: the left values based on the protein which exclude matches
    """
    innerMerge = pd.merge(df1, df2[['Protein']], how='left', indicator=True, on='Protein')
    innerMerge = innerMerge[innerMerge['_merge'] == 'left_only']
    return innerMerge


def combineDataframe(df1, df2):
    """
    :param df1: represents the first dataframe (dataset)
    :param df2: represents the second dataframe (dataset)
    :return: the outer join of both dataframes
    """
    mergeData = pd.merge(df1, df2, how='outer')
    return mergeData


if __name__ == '__main__':
    """
    comp1: compares UPI_v_U and DOWNU_v_EDU and returns all proteins from UPI_v_U and removes matches from DOWNU_v_EDU
    comp2: compares UPI_v_U and DOWNI_v_EDU and returns all proteins from UPI_v_U and removes matches from DOWNI_v_EDU
    comp3: compares DOWNI_v_U and DOWNU_v_EDU and returns all proteins from DOWNI_v_U and removes matches from DOWNU_v_EDU
    comp4: compares DOWNI_v_U and DOWNI_v_EDU and returns all proteins from DOWNI_v_U and removes matches from DOWNI_v_EDU
    """

    comp_1 = compareLeft(UPI_v_U, DOWNU_v_EDU)
    comp_2 = compareLeft(UPI_v_U, DOWNI_v_EDU)
    # combines comparison 1 and comparison 2 (comp1, comp2)
    mergedDFUp = combineDataframe(comp_1, comp_2).drop(columns=['_merge'])

    comp_3 = compareLeft(DOWNI_v_U, DOWNU_v_EDU)
    comp_4 = compareLeft(DOWNI_v_U, DOWNI_v_EDU)
    # combines comparison 3 and comparison 4 (comp3, comp4)
    mergedDFDown = combineDataframe(comp_3, comp_4).drop(columns=['_merge'])

    mergedDFUp.to_csv('C:/Users/micha/PycharmProjects/IPOND/A3B/DATA/merged_up.csv', index = False, header=True)
    mergedDFDown.to_csv('C:/Users/micha/PycharmProjects/IPOND/A3B/DATA/merged_down.csv', index = False, header=True)
