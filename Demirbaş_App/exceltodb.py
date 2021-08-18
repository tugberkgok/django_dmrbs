import pandas as pd
import openpyxl
import sqlite3
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData
from sqlalchemy.orm import mapper

xls = pd.ExcelFile('D:/İndirilenler/PiriReis Bilişim Bilgisayar ve Yüz Tanıma Dosyası Sifresiz.xlsx')
file_name='D:/İndirilenler/PiriReis Bilişim Bilgisayar ve Yüz Tanıma Dosyası Sifresiz.xlsx'

conn=sqlite3.connect('D:/C den/Masaüstü/Çalışma/Py/Demirbaş Web/Demirbaş_Web/db.sqlite3')

for sheet_name in xls.sheet_names:
    #print(sheet_name)
    df = pd.read_excel(file_name, sheet_name=sheet_name, index_col=None)
    #df = df.asytpe(str)
    #print(df)
    #print("-------")
    #print(df[3:][0:])
    for index, row in df[3:][0:].iterrows():
        #print(type(str(row[1])))

        query = "INSERT INTO Demirbaş_App_device (stok, device, number, brand, model, serial, status, exp) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        print(query)
        c = conn.cursor()
        c.execute(query)

conn.commit()
conn.close()