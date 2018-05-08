# -*- coding: cp949 -*-
import clickable
import sys
import os
import datetime
from functools import partial
from PyQt4 import QtCore, QtGui, uic
form_class = uic.loadUiType("interface.ui")[0]



class MyWindowClass(QtGui.QMainWindow, form_class):

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
        parent_avi="test"

    def log_btn_clicked(self):
        a='test'

    def ys_btn_clicked(self):
        parent_avi="test"
        os.system(parent_avi+".avi")
        
    def del_btn_clicked(self):
        parent_avi="test"

    def search_btn_clicked(self):
        self.search_data()

    def search_data(self):
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

            if d[1] not in dress:      ## check clothes
                flag=False

            for c in check:        ## check color
                if c not in d:
                    flag=False
        
            if myTime_to > myTime or myTime > myTime_from:   ## check time
                flag=False

            if flag:
                result_list.append(d)

        
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
                clickable.clickable(self.la[count]).connect(lambda x=count: self.show_detail(x,result_list[x]))
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
        
    
    def show_detail(self,index,result_list):
        pixmap=QtGui.QPixmap(str(result_list[0]))
        self.detail_image_lab1.setPixmap(pixmap)
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
                                             
app = QtGui.QApplication(sys.argv)   
myWindow = MyWindowClass()           
myWindow.showMaximized()                      
app.exec_()                          
