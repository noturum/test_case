import json
import re
from datetime import datetime
def sortTime(e):
    return e['time']
def dataToDict():
    comps=dict(json.load(open('competitors2.json','r+',encoding='utf-8')))
    with open('results_RUN.txt','r+',encoding='utf-8') as f:
        result=f.read().split('\n')[:-1]
        result=[{'num':re.sub('\D',
                '',res.split(' ')[0]),'state':res.split(' ')[1],
                 'time':res.split(' ')[2]} for res in result]
        tmpResult=[]

        for firstObj in result:
            for secondObj in result:
                if firstObj['num'] == secondObj['num'] and firstObj['state']=='start' and secondObj['state']=='finish':
                    datetimeFormat = '%H:%M:%S,%f'
                    time1 = firstObj['time']
                    time2 = secondObj['time']

                    time_dif = datetime.strptime(time2, datetimeFormat) - datetime.strptime(time1, datetimeFormat)
                    tmpResult.append({'num':firstObj['num'],
                                      'time':time_dif})

    tmpResult.sort(key=sortTime)
    for res in tmpResult:
        print('Результат {} {} {} {},{}'.format(tmpResult.index(res)+1,
                                             res['num'],
                                             comps[res['num']]['Name'],
                                             comps[res['num']]['Surname'],
                                             res['time']
                                             ))
if __name__=='__main__':
    #dataToDict()

    str1='(00000000000000000150-162=2150002,30)КОСГУ162ТС05.00.00код суб.126.01N108 Возв.по доп.сог.№2от 03.08.2022к сог.№41от01.02.2022на приоб.автом.санит.трансп.ППрНСОот07.05.2013№199-п '
    str2= '(00000000000000000150-162=2150002,30)КОСГУ162ТС05.00.00код суб.126.01N108 Возв.по доп.сог.№2от 03.08.2022к сог.№41от01.02.2022на приоб.автом.санит.трансп.ППрНСОот07.05.2013№199-п '
    if str1==str2:
        print(True)