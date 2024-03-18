"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    정수 = int(input())
    
    백,십 = divmod(정수,100)
    십,일 = divmod( 십,10)
    print(일,십,백,sep='')
    return


if __name__ == '__main__':
    main()
