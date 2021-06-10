from threading import Thread,Lock
import math
from time import sleep
from subprocess import Popen, PIPE
import logging
import os
wait = Lock()
wait_2 = Lock()#нужен для принта , потому что он потоко не безопасный, с логгами не получилось 
logging.basicConfig(level=logging.INFO,filename='test.log')
def start(start,end,process):
    with Lock():
        sleep(2)
        rez=[]
        tmp = True
        for i in range(int(start),int(end)+1):
            for g in range(2,10+1):
                if g != math.fabs(i):
                    if math.fabs(i) % g == 0:
                        tmp = False
                        break

            if tmp == True:
                rez.append(i)
            tmp= True
        with wait_2:
            print(f'Процесс: {process+1}, диапазон [{start},{end}], результат : \n{rez}\n')


if __name__ =='__main__':
    split = 10
    with Popen(['python','sss.py',' 1' ,"1000"], stdout=PIPE) as task:
        i = task.stdout.read().decode()
    i = i.split('\n')
    print('Первые два числа в списке это диапазон')
    print(i)
    list_ = []
    range_of_number = 0
    if int(i[0]) < 0:
        if int(i[1])<0:
            range_of_number = int(i[0]) + int(i[1])
            range_of_number = math.fabs(range_of_number) + 1
        elif int(i[1])>0:
            range_of_number = int(i[0]) - int(i[1])
            range_of_number = math.fabs(range_of_number) + 1
        elif int(i[1])==0:
            range_of_number = math.fabs(int(i[0])) + 1
    elif int(i[0]) >0:
        range_of_number = int(i[1]) - int(i[0]) +1
    elif int(i[0]) == 0:
        range_of_number = int(i[1]) + 1

    shag = int(i[0])
    for item in range(split):
        proc = Thread(target=start ,args=(shag,shag+int(range_of_number/split)-1,item))
        shag = shag+int(range_of_number/split)
        proc.start()


