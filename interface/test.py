import datetime

data = [ ['./img_data/2018_04_03_10_36_14/img2018_04_03_10_36_21_00.jpg', 'parka', 'Whites', 'Grays', 'violet'], ['./img_data/2018_04_03_10_36_14/img2018_04_03_10_36_23_01.jpg', 'parka', 'Whites', 'Grays'], ['./img_data/2018_04_03_10_36_14/img2018_04_03_10_36_25_02.jpg', 'jersey', 'Grays', 'Yellows'] ] 

result_list=[]

## use variable in interface
color1 = "Whites"
color2 = "Grays"
color3 = "None"

dress='parka'

time_to = '2018_04_03_10_36_20'
time_from = '2018_04_03_10_36_24'

## time range
myTime_to = datetime.datetime.strptime(time_to, '%Y_%m_%d_%H_%M_%S')
myTime_from = datetime.datetime.strptime(time_from, '%Y_%m_%d_%H_%M_%S')

print myTime_to
print myTime_from

check=[]
if color1 !='None':
    check.append(color1)
if color2 !='None':
    check.append(color2)
if color3 !='None':
    check.append(color3)

for d in data:
    flag=True

    dateANDtime = d[0][34:53]
    myTime = datetime.datetime.strptime(dateANDtime, '%Y_%m_%d_%H_%M_%S')

    if dress not in d:      ## check clothes
        flag=False

    for c in check:        ## check color
        if c not in d:
            flag=False
        
    if myTime_to > myTime or myTime > myTime_from:   ## check time
        flag=False

    if flag:
        result_list.append(d) 
        ##print d

print(result_list)
 
