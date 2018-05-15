# -*- coding: cp949 -*-
import clickable
import sys
import os
import datetime
from functools import partial
from PyQt4 import QtCore, QtGui, uic
form_class = uic.loadUiType("interface.ui")[0]




class MyWindowClass(QtGui.QMainWindow, form_class):

    video_name=""
    detail_flag=0
    del_image_detail=[]
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        self.nh_btn.clicked.connect(self.nh_btn_clicked)
        self.ssg_btn.clicked.connect(self.ssg_btn_clicked)
        self.jjd_btn.clicked.connect(self.jjd_btn_clicked)
        self.log_btn.clicked.connect(self.log_btn_clicked)
        self.ys_btn.clicked.connect(self.ys_btn_clicked)
        self.del_btn.clicked.connect(self.del_btn_clicked)
        self.search_btn.clicked.connect(self.search_btn_clicked)

        
        parent_img="test"
        pixmap=QtGui.QPixmap(parent_img+".jpg")
        
        
        self.detail_image_lab1.setPixmap(pixmap)
        self.detail_image_lab1.setScaledContents(True)
        
        """
        self.scro.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)        
        self.scro.setWidget(self.scrollAreaWidgetContents)
        """
        self.clo_all.stateChanged.connect(self.checked_all)

        


    def load_data(self):
        base_dir=os.getcwd()
        a=os.getcwd()
        os.chdir(a+"/feature_data")
        a=os.getcwd()
        b=os.listdir(a)
        
        

        for i in range(len(b)):
            data=open(b[i],"r")
            data_line=data.readline().split()
            data_list=[]

            while data_line!=[]:
                data_list.append(data_line)
                data_line=data.readline().split()
            data.close()

            if i==0:
                data_alllist=data_list
            else:
                data_alllist=data_alllist+data_list
        
        os.chdir(base_dir)
        return data_alllist

        
    def nh_btn_clicked(self):
        a='test'

    def ssg_btn_clicked(self):
        parent_avi="test"
        
    def jjd_btn_clicked(self):
        base_dir=os.getcwd()
        a=os.getcwd()
        os.chdir(a+"/video_data")
        a=os.getcwd()
        b=os.listdir(a)
        os.chdir(base_dir)
        
        self.scro.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.GridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)        
        self.scro.setWidget(self.scrollAreaWidgetContents)

        self.la=[]
        """
        for i in range(len(b)):
            videotime=b[i][6:25]
            videotime=videotime[0:4]+u"년 "+ videotime[5:7]+u"월"+videotime[8:10]+u"일 "+videotime[11:13]+u"시"+videotime[14:16]+u"분"+videotime[17:19] + u"초"
            self.la.append(QtGui.QLabel(videotime))
            self.GridLayout.addWidget(self.la[i])
            clickable.clickable(self.la[i]).connect(lambda x=i: self.show_detail_video(x,b))
        """
        for i in range(len(b)):
            videotime=b[i][6:25]
            videotime=videotime[0:4]+u"년 "+ videotime[5:7]+u"월"+videotime[8:10]+u"일 "+videotime[11:13]+u"시"+videotime[14:16]+u"분"+videotime[17:19] + u"초"
            self.la.append(QtGui.QPushButton(videotime))
            self.GridLayout.addWidget(self.la[i])
            clickable.clickable(self.la[i]).connect(lambda x=i: self.show_detail_video(x,b))
        
        
    def log_btn_clicked(self):
        log_data=open("Log.txt","r")
        all_log_data=log_data.read()
        log_data.close()

        self.scro.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.GridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)        
        self.scro.setWidget(self.scrollAreaWidgetContents)

        self.GridLayout.addWidget(QtGui.QLabel(all_log_data))
        
    def ys_btn_clicked(self):
        if self.video_name=="":
            notice=QtGui.QMessageBox.question(self,'Warning',u"선택된 영상이 없습니다")
            
        else:
            base_dir=os.getcwd()
            a=os.getcwd()
            os.chdir(a+"/video_data")
            os.system(self.video_name)
            os.chdir(base_dir)
        
    

    def search_btn_clicked(self):
        self.search_data()

    def search_data(self):
        self.video_name=""
        self.scro.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)        
        self.scro.setWidget(self.scrollAreaWidgetContents)
        
        data_alllist=self.load_data()
        result_list=[]
        
        t_to=self.time_to.dateTime()
        t_to_string=t_to.toString("yyyy_MM_dd_hh_mm_ss")
        t_from=self.time_from.dateTime()
        t_from_string=t_from.toString("yyyy_MM_dd_hh_mm_ss")
        color1=self.color_1.currentText()
        color2=self.color_2.currentText()
        color3=self.color_3.currentText()

        dress=[]

        if self.clo_down.isChecked():
            dress.append('down')
        if self.clo_cardigan.isChecked():
            dress.append('cardigan')
        if self.clo_blouse.isChecked():
            dress.append('blouse')
        if self.clo_top.isChecked():
            dress.append('top')
        if self.clo_tank.isChecked():
            dress.append('tank')
        if self.clo_jersey.isChecked():
            dress.append('jersey')
        if self.clo_Poncho.isChecked():
            dress.append('Poncho')
        if self.clo_parka.isChecked():
            dress.append('parka')
        if self.clo_turtleneck.isChecked():
            dress.append('turtleneck')
        if self.clo_joggers.isChecked():
            dress.append('joggers')
        if self.clo_jacket.isChecked():
            dress.append('jacket')
        if self.clo_hoodie.isChecked():
            dress.append('hoodie')
        if self.clo_blazer.isChecked():
            dress.append('blazer')
        if self.clo_tee.isChecked():
            dress.append('tee')
        if self.clo_sweater.isChecked():
            dress.append('sweater')
        
        myTime_to = datetime.datetime.strptime(str(t_to_string), '%Y_%m_%d_%H_%M_%S')
        myTime_from = datetime.datetime.strptime(str(t_from_string), '%Y_%m_%d_%H_%M_%S')
        
        check=[]
        if color1 !='None':
            check.append(color1)
        if color2 !='None':
            check.append(color2)
        if color3 !='None':
            check.append(color3)

        
        for d in data_alllist:
            flag=True

            dateANDtime = d[0][34:53]
            myTime = datetime.datetime.strptime(dateANDtime, '%Y_%m_%d_%H_%M_%S')

            if myTime_to > myTime or myTime > myTime_from:   ## check time
                flag=False

            for c in check:        ## check color
                if c not in d:
                    flag=False

            if d[1] not in dress:      ## check clothes
                flag=False
        
            

            if flag:
                result_list.append(d)

        if len(result_list)==0:
            notice=QtGui.QMessageBox.warning(self,'Message',u"검색 결과가 존재하지 않습니다")
        else:
            count=0
            self.la=[]

        
        
            for i in range((len(result_list)+2)/3):
                for j in range(3):
                    if count==len(result_list):
                        break
                    pixmap=QtGui.QPixmap(str(result_list[count][0]))
                    self.la.append(QtGui.QLabel())
                    pixmap=pixmap.scaledToWidth(150)
                    self.la[count].setPixmap(pixmap)
                    self.la[count].setScaledContents(True)
                    self.gridLayout.addWidget(self.la[count], i, j)
                    clickable.clickable(self.la[count]).connect(lambda x=count: self.show_detail_image(x,result_list[x]))
                    count=count+1
        
            if count < 7:
                for i in range(count/3,3):
                    for j in range(3):
                        if i==count/3:
                            if j > (count%3-1):
                                self.la.append(QtGui.QLabel())
                                self.la[count].setScaledContents(True)
                                self.gridLayout.addWidget(self.la[count], i, j)
                        elif i != count/3:
                            self.la.append(QtGui.QLabel())
                            self.la[count].setScaledContents(True)
                            self.gridLayout.addWidget(self.la[count], i, j)
                
    """
    def show_result(self,data_alllist):
        base_dir=os.getcwd()
        a=os.getcwd()
        os.chdir(a+"/image")

        
        count=0
        self.la=[]

     

        
        for i in range(len(test_result)/3+1):
            for j in range(3):
                pixmap=QtGui.QPixmap("test"+str(count)+".jpg")
                self.la.append(QtGui.QLabel())
                pixmap=pixmap.scaledToWidth(150)
                self.la[count].setPixmap(pixmap)
                self.la[count].setScaledContents(True)
                self.gridLayout.addWidget(self.la[count], i, j)
                clickable.clickable(self.la[count]).connect(lambda x=count: self.show_detail(x,test_result[x]))
                if count==len(test_result):
                    break
                count=count+1
             
        os.chdir(base_dir)
    """  
    def checked_all(self):
        x=self.clo_all.isChecked()
        self.clo_down.setChecked(x)
        self.clo_cardigan.setChecked(x)
        self.clo_blouse.setChecked(x)
        self.clo_top.setChecked(x)
        self.clo_tank.setChecked(x)
        self.clo_jersey.setChecked(x)
        self.clo_Poncho.setChecked(x)
        self.clo_parka.setChecked(x)
        self.clo_turtleneck.setChecked(x)
        self.clo_joggers.setChecked(x)
        self.clo_jacket.setChecked(x)
        self.clo_hoodie.setChecked(x)
        self.clo_blazer.setChecked(x)
        self.clo_tee.setChecked(x)
        self.clo_sweater.setChecked(x)
        
    def del_btn_clicked(self):
        if self.detail_flag==0:
            notice=QtGui.QMessageBox.warning(self,'Warning',u"삭제할 대상이 없습니다")
        elif self.detail_flag==1:
            result = QtGui.QMessageBox.question(self, 'Message', u"저장된 이미지와 특징데이터를 삭제하시겠습니까?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if result==QtGui.QMessageBox.Yes:
                self.del_image()    
            else:
                pass
        elif self.detail_flag==2:
            result = QtGui.QMessageBox.question(self, 'Message', u"저장된 영상과 관련된 데이터를 모두 삭제하시겠습니까?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if result==QtGui.QMessageBox.Yes:
                self.del_video()    
            else:
                pass

    def del_video(self):
        base_dir=os.getcwd()
        a=os.getcwd()
        os.chdir(a+"/video_data")
        os.system("del "+self.video_name)
        

        data_locate=self.video_name[6:25]
        
        os.chdir(a+"/feature_data")
        os.system("del "+data_locate+".txt")

        os.chdir(a+"/img_data")
        os.system("rmdir /s /q "+data_locate)

        os.chdir(base_dir)

        now=self.now_time()
        log_data=open("Log.txt","a")
        log_data.writelines(now+" Delete_Video   "+self.video_name+" \n")
        log_data.close()

        self.jjd_btn_clicked()

        
    def del_image(self):
        del_data=''
        for i in self.del_image_detail:
            del_data=del_data+i+" "
        del_data=del_data[0:len(del_data)-1]
        data_locate=del_data[11:30]
        data_file=open('feature_data/'+data_locate+".txt",'r')
        data=data_file.read()
        data_file.close()
        data_del=data.replace(del_data+"\n","")
        data_file=open('feature_data/'+data_locate+".txt",'w')
        data_file.write(data_del)
        data_file.close()        


        base_dir=os.getcwd()
        a=os.getcwd()
        os.chdir(a+"/img_data/"+data_locate)
        print(os.getcwd())
        print(del_data[0:60])
        os.system("del "+del_data[31:60])
        
        os.chdir(base_dir)

        now=self.now_time()
        log_data=open("Log.txt","a")
        log_data.writelines(now+" Delete_Image   "+del_data+" \n")
        log_data.close()
        
        
        self.search_data()
        
    def show_detail_image(self,index,result_list):
        self.detail_flag=1
        pixmap=QtGui.QPixmap(str(result_list[0]))
        self.detail_image_lab1.setPixmap(pixmap)
        self.video_name="video_"+result_list[0][11:30]+".avi"
        videotime=result_list[0][11:30]
        mantime=result_list[0][34:53]
        mancolor=result_list[2:len(result_list)]
        self.detail_videotime.setText(u"영상 촬영시간 : " + videotime[0:4]+u"년 "+ videotime[5:7]+u"월"+videotime[8:10]+u"일 "+videotime[11:13]+":"+videotime[14:16]+":"+videotime[17:19])
        self.detail_mantime.setText(u"인물 등장시간 : " + mantime[0:4]+u"년 "+ mantime[5:7]+u"월"+mantime[8:10]+u"일 "+mantime[11:13]+":"+ mantime[14:16]+":"+ mantime[17:19])
        self.detail_clo.setText(u"등장인물 의상정보 : " + result_list[1])
        str_mancolor=''
        for i in mancolor:
            if i==mancolor[0]:
                str_mancolor=i
            else:
                str_mancolor=str_mancolor+" "+i
        self.detail_color.setText(u"등장인물 색상정보 : " + str_mancolor)
        self.del_image_detail=result_list
    def show_detail_video(self,index,video_list):
        self.detail_flag=2
        self.video_name=video_list[index]
        self.detail_videotime.setText(self.video_name)
    def now_time(self):
        year = datetime.datetime.today().year
        month = datetime.datetime.today().month
        day = datetime.datetime.today().day
        hour = datetime.datetime.today().hour
        minute = datetime.datetime.today().minute
        second = datetime.datetime.today().second

        now=str(year)+"/ "+str(month)+"/"+str(day)+" "+str(hour)+":"+str(minute)+":"+str(second)
        return now
                                             
app = QtGui.QApplication(sys.argv)   
myWindow = MyWindowClass()
myWindow.show()
app.exec_()                          
