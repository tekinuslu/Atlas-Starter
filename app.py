import os
import sys

from flask import (Flask, flash, jsonify, redirect, render_template, request,
                   session, url_for)
# JSON
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
# IE 11 has issues with 308 when Windows <= 8.
from werkzeug.routing import RequestRedirect

#  Admin Panel
from models import Layers, User  # User@sqlite, Layers@postgres
from proxy import PrefixMiddleware  # as  # local class in proxy.py

# create Flask app
app = Flask(__name__)
# url_root_path = '/' + app.name # prefix
url_root_path = "/" + "atlas-starter"  # override prefix
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix=url_root_path)


RequestRedirect.code = 301

# DB
# SQlite #  see config file
# app.config.from_object(os.environ['APP_SETTINGS'])
try:
    app.config.from_object(os.environ["APP_SETTINGS"])
except:
    print(
        "  > Environment APP_SETTINGS is not set or accessible, reading local config file instead"
    )
    app.config.from_object("config_local.DevelopmentConfig")

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy(app)


ma = Marshmallow(app)


class UserSchema(ma.ModelSchema):
    class Meta:
        # model = User
        # Fields to expose
        fields = ("firstname", "lastname", "date_joined")


class LayersSchema(ma.ModelSchema):
    class Meta:
        ordered = True
        # fields = ("myid",
        fields = (
            "layer_id",
            "sldDiv",
            "infoDiv",
            "sld",
            "legend",
            "filterid",
            "filterdataid",
            "layer_name",
            "isPopup",
            "isgeojson",
            "meta_name",
            "meta_kind",
            "meta_org",
            "meta_updated",
            "title",
            "visible",
            "legend_url",
            # isBaselayer:True # fixed in layer.js
            "isExternal",
            "is_closed_dataset",
            "layer_type_str",
            "opacity",
            "layer_type",  # isBaselayer:true, isLufo:true, basisreg:true, themelayer:true
            "source",
        )


# JSON routes
@app.route("/layers")  # json
def layersopen():
    datalist = (
        Layers.query.order_by(Layers.ordering).filter_by(closed_dataset=False).all()
    )
    json = LayersSchema(many=True)
    output = json.dump(datalist)

    return jsonify({"layer": output})


@app.route("/layersc")  # json closed dataset
def layershidden():
    # if login true + require authkey for the layers

    if session.get("login"):
        # datalist = Layers.query.filter_by(closed_dataset=True) # closed sets
        datalist = Layers.query.order_by(Layers.ordering).filter_by(closed_dataset=True)
        json = LayersSchema(many=True)
        output = json.dump(datalist)

        return jsonify({"layer": output})
    else:
        return redirect(url_for("home"))
    # pass


# this fixes serialization problem on Opacity value, since it contains Decimal value.
def json_deserializer(*args, **kwgs):
    return json.loads(*args, parse_float=decimal.Decimal, **kwgs)


################### END JSON


#############
### Routes
#############


@app.route("/")
def home():
    #    pprint(app.__dict__)
    print("\n * The URL for this page is {} \n".format(url_for("home")))

    return render_template(
        "index.html", hostname=app.config["HOST"], apppath=url_root_path
    )


@app.route("/login/", methods=["GET", "POST"], endpoint="newlogin")
def login():

    if request.method == "POST":
        # get login user params
        user_details = request.form
        user_name = user_details["username"]

        # connect to database
        user = User.query.filter_by(username=user_name).first()

        # check user_name from db
        user = User.query.filter_by(username=user_name).first()

        if user is None:
            # get registered user from db

            # check password

            if user.verify_password(user_details["password"]):
                session["login"] = True
                session["firstName"] = user.firstname
                session["admin"] = user.is_admin  # used in admin.py
                session["super"] = user.is_superuser  # used in admin.py
                # push Success message
                flash(
                    "Welcome "
                    + session["firstName"]
                    + "! U bent succesvol ingelogd,"
                    + " uw kaartlagen geactiveerd.",
                    "success",
                )

                return redirect(url_root_path)

            else:
                flash("Wachtwoord is niet juist", "danger")

                return render_template("login.html")

        else:
            flash("Gebruikersnaam is niet juist", "danger")

            return render_template("login.html")

    return render_template("login.html")


@app.route("/logout/")
def logout():
    name = session["firstName"]

    session.clear()  # this should be before flash message
    flash("Bye " + name + "! U bent succesvol uitgelogd", "success")

    return redirect(url_for("home"))


if __name__ == "__main__":
    # check for initialization command
    # python app.py --init

    if "--init" in sys.argv:
        db.create_all()

    PORT = app.config["PORT"]
    # override port number, usage: python app.py --port 5000

    if "--port" in sys.argv:
        PORT = int(sys.argv[sys.argv.index("--port") + 1])

    app.run(host="0.0.0.0", debug=True, port=PORT)
    # app.run(host="0.0.0.0", debug=True, port=5600)


# EOF
