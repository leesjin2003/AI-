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
