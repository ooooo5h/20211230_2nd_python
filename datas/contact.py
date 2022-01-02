class Contact:
    
    def __init__(self):
        self.id = 0
        self.user_id = 0
        self.name = ''
        self.phone_num = ''
        self.memo = '' 
        
    # dict를 재료로 받아서, 객체 변수의 값들을 채워주는 기능
    def set_dat(self, info_dict):
        self.id = info_dict['id']
        self.user_id = info_dict['user_id']
        self.name = info_dict['name']
        self.phone_num = info_dict['phone_num']
        self.memo = info_dict['memo'] 
        
    # 연락처 상세보기 기능 추가
    def show_detail_info(self):
        print('===== 연락처 상세보기 =====')
        print(f'이름 : {self.name}')
        print(f'핸드폰 : {self.phone_num}')
        print(f'메모사항 : {self.memo}')
        print('==========================')
        print('1. 연락처 수정')
        print('2. 연락처 삭제')
        print('0. 이전 메뉴로')
        print('==========================')
        return int(input('추가 행동 선택 : '))
