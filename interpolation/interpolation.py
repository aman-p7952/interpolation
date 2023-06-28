#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 14:29:57 2023

@author: amanpandey
"""
import pandas as pd
import matplotlib.pyplot as plt
# from util.connect import connect
# import numpy as np
# command = '''SELECT  "dataStream" from Exercise  where id= 23008 '''
# print(command)
# frame = connect(command)[0]
# h = frame[-1]['device']['height']
# w = frame[-1]['device']['width']
# keypoints_with_scores = np.array(
#             [[[frame[j]["frames"][i]["y"]/h, (frame[j]["frames"][i]["x"]/w)+0.3, frame[j]["frames"][i]["score"]]for i in range(17)] for j in range(len(frame))  ])
# print(len(keypoints_with_scores))
# timestamp=[frame[i]['timestamp'] for i in range(len(frame))]
# print(len(timestamp))

df= pd.read_csv("./dataset/push1.csv")
df = df.drop("frame",axis = 1)
df.dropna(axis=0,how="any",inplace=True)
# if len(df)<LEN:
    
#     for i in range(len(df),LEN):
#         df.loc[len(df)] = 0
#         df["state"].values[i]="None"
# elif len(df)>LEN:
#     df.drop(df.index[[LEN,len(df)]])
df1=df.iloc[:, 0:132]
df1 = [pd.to_numeric(df1.iloc[i], errors='coerce') for i in range(len(df1))]

#print(df1.size(0))
# df2=[key[i] for i in df2]

from sklearn.decomposition import PCA

pca = PCA(n_components=2)

principalComponents = pca.fit_transform(df1)

principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])
finalDf = pd.concat([principalDf, df[['state']]], axis = 1)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)

# targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
# colors = ['r', 'g', 'b']
# for target, color in zip(targets,colors):
#     indicesToKeep = finalDf['state'] == target
#     ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
#                , finalDf.loc[indicesToKeep, 'principal component 2']
#                , c = color
#                , s = 50)
# ax.legend(targets)
# ax.grid()
ax.scatter(finalDf.loc[:, 'principal component 1']
                , finalDf.loc[:, 'principal component 2']
                # , c = color
                , s = 50)
