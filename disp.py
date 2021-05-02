import cv2
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import CNNModel 
import sqlite3

ch = input("Enter a character: ")
if ch =='a' or ch=='A':
    print(ch, "is an Alphabet")
   
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='b' or ch=='B':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='c' or ch=='C':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='d' or ch=='D':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='e' or ch=='E':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='f' or ch=='F':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='g' or ch=='G':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='h' or ch=='H':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='i' or ch=='I':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='j' or ch=='J':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='k' or ch=='K':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='l' or ch=='L':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='m' or ch=='M':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='n' or ch=='N':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='o' or ch=='O':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='p' or ch=='P':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='q' or ch=='Q':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='r' or ch=='R':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='s' or ch=='S':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='t' or ch=='T':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='u' or ch=='U':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='v' or ch=='V':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='w' or ch=='W':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='x' or ch=='X':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='y' or ch=='Y':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
elif ch =='z' or ch=='Z':
    print(ch, "is an Alphabet")
    img = cv2.imread("1.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("Cute Kitens", img)
else:
    print(ch, "is not an Alphabet")