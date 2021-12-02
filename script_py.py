import pandas as pd
import numpy as np


print("Hello World")

msgEvent = pd.read_csv('extracted_data/converted_data/MessageEvent_Caleb5.txt', sep="\t", header=None)
msgEventArray = np.array(msgEvent)

# msgEvent = np.genfromtxt('MessageEvent_Joseph.txt', dtype='str', delimiter="\t")


# print(type(msgEventArray[0][11]))

startTimesList = []
stopTimesList = []

for x in msgEventArray:
    if x[13] == "start":
        startTimesList.append(x[7])
    if x[13] == "stop":
        stopTimesList.append(x[7])

# print(startTimesList)

timeToComplete_img1 = stopTimesList[0] - startTimesList[0]
timeToComplete_img2 = stopTimesList[1] - startTimesList[1]

print("Time taken to complete image 1: ")
print(timeToComplete_img1)
print("Time taken to complete image 2: ")
print(timeToComplete_img2)




# --------------------
# GET THE GAZEPOINT STUFF

gazeEvent = pd.read_csv('extracted_data/converted_data/GazepointSampleEvent_Caleb5.txt', sep="\t", header=None)
gazeEventArray = np.array(gazeEvent)

coordinatesX_image1_List = []
coordinatesY_image1_List = []
coordinatesX_image2_List = []
coordinatesY_image2_List = []

for thing in gazeEventArray:
    if ((thing[7] >= startTimesList[0]) and (thing[7] <= stopTimesList[0])):
        coordinatesX_image1_List.append(thing[11])
        coordinatesY_image1_List.append(thing[12])
    if ((thing[7] >= startTimesList[1]) and (thing[7] <= stopTimesList[1])):
        coordinatesX_image2_List.append(thing[11])
        coordinatesY_image2_List.append(thing[12])

# print(len(coordinatesX_image2_List))

# --------- GENERATE INTERQUARTILE RANGES OF THE COORDINATES (IQR) WHICH IS THE MIDDLE 50%; THE LOWER THE NUMBER, THE LESS THEY LOOKED ALL OVER THE SCREEN
# ---------       WHICH MEANS THEIR GAZE WAS MORE CONCENTRATED

# IMAGE 1 CODE
img1_X = pd.DataFrame({'Values': coordinatesX_image1_List})
q75_img1X, q25_img1X = np.percentile(img1_X['Values'], [75, 25])
iqr_img1X = q75_img1X - q25_img1X

img1_Y = pd.DataFrame({'Values': coordinatesY_image1_List})
q75_img1Y, q25_img1Y = np.percentile(img1_Y['Values'], [75, 25])
iqr_img1Y = q75_img1Y - q25_img1Y

final_iqr_img1 = (iqr_img1X + iqr_img1Y) / 2
print("IQR for image 1 GazePoints: ")
print(final_iqr_img1)

# IMAGE 2 CODE
img2_X = pd.DataFrame({'Values': coordinatesX_image2_List})
q75_img2X, q25_img2X = np.percentile(img2_X['Values'], [75, 25])
iqr_img2X = q75_img2X - q25_img2X

img2_Y = pd.DataFrame({'Values': coordinatesY_image2_List})
q75_img2Y, q25_img2Y = np.percentile(img2_Y['Values'], [75, 25])
iqr_img2Y = q75_img2Y - q25_img2Y

final_iqr_img2 = (iqr_img2X + iqr_img2Y) / 2
print("IQR for image 2 GazePoints: ")
print(final_iqr_img2)

