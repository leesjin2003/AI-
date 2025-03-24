num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} × {num2} = {num1 * num2}")

# 0으로 나누는 경우를 방지하기 위한 조건 추가!
if num2 != 0:
    print(f"{num1} ÷ {num2} = {num1 / num2}")
else:
    print("0으로 나눌 수 없습니다!")
