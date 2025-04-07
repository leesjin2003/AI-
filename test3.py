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

for i in range(5):
    print("\n동물 그림 출력 프로그램")
    print("=================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토끼")
    print("=================")
    choice = input(f"[{i+1}/5] 선택 (1~3): ")

    if choice == "1":
        print("고양이")
        print_cat()
    elif choice == "2":
        print("강아지")
        print_dog()
    elif choice == "3":
        print("토끼")
        print_rabbit()
    else:
        print("잘못 입력하셨습니다!")
