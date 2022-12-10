'''
코드 작성 일자 : 2022-12-11
코드 작성자 : 윤동건
코드 이름 : utils.py
코드 목적 : 유용한 함수를 따로 저장하여 두고 나중에 불러와 사용하기 위함
'''


def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x-1)


def gugudan(x):
    for i in range(9):
        print((i+1) * x)

