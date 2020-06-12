import Leap, pandas as pd, numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
data =pd.read_csv('angka_sudut_panjang.csv', index_col=False)

import timeit
start_time = timeit.default_timer()
# code you want to evaluate

x=data.iloc[:,1:41].values
y=data.iloc[:,0]
knn=KNeighborsClassifier(n_neighbors=20)
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=5)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
list =[60.7426528931, -20.3381, -44.0985, -30.9451, 95.5250320435, -42.162, 4.11668, -81.951, 100.405960083, -11.6909, 0.43277, -95.8731, 95.6866149902, 20.1185, -8.09286, -89.1964, 87.7267990112, 47.0567, -26.2156, -64.6902, 69.6635360718, 60.7595, 17.0719, -18.2969, 99.8990859985, 45.236, 1.32764, -85.1855, 103.738143921, 29.084, -8.01297, -95.1301, 95.8818511963, 4.93065, -9.21727, -91.3547, 86.9827041626, -31.3389, -13.2869, -76.2075]

list_dicari = []

dicari =np.array(list)

baru= np.reshape(dicari,(-1,1))
baru_lagi=np.reshape(dicari,(1,-1))
a=knn.predict(baru_lagi)
print(a)


