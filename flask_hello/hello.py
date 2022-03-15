#coding=utf-8

from flask import Flask, redirect, request, jsonify,render_template,url_for
import json
app=Flask(__name__)
app.config["DEBUG"]=True
@app.route("/")
def index():
    #传递参数给html,html中获取方式： {{变量}}
    test=1
    return render_template("demo.html",num=test)


@app.route("/login",methods=["GET","POST"])
def login_fun():
    print(request.method)
    if request.method == "GET":
        return "please enter uaername..."
    else:
        #postman 中发送方式为URL params，而不是Headers
        username = request.args.get('username') or "no username"
        pwd = request.args.get('pwd') or "no pwd"
        print('args参数是', username,pwd)
        return username+ " " + pwd + " is ok"


@app.route("/json",methods=["POST"])
def json_fun():
    #postman 中发送方式Headers,raw,json
    myjson=json.loads(request.data)
    print("username:",myjson['username'])
    print("pwd:", str(myjson["pwd"]))
    return jsonify(msg="ok")


@app.route("/string/<string:username>")
def string_fun(username):
    return username +" "+ username


@app.route("/int/<int:post_id>")
def int_fun(post_id):
    return str(post_id)


@app.route("/baidu")
def baidu_fun():
    #return redirect("http://www.baidu.com")
    return redirect(url_for("string_fun",username="baidu"))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
