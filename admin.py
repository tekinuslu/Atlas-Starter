import flask_admin as admin
from flask import flash, redirect, render_template, request, session, url_for
from flask_admin import expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.view import func
from flask_admin.menu import MenuLink  # used for 'Go to Atlas' link at taskbar

from app import Layers, User, app, db, url_root_path

# from flask_admin import Admin as Admin


# Add administrative views here


#######################################################
#
# Create customized model view class for DB tables
#
#######################################################

#
#  LAYERS TABLE VIEW
#
class LayersView(ModelView):
    def is_accessible(self):
        # if session.get('login'):

        if session.get("login") and session.get(
            "admin"
        ):  # admins can edit, but normal users can access via ../layerc(losed)
            # print("LayersView is_accessible")
            print(
                "LayersView accessible login response: {}".format(session.get("login"))
            )

            return True
        return False  # no access, protects

    def inaccessible_callback(
        self, name, **kwargs
    ):  # instead of error message, redirect to admin.index in class MyAdminIndexView()
        return redirect(url_for("admin.index"))

    page_size = 50  # the number of entries to display on the list view
    can_view_details = True  # show a modal dialog with records details
    # action_disallowed_list = ['delete', ]

    # help text
    column_descriptions = dict(
        layer_id="An unique value for the layer. Ex: id_mylayer1",
        title="The title of the layer you want to see at the layer window",
        category="Name the category to create new layer group for this layer to be place. Ex: BOR",
        layer_type="Select if the layer is Basis registration, aerialphoto or a thematic layer",
        meta_name="help text",
        meta_kind="help text",
        meta_org="help text",
        layer_name="Layer name is the remote server, such as geoserver layer name, example: topp:mylayer",
        _popup_attributes="list of attribute/field names you want to see in a popup window",
        _search_fields="list of attribute/field names you want to make search in",
        projection="The projection definition for the layer to be loaded.",
        url="The basic wms link. ex: https://mijndatalab.nl/geoserver/topp/wms?",
        legend_url="The link to load legend for the layer",
        server_type="Ex: geoserver (default), mapserver, arcgis.",
        closed_dataset="When this option is checked layer is hidden for public access. It may require authkey definition as well, see below.",
        ordering="If basis registration layer, orderin value changes between 1-99. For Aerialphotos (luchtfoto) ordering value changes between 100-999 and for thematic layers, ordering value changes between 1000-9999.",
        authkey="Authentication key for remote server (geoserver) to access a closed/hidden layer for public access.",
    )
    column_default_sort = ("ordering", False)  # False --> Ascending

    # layer_type replaced on table display (list view) - main
    column_choices = {
        "layer_type": [
            ("isBaseLayer:true", "Base layer"),
            ("basisreg:true", "Basisreg layer"),
            ("isLufo:true", "Aerialphoto"),
            ("themelayer:true", "Thematic layer"),
        ]
    }
    # layer_type menu/drop down on Create tab
    form_choices = {
        "layer_type": [
            ("isBaseLayer:true", "Base layer"),
            ("basisreg:true", "Basisreg layer"),
            ("isLufo:true", "Aerialphoto"),
            ("themelayer:true", "Thematic layer"),
        ]
    }
    # search on title
    column_searchable_list = ("title",)


### END table Layers


#######################
#  USER TABLE VIEW
#

# role base solution
class SuperUserView(ModelView):
    def is_accessible(self):
        # if session.get('login') and session.get('super'): #1 test - works

        if session.get("login") and session.get("super"):
            print(
                "\nsuperUser_View accessible login response: {}".format(
                    session.get("login")
                )
            )

            return True
        return False  # no access, protects

    def inaccessible_callback(
        self, name, **kwargs
    ):  # instead of error message, redirect to admin.index in class MyAdminIndexView()
        return redirect(url_for("admin.index"))

    page_size = 50  # the number of entries to display on the list view
    can_view_details = True  # show a modal dialog with records details

    column_searchable_list = ["firstname", "email"]
    column_filters = ["username"]

    column_exclude_list = [
        "date_joined",
        "password_",
    ]  # exclude on list view a.k.a initial page

    # help text
    column_descriptions = dict(
        firstname="First name of the user.",
        lastname="Surname of the user.",
        username="System username.",
        password_="Password of username in plain text. It will be hashed and kept internally.",
        email="User's email",
        is_admin="Selected if the user is admins.",
        is_active="Selected if the user is active.",
        is_staff="Selected if the user is staff.",
    )
    ##
    form_columns = (
        "firstname",
        "lastname",
        "username",
        "password",
        "email",
        "is_admin",
        "is_active",
        "is_staff",
    )

    #    form_widget_args effects create and edit
    form_widget_args = {"password": {"type": "password"}}

    # DONT DELETE SELF super account
    def delete_model(self, model):
        """
            Delete model. - Modified

            :param model:
                Model to delete
        """

        _id = request.form["id"]

        ## if user id is in the list of super then reject deletion also reject updates!!!
        ##
        ##if True: # if the deleted user is_admin don't delete also includes self delete.
        clicked_user = self.get_one(_id)  # select single user row from DB

        if clicked_user.is_superuser:
            flash("You cannot delete a super (or self) account.", "warning")

            return False

        return super(SuperUserView, self).delete_model(model)


### end class superUser_view

### start admin view for user table
class AdminUserView(ModelView):
    def is_accessible(self):
        # if session.get('login') and session.get('super'): #1 test - works

        if session.get("login") and session.get("admin") and not session.get("super"):
            print(
                "\nadminUser_View accessible login response: {}".format(
                    session.get("login")
                )
            )

            return True
        else:
            return False  # no access, protects

    def inaccessible_callback(
        self, name, **kwargs
    ):  # instead of error message, redirect to admin.index in class MyAdminIndexView()
        return redirect(url_for("admin.index"))

    page_size = 50  # the number of entries to display on the list view
    can_view_details = True  # show a modal dialog with records details
    can_create = True
    can_view = False
    can_edit = True
    # can_delete = True
    action_disallowed_list = ["delete"]  # removes 'with selected / delete ' menu
    column_exclude_list = [
        "date_joined",
        "password_",
    ]  # exclude on list view a.k.a initial page

    column_searchable_list = ["firstname", "email"]
    column_filters = ["username"]

    # create_modal = True
    # edit_modal = True
    # edit_modal = False

    # help text
    column_descriptions = dict(
        firstname="First name of the user.",
        lastname="Surname of the user.",
        username="System username.",
        password_="Password of username in plain text. It will be hashed and kept internally.",
        email="User's email",
        is_admin="New admins can be assigned only by superuser account.",
        is_active="Selected if new user is active.",
        is_staff="Selected if new user is staff.",
    )
    #
    form_columns = (
        "firstname",
        "lastname",
        "username",
        "password",
        "email",
        "is_admin",
        "is_active",
        "is_staff",
    )

    # form_widget_args effects create and edit
    form_widget_args = {
        #    'firstname':{
        #                'readonly':True
        #                        },
        "is_admin": {"disabled": True},
        "password": {"type": "password"},
    }

    def get_query(self):
        return self.session.query(self.model).filter(self.model.is_superuser is False)

    def get_count_query(self):
        return self.session.query(func.count("*")).filter(
            self.model.is_superuser is False
        )

    def get_one(self, id):
        query = self.get_query()  # non-superuserlist

        return query.filter(self.model.id == id).one()

    # can_delete = False
    def delete_model(self, model):
        """
            Delete model. - Modified

            :param model:
                Model to delete
        """

        _id = request.form["id"]
        clicked_user = self.get_one(_id)  # select single user row from DB

        if clicked_user.is_admin:
            flash("You cannot delete an admin account.", "warning")

            return False

        return super(AdminUserView, self).delete_model(model)

    def update_model(self, form, model):
        """
            Update model. - Modified

            :param model:
                Model to edit
        """
        # reject editing values of Admins, only normal users are allowed.

        _id = request.values["id"]
        _login_firstname = session["firstName"]  # login

        clicked_user = self.get_one(_id)  # select single user row from DB
        # exclude self - admin can edit self row.

        if clicked_user.is_admin and clicked_user.firstname != _login_firstname:
            flash("You cannot update another admin account.", "warning")

            return False

        return super(AdminUserView, self).update_model(form, model)


### Create customized index view class that handles login & registration
### INDEX
### start admin routes


class MyAdminIndexView(admin.AdminIndexView):
    # this controls indexes
    def is_accessible(self):
        if session.get("login") and session.get("admin"):
            return True
        else:
            # return False

            return redirect(url_for(".index"))  # go to admin index for login check

    @expose("/")  # this is http://.../atlasbeta/admin/
    def index(self):  # internal referal '.index' . external referal as 'admin.index'
        if session.get("login"):  # login true?
            print("admin index login check : {}".format(session.get("admin")))

            if session.get("admin"):
                return self.render("admin_panel.html")
            else:
                return redirect(url_for("home"))  # atlasbeta home
        else:
            return redirect(url_for(".login_view"))  # goto login

    @expose("/login/", methods=("GET", "POST"))  # /admin/login/
    def login_view(self):

        if request.method == "POST":
            # get login user params
            user_details = request.form
            user_name = user_details["username"]

            # check user_name from db
            user = User.query.filter_by(username=user_name).first()

            # if user != None and ( user.is_admin == True or user.is_superuser == True):

            if user is not None and (user.is_admin or user.is_superuser):
                # get registered admin or superuser from db

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
                        + "! U bent succesvol ingelogd",
                        "success" + " Your layers activated.",
                    )

                    return redirect(url_for(".index"))

                else:
                    # get message if password is NOT correct
                    flash("Wachtwoord is niet juist", "danger")

                    return render_template("admin_login.html")

            else:
                # get messsage if username is NOT correct
                flash("Gebruikersnaam is niet juist of niet admin", "danger")

        return render_template("admin_login.html")

    # END of login

    @expose("/logout/")
    def logout_view(self):
        name = session["firstName"]
        session.clear()  # this should be before flash message

        flash("Bye " + name + "! U bent succesvol uitgelogd", "success")

        return redirect(url_for(".index"))


### end of admin routes


admin = admin.Admin(
    app,
    name="Panel",
    index_view=MyAdminIndexView(),
    base_template="base_admin.html",
    template_mode="bootstrap3",
)

admin.add_view(SuperUserView(User, db.session, endpoint="superUser"))  # users table
admin.add_view(AdminUserView(User, db.session, endpoint="adminUser"))  # users table

admin.add_view(LayersView(Layers, db.session))  # Layers

admin.add_link(
    MenuLink(name="Go to Atlas", category="", url=url_root_path, target="_blank")
)

# EOF
