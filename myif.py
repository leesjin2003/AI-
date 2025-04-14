# 아스키 코드 그림 출력 하기

# 만약에 1을 입력하면 1번 캐릭터 출력
# 만약에 2를 입력하면 2번 캐릭터 출력
# 3을 입력하면 3번 캐릭터 출력
# 잘못 입력하면 잘못 입력했다고 출력

# 아스키 아트 캐릭터 정의
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

def show_ascii_art(choice):
    if choice == "1":
        print(ascii_art_1)
    elif choice == "2":
        print(ascii_art_2)
    elif choice == "3":
        print(ascii_art_3)
    else:
        print("잘못된 선택입니다.")

def select_character_loop(max_count=None):
    count = 0
    while True:
        if max_count is not None and count >= max_count:
            print(f"{max_count}번의 선택이 끝났습니다. 프로그램을 종료합니다.")
            break

        if max_count is not None:
            print(f"\n({count + 1}/{max_count}) 원하는 캐릭터를 선택하세요:")
        else:
            print("\n원하는 캐릭터를 선택하세요:")

        print("1. 사람")
        print("2. 로봇")
        print("3. 고양이")
        print("0. 종료")
        choice = input("입력: ")

        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            show_ascii_art(choice)
            if max_count is not None:
                count += 1

def main():
    print("모드를 선택하세요:")
    print("1. 5번 선택 모드")
    print("2. 무한 선택 모드 (0을 입력하면 종료)")
    mode = input("입력: ")

    if mode == "1":
        select_character_loop(max_count=5)
    elif mode == "2":
        select_character_loop()
    else:
        print("잘못된 입력입니다. 프로그램을 종료합니다.")

if __name__ == "__main__":
    main()


