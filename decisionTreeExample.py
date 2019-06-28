# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 00:46:13 2019

@author: Sneha

Create a model that classifie whether the given fruit is Apple or Orange

"""


#%%   Create a DataSet


Feature = [[130,1],[140,1],[150,0],[170,0]]
Labels=[1,1,0,0]



#%% Create a model


from sklearn import tree

clf=tree.DecisionTreeClassifier()


#%% train the model

clf=clf.fit(Feature,Labels)


#%% Predit the value

print(clf.predict([[160,0]]))

#%%
'''
1 stands for apple 
0 stands for orange

''' 