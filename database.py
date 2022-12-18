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
            #print(data,img_path)
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
            "profile_pic": 0, #일단은 이렇게 구현해 놓고 나중에 고치기...
            "nickname": 0,
            "img_path": "/static/img_user/review/"+img_path
        }
        self.db.child("review").push(review_info)
        return True
    
    ########################################
    #리뷰 조회화면, 메뉴 조회화면에서 리뷰와 메뉴를 추가하는 함수
    def add_menu(self, store_name, data, img_path): 
        print("메뉴 조회화면에서의 메뉴 추가 함수 실행")
        menu_info ={
            "store_name": store_name,
            "menu_name": data['txt_input_name'],
            "menu_price": data['txt_input_price'],
            "img_path": "/static/img_user/menu/"+img_path
        }
        if self.menu_duplicate_check(store_name, data['txt_input_name']):
            self.db.child("menu").push(menu_info)
            print("메뉴 등록 정상적으로 완료")
            return True
        else:
            return False
        
    def add_review(self, store_name, data, img_path, nickname, profile): 
        print("리뷰 조회화면에서의 리뷰 추가 함수 실행")
        review_info ={
            "store_name": store_name,
            "rating": data['rating'],
            "review_txt": data['input_review'],
            "like_num": 0,
            "profile_pic": profile, #고침
            "nickname": 0,
            "img_path": "/static/img_user/review/"+img_path,
            "reviewer_nickname": nickname
        }
        self.db.child("review").push(review_info)
        print("리뷰 등록 정상적으로 완료")
        return True
    
    #메뉴 등록 시 중복 체크하는 함수
    def menu_duplicate_check(self, store_name, menu_name):
        print("가게 이름과 메뉴명이 모두 일치하는지 중복 체크중...")
        menuList = self.db.child("menu").get()
        if menuList.each() is not None:
            for menu in menuList.each():
                value = menu.val()
                if value['menu_name'] == menu_name and value['store_name'] == store_name:
                    return False
            return True
        else:
            return True
        
    #레스토랑의 리뷰 수 업데이트 하는 함수
    def update_review_num(self, category, store_name):
        restaurants = self.db.child("restaurant").child(category).get()
        if restaurants.each() is not None:
            for res in restaurants.each():
                value = res.val()
                if value['store_name'] == store_name:
                    old_review_num = value['review_num']
                    update_review_num = old_review_num + 1 #더하기 1씩 하면 오류가 생길 수 있으므로, len으로 계산하여 업데이트하는 방식 나중에 구현하기...
                    keyValue = res.key()
                    self.db.child("restaurant").child(category).child(keyValue).update({"review_num": update_review_num})
                    print()
                    return True
            return False
        else:
            return False
    
    #각 리뷰의 like 수 +1 로 업데이트 하는 함수
    def update_review_like(self, store_key):
        reviews = self.db.child("review").get()
        if reviews.each() is not None:
            for review in reviews.each():
                value = review.val()
                if review.key() == store_key:
                    old_review_like = value['like_num']
                    update_review_like = old_review_like + 1 #더하기 1씩 하면 오류가 생길 수 있으므로, len으로 계산하여 업데이트하는 방식 나중에 구현하기...
                    keyValue = review.key()
                    self.db.child("review").child(keyValue).update({"like_num": update_review_like})
                    print()
                    return update_review_like
            return False
        else:
            return False
    
    #해당 사용자의 ID를 firebase에 업데이트함
    def update_like_table(self, review_key, _id):
        fake_info ={
        "fake_value": ""
        }
        self.db.child("review_like").child(review_key).child(_id).set(fake_info)
        print()
        return True
    
    def reset_like_table(self, review_key, _id):
        print("reset_like_table 함수 실행 시작")
        self.db.child("review_like").child(review_key).child(_id).remove()
        print("정상적으로 삭제되었습니다.")
        return True
    
    #각 리뷰의 like 수 -1로 업데이트 하는 함수
    def reset_review_like(self, store_key):
        reviews = self.db.child("review").get()
        if reviews.each() is not None:
            for review in reviews.each():
                value = review.val()
                if review.key() == store_key:
                    old_review_like = value['like_num']
                    update_review_like = old_review_like - 1 #더하기 1씩 하면 오류가 생길 수 있으므로, len으로 계산하여 업데이트하는 방식 나중에 구현하기...
                    keyValue = review.key()
                    if update_review_like >=0:
                        self.db.child("review").child(keyValue).update({"like_num": update_review_like})
                    else:
                        update_review_like = 0
                        self.db.child("review").child(keyValue).update({"like_num": update_review_like})
                    print()
                    return update_review_like
            return False
        else:
            return False
        
    #각 리뷰의 누른 like 수 체크하는 함수
    def check_review_like(self, store_key, _id):
        reviews = self.db.child("review_like").get()
        if reviews.each() is not None:
            for review in reviews.each():
                value = review.val()
                if review.key() == store_key:
                    for name in value:
                        print("#"*100)
                        print(name)
                        print("#"*100)
                        if name == _id:
                            print("#"*100)
                            print(name, _id)
                            print("#"*100)
                            return True
                    return False
        else:
            return False
            
    ########################################
    #로그인 정보를 DB와 비교하여 일치하는 id와 pw가 있는지 확인하는 함수
    def search_loginInfo(self, id_, pw_):
        users = self.db.child("users").get()
        if users.each() is not None:
            for user in users.each():
                value = user.val()
                if value['id'] == id_ and value['pw'] == pw_:
                    return value
            return False
        else:
            return False
    
    #회원가입 정보를 DB에 저장하는 코드
    def insert_user(self, data, pw):
        register_info = {
            "nickname": data['registerNickname'],
            "id": data['registerId'],
            "profile_pic": 0, #기본 프로필 사진의 값
            "pw": pw
        }
        if self.register_duplicate_check(str(data['registerId'])):
            self.db.child("users").push(register_info)
            #print(data)
            return True
        else:
            return False
    
    #회원가입 정보를 중복 체크하는 코드
    def register_duplicate_check(self, id_string):
        users = self.db.child("users").get()
        #print("users###", users.val())
        if str(users.val()) == "None": # first registration
            return True
        else:
            for res in users.each():
                value = res.val()
                if value['id'] == id_string:
                    return False
            return True
    
    ########################################
    #카테고리 리스트에 보여주기 위해 restaurant 테이블에서 데이터 가져오기
    def get_restaurants(self, category):
        restaurants = self.db.child("restaurant").child(category).get().val()
        #print(restaurants)
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
        #print(target_value)
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
                #print(rates)
        if len(rates) is 0:
            return 0
        else:
            return round((sum(rates)/len(rates)),1)
    
    ##########################################
    #메뉴 세부 화면에서 보여주기 위해 맛집 이름으로 menu 테이블에서 정보 가져오기
    def get_food_byname(self, name):
        restaurants = self.db.child("menu").get()
        target_value=[]
        for res in restaurants.each():
            value = res.val()
            if value['store_name'] == name:
                target_value.append(value)
        #print(target_value)
        return target_value
    
    ##########################################
    #리뷰 세부 화면에서 보여주기 위해 맛집 이름으로 review 테이블에서 정보 가져오기
    def get_review_byname(self, name):
        restaurants = self.db.child("review").get()
        target_value=[]
        for res in restaurants.each():
            value = res.val()
            if value['store_name'] == name:
                value['key'] = res.key()
                target_value.append(value)
        #print(target_value)
        return target_value
    
    ##########################################
    #프로필 사진 가져오는 함수
    def get_profile_pic(self, num):
        profile_info ={
            0: "/static/profile/profile_common.png",
            1: "/static/profile/profile_dog.png",
            2: "/static/profile/profile_duck.png",
            3: "/static/profile/profile_monkey.png",
            4: "/static/profile/profile_rabbit.png",
            5: "/static/profile/profile_squirrel.png",
            6: "/static/profile/profile_alien.png",
            7: "/static/profile/profile_cat.png"
        }
        return profile_info[num]
    
    #DB에서 유저의 프로필 사진을 수정하는 함수
    def update_user_profile(self, profile_num, _id):
        print(profile_num)
        users = self.db.child("users").get()
        if users.each() is not None:
            for user in users.each():
                value = user.val()
                if value['id'] == _id:
                    self.db.child("users").child(user.key()).update({"profile_pic": profile_num})
                    return True
            return False
        else:
            return False     
    
    ##########################################
    #마커 정보를 표현해주기 위해 레스토랑의 position을 전부 가져오는 함수
    def get_all_restaurants(self):
        restaurants = self.db.child("restaurant").get().val()
        storeList = []
        for value in restaurants.values():
            print(value)
            for val in value.values():
                storeList.append(val['position'])
        return storeList
    
    ##########################################
    #마커 정보를 표현해주기 위해 레스토랑의 이름을 전부 가져오는 함수
    def get_all_restaurants_name(self):
        restaurants = self.db.child("restaurant").get().val()
        storeList = []
        for value in restaurants.values():
            print(value)
            for val in value.values():
                storeList.append(val['store_name'])
        return storeList
    
    ##########################################
    #마커 정보를 표현해주기 위해 레스토랑의 주소를 전부 가져오는 함수
    def get_all_restaurants_addr(self):
        restaurants = self.db.child("restaurant").get().val()
        storeList = []
        for value in restaurants.values():
            print(value)
            for val in value.values():
                storeList.append(val['addr'])
        return storeList
    
    ##########################################
    #마커 정보를 표현해주기 위해 레스토랑의 주소를 전부 가져오는 함수
    def get_all_restaurants_tel(self):
        restaurants = self.db.child("restaurant").get().val()
        storeList = []
        for value in restaurants.values():
            print(value)
            for val in value.values():
                storeList.append(val['tel'])
        return storeList
    
    ##########################################
    #마커 이미지 변경에 사용될 리뷰수를 가져오는 함수
    def get_all_restaurants_review_num(self):
        restaurants = self.db.child("restaurant").get().val()
        storeList = []
        for value in restaurants.values():
            for val in value.values():
                storeList.append(val['review_num'])
        return storeList
    
    ##########################################
    #카테고리별 클릭을 통한 마커 표시에 사용될 카테고리를 가져오는 함수
    def get_all_restaurants_category(self):
        restaurants = self.db.child("restaurant").get().val()
        storeList = []
        for value in restaurants.values():
            for val in value.values():
                storeList.append(val['food_category'])
        return storeList
