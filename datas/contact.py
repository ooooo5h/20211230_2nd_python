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