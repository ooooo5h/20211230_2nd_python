import pymysql
from time import sleep

db_connect = pymysql.connect(
    host='finalproject.cbqjwimiu76h.ap-northeast-2.rds.amazonaws.com',
    port=3306,
    user='admin',
    passwd='Vmfhwprxm!123',
    db='test_phone_book',
    charset='utf8')

cursor = db_connect.cursor()


# 메인화면 보여주는 함수
def print_main_menu():
    print('===== 전화번호부 =====')
    print('1. 로그인')
    print('2. 회원가입')
    print('0. 프로그램 종료')
    print('=====================')
    menu_num = int(input('메뉴 선택 : '))
    return menu_num


# 회원가입 실행 함수
def sign_up():
    
    input_email = input('이메일 : ')
    input_passwd = input('비밀번호 : ')
    input_nickname = input('닉네임 : ')
    
    sql = f"""
    INSERT INTO users (users.email, users.password, users.nickname) 
    VALUES ('{input_email}', '{input_passwd}', '{input_nickname}' ) """
    
    cursor.execute(sql)
    db_connect.commit()
    
    print(f'{input_nickname}님 환영합니다. 회원가입이 완료되었습니다.')
    sleep(2)


# 로그인 함수
def sign_in():
    
    login_email = input('이메일 : ')
    login_passwd = input('비밀번호 : ')
    
    sql = f"SELECT * FROM users WHERE users.email = '{login_email}' AND users.password = '{login_passwd}'"
    
    cursor.execute(sql)
    user_list = cursor.fetchall()
 
    if len(user_list) > 0:
        
        login_user = user_list[0]
        user_nickname = login_user[3]
        
        print(f'{user_nickname}님 환영합니다!')
        sleep(2)
        
        return True
    else:
        
        print('없는 정보입니다. 다시 확인해주세요.')
        sleep(2)
        
        return False