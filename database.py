import pyrebase

config = { "apiKey": "AIzaSyDu-C3mhLuthS--Opm5buewNjqJ_P6B834", 
          "authDomain": "ettopia-db.firebaseapp.com",
          "databaseURL": "https://ettopia-db-default-rtdb.firebaseio.com/",
          "storageBucket": "ettopia-db.appspot.com" }

          
import json

class DBhandler:
    def __init__(self):
        with open('./authentication/firebase_auth.json') as f:
            config=json.load(f)
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()
        
    def insert_restaurant(self, name, data, img_path):  # 중복확인이 필요한 키값들을 받는 부분에 들어갈 함수 추가 (테이블 이름 == class 이름)
        restaurant_info ={
            "store_name": data['store_name'],
            "addr": data['store_address'],
            "tel": data['store_tel'],
            "food_category": data['btn_food_hidden'],
            "min_price": data['value_min_price'],
            "max_price": data['value_max_price'],
            "park": data['btn_park_hidden'],
            "site": data['txt_input_site'],
        }
        if self.restaurant_duplicate_check(name):
            self.db.child("restaurant").child(name).set(restaurant_info)
            print(data,img_path)
            return True
        else:
            return False
        
    def restaurant_duplicate_check(self, name):
        restaurants = self.db.child("restaurant").get()
        for res in restaurants.each():
            if res.key() == name:
                return False
        return True
    
    ########################################
    #맛집 등록시 메뉴 등록과 리뷰 등록을 하는 경우
    def insert_menu_temp(self, name, data, img_path): 
        menu_info ={
            "store_name": data['store_name'],
            "menu_name": data['txt_input_name'],
            "menu_price": data['txt_input_price'],
        }
        self.db.child("menu").child(name).set(menu_info)
        return True
    
    def insert_review_temp(self, name, data, img_path): 
        review_info ={
            "store_name": data['store_name'],
            "rating": data['rating'],
            "review_txt": data['input_review'],
        }
        self.db.child("review").child(name).set(review_info)
        return True
    
    # register_menu의 DB연결
    def insert_menu(self, name, data):
        menu_info={
            "name": data['name'],
            "price": data['price'],
            #vegi 내용 받아오는 코드 필요
            "allergy": data['allergy'],
            # 메뉴 이미지 받아오기
        }
        self.db.child("restaurant").child(name).set(menu_info)
        print(data)
        return True
    
    def menu_duplicate_check(self, name):
        menuList = self.db.child("restaurant").get()
        for res in menuList.each():
            if res.key() == name:
                return False
        return True
    
    #register_review의 DB연결
    def insert_review(self, name, data):
        review_info={
            "review": data['review'],
            
            #vegi 내용 받아오는 코드 필요
            # 메뉴 이미지 받아오기
        }
        self.db.child("restaurant").child(menu).set(menu_info)
        print(data)
        return True
    
    #로그인 정보를 DB에 저장하는 코드-아직 ID만 체그, PW는 체크 못함
    def search_loginInfo(self, idCheck, pwCheck):
        users = self.db.child("users").get()
        for user in users.each():
            print(user.val())
            if user.key() == idCheck and user.val() == pwCheck:
                print(db.reference('users').child('idCheck').child('registerPassword'))
                return True
        return False
    
    #회원가입 정보를 DB에 저장하는 코드
    def insert_registerInfo(self, name, data):
        register_info = {
            "registerNickname": data['registerNickname'],
            "registerId": data['registerId'],
            "registerPassword": data['registerPassword']
        }
        if self.register_duplicate_check(name):
            self.db.child("users").child(name).set(register_info)
            print(data)
            return True
        else:
            return False
    
    def register_duplicate_check(self, name):
        registers = self.db.child("users").get()
        for regi in registers.each():
            if regi.key() == name:
                return False
        return True
    