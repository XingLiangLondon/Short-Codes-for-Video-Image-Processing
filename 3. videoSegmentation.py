# Coded By Reda AI Batat

import numpy as np
import cv2
import time

#cap = cv2.VideoCapture("test1.mp4")
#cap = cv2.VideoCapture("test1_small.mp4")

fileName = "BM30c"

cap = cv2.VideoCapture(f"E:\\Reda\\Not Segmented\\Conversation\\65+\\{fileName}.mov")


print(f"Frame rate: {cap.get(5)}")

ret, lastFrame = cap.read()

h, w, _ = lastFrame.shape
print(w, h)


hits = 0
recording = False
segmentNumber = 0

frames = []

start = time.time()

out = None

whenToCount = 2000
whenToRecord = 37
whenToStop = 10

while cap.isOpened():

	timePassed = time.time() - start

	ret, frame = cap.read()

	# Reached the end of the video.
	if(not ret):
		break

	diff = cv2.absdiff(lastFrame, frame)
	diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

	_, diff = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)

	cropped = diff[:, :w-150]
	cv2.imshow("Cropped", cropped)

	#numOfWhitePixels = np.sum(diff == 255)
	numOfWhitePixels = np.sum(cropped == 255)

	cv2.imshow("Video", frame)

	if not recording:
		frames.append(frame)

	if recording:
		out.write(frame)

	#print(numOfWhitePixels)
	if numOfWhitePixels > whenToCount:
		hits += 1

	if (timePassed > 5):
		print(hits)

		if hits > whenToRecord and not recording:
			print("Started recording")
			recording = True

			out = cv2.VideoWriter(f"{fileName}_segment{segmentNumber}.avi", cv2.VideoWriter_fourcc('M','J','P','G'), cap.get(5), (lastFrame.shape[1], lastFrame.shape[0]), True)
			

			for frame in frames:
				out.write(frame)

			segmentNumber += 1


		if hits < whenToStop and recording:
			print("Stopped recording")
			out.release()
			recording = False


		if hits < whenToStop:
			frames = []


		hits = 0

		start = time.time()

	cv2.imshow("Difference", diff)
	

	key = cv2.waitKey(25)

	if key == 27:
		break


	lastFrame = frame

if out is not None:
	out.release()

cap.release()
cv2.destroyAllWindows()

print("Finished Segmenting")
