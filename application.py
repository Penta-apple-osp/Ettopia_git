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

@application.route("/categoryList")
def view_category_list():
    return render_template("categoryList.html")

@application.route("/homePage")
def view_home_page():
    return render_template("homePage.html")

@application.route("/loginRegister")
def view_login_register():
    return render_template("loginRegister.html")

@application.route("/menuList")
def view_menu_list():
    return render_template("menuList.html")

@application.route("/menuRegister", methods=['POST'])
def reg_menu():
    data=request.form
    print(data)
    return render_template("menuRegister.html", data=data)

#######################################################################
# 실습과제1 제출용
@application.route("/register_menu", methods=['POST'])
def reg_menu_menu():
    data=request.form
    print(data)
    return render_template("register_menu.html", data=data)

@application.route("/register_review", methods=['POST'])
def reg_review():
    data=request.form
    print(data)
    return render_template("register_review.html", data=data)

@application.route("/myPage")
def view_my_page():
    return render_template("myPage.html")

@application.route("/reviewList")
def view_review_list():
    return render_template("reviewList.html")

@application.route("/storeDetail")
def view_store_detail():
    return render_template("storeDetail.html")

@application.route("/storeRegister", methods=['POST'])
def view_store_register():
    data=request.form
    print(data)
    return render_template("storeRegister.html", data=data)

#######################################################################
#회원가입 폼 제출을 위한 코드
@application.route("/submit_register_post", methods=['POST'])  #중복확인 코드 필요
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
@application.route("/submit_store_info", methods=['POST'])
def submit_store_info():
    data=request.form
    print(data)
    #메뉴 사진이 존재하면 메뉴 정보 DB에 저장하는 함수 호출
    if  request.files["chooseMenuFile"] != "":
        menu_image_file=request.files["chooseMenuFile"]
        menu_image_file.save("static/img_user/{}".format(menu_image_file.filename))
        DB.insert_menu_temp(data['store_name'], data, menu_image_file.filename)
    #리뷰 사진이 존재하면 리뷰 정보 DB에 저장하는 함수 호출
    if request.files["chooseReviewFile"] != "":
        review_image_file=request.files["chooseReviewFile"]
        review_image_file.save("static/img_user/{}".format(review_image_file.filename))
        DB.insert_review_temp(data['store_name'], data, review_image_file.filename)
    store_image_file=request.files["chooseFile"]
    store_image_file.save("static/img_user/{}".format(store_image_file.filename))
    if DB.insert_restaurant(data['store_name'], data, store_image_file.filename):
        return render_template("result.html", data=data, img_path="static/img_user/"+store_image_file.filename)
    else:
        return "이미 존재하는 레스토랑입니다."

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
#11주차 그룹과제2를 위한 리뷰 제출 코드
@application.route("/submit_review_post", methods=['POST'])
def submit_review_post():
    image_file=request.files["chooseFile"]
    image_file.save("static/img_user/{}".format(image_file.filename))
    data=request.form
    print(data)
    return render_template("register_review.html", data=data, img_path="static/img_user/"+image_file.filename)

#######################################################################
#11주차 과제2 제출 코드 + 이미 등록되어 있는 가게에서의 메뉴 추가

@application.route("/submit_menu_post", methods=['POST'])
def submit_menu_post():
    data=request.form
    print(data)
    if DB.insert_menu(data['name'], data):
        return render_template("register_menu.html", data=data)
    else:
        return "Menu name already exist!"
    

@application.route("/register_menu", methods=['POST'])
def submit_addmenu_post():  # 이름 수정할 예정 코드 확인용 임시 이름
    data=request.form
    print(data)
    if DB.insert_menu(data['name'], data):
        return render_template("menuList.html", data=data)
    else:
        return "이미 등록된 메뉴입니다."


#######################################################################
#호스팅을 위한 코드
if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
    