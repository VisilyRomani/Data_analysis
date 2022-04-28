import unittest
import pandas as pd
import numpy.testing as np
from pandas._testing import assert_frame_equal
from removeFalsePositive import compareLeft, combineDataframe


class TestRemoveFalsePositive(unittest.TestCase):
    def test_same_data(self):
        """
        dataframes with some matching data
        """
        data1 = [['abc', 123], ['cde', 13], ['efg', 567], ['hij', 789]]
        data2 = [['abc', 123], ['cde', 13]]
        data3 = [['efg', 567], ['hij', 789]]
        df1 = pd.DataFrame(data1, columns=['Protein', 'FC'])
        df2 = pd.DataFrame(data2, columns=['Protein', 'FC'])
        df3 = pd.DataFrame(data3, columns=['Protein', 'FC'])
        result = compareLeft(df1, df2).drop(columns=['_merge'])
        result.reset_index(drop=True, inplace=True)
        assert_frame_equal(result, df3)

    def test_right_big(self):
        """
        dataframe with right matching all left and right is bigger
        """
        data1 = [['abc', 123], ['cde', 13], ['efg', 567], ['hij', 789]]
        data2 = [['abc', 123], ['cde', 13]]
        df1 = pd.DataFrame(data1, columns=['Protein', 'FC'])
        df2 = pd.DataFrame(data2, columns=['Protein', 'FC'])
        result = compareLeft(df2, df1).drop(columns=['_merge'])
        np.assert_array_equal(result.values, pd.DataFrame([], columns=['Protein', 'FC']).values)

    def test_different_df(self):
        """
        comparing completely different dataframes
        """
        data1 = [['abc', 123], ['cde', 13], ['efg', 567], ['hij', 789]]
        data3 = [['ase', 567], ['kuy', 4562], ['dfg', 978], ['fd', 23]]
        df1 = pd.DataFrame(data1, columns=['Protein', 'FC'])
        df3 = pd.DataFrame(data3, columns=['Protein', 'FC'])
        result = compareLeft(df1, df3).drop(columns=['_merge'])
        np.assert_array_equal(result.values, df1.values)

    def test_duplicate(self):
        data1 = [['abc', 123], ['cde', 13], ['efg', 567], ['hij', 789]]
        df1 = pd.DataFrame(data1, columns=['Protein', 'FC'])
        result = compareLeft(df1, df1).drop(columns=['_merge'])
        np.assert_array_equal(result.values, pd.DataFrame([], columns=['Protein', 'FC']).values)

    def test_combineDataframetest1(self):
        data1 = [['abc', 123], ['cde', 13], ['efg', 567], ['hij', 789]]
        df1 = pd.DataFrame(data1, columns=['Protein', 'FC'])
        result = combineDataframe(df1, df1)
        np.assert_array_equal(result.values, df1.values)

    def test_combineDataframetest2(self):
        data1 = [['abc', 123], ['cde', 13], ['efg', 567], ['hij', 789]]
        df1 = pd.DataFrame(data1, columns=['Protein', 'FC'])

        data2 = [['sef', 64]]
        df2 = pd.DataFrame(data2, columns=['Protein', 'FC'])

        data3 = [['abc', 123], ['cde', 13], ['efg', 567], ['hij', 789],['sef', 64]]
        df3 = pd.DataFrame(data3, columns=['Protein', 'FC'])

        result = combineDataframe(df1, df2)
        np.assert_array_equal(result.values, df3.values)

    def test_combineDataframetest3(self):
        data1 = [['abc', 123], ['cde', 13], ['efg', 567], ['hij', 789]]
        df1 = pd.DataFrame(data1, columns=['Protein', 'FC'])

        data2 = [['sef', 64]]
        df2 = pd.DataFrame(data2, columns=['Protein', 'FC'])

        data3 = [['sef', 64], ['abc', 123], ['cde', 13], ['efg', 567], ['hij', 789]]
        df3 = pd.DataFrame(data3, columns=['Protein', 'FC'])

        result = combineDataframe(df2, df1)
        np.assert_array_equal(result.values, df3.values)



if __name__ == '__main__':
    unittest.main()
