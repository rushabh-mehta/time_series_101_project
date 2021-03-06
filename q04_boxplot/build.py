# %load q04_boxplot/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import seaborn as sns
import datetime
# import sys
# sys.path.append('./')
from greyatomlib.time_series_101_project.q02_data_splitter.build import q02_data_splitter

'write your solution here'
def q04_boxplot(path,x='month',y='Sales',kind='box',order_of_the_axis=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],temp=8):
    X_train,X_test = q02_data_splitter(path)
    X_train['month'] = X_train['Month'].dt.strftime('%b')
    X_train['year'] = X_train['Month'].dt.year
    sns.factorplot(x=x,y=y,data=X_train,kind=kind)
    plt.show()


