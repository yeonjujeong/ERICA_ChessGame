<<<<<<< HEAD
def Board():   
  
  
=======
def Board():

>>>>>>> 74c713d10a6079ca88c8d8e247a7c7eb3a87e74e
    arr = [['車','象','馬','士',"0 ",'士',"馬",'象','車'],

       ["0 ","0 ","0 ","0 ","漢","0 ","0 " ,"0 ","0 "],

       ["0 ",'包',"0 ","0 ","0 ","0 ","0 ",'包',"0 "],

       ['兵',"0 ",'兵',"0 ",'兵',"0 ",'兵',"0 ",'兵'],

       ["0 ","0 ","0 ","0 ","0 ","0 ","0 " ,"0 ","0 "],

       ["0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 "],

       ['卒' , "0 ",'卒',"0 " ,'卒', "0 ",'卒', "0 ",'卒'],

       [ "0 ",'包', "0 ","0 ", "0 ", "0 ", "0 ",'包', "0 "],

       [ "0 ","0 " ,"0 " ,"0 " , "楚", "0 ","0 " ,"0 " ,"0 " ],

       ['車','象','馬','士',"0" ,'士','馬','象','車']]

    print("   ",end='')

    for i in range(9):

        print(str(i+1)+"열  ",end="")

    print('\n')

    for i in range(0,10):

        print(chr(65+i)+'행 ',end='')

        for j in range(0,9):

            if(j!=8):

                print(arr[i][j]+" - ",end="")

            elif(j==8):

                print(arr[i][j],end="\n")

        if(i!=9):

            print("    |"*9)



Board()