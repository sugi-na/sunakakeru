from flask import Flask,render_template,request,redirect,session

app = Flask (__name__)


#-----シークレットキーのセット/" "この中は通常　乱数が入る"
app.secret_key="SUNABACO"




#------template作成
  
@app.route('/')
def template():
    return render_template('base.html')

#1 が押されたとき
@app.route('/daijyobu',methods=['POST'])
def daijyobu():
    return render_template("daijyobu.html")

#2 が押されたとき
@app.route('/warai',methods=['POST'])
def warai():
    return render_template("warai.html")    

#3がおされたとき
@app.route('/gennki',methods=['POST'])
def gennki():
    return render_template("gennki.html") 

#4
@app.route('/itudemo',methods=['POST'])
def itudemo():
    return render_template("itudemo.html")     

#5
@app.route('/jisin',methods=['POST'])
def jisin():
    return render_template("jisin.html")
#6
@app.route('/miti',methods=['POST'])
def miti():
    return render_template("miti.html")    

#7
@app.route('/musiba',methods=['POST'])
def musiba():
    return render_template("musiba.html")    

#8
@app.route('/neru',methods=['POST'])
def neru():
    return render_template("neru.html") 

#9
@app.route('/sasuga',methods=['POST'])
def sasuga():
    return render_template("sasuga.html") 

#10
@app.route('/takara',methods=['POST'])
def takara():
    return render_template("takara.html")

#ひょうしへ
@app.route('/base',methods=['POST'])
def base():
    return render_template("base.html")














#-------最後のきめ文句　ここから後は書いても無駄
if __name__=="__main__":
    app.run(debug=True)