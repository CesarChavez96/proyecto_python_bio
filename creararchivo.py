from tkinter import *
import subprocess
import os
from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation
import time 
#import xlsxwriter

#def select():  
#   sel = "Value = " + str(v.get())  
#   label.config(text = sel)  
def ver(value):
	print(value)
root = Tk()

scl = Scale( root,from_=1,to=20,
tickinterval=2,
length=400,
resolution=1,
showvalue=NO,
orient=HORIZONTAL,
command=ver,
label="Velocidad del Puntero"
)
scl.pack(expand=YES, fill=Y)

def velocidad():
	wb = Workbook()  
	sheet = wb.active  
  
	sheet['A1'] = 87  
	sheet['A2'] = "Devansh"  
	sheet['A3'] = 41.80  
	sheet['A4'] = 10  
  
	now = time.strftime("%x")  
	sheet['A5'] = now  
  
	wb.save('C:\\Users\\cesar\\Desktop\\python\\sample_file.xlsx')  	
	file = open('C:\\Users\\cesar\\Desktop\\python\\archivo.sh', 'w')
	file.write("#!/bin/sh" + os.linesep)
	file.write("xset m " + str( scl.get())+ "1")
	file.close()
	subprocess.run(["chmod", "+x", 'C:\\Users\\cesar\\Desktop\\python\\archivo.sh'])
	subprocess.run(['C:\\Users\\cesar\\Desktop\\python\\archivo.sh'])

aplicar = Button(
root,
text="Aplicar",
command=velocidad
)
aplicar.pack()
root.mainloop()