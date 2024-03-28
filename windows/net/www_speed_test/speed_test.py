import os, time
from urllib.request import urlopen
from datetime import *
import time

def Process(url,n):
    minSpan = 10.0
    maxSpan = 0.0
    sumSpan= 0.0
    over1s = 0
    for i in range(n):
        startTime = datetime.now()
        try:
            res =urlopen(url,timeout=10)
            print(res.getcode())
        except:
            pass

        endTime = datetime.now()
        span = (endTime-startTime).total_seconds()
        sumSpan = sumSpan + span
        if span < minSpan:
            minSpan = span
        if span > maxSpan:
            maxSpan = span
        #超过一秒的
        if span>1:
            over1s=over1s + 1
        print(u'%s Spent :%s seconds'%(url,span))
    print(u'requested:%s times,Total Spent:%s seconds,avg:%s seconds, max:%s seconds,min:%s seconds,over 1 secnod:%s times'%(n,sumSpan,sumSpan/n,maxSpan,minSpan,over1s))
    print('\n')
    
    

if __name__=='__main__':

    #Process('http://www.baidu.com',100)
    Process('http://192.168.13.156',100)


