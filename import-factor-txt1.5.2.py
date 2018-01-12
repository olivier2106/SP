
#librairies
import numpy as np
import pandas as pd
import os
from datetime import date, timedelta

#import excel
df=pd.read_csv('C:\\Users\\Olivier\\Documents\\Doc Perso\\Axes de recherche\\Factor\\dmrs_hedgeportfolios_daily.txt',delimiter="\t")
print (df.date)
df['date2'] = pd.to_datetime(df['date'], unit='ms')

"""
#get correct dates
def int2date(argdate: int):
    year = int(argdate / 10000)
    month = int((argdate % 10000) / 100)
    day = int(argdate % 100)

    return date(year, month, day)

df["Date"]=int2date(df["date"])



#definition des functions de marqueurs temporels

def first_friday_df():
    ligne_start=1
    n=len(df["Date"])
    vect=[0]*n
    for k in range(ligne_start,n+ligne_start):
        if (df["Date"][k].weekday()==4) and (0<df["Date"][k].day<8):
            vect[k]=1
    return vect

df["first_friday_df"]=first_friday_df()
"""
#output
df.to_excel('C:\\Users\\Olivier\\Documents\\Doc Perso\\Axes de recherche\\Factor\\dmrs_hedgeportfolios_daily.xlsx')
os.startfile('C:\\Users\\Olivier\\Documents\\Doc Perso\\Axes de recherche\\Factor\\dmrs_hedgeportfolios_daily.xlsx')
