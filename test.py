import unittest
import pandas as pd
import numpy as np

"""
You are give a dataset of our different campaigns, their keywords, and average position

  campaignname                           keyword  averageposition  impressions
0       IDT US                best id protection              1.5            2
1       IDT US      identity protection services              4.0            4
2       IDT US        credit monitoring services              2.7          356
3       IDT US         identity theft protection              5.0           58
4       IDT US           identity theft services              3.0            1
5       IDT US         fraud protection services              6.0            1
6       IDT US      +credit +monitoring +reviews              2.3           10

write a model that - given a campaign name, and n-gram will return an estimated position or the n-gram.

1) Write the code according to clean-code best practices.
2) Think about the usability of your API. how do you make it acessible to developers? 
3) How would you test your code? you dont have to write tests, but be prepared with an answer. 

"""


class TestStringMethods(unittest.TestCase):

    def test_dataset(self):
        dataset = pd.read_csv("dataset.csv")
        print(dataset.head(10))


if __name__ == '__main__':
    unittest.main()