# 아스카 코드 그림 출력 하기

def print_cat():
    cat = """
        ╱|、
       (˚ˎ 。7  
        |、˜〵  
       じしˍ,)ノ
    """
    print(cat)

def print_dog():
    dog = """
        ．．．．．/)─―ヘ
  　　　━／　　　　＼
  　 ／　　　　●　　●丶
  　｜　　　　　　　▼　| (침묵)
  　｜　　　　　　　亠ノ 　
  　 U￣U￣￣￣U￣￣U
    """
    print(dog)

def print_rabbit():
    rabbit = """
        ⢀⣀⡀
        ⢠⠏⠀⢸⠀⠀⡴⠒⣆
        ⢸⡀⠀⢸⡆⡼⠁⠀⡇
      ⣠⠃⠀⠀⠉⠉ ⠁     ⢸
      ⢠⠇⠀⠀⠀⠀⠀⠀    ⠈⡇
      ⠘⣆ o̴̶̷᷄      ·̭     o̴̶̷̥᷅⠀⣰⠃
      ⠈⠙⠒⠲⠶⠒⠚⠋⠁
    """
    print(rabbit)

# 프로그램 시작
print("그림 출력 프로그램")
print("=================")
print("1. 고양이")
print("2. 강아지")
print("3. 토끼")
print("=================")

# 사용자 입력 받기
n = int(input("선택: "))

# 입력값에 따라 출력
if n == 1:
    print("고양이")
    print_cat()
elif n == 2:
    print("강아지")
    print_dog()
elif n == 3:
    print("토끼")
    print_rabbit()
else:
    print("잘못 입력하셨습니다!")


    for i in range(5):
    print(f"\n[{i+1}/5] 숫자를 입력하세요 (1~3):")
    choice = input("입력: ")

    if choice == "1":
        print(ascii_art_1)
    elif choice == "2":
        print(ascii_art_2)
    elif choice == "3":
        print(ascii_art_3)
    else:
        print("잘못 입력하셨습니다!")
#0이 입력되면 프로그램 종료



# 동물 그림 출력 프로그램이 총 5번 반복 실행될 수 있게 만드시오.

# 위 프로그램을 완성한 사람은 프로그램이 계속(무한) 반복하게 하고
# 만약에 0을 입력하면 종료 되는 프로그램을 만드시오.
