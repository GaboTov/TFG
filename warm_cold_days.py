# -*- coding: utf-8 -*-
# Commented out IPython magic to ensure Python compatibility.
!pip install --upgrade openpyxl
import openpyxl
import pandas as pd
import numpy as np
!pip install xlsxwriter
!pip install xlrd
from google.colab import drive 
drive.mount('/content/drive')
# %cd '/content/drive/My Drive/Colab Notebooks/TFG'

!ls

datos_madrid = 'madrid_datos.xlsx'
df_madrid = pd.read_excel(datos_madrid)
tn = df_madrid.columns

spring = df_madrid[df_madrid.month.isin([3,4,5])]
summer = df_madrid[df_madrid.month.isin([6,7,8])]
fall = df_madrid[df_madrid.month.isin([9,10,11])]
winter = df_madrid[df_madrid.month.isin([12,1,2])]
winter_tn10 = -5
winter_tn90 = 72
winter_tx10 = 66
winter_tx90 = 146
summer_tn10 = 128
summer_tn90 = 213
summer_tx10 = 236
summer_tx90 = 350
fall_tn10 = 40
fall_tn90 = 170
fall_tx10 = 113
fall_tx90 = 285.1
spring_tn10 = 32
spring_tn90 = 129
spring_tx10 = 118
spring_tx90 = 250

"""warm days """

def warm_days_TN (percentil,year_i,year_f,season):
  i = year_i 
  warm_day = []
  while i < year_f:
    year = season[season.year.isin([i])]
    days = len(year[year.TN > percentil])
    
    warm_day.append(days)
    
    i += 1 
  return warm_day

tn_warm_d_spring = warm_days_TN(spring_tn90,1950,2020,spring)
tn_warm_d_summer = warm_days_TN(summer_tn90,1950,2020,summer)
tn_warm_d_fall = warm_days_TN(fall_tn90,1950,2020,fall)

def warm_days_TX (percentil,year_i,year_f,season):
  i = year_i 
  warm_day = []
  while i < year_f:
    year = season[season.year.isin([i])]
    days = len(year[year.TX > percentil])
    
    warm_day.append(days)
    
    i += 1 
  return warm_day
tx_warm_d_spring = warm_days_TX(spring_tx90,1951,2020,spring)
tx_warm_d_summer = warm_days_TX(summer_tx90,1951,2020,summer)
tx_warm_d_fall = warm_days_TX(fall_tx90,1951,2020,fall)

"""Cold days"""

def cold_days_TN (percentil,year_i,year_f,season):
  i = year_i 
  cold_day = []
  while i < year_f:
    year = season[season.year.isin([i])]
    days = len(year[year.TN < percentil])
    
    cold_day.append(days)
    
    i += 1 
  return cold_day
tn_cold_d_spring = cold_days_TN (winter_tn10,1950,2020,spring)
tn_cold_d_summer = cold_days_TN (summer_tn10,1950,2020,summer)
tn_cold_d_fall = cold_days_TN (fall_tn10,1950,2020,fall)

def cold_days_TX (percentil,year_i,year_f,season):
  i = year_i 
  cold_day = []
  while i < year_f:
    year = season[season.year.isin([i])]
    days = len(year[year.TX < percentil])
    
    cold_day.append(days)
    
    i += 1 
  return cold_day
tx_cold_d_spring = cold_days_TX(winter_tx10,1950,2020,spring)
tx_cold_d_summer = cold_days_TX(summer_tx10,1950,2020,summer)
tx_cold_d_fall = cold_days_TX (fall_tx10,1950,2020,fall)



