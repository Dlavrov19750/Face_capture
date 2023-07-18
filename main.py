import numpy as np
import cv2 as cv

cap = cv.VideoCapture('bayan.mp4')
if not cap.isOpened():
	print("Cannot open camera")
	exit()
while True:
	# Capture frame-by-frame
	ret, frame = cap.read()
	# if frame is read correctly ret is True
	if not ret:
		print("Can't receive frame (stream end?). Exiting ...")
	break
	# Our operations on the frame come here
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	# write the flipped frame
	out.write(frame)
	output_file_name = "output_single.mp4"
	out.open(output_file_name, fourcc, fps, (width, height), True)
	# Display the resulting frame
	cv.imshow('frame', gray)
	if cv.waitKey(50) == ord('q'):
		break
# When everything done, release the capture
cap.release()






