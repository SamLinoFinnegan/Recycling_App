import os
from hashlib import sha3_512
from flask import Flask, render_template, request, session, redirect, url_for, flash, json
from models import User, Product
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from flask_caching import Cache



cache = Cache()

PATH_IMG = os.path.join(os.getcwd(), os.path.join(os.path.basename("static"), os.path.basename("images")))



load_dotenv()

app = Flask(__name__)

app.secret_key = os.environ.get('FLASK_SECRET_KEY') or os.urandom(16)

def make_dict(name, description, pack, dbin):
    """
    Create custom dictionaries in a clean and ease way
    """
    my_dict = {
        "name":name,
        "trigger":description,
        "pack":pack,
        "bin":dbin
    }
    return my_dict

def hash_password(password):
    """
    Hash user password
    """
    return sha3_512(password.encode("utf-8")).hexdigest()


@app.route("/", methods=["GET", "POST"])
def index(title="Welcome"):
    """
    Return index page
    """
    return render_template("index.html", title=title)

@app.route("/mission", methods=["GET", "POST"])
def mission(title="Mission"):
    """
    Return mission page
    """
    return render_template("mission.html", title=title)


@app.route("/home", methods=["GET", "POST"])
def home(title="Home"):
    """
    Return home page
    """
    prod = Product.select()

    #loading the data directly from database
    prod_dict = json.loads(json.dumps([make_dict(p.name, p.trigger, p.pack, p.bin) for p in prod]))
    
    # we are getting a list of the product names from the database and we are eliminating the space in the names
    prod_names = [product.name.replace(" ", "") for product in prod]
    
    # passing the list of name with no space to the home.html file
    return render_template("home.html", prod=prod_names, prod_obj=prod_dict, title=title)




@app.route("/login", methods=["GET", "POST"])
def log_in(title="Log In"):
    """
    Log in the user
    """

    if request.method == "POST":

        user = request.form["user_name"]
        password = request.form["user_password"]
        registered_user = User.select().where(User.name == user.lower()).first()

        if registered_user and registered_user.password == hash_password(password):

            flash('You were successfully logged in')
            session["user"] = user

            return redirect(url_for("admin_page"))

        flash("Invalid credentials")

    return render_template("login.html", title=title)


@app.route("/admin", methods=["GET", "POST"])
def admin_page(title="admin"):
    """
    Load admin page and manipulate the database, here the admin wiil have 
    accesss to the database and will be able to add or remove items
    """
    if "user" in session:

        products = Product.select()

        if request.method == "POST":
            if "add_product" in request.form:
                prod = request.form["product"]
                descrip = request.form["description"]
                pack = request.form["packaging"]
                img = request.files["image"]

                if 'image' not in request.files:
                    flash('No file part')
                    return render_template("admin_page.html", title=title, prods=products)
                
                filename = secure_filename(img.filename)
                img.save(os.path.join(PATH_IMG, filename))
                
                pack_list = pack.split()

                Product.create(name=prod, description=descrip, pack=pack_list)

                return render_template("admin_page.html", title=title, prods=products)
            
            if "delete_product" in request.form:
                
                prod = request.form["delete_product"]
                product = Product.get(Product.name.startswith(prod))
                product.delete_instance()

                return render_template("admin_page.html", title=title, prods=products)
            
        return render_template("admin_page.html", title=title, prods=products)
    else:
        flash("You must be logged in")
        return redirect(url_for("log_in"))


@app.route("/logout")
def log_out():
    """
    Log out the user
    """
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()