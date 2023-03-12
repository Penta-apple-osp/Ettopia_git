from flask import Flask, render_template, request, url_for, flash, redirect
from database import DBhandler
import sys
application = Flask(__name__)
application.config["SECRET_KEY"] = "anything-you-want"
DB = DBhandler()

#######################################################################
#화면 사이의 연결을 위한 코드
@application.route("/")
def hello():
    return render_template("index.html")

@application.route("/aboutUs")
def view_about_us():
    return render_template("aboutUs.html")

@application.route("/homePage")
def view_home_page():
    return render_template("homePage.html")

@application.route("/loginRegister")
def view_login_register():
    return render_template("loginRegister.html")

@application.route("/menuRegister", methods=['POST'])
def reg_menu():
    data=request.form
    print(data)
    return render_template("menuRegister.html", data=data)

@application.route("/myPage")
def view_my_page():
    return render_template("myPage.html")

@application.route("/storeRegister", methods=['POST']) #맛집 등록 화면으로 이동하는 함수-마커 클릭시 정보 받아와야 하기 때문에 POST 형식
def view_store_register():
    data=request.form
    print(data)
    return render_template("storeRegister.html", data=data)

#######################################################################
#회원가입 폼 제출을 위한 코드
@application.route("/submit_register_post", methods=['POST'])  #미 구현 - 아이디와 PW 중복확인 코드 필요
def submit_register():
    data=request.form
    print(data)
    if DB.insert_registerInfo(data['registerId'], data):
        return render_template("homePage.html")
    else:
        return "이미 존재하는 ID 입니다."

#로그인 폼 제출을 위한 코드
@application.route("/submit_login_post", methods=['POST'])
def submit_login():
    data=request.form
    if DB.search_loginInfo(data['loginId'], data['loginPassword']):
        return render_template("homePage.html")
    else:
        return "존재하지 않는 ID 또는 비밀번호입니다."

#######################################################################
#가게의 이미지와 등록 정보를 제출하기 위한 코드
@application.route("/submit_store_info", methods=['POST', 'GET'])
def submit_store_info():
    data=request.form
    print(data)
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
        return redirect(url_for('view_restaurant_detail', category=data['btn_food_hidden'], name=data['store_name']))
    else:
        flash("이미 존재하는 레스토랑입니다.")
        return redirect(url_for('view_home_page'))

#######################################################################
#미구현 - 리뷰 조회 화면과 메뉴 조회 화면에서의 추가하는 함수
@application.route("/submit_img_review", methods=['POST'])
def submit_img_review():
    image_file=request.files["file"]
    image_file.save("static/img_user/{}".format(image_file.filename))
    data=request.form
    return render_template("result.html", data=data)

@application.route("/submit_img_menu", methods=['POST'])
def submit_img_menu():
    image_file=request.files["file"]
    image_file.save("static/img_user/{}".format(image_file.filename))
    data=request.form
    return render_template("result.html", data=data)

#######################################################################
#카테고리 리스트에서 맛집 정보 가져오는 함수
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
    data = DB.get_restaurants(category) #read the table
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
    print(data)
    return render_template("storeDetail.html", data=data, avg_rate=avg_rate, menuData=menuData, reviewData=reviewData, 
                           menu_total=menu_tot_count, review_total=review_tot_count, menuRange=range(menu_tot_count),
                           menuLeft=range(4-menu_tot_count), reviewRange=reviewRange, category=category)

# 각 맛집당 메뉴 세부화면 동적 라우팅 코드 --> 맛집 세부화면에서 메뉴 더보기 클릭시 메뉴 세부 화면으로 이동
@application.route("/menuList/<category>/<store_name>/")
def view_foods(category, store_name):
    storeData = DB.get_restaurant_byname(str(category), str(store_name))
    data = DB.get_food_byname(str(store_name))
    tot_count = len(data)
    page_count = len(data)
    print(data)
    row = int(tot_count/4)
    left = int(tot_count%4)
    print(row)
    return render_template("menuList.html", datas=list(data), total=tot_count, row=range(row), row2=range(4), 
                           left=range(left), left2=range(4-left), storeData=storeData)

# 각 맛집당 리뷰 세부화면 동적 라우팅 코드 --> 맛집 세부화면에서 리뷰 더보기 클릭시 리뷰 세부 화면으로 이동
@application.route("/reviewList/<store_name>/")
def view_reviews(store_name):
    data = DB.get_review_byname(str(store_name))
    tot_count = len(data)
    page_count = len(data)
    print(data)
    print(tot_count)
    return render_template("reviewList.html", datas=data, total=tot_count)

#######################################################################
#호스팅을 위한 코드
if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)