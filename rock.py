import random
import os
import time
def game():
    percent = 45
    os.system('cls')
    coin = 100
    while 1:
        print("코인수:", coin)
        try:
            betting=int(input("코인을 얼마 거실지 정하세요: "))
        except:
            print("제대로 된 숫자를 입력하세요.")
            continue
        while betting > coin:
            print("가진 코인보다 많은 코인을 베팅 거실 수는 없습니다.")
            try:
                betting=int(input("coin을 얼마 거실지 정하세요: "))
            except:
                continue
        while betting == 0:
            print("0개 이상의 코인을 겨셔야 합니다.")
            try:
                betting=int(input("coin을 얼마 거실지 정하세요: "))
            except:
                continue
        if betting == coin:
            print("올인하셨습니다.")

        person=str(input("무엇을 낼지 정하세요(가위, 바위, 보):\n"))
        while(person != "가위" and person != "바위" and person != "보"):
            print("가위, 바위, 보 중에 하나만 낼 수 있습니다.")
            person=str(input("무엇을 낼지 정하세요(가위, 바위, 보):\n"))
            
        machine = random.randint(1,100)
        if person == "가위" or person == "S" or person == "s":
            if machine > percent:
                print("상대: 주먹")
                wl = 0
            elif machine <= percent:
                print("상대: 보")
                wl = 1
            
        if person == "바위" or person == "R" or person == "r":
            if machine > percent:
                print("상대: 보")
                wl = 0
            elif machine <= percent:
                print("상대: 가위")
                wl = 1
            
        if person == "보" or person == "P" or person == "p":
            if machine > percent:
                print("상대: 가위")
                wl = 0
            elif machine <= percent:
                print("상대: 바위")
                wl = 1

        if wl == 1:
            print("\n이겼습니다!!\n")
            coin = coin + betting

        elif wl == 0:
            print("\n졌습니다..\n")
            coin = coin - betting

        time.sleep(1)
        os.system('cls')
        if coin == 0:
            print("파산하셨습니다...")
            ans = str(input("다시 하시겠습니까?(네 / 아니오): "))
            while (ans != "네" and ans != "Y" and ans != "YES" and ans != "yes" and ans != "아니오" and ans != "N" and ans != "NO" and ans != "no"):
                print("네 / 아니오 중에 하나만 입력하세요")
                ans = str(input("다시 하시겠습니까?(네 / 아니오): "))
            if ans == "네" or ans == "Y" or ans == "YES" or ans == "yes":
                game()
                return 0
            elif ans == "아니오" or ans == "N" or ans == "NO" or ans == "no":
                exit()

game()
