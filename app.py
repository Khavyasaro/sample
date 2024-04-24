import pandas as pd
import numpy as np
import math, datetime
from sklearn import preprocessing #, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns


style.use('ggplot')

df = pd.read_csv("performance.csv")



df = df[[ "Part No", "Description", "Supplier Name", "Model", "Jan Sch", "Jan Del", "Jan Sup", "Feb Sch", "Feb Del", "Feb Sup", "Mar Sch", "Mar Del", "Mar Sup", "Apr Sch", "Apr Del", "Apr Sup", "May Sch", "May Del", "May Sup", "Jun Sch", "Jun Del", "Jun Sup", "July Sch", "Jul Del", "Jul Sup", "Aug Sch", "Aug Del", "Aug Sup", "Sep Sch", "Sep Del", "Sep Sup", "Oct Sch", "Oct Del", "Oct Sup", "Nov Sch", "Nov Del", "Nov Sup", "Dec Sch", "Dec Del", "Dec Sup", ]]
df1 = df[["Jan Sup", "Feb Sup", "Mar Sup", "Apr Sup", "May Sup", "Jun Sup", "Jul Sup", "Aug Sup", "Sep Sup", "Oct Sup", "Nov Sup", "Dec Sup", ]]
