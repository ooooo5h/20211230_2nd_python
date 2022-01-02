import pymysql
from time import sleep
from pymysql.cursors import DictCursor
from datas import Contact

db_connect = pymysql.connect(
    host='finalproject.cbqjwimiu76h.ap-northeast-2.rds.amazonaws.com',
    port=3306,
    user='admin',
    passwd='Vmfhwprxm!123',
    db='test_phone_book',
    charset='utf8',
    cursorclass= DictCursor)

cursor = db_connect.cursor()

login_user_id = 0

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
        user_nickname = login_user['nickname']
        
        global login_user_id
        login_user_id = login_user['id']
        
        print(f'{user_nickname}님 환영합니다!')
        sleep(2)
        
        return True
    else:
        
        print('없는 정보입니다. 다시 확인해주세요.')
        sleep(2)
        
        return False
    

# 로그인 이후, 메뉴창
def print_phone_book_menu():
    print('===== 메인 메뉴 =====')
    print('1. 전화번호 추가 등록')
    print('2. 전화번호 목록 조회')
    print('3. 내 전화번호부 검색')
    print('0. 로그아웃')
    print('====================')
    num = int(input('메뉴 선택 : '))
    return num

# 전화번호 추가 등록
def add_phone_num():
    
    input_name = input('이름 : ')
    input_phone = input('연락처 : ')
    input_memo = input('특이사항 : ')
    
    sql = f"""
    INSERT INTO contacts (contacts.name, contacts.phone_num, contacts.memo, contacts.user_id) 
    VALUES ('{input_name}','{input_phone}','{input_memo}', {login_user_id})"""
    
    cursor.execute(sql)
    db_connect.commit()
    
    print('연락처 등록이 완료되었습니다.')
    sleep(2)
    
# 로그인한 사용자가 등록한 모든 연락처 출력
def show_all_contacts():
    
    sql = f"SELECT * FROM contacts WHERE contacts.user_id = {login_user_id}"
    cursor.execute(sql)
    contact_list = cursor.fetchall()
    
    for contact in contact_list:
        
        name = contact['name']
        phone_num = contact['phone_num']
        memo = contact['memo']
        result = f"{name}({memo}) : {phone_num}"
        print(result)
        
    sleep(2)
    
    
# 전화번호부에서 이름 기준으로 검색
def search_my_contact_list():
    
    input_keyword = input('검색할 이름의 일부를 입력하세요 : ')
    
    sql = f"""
    SELECT * FROM contacts 
    WHERE contacts.user_id = {login_user_id} AND 
    contacts.name LIKE '%{input_keyword}%'"""
    
    cursor.execute(sql)
    result = cursor.fetchall()
    
    if len(result) == 0:
        print('검색 결과가 없습니다.')
        sleep(1)
    else:             
        print('===== 검색 결과 =====')
        # 검색 결과를 확인하자
        for idx, row in enumerate(result):
            
            line = f"{idx+1}. {row['name']} ({row['memo']})"
            print(line)
                      
        contact_num = int(input('상세 보기 연락처 선택 : '))
        
        # contact_num에 맞는 line을 가지고(dict), Contact 형태의 객체로 변환하자(클래스 활용)
        contact = Contact()
        
        # 위치에 맞는 dict를 꺼내와서 contact객체의 내용물 변수들을 채우자
        select_line = result[contact_num-1]
        
        # 이렇게 모든 걸 셋팅하기 너무 귀찮아! 클래스의 기능으로 추가해주자(메쏘드)
        # contact.id = select_line['id']
        contact.set_dat(select_line)
        
        # 연락처의 상세 정보를 표시하자(역시 메쏘드로)
        detail_num = contact.show_detail_info()
        
        if detail_num == 1:
            update_contact()
            
        elif detail_num == 2:
            delete_contact()
        
           
    # 연락처 수정
    def update_contact():
        pass
     
    # 연락처 삭제
    def delete_contact():
        pass