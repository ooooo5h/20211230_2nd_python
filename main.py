from phone_book import add_phone_num, print_main_menu, search_my_contact_list, sign_up, sign_in, print_phone_book_menu, show_all_contacts
from time import sleep

while True:
    menu_num = print_main_menu()
    
    if menu_num == 1:       
        # 1번 : 로그인
        login_result = sign_in()
        # 로그인 성공하면, 개인별 연락처 메뉴로 이동
        if login_result:
            while True:
                num = print_phone_book_menu()
                if num == 0:
                    print('로그아웃 후 메인으로 돌아갑니다.')
                    sleep(2)
                    break
                elif num == 1:
                    add_phone_num()
                elif num == 2:
                    show_all_contacts()
                elif num == 3:
                    search_my_contact_list()
        
    elif menu_num == 2:        
        # 2번 : 회원가입
        sign_up()
              
    elif menu_num == 0:
        print('프로그램을 종료합니다.')
        break