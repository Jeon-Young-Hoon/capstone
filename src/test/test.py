import cv2


def webcam_control():
	
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	output = cv2.VideoWriter('./trash/test.avi',fourcc,20.0,(640,480))

	webcam = cv2.VideoCapture('test/test.avi')

	while webcam.isOpened():

		ret,frame=webcam.read()
		
		copy_frame=cv2.resize(frame,(640,480),interpolation=cv2.INTER_AREA)
		
		cv2.imshow('cframe',copy_frame)

		#ui
		key = cv2.waitKey(1) & 0xFF
		if key == ord('q'):
			break

def main():
	webcam_control()

main()
