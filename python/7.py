"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!

    연도 = int(input())
    월 = int(input())

    판별=0
    if 월 in [4,6,9,11]:
        print('30')
        판별=1
       

    if 판별==0:
        if 월==2:
            판별=1
            if (연도%4==0 and 연도%100!=0 and 연도%400==0) or 연도%4==0:
                print('29')
            else:
                print('28')
            
    if 판별==0:
        print('31')
        

        
        


    
    return


if __name__ == '__main__':
    main()
