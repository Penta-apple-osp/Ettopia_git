from flask import Flask, render_template, request, url_for, flash, redirect, session, jsonify
from database import DBhandler
import hashlib
import sys
application = Flask(__name__)
application.config["SECRET_KEY"] = "anything-you-want"
DB = DBhandler()

#######################################################################
#화면 사이의 연결을 위한 코드
@application.route("/")
def hello():
    data=DB.get_all_restaurants()
    data_review_num=DB.get_all_restaurants_review_num()
    data_category=DB.get_all_restaurants_category()
    data_name=DB.get_all_restaurants_name()
    data_addr=DB.get_all_restaurants_addr()
    data_tel=DB.get_all_restaurants_tel()
    tot_store = len(data)
    return render_template("homePage.html", datas=data, tot_store=tot_store, datas_review_num=data_review_num, 
                           datas_category=data_category, datas_name=data_name, datas_addr=data_addr, datas_tel=data_tel)

@application.route("/aboutUs")
def view_about_us():
    return render_template("aboutUs.html")

@application.route("/homePage")
def view_home_page():
    data=DB.get_all_restaurants()
    data_review_num=DB.get_all_restaurants_review_num()
    data_category=DB.get_all_restaurants_category()
    data_name=DB.get_all_restaurants_name()
    data_addr=DB.get_all_restaurants_addr()
    data_tel=DB.get_all_restaurants_tel()
    tot_store = len(data)
    return render_template("homePage.html", datas=data, tot_store=tot_store, datas_review_num=data_review_num, 
                           datas_category=data_category, datas_name=data_name, datas_addr=data_addr, datas_tel=data_tel)

@application.route("/loginRegister")
def view_login_register():
    return render_template("loginRegister.html")

@application.route("/menuRegister", methods=['POST'])
def reg_menu():
    data=request.form
    print(data)
    return render_template("menuRegister.html", data=data)

@application.route("/reviewRegister", methods=['POST'])
def reg_review():
    data=request.form
    print(data)
    return render_template("reviewRegister.html", data=data)

@application.route("/myPage")
def view_my_page():
    return render_template("myPage.html")

@application.route("/storeRegister", methods=['POST']) #맛집 등록 화면으로 이동하는 함수-마커 클릭시 정보 받아와야 하기 때문에 POST 형식
def view_store_register():
    data=request.form
    print(data)
    return render_template("storeRegister.html", data=data)

# 사용자의 프로필 이미지 변경하는 함수
@application.route("/modifyProfile", methods=['POST'])
def modify_profile():
    data=request.form  
    DB.update_user_profile(int(data['profile_change']), session['id'])
    session['profile_pic']=DB.get_profile_pic(int(data['profile_change']))
    session['profile_num']=int(data['profile_change'])
    return redirect(url_for('view_my_page'))

########################################################################
#카테고리마커 테스트 코드

@application.route("/categoryMarkertest")
def view_categoryMarkertest():
    data=DB.get_all_restaurants()
    tot_store = len(data)
    return render_template("categoryMarkertest.html", datas=data, tot_store=tot_store)

#######################################################################
#회원가입 폼 제출을 위한 코드
@application.route("/submit_register_post", methods=['POST'])
def submit_register():
    data=request.form
    print(data)
    pw=request.form['registerPassword']
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    if DB.insert_user(data, pw_hash):
        return redirect(url_for('view_home_page'))
    else:
        flash("이미 존재하는 ID 입니다. 다른 ID를 만들어주세요!")
        return render_template("loginRegister.html")

#로그인 폼 제출을 위한 코드
@application.route("/submit_login_post", methods=['POST'])
def submit_login():
    id_=request.form['loginId']
    pw=request.form['loginPassword']
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    data=DB.search_loginInfo(id_, pw_hash)
    if data:
        print(id_)
        print(data['profile_pic'])
        session['id']=id_
        session['profile_pic']=DB.get_profile_pic(data['profile_pic'])
        session['profile_num']=data['profile_pic']
        session['nickname']=data['nickname']
        return redirect(url_for('view_home_page'))
    else:
        flash("존재하지 않는 ID 또는 비밀번호입니다.")
        return render_template("loginRegister.html")
    
#######################################################################
#로그아웃하는 기능-로그아웃시 홈페이지로 이동
@application.route("/logout")
def logout_user():
    session.clear()
    return redirect(url_for('view_home_page'))

#######################################################################
#가게의 이미지와 등록 정보를 제출하기 위한 코드
@application.route("/submit_store_info", methods=['POST', 'GET'])
def submit_store_info():
    data=request.form
    print("가게 등록 함수 실행 여부")
    review_num=0
    #메뉴명이 존재하면 메뉴 정보 DB에 저장하는 함수 호출
    if  data['txt_input_name'] != "":
        menu_image_file=request.files["chooseMenuFile"]
        menu_image_file.save("static/img_user/menu/{}".format(menu_image_file.filename))
        DB.insert_menu(data['store_name'], data, menu_image_file.filename)
    #리뷰 사진이 존재하면 리뷰 정보 DB에 저장하는 함수 호출
    if data['input_review'] != "":
        review_num=1
        review_image_file=request.files["chooseReviewFile"]
        review_image_file.save("static/img_user/review/{}".format(review_image_file.filename))
        DB.insert_review(data['store_name'], data, review_image_file.filename)
    #맛집과 관련한 정보를 DB에 저장하는 함수 호출
    store_image_file=request.files["chooseFile"]
    store_image_file.save("static/img_user/store/{}".format(store_image_file.filename))
    if DB.insert_restaurant(data['store_name'], data, store_image_file.filename, review_num):
        return redirect(url_for('view_restaurant_detail', category=data['btn_food_hidden'], store_name=data['store_name']))
    else:
        flash("이미 등록되어 있는 레스토랑입니다.")
        return redirect(url_for('view_home_page'))

#######################################################################
#메뉴 조회 화면에서 메뉴 추가하는 함수
@application.route("/register_menu/<category>/<store_name>/", methods=['POST', 'GET'])
def submit_menu(category, store_name):
    data=request.form
    print(data)
    print(category)
    menu_image_file=request.files["chooseMenuFile"]
    menu_image_file.save("static/img_user/menu/{}".format(menu_image_file.filename))
    if DB.add_menu(store_name, data, menu_image_file.filename):
        return redirect(url_for('view_foods', category=category, store_name=store_name))
    else:
        flash("이미 존재하는 메뉴입니다.")
        return redirect(url_for('view_foods', category=category, store_name=store_name))
    
#리뷰 조회 화면에서 리뷰 추가하는 함수
@application.route("/register_review/<category>/<store_name>/", methods=['POST', 'GET'])
def submit_review(category, store_name):
    data=request.form
    review_num=1
    review_image_file=request.files["chooseReviewFile"]
    review_image_file.save("static/img_user/review/{}".format(review_image_file.filename))
    DB.add_review(store_name, data, review_image_file.filename, session['nickname'], session['profile_num']) #닉네임과 프로필 사진도 리뷰에 같이 올려주기 
    DB.update_review_num(category, store_name) #해당 가게의 리뷰 수 +1
    return redirect(url_for('view_reviews', category=category, store_name=store_name))

#######################################################################
#각 카테고리당 카테고리 리스트 동적 라우팅 코드 --> 카테고리 리스트에서 맛집 정보 가져오는 함수
@application.route("/categoryList", methods=['POST'])
def list_restaurants():
    formdata=request.form #카테고리와 페이지를 알려줌
    print(formdata)
    page = int(formdata['page'])
    category = formdata['value_category']
    limit = 6
    start_idx=limit*page
    end_idx=limit*(page+1)
    desc = DB.restaurants_desc(category) #read the table
    avgs = []
    data = DB.get_restaurants(category) #read the table
    for value in data.values():
        print(value)
        avg = DB.get_avgrate_byname(value['store_name'])
        value['store_avg'] = round(avg, 1)
    print(data)
    tot_count = len(data)
    data = dict(list(data.items())[start_idx:end_idx])
    #총 데이터 리스트, 전체 데이터 길이(가게 수), 한 페이지에 보여줄 가게 수, 현재 페이지 넘버, 전체 페이지 수
    return render_template("categoryList.html", datas=data.items(), total=tot_count, limit=limit, 
                           page=page, page_count=int((tot_count/7)+1), category=category, desc=desc)

#######################################################################
# 각 맛집당 맛집 세부화면 동적 라우팅 코드 --> 특정 식당 리스트 클릭시 해당 식당의 정보 중 식당 이름을 받아 연결
@application.route("/storeDetail/<category>/<store_name>/")
def view_restaurant_detail(category, store_name):
    data = DB.get_restaurant_byname(str(category), str(store_name))   # 맛집이름으로 데이터를 가져오는 함수
    avg_rate = DB.get_avgrate_byname(str(store_name))  # 맛집이름으로 평균평점을 가져오는 함수
    menuData = DB.get_food_byname(str(store_name))
    reviewData = DB.get_review_byname(str(store_name))
    menu_tot_count = len(menuData)
    review_tot_count = len(reviewData)
    if review_tot_count >= 4:
        reviewRange=range(4)
    else:
        reviewRange=range(review_tot_count)
    #print(data)
    return render_template("storeDetail.html", data=data, avg_rate=avg_rate, menuData=menuData, reviewData=reviewData, 
                           menu_total=menu_tot_count, review_total=review_tot_count, menuRange=range(menu_tot_count),
                           menuLeft=range(4-menu_tot_count), reviewRange=reviewRange, category=category, store_name=store_name)

# 각 맛집당 메뉴 세부화면 동적 라우팅 코드 --> 맛집 세부화면에서 메뉴 더보기 클릭시 메뉴 세부 화면으로 이동
@application.route("/menuList/<category>/<store_name>/")
def view_foods(category, store_name):
    storeData = DB.get_restaurant_byname(str(category), str(store_name))
    data = DB.get_food_byname(str(store_name))
    tot_count = len(data)
    page_count = len(data)
    #print(data)
    row = int(tot_count/4)
    left = int(tot_count%4)
    #print(row)
    return render_template("menuList.html", datas=list(data), total=tot_count, row=range(row), row2=range(4), 
                           left=range(left), left2=range(4-left), storeData=storeData, store_name=store_name, category=category)

# 각 맛집당 리뷰 세부화면 동적 라우팅 코드 --> 맛집 세부화면에서 리뷰 더보기 클릭시 리뷰 세부 화면으로 이동
@application.route("/reviewList/<category>/<store_name>/")
def view_reviews(category, store_name):
    data = DB.get_review_byname(str(store_name))
    for review in data:
        print(review)
        review['profile_pic'] = DB.get_profile_pic(review['profile_pic'])
    tot_count = len(data)
    page_count = len(data)
    print(data)
    print(tot_count)
    return render_template("reviewList.html", datas=data, total=tot_count, store_name=store_name, category=category)

#######################################################################
# Like를 누를 시 DB에 사용자 정보를 저장하는 코드
@application.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if 'id' not in session:
        return jsonify({ 'result' : "notauser", 'elementId' : data['elementId']})
    else:
        print(f"add 함수 실행 결과: {data['reviewKey']}")
        like_num = DB.update_review_like(data['reviewKey'])
        DB.update_like_table(data['reviewKey'], session['id'])
        return jsonify({ 'result' : "success", 'elementId' : data['elementId'], 'like_num' : like_num})

#######################################################################
@application.route('/checkLike', methods=['POST'])
def checkLike():
    data = request.get_json()
    print(f"checkLike 함수 실행 결과: {data['reviewKey']}")
    #유저가 로그인 되어 있는 상황에서만 되어야 함
    if 'id' not in session:
        return jsonify({ 'result' : "error", 'elementId' : data['elementId']})
    else:
        likeResult = DB.check_review_like(data['reviewKey'], session['id'])
        print(f"checkLike 함수 결과 반환: {likeResult}")
        if likeResult == True:
            return jsonify({ 'result' : "success", 'elementId' : data['elementId'], 'like_result' : likeResult})
        elif likeResult == False:
            return jsonify({ 'result' : "error", 'elementId' : data['elementId'], 'like_result' : likeResult})
        else:  # None일때
            return jsonify({ 'result' : "none", 'elementId' : data['elementId'], 'like_result' : likeResult})

#######################################################################
# Like 취소 시 DB에 저장되어 있던 사용자 정보를 삭제하는 코드
@application.route('/sub', methods=['POST'])
def sub():
    data = request.get_json()
    print(f"sub 함수 실행 결과: {data['reviewKey']}")
    if 'id' not in session:
        return jsonify({ 'result' : "notauser", 'elementId' : data['elementId']})
    else:
        like_num = DB.reset_review_like(data['reviewKey'])
        DB.reset_like_table(data['reviewKey'], session['id'])
        return jsonify({ 'result' : "success", 'elementId' : data['elementId'], 'like_num' : like_num})

#######################################################################
#호스팅을 위한 코드
if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
    

