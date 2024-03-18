"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    
    알파벳 = input()
    모음 = ['a','e','i','o','u']
    
    판별 = 0

    for i in 모음:
        if 알파벳==i:
            print('O')
            판별=판별+1
    
    if 판별 == 0:
        print('X')

    
            

    return


if __name__ == '__main__':
    main()

