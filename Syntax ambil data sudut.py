import Leap, pandas as pd, numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.multiclass import OneVsOneClassifier
from sklearn.svm import SVC
data =pd.read_csv('angka.csv', index_col=False)

import timeit
start_time = timeit.default_timer()
# code you want to evaluate

x=data.iloc[:,1:11].values
y=data.iloc[:,0]
knn=KNeighborsClassifier(n_neighbors=20)
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=5)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
list ='58.2675895691,93.4447097778,112.943069458,107.31952667200001,92.7183609009,66.4650497437,71.8667449951,100.71430206299999,90.8048400879,1.8559494019'
new_list = list.split(',')
list_dicari = []
results = map(float, new_list)
elapsed = timeit.default_timer() - start_time
print(y_train.shape)
dicari =np.array(results)
baru= np.reshape(dicari,(-1,1))
baru_lagi=np.reshape(dicari,(1,-1))
a=knn.predict(baru_lagi)
clf = OneVsOneClassifier(SVC(kernel='rbf', gamma='auto'))  # Deklarasi spesifikasi classifier
clf.fit(x_train, y_train)  # Training data atau nge fit in model nya
y_pred = clf.predict(baru_lagi)
print(y_pred)




"""
def main():
    controller = Leap.Controller()
    while not controller.is_connected:
        pass
    print "Connected."
    print "Start training..."
    while controller.is_connected:
        take_input()

def take_input():
    print "Taking input."
    controller = Leap.Controller()
    last_frame = 0
    while  True:
        frame = controller.frame()
        if frame.id != last_frame:
            last_frame = frame.id
            fingers_1 = []
            fingers_2 = []
            for index_type in range(0,1): #Sort the fingers from thumb to pinky.
                fingers_1.append(frame.hands.leftmost)
                fingers_2.append(frame.hands.rightmost)
                fingers_1.append(frame.hands.leftmost.palm_position)
                fingers_2.append(frame.hands.rightmost.palm_position)
            hand_right = fingers_2[0]
            hand_left = fingers_1[0]
            for finger_right in hand_right.fingers:
                bone_right = finger_right.bone(3)
                distance_right = fingers_2[1].distance_to(bone_right.next_joint)
            for finger_left in hand_left.fingers:
                bone_left = finger_left.bone(3)
                distance_left = fingers_1[1].distance_to(bone_left.next_joint)
            count +=1 """






