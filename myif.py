# 아스키 코드 그림 출력 하기

# 만약에 1을 입력하면 1번 캐릭터 출력
# 만약에 2를 입력하면 2번 캐릭터 출력
# 3을 입력하면 3번 캐릭터 출력
# 잘못 입력하면 잘못 입력했다고 출력

# 아스키 아트 캐릭터 정의
ascii_art_1 = """
  (•_•)
  <)   )╯
   /   \\
"""
ascii_art_2 = """
  ( •_•)
  ( (  > 
   \\  ) 
"""
ascii_art_3 = """
  (⌐■_■)
  ( •_•)>⌐■-■
"""

# 사용자 입력 받기
choice = input("숫자를 입력하세요 (1~3): ")

# 입력값에 따라 출력
if choice == "1":
    print(ascii_art_1)
elif choice == "2":
    print(ascii_art_2)
elif choice == "3":
    print(ascii_art_3)
else:
    print("잘못 입력하셨습니다!")
