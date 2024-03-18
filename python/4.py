"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():

    점수 = int(input())
    
    if 점수<=100 and 점수>=90:
        print('A')
    elif 점수 >=80:
        print('B')
    elif 점수 >=70:
        print('C')
    elif 점수 >=60:
        print('D')
    elif 점수 <60  and 점수 >=0:
        print('F')

    return


if __name__ == '__main__':
    main()
