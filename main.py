from phone_book import print_main_menu, sign_up

while True:
    menu_num = print_main_menu()
    
    if menu_num == 1:       
        # 1번 : 로그인
        pass
    
    elif menu_num == 2:        
        # 2번 : 회원가입
        sign_up()
              
    elif menu_num == 0:
        print('프로그램을 종료합니다.')
        break