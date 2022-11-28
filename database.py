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
        
    def insert_restaurant(self, name, data, img_path, review_num):  # 중복확인이 필요한 키값들을 받는 부분에 들어갈 함수 추가 (테이블 이름 == class 이름)
        restaurant_info ={
            "store_name": data['store_name'],
            "addr": data['store_address'],
            "tel": data['store_tel'],
            "food_category": data['btn_food_hidden'],
            "min_price": data['value_min_price'],
            "max_price": data['value_max_price'],
            "park": data['btn_park_hidden'],
            "hour_open": data['value_open_hour'],
            "hour_close": data['value_close_hour'],
            "site": data['txt_input_site'],
            "img_path": "/static/img_user/store/"+img_path,
            "review_num": review_num,
            "position": data['store_position']
        }
        if self.restaurant_duplicate_check(name, data):
            self.db.child("restaurant").child(data['btn_food_hidden']).push(restaurant_info)
            print(data,img_path)
            return True
        else:
            return False
        
    def restaurant_duplicate_check(self, name, data):
        restaurants = self.db.child("restaurant").child(data['btn_food_hidden']).get()
        print("가게 이름 중복 체크중...")
        #아예 카데고리 자체가 존재하지 않는 경우, 중복 체크가 불가능함.
        #따라서 DB 검색 결과를 NoneType 체크->NoneType이라면 그냥 바로 DB에 저장, 아니라면 중복 체크
        if restaurants.each() is not None:
            for res in restaurants.each():
                value = res.val()
                if value['store_name'] == name:
                    return False
            return True
        else:
            return True
    
    ########################################
    #맛집 등록시 메뉴 등록과 리뷰 등록을 하는 경우
    def insert_menu(self, name, data, img_path): 
        menu_info ={
            "store_name": data['store_name'],
            "menu_name": data['txt_input_name'],
            "menu_price": data['txt_input_price'],
            "img_path": "/static/img_user/menu/"+img_path
        }
        self.db.child("menu").push(menu_info)
        return True
    
    def insert_review(self, name, data, img_path): 
        review_info ={
            "store_name": data['store_name'],
            "rating": data['rating'],
            "review_txt": data['input_review'],
            "like_num": 0,
            "img_path": "/static/img_user/review/"+img_path
        }
        self.db.child("review").push(review_info)
        return True
    
    ########################################
    #리뷰 조회화면, 메뉴 조회화면에서 리뷰와 메뉴를 추가하는 함수
    #미구현- 메뉴를 중복확인하는 함수
    def menu_duplicate_check(self, name):
        menuList = self.db.child("restaurant").get()
        for res in menuList.each():
            if res.key() == name:
                return False
        return True
    
    ########################################
    #로그인 정보를 DB에 저장하는 코드-아직 ID만 체그, PW는 체크 못함
    def search_loginInfo(self, idCheck, pwCheck):
        users = self.db.child("users").get()
        if users.each() is not None:
            for user in users.each():
                print(user.val())
                if user.key() == idCheck and user.val() == pwCheck:
                    print(self.db.reference('users').child('idCheck').child('registerPassword'))
                    return True
            return False
        else:
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
    
    #회원가입 정보를 중복 체그하는 코드
    def register_duplicate_check(self, name):
        registers = self.db.child("users").get()
        if registers.each() is not None:
            for regi in registers.each():
                if regi.key() == name:
                    return False
            return True
        else:
            return True
    
    ########################################
    #카테고리 리스트에 보여주기 위해 restaurant 테이블에서 데이터 가져오기
    def get_restaurants(self, category):
        restaurants = self.db.child("restaurant").child(category).get().val()
        print(restaurants)
        return restaurants
    
    def restaurants_desc(self, category):
        desc_info ={
            "한식": "든든하게 먹는 한 끼 식사",
            "양식": "분위기 좋은 곳에서 식사하기",
            "중식": "오늘 저녁은 마라탕 어때요?",
            "일식": "아기자기한 한 그릇 식사하기",
            "태국": "쌀국수 한 그릇 어때요?",
            "인도": "이국적인 음식을 먹고 싶을 때",
            "음료&카페": "카공도 하고 맛있는 것도 먹고",
            "디저트": "공부하느라 떨어진 당 충전!",
            "분식": "떡볶이는 영혼의 음식",
            "페스트푸드": "수업 가기 전 빠르게 먹는 음식",
            "샐러드&샌드위치": "가볍게 한 끼 대용",
            "야식": "맛있으면 0 칼로리!"
        }
        return desc_info[category]
    
    ##########################################
    #가게 세부 화면에서 보여주기 위해 맛집 이름으로 restaurant 테이블에서 정보 가져오기
    def get_restaurant_byname(self, category, name):
        restaurants = self.db.child("restaurant").child(category).get()
        target_value=""
        for res in restaurants.each():
            value = res.val()
            if value['store_name'] == name:
                target_value = value
        print(target_value)
        return target_value
        
    # 맛집 이름으로 review 테이블에서 평점 불러와 평균 계산하기
    def get_avgrate_byname(self, name):
        print("평균함수 실행됨")
        reviews = self.db.child("review").get()
        rates = []
        for res in reviews.each():
            value = res.val()
            if value['store_name'] == name:
                rates.append(float(value['rating']))
                print(rates)
        if len(rates) is 0:
            return 0
        else:
            return sum(rates)/len(rates)
    
    ##########################################
    #메뉴 세부 화면에서 보여주기 위해 맛집 이름으로 menu 테이블에서 정보 가져오기
    def get_food_byname(self, name):
        restaurants = self.db.child("menu").get()
        target_value=[]
        for res in restaurants.each():
            value = res.val()
            if value['store_name'] == name:
                target_value.append(value)
        print(target_value)
        return target_value
    
    ##########################################
    #리뷰 세부 화면에서 보여주기 위해 맛집 이름으로 review 테이블에서 정보 가져오기
    def get_review_byname(self, name):
        restaurants = self.db.child("review").get()
        target_value=[]
        for res in restaurants.each():
            value = res.val()
            if value['store_name'] == name:
                target_value.append(value)
        print(target_value)
        return target_value
    