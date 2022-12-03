
from flask import *
from DBM import *
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("homenew.html")


@app.route("/signup")
def sign():
    return render_template("signupnew.html")


@app.route("/login")
def lgn():
    return render_template("loginnew.html")



@app.route("/adddataauthor", methods=["post"])
def add():
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    city = request.form["city"]
    t = (username, password, email, city)
    addAuthor(t)
    return redirect("/login")


@app.route("/adddatauser", methods=["post"])
def ad():
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    city = request.form["city"]
    t = (username, password, email, city)
    addUser(t)
    return redirect("/login")


@app.route("/loga", methods=["post"])
def lga():
    email = request.form["email"]
    password = request.form["password"]
    t = (email, password)
    t1 = checklgauthor(t)
    if t in t1:
        return redirect("/authorpg")
    else:
        return redirect("/login")


@app.route("/logu", methods=["post"])
def lgu():
    email = request.form["email"]
    password = request.form["password"]
    t = (email, password)
    t1 = checklguser(t)
    if t in t1:
        return redirect("/allpost")
    else:
        return redirect("/login")


@app.route("/authorpg")
def aut():
    return render_template("authorpagenew.html")


@app.route("/addpost")
def addpost():
    return render_template("addpostnew.html")




@app.route("/allpost")
def allpost():
    t=selectAllpost()
    return render_template("viewpostnew.html",elist=t)


@app.route("/authpost")
def authpost():
    t=selectAllpost()
    return render_template("authpost.html",elist=t)


@app.route("/addpostauthor", methods=["post"])
def addpo():
    username = request.form["username"]
    blogtitle = request.form["blogtitle"]
    post = request.form["post"]
    t = (username, blogtitle, post)
    addPost(t)
    return redirect("/authorpg")



@app.route("/del")
def de():
    username = request.args.get("username")
    deletePost(username)
    return redirect("/authpost")

@app.route("/edit")
def ed():
    username = request.args.get("username")
    el = selectuserById(username)
    return render_template("updatenew.html", t=el)


@app.route("/upd", methods=["post"])
def upd():
    username = request.form["username"]
    blogtitle = request.form["blogtitle"]
    post = request.form["post"]
    t = (username,blogtitle,post,username)
    updatePost(t)
    return redirect("/authpost")




if __name__ == "__main__":
    app.run(debug=True)
