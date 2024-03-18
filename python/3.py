"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    
    시간 = int(input())
    
    if 시간<12 and 시간>=0:
        print('AM')
    elif 시간<=23 and 시간>=12:
        print('PM')

    return


if __name__ == '__main__':
    main()
