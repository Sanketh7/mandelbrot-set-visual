#!/usr/bin/env python3

import math
from tkinter import *

c_real = input("Enter the REAL part of \"c\": ")
c_imag = input("Enter the IMAGINARY part of \"c\" (w/o \"i\"): ")
c = [float(c_real), float(c_imag)]

iterAmount = int(input("Enter the number of iterations to compute and draw: "))
iterPrintAmount = int(input("Enter the number of iterations to print: "))

tk = Tk()
tk.resizable(0,0)
canvas = Canvas(tk, width=500, height=500, highlightthickness=0, relief='ridge')
canvas.pack()

w = 500
h = 500

canvas.create_text(w/4, h/2+20, text="-1", font=('Courier', 22))
canvas.create_text(w*(3/4), h/2+20, text="+1", font=('Courier', 22))
canvas.create_text(w/2+10, w/4, text="i", font=('Courier', 22))
canvas.create_text(w/2+20, h*(3/4)-2, text="-i", font=('Courier', 22))

for b in range(0, h, 125):
    if b == 0:
        canvas.create_line(0, b, w, b, width=1)
    if b == 250:
        canvas.create_line(0, b, w, b, width=2, fill="blue")
    else:
        canvas.create_line(0, b, w, b, width=1)
for a in range(0, w, 125):
    if a == 0:
        canvas.create_line(a, 0, a, h, width=1)
    if a == 250:
        canvas.create_line(a, 0, a, h, width=2, fill="blue")
    else:
        canvas.create_line(a, 0, a, h, width=1)
    

def drawpoint(re, im):
    if re > 0:
        x = ((re/2) * 250) + 250
    elif re < 0:
        x = (2+re)/2 * 250
    elif re == 0:
        x = 250

    if im > 0:
        y = (2-im)/2 * 250
    elif im < 0:
        y = ((abs(im)/2) * 250) + 250
    elif im == 0:
        y = 250


    canvas.create_oval(x-1, y-1, x+1, y+1, fill="green")
        

#c = [-0.728, -0.128] # initial c value

iternumber = [0, 0]
orbitarray = []

def checkmandel(number):
  magstep1 = (number[0]*number[0]) + (number[1]*number[1])
  magnitude = math.sqrt(magstep1)
  
  if magnitude > 2:
    return "stop"
    
def mandel(num, cval):
  re = (num[0] * num[0]) - (num[1] * num[1])
  im = 2 * num[0] * num[1]
  
  cre = cval[0]
  cim = cval[1]
  return [re+cre, im+cim]


for x in range(0,iterAmount):
  iternumber = mandel(iternumber, c)
  #print(x)
  if checkmandel(iternumber) == "stop":
    print("NOT PART OF SET")
    break
  
  #print(iternumber)
  orbitarray.append(iternumber)

for z in orbitarray:
    drawpoint(z[0], z[1])

print("\n\nThese are the first " + str(iterPrintAmount) + " iterations (starting with z=0):")
for i in range(0, iterPrintAmount):
    if z[1] < 0:
        print(str(z[0]) + " - " + str(abs(z[1]))+"i")
    else:
        print(str(z[0]) + " + " + str(z[1])+"i")
        
tk.mainloop()
