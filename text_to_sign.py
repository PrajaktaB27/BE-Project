# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 15:17:38 2021

@author: sheet
"""
import tkinter as tk
from tkinter.filedialog import askopenfilename
import os
# import sys
from PIL import Image, ImageTk
import PIL.Image
import cv2
import tflearn
import numpy as np
import tensorflow as tf
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression


import warnings
warnings.filterwarnings('ignore') # suppress import warnings



root=tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.configure(background="cyan3")
Married = tk.StringVar()
root.title(" "*190+"---Text to Sign Conversion---")
import tkinter as tk
image2 =Image.open('back.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)
lbl = tk.Label(root, text="Text To Sign Conversion", font=('times', 40,' bold '), height=1, width=30,bg="Black",fg="indian red")
lbl.place(x=250, y=5)

def getTextInput():
    #result=textExample.get("1.0","end")
    ch=Married.get()
    print(ch)
   # ch=[char for char in result]
    list1 = list(ch)
    print(list1)
    counter = -1
    for i in list1:
      
    # incrementing counter
        counter = counter + 1
        print(counter)
        ch = list1[counter]
        print(ch)
        
        if ch =='a' or ch=='A':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/A.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='b' or ch=='B':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/B.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='c' or ch=='C':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/C.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='d' or ch=='D':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/D.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='e' or ch=='E':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/E.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='f' or ch=='F':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/F.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='g' or ch=='G':
            IMAGE_SIZE = 200
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/g.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='h' or ch=='H':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/H.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='i' or ch=='I':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/I.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(0)
        elif ch =='j' or ch=='J':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/j.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='k' or ch=='K':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/K.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='l' or ch=='L':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/L.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='m' or ch=='M':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/M.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='n' or ch=='N':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/N.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='o' or ch=='O':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/O.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='p' or ch=='P':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/P.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='q' or ch=='Q':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/Q.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='r' or ch=='R':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/R.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='s' or ch=='S':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/S.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='t' or ch=='T':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/T.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='u' or ch=='U':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/U.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='v' or ch=='V':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/V.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='w' or ch=='W':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/W.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='x' or ch=='X':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/X.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='y' or ch=='Y':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/Y.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch =='z' or ch=='Z':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/Z.jpg', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        elif ch ==' ':
            IMAGE_SIZE = 200
            print(ch, "is an Alphabet")
            img = cv2.imread('C:/Users/Admin/OneDrive/Desktop/Sign-Language-master/CH/black.png', 1)
            c = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Color image', c)
            cv2.waitKey(1000)
        else:
            print(ch, "is not an Alphabet")
# Printing length of list 
        print ("Length of list using naive method is : " + str(counter))
        

l10 = tk.Label(root, text="Enter Text Here.:",font=("Times new roman", 20, "bold"), bg="pink")
l10.place(x=300, y=150)
Married=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=Married)
Married.place(x=600,y=150)


btnRead=tk.Button(root, height=1, width=10, text="Display Sign",font=("Tempus Sans ITC", 25, "bold"), 
                    command=getTextInput)

btnRead.place(x=500,y=250)

root.mainloop()