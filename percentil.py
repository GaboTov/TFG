

!pip install --upgrade openpyxl
import openpyxl
import pandas as pd
import numpy as np
!pip install xlsxwriter
!pip install xlrd



datos_acoruña = 'acoruña_datos.xlsx'
df_acoruña = pd.read_excel(datos_acoruña)
df_acoruña.columns

df_acoruña = df_acoruña.rename(columns={'   RR': 'RR'})
df_acoruña = df_acoruña.rename(columns={'   TN': 'TN'})
df_acoruña = df_acoruña.rename(columns={'   TX': 'TX'})
df_acoruña.columns

df_acoruña.describe()

def reference_period (df,inicial, final):
  yearsf = df[df.Year<=final]
  years = yearsf[yearsf.Year>=inicial]
  return years

reference_period = reference_period(df_acoruña,1971,2000)

spring = reference_period[reference_period.Month.isin([3,4,5])] 
summer = reference_period[reference_period.Month.isin([6,7,8])] 
fall = reference_period[reference_period.Month.isin([9,10,11])] 
winter = reference_period[reference_period.Month.isin([12,1,2])]

reference_period

spring_arr_TN = np.array(spring.iloc[:, 4])
spring_arr_TX = np.array(spring.iloc[:, -1])

"""Pecentile TN"""

percentile10 = np.percentile(spring_arr_TN, 10)
acoruña_spring_tn10 = spring[spring.TN < percentile10]
acoruña_spring_tn10

percentile90 = np.percentile(spring_arr_TN,90)
acoruña_spring_tn90 = spring[spring.TN > percentile90]
acoruña_spring_tn90



"""Percentile TX"""

percentile_tx10 = np.percentile(spring_arr_TX, 10)
acoruña_spring_tx10 = spring[spring.TX < percentile_tx10]
acoruña_spring_tx10

percentile_tx90 = np.percentile(spring_arr_TX,90)
acoruña_spring_tx90 = spring[spring.TX > percentile_tx90]
acoruña_spring_tx90
