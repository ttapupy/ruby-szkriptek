#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# magyartalanító script: az idézőjelben ("") lévő szöveget módosítja, majd törli az idézőjelet
import re

sql_file=input('Add meg a javítandó fájl elérési útvonalát és nevét: ')

kuka=[('á','a'),('é','e'),('í','i'),('ó','o'),('ö','o'),('ő','o'),('ú','u'),('ü','u'),('ű','u')]

with open(sql_file, 'r', encoding='utf-8') as all:
    szoveg=all.read()

quoted= re.findall(r'(\".+?\")', szoveg)
q=''
print(quoted)
for m in quoted:
    q = m
    for i in kuka:
        if i[0] in m or i[0].upper() in m:
            print(i)
            q=q.replace((i[0]) , i[1])
            print(q)
            q=q.replace((i[0]).upper() , i[1].upper())
    q = re.sub('[^0-9a-zA-Z\"]+', '_', q)
    szoveg = szoveg.replace(m, q)

while '__' in szoveg:
    szoveg=szoveg.replace('__', '_')
szoveg=szoveg.replace('"', '')


with open(sql_file, 'w', encoding='utf-8') as all:
    all.write(szoveg)

print('Kész. A módosított file eleje így néz ki:', szoveg[:255])