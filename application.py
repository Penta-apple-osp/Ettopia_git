from flask import Flask, render_template, request, url_for
import sys
application = Flask(__name__)

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

@application.route("/myPage")
def view_my_page():
    return render_template("myPage.html")

@application.route("/reviewList")
def view_review_list():
    return render_template("reviewList.html")

@application.route("/storeDetail")
def view_store_detail():
    return render_template("storeDetail.html")

@application.route("/storeRegister")
def view_store_register():
    return render_template("storeRegister.html")

#폼 제출을 위한 코드
@application.route("/submit_register_post", methods=['POST'])
def submit_register():
    data=request.form
    print(data)
    return render_template("result.html", data=data)

@application.route("/submit_login_post", methods=['POST'])
def submit_login():
    data=request.form
    return render_template("result.html", data=data)


#이미지와 등록 정보를 제출하기 위한 코드
@application.route("/submit_img_store", methods=['POST'])
def submit_img_store():
    image_file=request.files["chooseFile"]
    image_file.save("static/img_user/{}".format(image_file.filename))
    data=request.form
    print(data)
    return render_template("result.html", data=data, img_path="static/img_user/"+image_file.filename)

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

#호스팅을 위한 코드
if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
    
    