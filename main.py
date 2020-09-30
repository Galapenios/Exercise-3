# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
from tabulate import tabulate


current = input("which folder would you like to see?" )
if current == '':
    current = os.getcwd()


filelist = os.listdir(current)
for x in filelist:
    R = str(os.access(x, os.R_OK))  # readable?#
    W = str(os.access(x, os.W_OK))  # writeable?#
    X = str(os.access(x, os.X_OK))  # executable?#
    F = str(os.access(x, os.F_OK))  # findable?#

    RR = "   readable: " + R
    WW = "   writable: " + W
    XX = "   executable: " + X
    FF = "   findable: " + F

    table = [[x,RR, WW, XX, FF]]
    output = tabulate(table, tablefmt='grid')
    print (output)
print("you are currently in:" + current)









