import datetime
import cv2
import time
import os
from config import *
from feature_function import *


def reinit_tracker(frame, hog, _type="hog"):
    tracker = cv2.MultiTracker_create()
    if _type == "hog":
        (rects, weights) = hog.detectMultiScale(frame, winStride=(4,4), padding=(0,0), scale=1.18)
    for rect in rects:
        tracker.add(cv2.TrackerKCF_create(), frame, tuple(rect))

    return tracker

def predict_with_write_detections(img,rects,nowstr,index,f,thickness=1):
        res_data=[]
        for   [x,y,w,h] in rects:
                #print x,y,w,h
                #crop img create        
                pad_w,pad_h = int(0.15*w-1),int(0.05*h-1)
                x_min,x_max,y_min,y_max=x+pad_w,x+w-pad_w,y+pad_h,y+h-pad_h
                crop_img=img[y_min:y_max ,x_min:x_max]

                #save
                imwrite_str=img_data_path+nowstr[0]+'/img'+nowstr[1]+'_%02d'%(index)+'.jpg'
                tmp='a'
                while os.path.isfile(imwrite_str) == True:
                        imwrite_str=imwrite_str[:-6]+tmp+imwrite_str[-5:]
                        tmp= chr(ord(tmp)+1)
                cv2.imwrite(imwrite_str,crop_img)
                #feature data   
                colors=image_color_cluster(crop_img)
                res=predict_img(imwrite_str)[0]
                score=predict_img(imwrite_str)[1]
                res_data.append([res,colors])
                res_write_str=imwrite_str+' '+res+' '+' '.join(colors)+'\n'
                f.write(res_write_str)

        #print 'shape',(res_data[0])
        return res_data[0],score

def webcam_control(file_name):
        filename=datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        current_datetime=datetime.datetime.now()
        font = cv2.FONT_HERSHEY_SIMPLEX

        #video init
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        output = cv2.VideoWriter(video_data_path+filename+".avi",fourcc,20.0,(1080,720))
        #output = cv2.VideoWriter(video_data_path+filename+".avi",fourcc,20.0,(640,360))
        #webcam = cv2.VideoCapture('test/rotate.avi')
        webcam = cv2.VideoCapture(file_name)
        #webcam = cv2.VideoCapture(0)
        webcam.set(1, 60)

        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        #img init
	
        if not os.path.isdir(img_data_path+filename):
                os.mkdir(img_data_path+filename)

	#feature init
        f=open(feature_data_path+filename+'.txt','a')

        #track
        tracker=cv2.MultiTracker_create()
        needHogVerif=0
        allBoxes=[]
        speedBoxes=[]
        Boxes_feature=[]
        focalLength=0
        HOG_VERIF_TRESH=72
        KNOWN_DISTANCE = 24.0
        KNOWN_WIDTH = 11.0
        MAX_DISTANCE = 10
        isNew=True
        isNew2=True
        start=True

	
        while webcam.isOpened():
                #declare
                
                start_time=time.time()	
                current_datetime=datetime.datetime.now()
                current_datetime_str=current_datetime.strftime('%Y/%m/%d  %H:%M:%S')
                current_datetime_str2=current_datetime.strftime('%Y_%m_%d_%H_%M_%S')

                 #read
                ret,frame=webcam.read()

                if start:
                    cv2.imwrite('F:/video_preview/'+filename+".jpg",frame)
                    start=False               
                #print frame.shape
                #copy_frame=frame.copy()
                copy_frame=cv2.resize(frame,(1080,720))#,interpolation=cv2.INTER_AREA)
                #copy_frame=cv2.resize(frame,(640,360))#,interpolation=cv2.INTER_AREA)
                #cv2.imshow('origin',copy_frame)
                #process
                ok,boxes=tracker.update(copy_frame)	
                nBox=0
                
                if not ok or boxes is () or needHogVerif > HOG_VERIF_TRESH:
			#cv2.imshow('origin',copy_frame)
			#cv2.imshow('cframe',copy_frame)
                        needHogVerif=0
                        tracker = reinit_tracker(copy_frame,hog)
                        isNew=True
                        isNew2=True

                        speedBoxes=[]
                        Boxes_feature=[]
                        allBoxes=[]
			#fps=str(int(1/(time.time()-start_time)))
			#cv2.putText(copy_frame,'fps:'+fps,(50,50),font,1,(255,255,255),2,cv2.LINE_AA)
			#cv2.putText(copy_frame,current_datetime_str,(420,30), font, 0.5,(255,255,255),2,8)

			#cv2.imshow('cframe',copy_frame)
			#output.write(copy_frame)

                if isNew2==False:
                        realboxes=[]
                        for i , box in enumerate(boxes):
                                if isNew:
                                        allBoxes.append([box])
                                        Boxes_feature.append(predict_with_write_detections(copy_frame,[[int(box[0]),int(box[1]),int(box[2]),int(box[3])]],[filename,current_datetime_str2],i,f))
                                else:
                                        allBoxes[nBox].append(box)
				
                        for i , box in enumerate(boxes):
                                pad_w,pad_h = int(0.15*box[2]-1) , int(0.05*box[3]-1) 
                                p1 = (int(box[0])+pad_w, int(box[1])+pad_h)
                                p2 = (int(box[2])+int(box[0])-pad_w, int(box[3])+int(box[1])-pad_h)
                                cv2.rectangle(copy_frame, p1, p2, (255,255,255), 2)
                                cv2.putText(copy_frame,str(Boxes_feature[i][0][0])+':'+str(int(Boxes_feature[i][1]*100))+'%',(int(box[0]), int(box[1])+5), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255,255,255),1, cv2.LINE_AA)
        
                                nBox+=1
	
                        isNew=False
                isNew2=False
                needHogVerif+=1
	
			#draw
		#print time.time()-start_time
		#fps=str(int(1/(time.time()-start_time)))
		#cv2.putText(copy_frame,'fps:'+fps,(50,50),font,1,(255,255,255),2,cv2.LINE_AA)
                cv2.putText(copy_frame,current_datetime_str,(420,30), font, 0.5,(255,255,255),2,8)

                cv2.imshow('cframe',copy_frame)
                output.write(copy_frame)
		#ui
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                        break

