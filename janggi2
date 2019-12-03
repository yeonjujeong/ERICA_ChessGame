def red_run(x1,x2,y1,y2):
    if(arr_red[x1][x2]=="兵"):
        # x1과 y1,x2와 y2는 1차이나야함 예외처리할것
        if(arr_red[y1][y2]=="* " and arr_blue[y1][y2]=="* "):
            arr_red[y1][y2] = "兵"
            arr_red[x1][x2] = "* "
            print("성공")
        elif(arr_blue[y1][y2]!="* "):
            arr_red[y1][y2] = "兵"
            arr_blue[x1][x2] = "* "
        else:
            ("이미 같은 팀의 장기가 놓여있습니다. 다시 입력해주세요")
            #다시받는거 예외처리로 넘어가야함
def blue_run(x1,x2,y1,y2):
    if(arr_blue[x1][x2]=="卒"):
        if(arr_red[y1][y2]=="* " and arr_blue[y1][y2]=="* "):
            arr_blue[y1][y2] = "卒"
            arr_blue[x1][x2] = "* "
            print("성공")
        elif(arr_red[y1][y2]!="* "):
            arr_blue[y1][y2] = "卒"
            arr_red[x1][x2] = "* "
        else:
            ("이미 같은 팀의 장기가 놓여있습니다. 다시 입력해주세요")
            #다시받는거 예외처리로 넘어가야함
def main():
    print("장기하-자.")
    x = input("Player 1의 상차림을 선택하세요(안=1/바깥=2/오른=3/왼=4):")
    y = input("Player 2의 상차림을 선택하세요(안=1/바깥=2/오른=3/왼=4):")
    Select_red_board(x)
    Select_blue_board(y)
    Board()
    a1 = ord(input("이동시킬 말의 행과 열을 입력하시오.\n몇 행?: "))-65
    a2 = int(input("몇 열?: "))-1
    b1 = ord(input("이동할 행과 열을 입력하시오.\n몇 행?: "))-65
    b2 = int(input("몇 열?: "))-1
    if(turn):
        red_run(a1,a2,b1,b2)
        Board()
    else:
        blue_run(a1,a2,b1,b2)
        Board()



main()  
