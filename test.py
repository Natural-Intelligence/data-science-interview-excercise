import unittest
import pandas as pd
import numpy as np

"""
As a marketing company we are always looking for search terms that will show up in high position. 
You are given a dataset of our different google campaigns, their keywords, and average position

  campaignname                           keyword  averageposition  impressions
0       IDT US                best id protection              1.5            2
1       IDT US      identity protection services              4.0            4
2       IDT US        credit monitoring services              2.7          356
3       IDT US         identity theft protection              5.0           58
4       IDT US           identity theft services              3.0            1
5       IDT US         fraud protection services              6.0            1
6       IDT US      +credit +monitoring +reviews              2.3           10

write a model that - given a campaign name, and an n-gram will return an estimated position or the n-gram.

for example - 
for input (campaign: "IDT US", keyword: "best social security number prevention service") you might return average position 2.4 
for input (campaign: "IDT US", keyword: "fraud service") you might return average position 7.3

1) Write the code according to clean-code best practices.
2) Write a module that will be used by developers to estimate the positions of their ads,
   Think about the usability of your API. how do you make it acessible to developers? 
3) How would you test your code?
"""


class TestStringMethods(unittest.TestCase):

    def test_dataset(self):
        dataset = pd.read_csv("dataset.csv")
        print(dataset.head(10))


if __name__ == '__main__':
    unittest.main()