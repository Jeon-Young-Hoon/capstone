import datetime
import cv2
import time


def webcam_control():
	
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	output = cv2.VideoWriter('./trash/test.avi',fourcc,20.0,(640,480))

	webcam = cv2.VideoCapture('test/test.avi')

	font = cv2.FONT_HERSHEY_SIMPLEX

	hog = cv2.HOGDescriptor()
	hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

	tracker=cv2.MultiTracker_create()


	
	while webcam.isOpened():
		#declare
		
		start_time=time.time()	
		current_datetime=datetime.datetime.now()
		current_datetime_str=current_datetime.strftime('%Y/%m/%d  %H:%M:%S')

		#read
		ret,frame=webcam.read()
		#copy_frame=frame.copy()
		copy_frame=cv2.resize(frame,(640,360),interpolation=cv2.INTER_AREA)
		
		#process
		(rects,weights) = hog.detectMultiScale(copy_frame, winStride=(8,8),
			padding=(8,8), scale=1.03, useMeanshiftGrouping=True)
		
		fps=str(int(1/(time.time()-start_time)))
		#draw
		for (x, y, w, h) in rects:
			cv2.rectangle(copy_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		cv2.putText(copy_frame,'fps:'+fps,(50,50),font,1,(255,255,255),2,cv2.LINE_AA)
		cv2.putText(copy_frame,current_datetime_str,(420,30), font, 0.5,(255,255,255),2,8)

		cv2.imshow('cframe',copy_frame)

		#ui
		key = cv2.waitKey(1) & 0xFF
		if key == ord('q'):
			break

def main():
	webcam_control()

main()
