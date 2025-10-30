for i in range(1,101):
    if i % 2 == 0 and i % 5 == 0:
        print("2,5의 배수입니다")
    elif i % 2 == 0:
        print("2의 배수입니다")
    elif i % 5 == 0:
        print("5의 배수입니다")
    else:
        print(i)
# 1에서 100까지의 숫자 중 2나 5의 배수 찾기