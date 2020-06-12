# Creates dataset

import sys,time
import pandas as pd, numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
data =pd.read_csv('angka_sudut_panjang.csv', index_col=False)

sys.path.append('/home/ganesh/PycharmProjects/Gesture To Text/lib/x64')

x=data.iloc[:,1:41].values
y=data.iloc[:,0]
knn=KNeighborsClassifier(n_neighbors=20)
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=5)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
# Importing Leap SDK
import Leap

# The dataset contains the distance of all the bones in all the fingers
# to the palm center, the distance of thumbs to all the finger tips.
# This is all per frame. For one training example, 100 frames are used.

def main():
    # Creating dataset by asking for the gesture first, and
    # the number of examples we want to add.

    controller = Leap.Controller()
    while not controller.is_connected:
        pass
    print "Connected."
    count_ex = 0
    # Used to normalize the finger lengths across people
    # so that dataset can scale well to real world examples.
    calib = calibrate()
    print "The calibrated value is: ", calib
    print "Start training..."
    while True:
        # This function detects that your hand is moving.
        # We need to start taking input when the hand stops moving.
        moving()
        # The function where the input is taken.
        take_input()
        # Again, one more function to loop while the user changes
        # the gesture he's performing.
        not_moving()
        count_ex = count_ex + 1


# Looping function before the user makes the gesture.
def moving():
    controller = Leap.Controller()
    while not controller.is_connected:
        pass
    fingers = []
    while not fingers: #Keep waiting for the fingers to be detected.
        frame = controller.frame()
        fingers = frame.fingers
        pass
    print "Fingers detected."
    time.sleep(1)
    print "Waiting until hand stops moving."
    last_frame = 0
    while controller.is_connected:
        frame = controller.frame()
        if frame.id != last_frame: # Ensuring that we won't process the same frame twice.
            last_frame = frame.id
            fingers_1 = []
            for index_type in range(0,5): #Sort the fingers from thumb to pinky.
                fingers_1.append(frame.fingers.finger_type(index_type)[0])
            check(fingers_1)
            flag = 0
            for finger in fingers_1:
                if finger.tip_velocity.magnitude < 200:
                    # Using the velocity to guess whether
                    # the hand is moving or not.
                    flag = flag + 1
            if flag == 5:
                print "Hand not moving. Starting to take input."
                return 1


# Helper function to ensure that the finger tip is read properly.
def check(fingers_1):
    for i in range(len(fingers_1)):
        if fingers_1[i].tip_position.magnitude == 0:
            print "Finger not detected."
            exit()
            # del fingers_1[i]


# The actual function which takes the input.
def take_input():
    print "Taking input."

    controller = Leap.Controller()
    count = 0
    last_frame = 0

    while  last_frame<1:
        string = ''
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
                string += (str(distance_right)+', ')
                sudut = Leap.Vector(finger_right.tip_position - fingers_2[1])
                b = str(sudut).replace('(', '')
                c = b.replace(')', '')
                string += (str(c)+', ')

            for finger_left in hand_left.fingers:
                bone_left = finger_left.bone(3)
                distance_left = fingers_1[1].distance_to(bone_left.next_joint)
                string += (str(distance_left) + ', ')
                sudut = Leap.Vector(finger_left.tip_position - fingers_1[1])
                b = str(sudut).replace('(', '')
                c = b.replace(')', '')
                if count < 4:
                    string += (c+ ', ' )
                else:
                    string +=(c)
                count +=1
            print(string)
            string_list =string.split(',')
            print(string_list)
            last_frame +=1
            results =map(float,string_list)
            dicari = np.array(results)
            baru = np.reshape(dicari, (-1, 1))
            baru_lagi = np.reshape(dicari, (1, -1))
            hasil_knn = knn.predict(baru_lagi)
            print(hasil_knn)






# Wait till the hand starts moving.
# Looping function to wait after the user performs the gesture.
def not_moving():
    controller = Leap.Controller()
    while not controller.is_connected:
        pass
    print "Waiting until hand is moving."
    fingers = []
    while not fingers:  # Keep waiting for the fingers to be detected.
        frame = controller.frame()
        fingers = frame.fingers
        pass
    #print "Fingers detected."
    last_frame = 0
    while controller.is_connected:
        frame = controller.frame()
        if frame.id != last_frame:
            last_frame = frame.id
            fingers_1 = []
            for index_type in range(0, 5):  # Sort the fingers from thumb to pinky.
                fingers_1.append(frame.fingers.finger_type(index_type)[0])
            check(fingers_1)
            for finger in fingers_1:
                if finger.tip_velocity.magnitude > 200:
                    print "Moving.Going back to main."
                    return


# Function used to normalize all the finger lengths across people.
def calibrate():

    print "Calibrating hand. Please hold it steady."
    moving()
    controller = Leap.Controller()
    frame = controller.frame()
    hands = frame.hands
    fingers = frame.fingers
    for finger in fingers:
        if finger.type == 2:
            middle_finger = finger
            break

    last_frame = 0
    palm_center = hands[0].palm_position
    calib = palm_center.distance_to(middle_finger.tip_position)
    # Using the distance of the middle finger tip to the palm centre as
    # the constant among people.
    print "Calibrating done. Please remove your hand."

    while controller.is_connected:
        frame = controller.frame()
        if frame.id != last_frame:
            last_frame = frame.id
            hands = frame.hands
            if not hands:
                return calib


main()





