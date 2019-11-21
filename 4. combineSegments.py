# Coded By Reda AI Batat

import glob
import cv2
import re


path = glob.glob("*.avi")

name = path[0].split("_")[0]

out = cv2.VideoWriter(f"{name}_allSegmentsCombined.avi", cv2.VideoWriter_fourcc('M','J','P','G'), 25, (640, 360), True)


numOfVideos = 0

videoNumbers = []

for vid in path:
	numOfVideos += 1

	numbersInVideoFileName = re.findall(r'\d+', vid)

	videoNumbers.append(int(numbersInVideoFileName[1]))

print("Number of segments: ", numOfVideos)

videoNumbers = sorted(videoNumbers)

print(videoNumbers)


for segmentNum in videoNumbers:
	print(f"{name}_segment{segmentNum}.avi")

	cap = cv2.VideoCapture(f"{name}_segment{segmentNum}.avi")

	while cap.isOpened():
		# Write to combined file

		ret, frame = cap.read()

		if(not ret):
			break

		
		out.write(frame)

		#print(frame)
		#cv2.waitKey(1)

	cap.release()



out.release()
print("Finished")
