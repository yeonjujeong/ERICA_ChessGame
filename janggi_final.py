arr_red =[["* " for i in range(9)] for i in range(10)]
arr_blue = [["* " for i in range(9)] for i in range(10)]
turn = True #red=true,blue=false
end = True 

def Select_red_board(x):
    #Board_select_fuction
    #basic_red
    arr_red[0][0] = "車"
    arr_red[0][8] = "車"
    arr_red[0][3] = "士"
    arr_red[0][5] = "士"
    arr_red[1][4] = "漢"
    arr_red[2][1] = "包"
    arr_red[2][7] = "包"
    for i in range(5):
        arr_red[3][i*2] = "兵"
    if(x==1):
        arr_red[0][1] = "馬"
        arr_red[0][7] = "馬"
        arr_red[0][2] = "象"
        arr_red[0][6] = "象"
    elif(x==2):
        arr_red[0][2] = "馬"
        arr_red[0][6] = "馬"
        arr_red[0][1] = "象"
        arr_red[0][7] = "象"
    elif(x==3):
        arr_red[0][2] = "馬"
        arr_red[0][7] = "馬"
        arr_red[0][1] = "象"
        arr_red[0][6] = "象"
    elif(x==4):
        arr_red[0][1] = "馬"
        arr_red[0][6] = "馬"
        arr_red[0][2] = "象"
        arr_red[0][7] = "象"

def Select_blue_board(y):
    #basic_blue
    arr_blue[9][0] = "車"
    arr_blue[9][8] = "車"
    arr_blue[9][3] = "士"
    arr_blue[9][5] = "士"
    arr_blue[8][4] = "楚"
    arr_blue[7][1] = "包"
    arr_blue[7][7] = "包"
    for i in range(5):
        arr_blue[6][i*2] = "卒"
    if(y==1):
        arr_blue[9][1] = "馬"
        arr_blue[9][7] = "馬"
        arr_blue[9][2] = "象"
        arr_blue[9][6] = "象"
    elif(y==2):
        arr_blue[9][2] = "馬"
        arr_blue[9][6] = "馬"
        arr_blue[9][1] = "象"
        arr_blue[9][7] = "象"
    elif(y==3):
        arr_blue[9][1] = "馬"
        arr_blue[9][6] = "馬"
        arr_blue[9][2] = "象"
        arr_blue[9][7] = "象"
    elif(y==4):
        arr_blue[9][2] = "馬"
        arr_blue[9][7] = "馬"
        arr_blue[9][1] = "象"
        arr_blue[9][6] = "象"

def Board():
    #Board_print_fuction
    print("   ",end='')
    for i in range(9):
        print(str(i+1)+"열  ",end="")
    print('\n')
    #piece_print_color_red_or_blue
    C_WHITE  = "\033[37m"
    C_RED    = "\033[31m"
    C_BLUE   = "\033[34m"
    for i in range(0,10):
        print(chr(i+65)+'행 ',end='')
        for j in range(0,9):
            if(j!=8):
                if(arr_red[i][j]=="* " and arr_blue[i][j]=="* "):
                    print(C_WHITE+"*  - ",end="")
                elif(arr_red[i][j]=="* "):
                    print(C_BLUE+ arr_blue[i][j]+C_WHITE+" - ",end="")
                elif(arr_blue[i][j]=="* "):
                    print(C_RED+arr_red[i][j]+C_WHITE+" - ",end="")
            elif(j==8):
                if(arr_red[i][j]=="* " and  arr_blue[i][j]=="* "):
                    print(C_WHITE+"*   ")
                elif(arr_red[i][j]=="* "):
                    print(C_BLUE+arr_blue[i][j]+C_WHITE)
                elif(arr_blue[i][j]=="* "):
                    print(C_RED+arr_red[i][j]+C_WHITE)
        if(i==0 or i==7):
            print("    |    |    |    | \  |  / |    |    |    |")
        elif(i==1 or i==8):
            print("    |    |    |    | /  |  \ |    |    |    |")
        elif(i!=9):
            print("    |"*9)
    if(turn):
        print("this turn is red")
    else:
        print("this turn is blue")
    print('\n')

def red_Startpos():
    try:
        x = int(input("Player 1의 상차림을 선택하세요(안=1/바깥=2/오른=3/왼=4):"))
        while not(x==1 or x==2 or x==3 or x==4):
            print("다시 입력해주세요.")
            x = int(input("Player 1의 상차림을 선택하세요(안=1/바깥=2/오른=3/왼=4):"))
        return x
    except ValueError:
        print("다시 입력해주세요.")
        red_Startpos()
def blue_Startpos():
    try:
        y = int(input("Player 2의 상차림을 선택하세요(안=1/바깥=2/오른=3/왼=4):"))
        while not (y==1 or y==2 or y==3 or y==4):
            print("다시 입력해주세요.")
            y = int(input("Player 2의 상차림을 선택하세요(안=1/바깥=2/오른=3/왼=4):"))
        return y
    except ValueError:
        print("다시 입력해주세요.")
        blue_Startpos()

def Movepos_bf1():
    print("이동시킬 말의 행과 열을 입력하시오.")
    a1 = input("몇 행?(A~J): ")
    while (chr(65)>a1 or a1>=chr(75)):
        print("다시 입력해주세요.")
        a1 = input("몇 행?(A~J): ")
    return a1

def Movepos_bf2():
    try:
        a2 = int(input("몇 열?(1~9): "))
        while (a2>9 or a2<1):
            print("다시 입력해주세요.")
            a2 = int(input("몇 열?(1~9): "))
        return a2
    except ValueError:
        print("다시 입력해 주세요")
        Movepos_bf2()

def Movepos_af1():
    print("말의 이동시킬 행과 열을 입력하시오.")
    b1 = input("몇 행?(A~J): ")
    while (chr(65)>b1 or b1>=chr(75)):
        print("다시 입력해주세요.")
        b1 = input("몇 행?(A~J): ")
    return b1

def Movepos_af2():
    try:
        b2 = int(input("몇 열?(1~9): "))
        while (b2>9 or b2<1):
            print("다시 입력해주세요.")
            b2 = int(input("몇 열?(1~9): "))
        return b2
    except ValueError:
        print("다시 입력해주세요.")
        Movepos_af2()

def red_byeong(x1,x2,y1,y2):
    global turn
    while(x1==y1 and y1==y2 or x2==y2 and y1-x1!=1 or x1==y1 and abs(x2-y2)!=1):
        print("兵이 이동할 수 없는 곳입니다.")
        main_run()
    if(arr_blue[y1][y2]=="* " and arr_red[y1][y2]=="* "):
        arr_red[y1][y2] = "兵"
        arr_red[x1][x2] = "* "
        turn = False
        print("blue_turn")
    elif(arr_blue[y1][y2]!="* "):
        arr_red[y1][y2] = "兵"
        arr_red[x1][x2] = "* "
        arr_blue[y1][y2] = "* "         
        turn = True
        print("again red_turn")

def blue_jjol(x1,x2,y1,y2):
    global turn
    while(x1==y1 and y1==y2 or x2==y2 and y1-x1!=-1 or x1==y1 and abs(x2-y2)!=1):
        print("卒이 이동할 수 없는 곳입니다.")
        main_run() 
    if(arr_red[y1][y2]=="* " and arr_blue[y1][y2]=="* "):
        arr_blue[y1][y2] = "卒"
        arr_blue[x1][x2] = "* "
        turn = True
        print("again red_turn")
    elif(arr_red[y1][y2]!="* "):
        arr_blue[y1][y2] = "卒"
        arr_blue[x1][x2] = "* "
        arr_red[y1][y2] = "* "
        turn = False
        print("again blue_turn")

def red_cha(x1,x2,y1,y2):
    global turn
    while(x1!=y1 and x2!= y2):
        print("cha can't move that position")
        main_run()
    if(x2 < y2 and x1 == y1):
        sum = 1
        for i in range(x2, y2):
            if(arr_red[x1][i] == "* " and arr_blue[x1][i] == "* "):
                sum+=1
        if(sum!=y2-x2):        
            print("wrong position")
            main_run()
    elif(x2 > y2 and x1 == y1):
        sum = 1
        for i in range(x2, y2, -1):
            if(arr_red[x1][i] == "* " and arr_blue[x1][i] == "* "):
                sum+=1
        if(sum != x2-y2):        #이것도. //kimjeongmin
            print("wrong position")
            main_run()
    elif(x1 < y1 and x2==y2):
        sum = 1
        for i in range(x1, y1):
            if(arr_red[i][x2] == "* " and arr_blue[i][x2] == "* "):
                sum+=1
        if(sum!=y1-x1):
            print("wrong position")
            main_run()
    elif(x1 > y1 and x2 == y2):
        sum = 1
        for i in range(x1, y1, -1):
            if(arr_red[i][x2] == "* " and arr_blue[i][x2] == "* "):
                sum+=1
        if(sum != x1-y1):
            print("wrong position")
            main_run()
    if(arr_blue[y1][y2] =="* "):
        arr_red[y1][y2] = "車"
        arr_blue[y1][y2] = "* "
        arr_red[x1][x2] = "* "
    elif(arr_blue[y1][y2]!="* "):
        arr_red[y1][y2] = "車"
        arr_red[x1][x2] = "* "
        arr_blue[y1][y2] = "* "
    turn = False

def blue_cha(x1,x2,y1,y2):
    global turn
    while(x1!=y1 and x2!= y2):
        print("cha can't move that position")
        main_run()
    if(x2 < y2 and x1 == y1):
        sum = 1
        for i in range(x2, y2):
            if(arr_red[x1][i] != "* " and arr_blue[x1][i] != "* "):
                sum+=1
        if(sum!=y2-x2):
            print("wrong position")
            main_run()
    elif(x2 > y2 and x1 == y1):
        sum = 1
        for i in range(x2, y2, -1):
            if(arr_red[x1][i] != "* " and arr_blue[x1][i] != "* "):
                sum+=1
        if(sum != x2-y2):
            print("wrong position")
            main_run()
    elif(x1 < y1 and x2==y2):
        sum = 1
        for i in range(x1, y1):
            if(arr_red[i][x2] != "* " and arr_blue[i][x2] != "* "):
                sum+=1
        if(sum!=y1-x1):
            print("wrong position")
            main_run()
    elif(x1 > y1 and x2 == y2):
        sum = 1
        for i in range(x1, y1, -1):
            if(arr_red[i][x2] != "* " and arr_blue[i][x2] != "* "):
                sum+=1
        if(sum != x1-y1):
            print("wrong position")
            main_run()
    if(arr_red[y1][y2] == "* "):
        arr_blue[y1][y2] = "車"
        arr_blue[x1][x2] = "* "
    elif(arr_red[y1][y2]!="* "):    
        arr_blue[x1][x2] = "* "
        arr_blue[y1][y2] = "車"
        arr_red[y1][y2] = "* "
    turn = True

def red_sa(x1,x2,y1,y2):
    global turn    
    while(x1!=y1 and x2!=y2 or arr_red[y1][y2]!="* " or 0>y1 or y1>2 or 3>y2 or y2>5):
        if(x1==0 and x2==3):
            if(y1==0 and y2==4 or y1==1 and y2==3 or y1==1 and y2==4):
                break
        elif(x1==0 and x2==5):
            if(y1==0 and y2==4 or y1==1 and y2==4 or y1==1 and y2==5):
                break
        elif(x1==2 and x2==3):
            if(y1==2 and y2==4 or y1==1 and y2==4 or y1==2 and y2==3):
                break
        elif(x1==2 and x2==5):
            if(y1==2 and y2==4 or y1==1 and y2==4 or y1==1 and y2==5):
                break
        elif(x1==1 and x2==4):
            if(y1==0 and y2==3 or y1==0 and y2==4 or y1==0 and y2==5 or y1==1 and y2==3 or y1==1 and y2==5 or y1==2 and y2==3 or y1==2 and y2==4 or y1==2 and y2==5):
                break
        print("기물을 움직일 수 없습니다.")
        main_run() 
    if(arr_blue[y1][y2]=="* "):
        arr_red[y1][y2]="士"
        arr_red[x1][x2]="* "
        print("blue_turn")
        turn = False
    elif(arr_blue[y1][y2]!="* "):
        arr_red[y1][y2]="士"
        arr_red[x1][x2]="* "
        arr_blue[y1][y2]="* "
        print("again red_turn")
        turn = True

def blue_sa(x1,x2,y1,y2):
    global turn
    while(x1!=y1 and x2!= y2 or arr_blue[y1][y2]!="* " or 7>y1 or y1>9 or 3>y2 or y2>5):
        if(x1==9 and x2==5):
            if(y1==9 and y2==4 or y1==8 and y2==5 or y1==8 and y2==4):
                break
        elif(x1==9 and x2==5):
            if(y1==9 and y2==4 or y1==8 and y2==4 or y1==8 and y2==3):
                break
        elif(x1==7 and x2==3):
            if(y1==7 and y2==4 or y1==8 and y2==4 or y1==7 and y2==5):
                break
        elif(x1==7 and x2==5):
            if(y1==7 and y2==4 or y1==8 and y2==4 or y1==8 and y2==3):
                break
        elif(x1==8 and x2==4):
            if(y1==9 and y2==5 or y1==9 and y2==4 or y1==9 and y2==3 or y1==8 and y2==5 or y1==8 and y2==3 or y1==7 and y2==5 or y1==7 and y2==4 or y1==7 and y2==3):
                break
        print("기물을 움직일 수 없습니다.")
        main_run()
    if(arr_red[y1][y2]=="* "):
        arr_blue[y1][y2]="士"
        arr_blue[x1][x2]="* "
        print("red_turn")
        turn = True
    elif(arr_red[y1][y2]!="* "):
        arr_blue[x1][x2]="* "
        arr_blue[y1][y2]="士 "
        arr_red[y1][y2]="* "
        print("again blue_turn")
        turn = False

def red_han(x1,x2,y1,y2):
    global turn
    while True:
        if not((abs(x1-y1)<=1 and abs(x2-y2)<=1) and (y2>=3 and y2<=5 and y1<=2) and (x1 !=y1 or x2!=y2)):
            print("기물을 움직일 수 없습니다.")
            main_run()
        else:
            if (x1 == 0 and x2 == 4):
                if((y1 == 1 and y2 == 3) or (y1 == 1 and y2 == 5)):
                    print("기물을 움직일 수 없습니다.")
                    main_run()
                else:
                    break
            elif(x1 == 1 and x2 == 3):
                if(y1 == 0 and y2 == 4 or y1 == 2 and y2 == 4):
                    print("기물을 움직일 수 없습니다.")
                    main_run()
                else:
                    break            
            elif(x1 == 1 and x2 == 5):
                if(y1 == 0 and y2 == 4 or y1 == 2 and y2 == 4):
                    print("기물을 움직일 수 없습니다.")
                    main_run()
                else:
                    break            
            elif(x1 == 2 and x2 == 4):
                if(y1 == 1 and y2 == 3 or  y1 == 1 and y2 == 5):
                    print("기물을 움직일 수 없습니다.")
                    main_run()
                else:
                    break
            else:
                break
 
    if(arr_red[y1][y2]=="* " and arr_blue[y1][y2]=="* "):
        arr_red[y1][y2]="漢"
        arr_red[x1][x2]="* "
        turn = False
    elif(arr_blue[y1][y2] != "* "):
        arr_red[y1][y2] = "漢"
        arr_red[x1][x2] = "* "
        arr_blue[y1][y2] = "* "
        turn = False
        

def blue_cho(x1,x2,y1,y2):
    global turn
    while True:
        if not((abs(x1-y1)<=1 and abs(x2-y2)<=1) and (y2>=3 and y2<=5 and y1>=6) and (x1 !=y1 or x2!=y2)):
            print("기물을 움직일 수 없습니다.")
            main_run()
        else:
            if (x1 == 9 and x2 == 4):
                if((y1 == 8 and y2 == 3) or (y1 == 8 and y2 == 5)):
                    print("기물을 움직일 수 없습니다.")
                    main_run()
                else:
                    break
            elif(x1 == 8 and x2 == 3):
                if(y1 == 7 and y2 == 4 or y1 == 9 and y2 == 4):
                    print("기물을 움직일 수 없습니다.")
                    main_run()
                else:
                    break

            elif(x1 == 8 and x2 == 5):
                if(y1 == 7 and y2 == 4 or y1 == 9 and y2 == 4):
                    print("기물을 움직일 수 없습니다.")
                    main_run()
                else:
                    break

            elif(x1 == 7 and x2 == 4):
                if(y1 == 8 and y2 == 3 or  y1 == 8 and y2 == 5):
                    print("기물을 움직일 수 없습니다.")
                    main_run()
                else:
                    break
            else:
                break
            
    if(arr_red[y1][y2]=="* " and arr_blue[y1][y2]=="* "):
        arr_blue[y1][y2]="楚"
        arr_blue[x1][x2]="* "
        turn = True
       
    elif(arr_red[y1][y2] != "* "):
        arr_blue[y1][y2] = "楚"
        arr_blue[x1][x2] = "* "
        arr_red[y1][y2] = "* "
        turn = True
        

def red_ma(x1,x2,y1,y2):
    global turn
    while not(y1-x1==2 and abs(y2-x2)==1 and arr_red[x1+1][x2]=="* " and arr_blue[x1+1][x2]=="* " or x1-y1==2 and abs(y2-x2)==1 and arr_red[x1-1][x2]=="* " and arr_blue[x1-1][x2]=="* " or y2-x2==2 and abs(y1-x1)==1 and arr_red[x1][x2+1]=="* " and arr_blue[x1][x2+1]=="* " or x2-y2==2 and abs(y1-x1)==1 and arr_red[x1][x2-1]=="* " and arr_blue[x1][x2-1]=="* "):
        print("기물을 움직일 수 없습니다.")
        main_run()
    if(arr_red[y1][y2]=="* " and arr_blue[y1][y2]=="* "):
        arr_red[y1][y2] = "馬"
        arr_red[x1][x2] = "* "
    elif(arr_blue[y1][y2]!="* "):
        arr_red[y1][y2] = "馬"
        arr_red[x1][x2] = "* "
        arr_blue[y1][y2] = "* "
    turn = False

def blue_ma(x1,x2,y1,y2):
    global turn
    while not(y1-x1==2 and abs(y2-x2)==1 and arr_red[x1+1][x2]=="* " and arr_blue[x1+1][x2]=="* " or x1-y1==2 and abs(y2-x2)==1 and arr_red[x1-1][x2]=="* " and arr_blue[x1-1][x2]=="* " or y2-x2==2 and abs(y1-x1)==1 and arr_red[x1][x2+1]=="* " and arr_blue[x1][x2+1]=="* " or x2-y2==2 and abs(y1-x1)==1 and arr_red[x1][x2-1]=="* " and arr_blue[x1][x2-1]=="* "):
        print("기물을 움직일 수 없습니다.")
        main_run()
    if(arr_red[y1][y2]=="* " and arr_blue[y1][y2]=="* "):
        arr_blue[y1][y2] = "馬"
        arr_blue[x1][x2] = "* "
    elif(arr_red[y1][y2]!="* "):
        arr_blue[y1][y2] = "馬"
        arr_blue[x1][x2] = "* "
        arr_red[y1][y2] = "* "
    turn = True

def red_po(x1,x2,y1,y2):   #포에 대한 설명 : 1.포는 포를 잡지 못하고 2.포는 포를 넘지 못한다. 3.포는 다른 기물을 하나 넘어서 가야한다 하지만 두개 이상은 넘지 못한다.
    global turn            #구현 한 것들 : 다른 기물을 하나 넘어서 가야한다. 하지만 두개 이상은 넘지 못한다.
    while(x1!=y1 and x2!= y2):
        print("기물을 움직일 수 없습니다.")
        main_run()
    while(arr_red[y1][y2]!="* "):
        print("기물을 움직일 수 없습니다.")
        main_run()
    for i in range(0,9):
        if((arr_red[x1][i]!="* " or arr_blue[x1][i]!="* ") and x1 == y1 and x2<i):
            for j in range(i+1,9):
                if(arr_red[x1][j]!="* "):
                    for k in range(i+1,j):
                        if(k==y2):
                            if(arr_blue[x1][k]=="* "):
                                arr_red[y1][k]="包"
                                arr_red[x1][x2]="* "
                                print("blue turn")
                                turn = False
                                break
                            elif(arr_blue[x1][k]!="* "):
                                arr_blue[x2][k]="* "
                                arr_red[x2][k]="包 "
                                arr_red[x1][x2]="* "
                                turn = True
                                print("again red_turn")
                                break

        if((arr_red[x1][i]!="* " or arr_blue[x1][i]!="* ") and x1 == y1 and x2>i):
            for j in range(i-1,-1,-1):
                 if(arr_red[x1][j]!="* "):
                     for k in range(i-1,j,-1):
                         if(k==y2):
                             if(arr_blue[x1][k]=="* "): 
                                 arr_red[y1][k]="包"
                                 arr_red[x1][x2]="* "
                                 print("blue_turn")
                                 turn =False
                                 break
                             elif(arr_blue[x1][k]!="* "):
                                 arr_red[y1][k]="包 "
                                 arr_red[x1][x2]="* "
                                 arr_blue[x1][k]="*"
                                 turn = True
                                 print("again red_turn")
                                 break
    for i in range(0,10):
        if((arr_red[i][x2]!="* " or arr_blue[i][x2]!="* ")and x2 == y2 and x2<i):
            for j in range(i+1,10):
                if(arr_red[j][x2]!="* "):
                    for k in range(i+1,j):
                        if(k==y1):
                            if(arr_blue[k][y2]=="* "):
                                arr_red[k][y2]="包"
                                arr_red[x1][x2]="* "
                                turn = False
                                print("blue_turn")
                                break
                            elif(arr_blue[k][y2]!="* "):
                                arr_blue[k][y2]="* "
                                arr_red[k][y2]="包"
                                arr_red[x1][x2]="* "
                                turn = True
                                print("again red_turn")
                                break
        if((arr_red[i][x2]!="* " or arr_blue[i][x2]!="* ") and x2==y2 and x2>i):
            for j in range(i+1,10):
                if(arr_red[j][x2]!="* "):
                    for k in range(i+1,j):
                        if(k==y1):
                            if(arr_blue[k][y2]=="* "):
                                arr_red[k][y2]="包"
                                arr_red[x1][x2]="* "
                                print("blue_trun")
                                trun = False
                                break
                            elif(arr_blue[k][y2]!="* "):
                                arr_blue[k][y2]="* "
                                arr_red[k][y2]="包"
                                arr_red[x1][x2]="* "
                                print("again red_turn")
                                turn = True
                                break
                                
def blue_po(x1,x2,y1,y2):
    global turn
    while(x1!=y1 and x2!= y2):
        print("기물을 움직일 수 없습니다.")
        main_run()
    while(arr_red[y1][y2]!="* "):
        print("기물을 움직일 수 없습니다.")
        main_run()
    for i in range(0,9):
        if((arr_blue[x1][i]!="* " or arr_red[x1][i]!="* ") and x1 == y1 and x2<i):
            for j in range(i+1,9):
                if(arr_blue[x1][j]!="* "):
                    for k in range(i+1,j):
                        if(k==y2):
                            if(arr_red[x1][k]=="* "):
                                arr_blue[y1][k]="包"
                                arr_blue[x1][x2]="* "
                                print("red_turn")
                                turn = True
                                break
                            elif(arr_red[x1][k]!="* "):
                                arr_red[x2][k]="* "
                                arr_blue[x2][k]="包 "
                                arr_blue[x1][x2]="* "
                                turn = False
                                print("again blue_turn")
                                break

        if((arr_blue[x1][i]!="* " or arr_red[x1][i]!="* ")and x1 == y1 and x2>i):
            for j in range(i-1,-1,-1):
                 if(arr_blue[x1][j]!="* "):
                     for k in range(i-1,j,-1):
                         if(k==y2):
                             if(arr_red[x1][k]=="* "): 
                                 arr_blue[y1][k]="包"
                                 arr_blue[x1][x2]="* "
                                 print("red_turn")
                                 turn = True
                                 break
                             elif(arr_red[x1][k]!="* "):
                                 arr_blue[y1][k]="包 "
                                 arr_blue[x1][x2]="* "
                                 arr_red[x1][k]="*"
                                 turn = False
                                 print("again blue_turn")
                                 break
    for i in range(0,10):
        if((arr_blue[i][x2]!="* " or arr_red[i][x2]!="* ")and x2==y2 and x2<i):
            for j in range(i+1,10):
                if(arr_blue[j][x2]!="* "):
                    for k in range(i+1,j):
                        if(k==y1):
                            if(arr_red[k][y2]=="* "):
                                arr_blue[k][y2]="包"
                                arr_blue[x1][x2]="* "
                                print("red_turn")
                                turn = True
                                break
                            elif(arr_red[k][y2]!="* "):
                                arr_red[k][y2]="* "
                                arr_blue[k][y2]="包"
                                arr_blue[x1][x2]="* "
                                print("again blue_turn")
                                turn = False
                                break
                                
        if((arr_blue[i][x2]!="* " or arr_red[i][x2]!="* ") and x2==y2 and x2>i):
            for j in range(i-1,-1,-1):
                if(arr_blue[j][x2]!="* "):
                    for k in range(i-1,j,-1):
                        if(k==y2):
                            if(arr_red[k][y2]=="* "):
                                arr_blue[k][y2]="包"
                                arr_blue[x1][x2]="* "
                                print("red_trun")
                                trun = True
                                break
                            elif(arr_red[k][y2]!="* "):
                                arr_blue[k][y2]="* "
                                arr_red[k][y2]="包"
                                arr_red[x1][x2]="* "
                                print("again blue_turn")
                                turn = False
                                break
def red_shang(x1,x2,y1,y2):
    global turn
    while(1):
        if(y1-x1==3 and y2-x2==2 and arr_blue[x1+1][x2]=="* " and arr_red[x1+1][x2]=="* "and arr_blue[x1+2][x2+1]=="* " and arr_red[x1+2][x2+1]=="* " ):
            break
        elif(y1-x1==3 and x2-y2==2 and arr_blue[x1+1][x2]=="* " and arr_red[x1+1][x2]=="* "and arr_blue[x1+2][x2-1]=="* " and arr_red[x1+2][x2-1]=="* " ):
            break
        elif(x1-y1==3 and y2-x2==2 and arr_blue[x1-1][x2]=="* " and arr_red[x1-1][x2]=="* "and arr_blue[x1-2][x2+1]=="* " and arr_red[x1-2][x2+1]=="* " ):
            break
        elif(x1-y1==3 and x2-y2==2 and arr_blue[x1-1][x2]=="* " and arr_red[x1-1][x2]=="* "and arr_blue[x1-2][x2-1]=="* " and arr_red[x1-2][x2-1]=="* " ):
            break
        main_run()
    if(arr_blue[y1][y2]=="* " and arr_red[y1][y2]=="* "):
        arr_red[y1][y2] = "象"
        arr_red[x1][x2] = "* "
    elif(arr_blue[y1][y2]!="* "):
        arr_red[y1][y2] = "象"
        arr_red[x1][x2] = "* "
        arr_blue[y1][y2] = "* "

def blue_shang(x1,x2,y1,y2):
    global turn
    while(1):
        if(y1-x1==3 and y2-x2==2 and arr_blue[x1+1][x2]=="* " and arr_red[x1+1][x2]=="* "and arr_blue[x1+2][x2+1]=="* " and arr_red[x1+2][x2+1]=="* " ):
            break
        if(y1-x1==3 and x2-y2==2 and arr_blue[x1+1][x2]=="* " and arr_red[x1+1][x2]=="* "and arr_blue[x1+2][x2-1]=="* " and arr_red[x1+2][x2-1]=="* " ):
            break
        if(x1-y1==3 and y2-x2==2 and arr_blue[x1-1][x2]=="* " and arr_red[x1-1][x2]=="* "and arr_blue[x1-2][x2+1]=="* " and arr_red[x1-2][x2+1]=="* " ):
            break 
        if(x1-y1==3 and x2-y2==2 and arr_blue[x1-1][x2]=="* " and arr_red[x1-1][x2]=="* "and arr_blue[x1-2][x2-1]=="* " and arr_red[x1-2][x2-1]=="* " ):
            break
        main_run()
    if(arr_blue[y1][y2]=="* " and arr_red[y1][y2]=="* "):
        arr_blue[y1][y2] = "象"
        arr_blue[x1][x2] = "* "
    elif(arr_red[y1][y2]!="* "):
        arr_blue[y1][y2] = "象"
        arr_blue[x1][x2] = "* "
        arr_red[y1][y2] = "* "
   
def red_run():
    global turn
    x1 = ord(Movepos_bf1())-65
    x2 = Movepos_bf2()-1
    while(arr_red[x1][x2]=="* "):
        print("wrong position")
        x1 = ord(Movepos_bf1())-65
        x2 = Movepos_bf2()-1
    y1 = ord(Movepos_af1())-65
    y2 = Movepos_af2()-1
    while(arr_red[y1][y2]!="* "):
        print("already red exists")
        y1 = ord(Movepos_af1())-65
        y2 = Movepos_af2()-1
    if(arr_red[x1][x2]=="兵"):
        red_byeong(x1,x2,y1,y2)
    
    if(arr_red[x1][x2] == "車"):
        red_cha(x1,x2,y1,y2)
       
    if(arr_red[x1][x2] == "士"):
        red_sa(x1,x2,y1,y2)

    if(arr_red[x1][x2] == "包"):
        red_po(x1,x2,y1,y2)
    
    if(arr_red[x1][x2] == "漢"):
        red_han(x1,x2,y1,y2)
    
    if(arr_red[x1][x2] == "馬"):
        red_ma(x1,x2,y1,y2)

    if(arr_red[x1][x2] == "象"):
        red_shang(x1,x2,y1,y2)

def blue_run():
    global turn
    x1 = ord(Movepos_bf1())-65
    x2 = Movepos_bf2()-1
    while(arr_blue[x1][x2]=="* "):
        print("wrong position")
        x1 = ord(Movepos_bf1())-65
        x2 = Movepos_bf2()-1
    y1 = ord(Movepos_af1())-65
    y2 = Movepos_af2()-1
    while(arr_blue[y1][y2]!="* "):
        print("already blue  exists")
        y1 = ord(Movepos_af1())-65
        y2 = Movepos_af2()-1
    if(arr_blue[x1][x2]=="卒"):
        blue_jjol(x1,x2,y1,y2)
                   
    if(arr_blue[x1][x2] == "車"):
        blue_cha(x1,x2,y1,y2)

    if(arr_blue[x1][x2] == "士"):
        blue_sa(x1,x2,y1,y2)

    if(arr_blue[x1][x2] == "包"):
        blue_po(x1,x2,y1,y2)
        
    if(arr_blue[x1][x2] == "楚"):
        blue_cho(x1,x2,y1,y2)

    if(arr_blue[x1][x2] == "馬"):
        blue_ma(x1,x2,y1,y2)
   
    if(arr_blue[x1][x2] == "象"):
        blue_shang(x1,x2,y1,y2)

def main_run():
    global end
    while(end):
        if(turn):
            Board()
            blue_run()
            sum=0
            for i in range(10):
                for j in range(9):
                    if(arr_red[i][j]=="" or arr_blue[i][j]==""):
                        sum += 1
            if(sum!=2):
                end = False

def main():
    print("장기하-자.")
    x = red_Startpos()
    y = blue_Startpos()
    Select_red_board(x)
    Select_blue_board(y)
    Board()
    while(end):
        if(turn):
            Board()
            red_run()
        else:
            Board()
            blue_run()

main()
