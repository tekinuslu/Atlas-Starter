from datetime import datetime

from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import check_password_hash, generate_password_hash

#
from app import db


# db model
# class User(object):
class User(db.Model):
    """Model for user accounts in SQLlite."""

    """Model for user accounts in Postgress also"""
    __tablename__ = "users"
    __bind_key__ = "db1"  # sqlite

    #  ## INIT
    #    def __init__(self, firstname=None, lastname=None, username=None,
    #                password=None,
    #                password_hash=None,
    #                email=None,
    #                date_joined=None, last_login=None,
    #                is_active=None, is_admin=None,
    #                is_staff=None, is_superuser=None):
    #        print ('Initializing..')
    #        self.firstname = firstname
    #        self.lastname  = lastname
    #        self.username  = username
    #        self.password_  = password
    #        self.email     = email
    #        self.date_joined = date_joined
    #        self.last_login = last_login
    #        self.is_active = is_active
    #        self.is_admin = is_admin
    #        self.is_staff = is_staff
    #        self.is_superuser = is_superuser

    id = db.Column(
        db.Integer, primary_key=True
    )  # primary keys are required by SQLAlchemy
    firstname = db.Column(db.String(64), nullable=True)
    lastname = db.Column(db.String(64), nullable=True)
    username = db.Column(db.String(64), index=False, unique=True, nullable=False)
    password_ = db.Column(
        db.String(128), nullable=False  # hashed also
    )  # see hybrid_property for functionality change
    # password_hash = db.Column(db.String(128),
    #                  nullable=True)
    email = db.Column(
        "email",
        db.String(80),
        index=True,
        unique=False,  # True if needed
        nullable=False,
    )
    date_joined = db.Column(
        db.DateTime(),
        index=False,
        unique=False,
        nullable=False,
        default=datetime.utcnow,
    )
    last_login = db.Column(
        db.DateTime(),
        index=False,
        unique=False,
        nullable=False,
        default=datetime.utcnow,
    )
    is_active = db.Column(
        db.Boolean, index=False, unique=False, nullable=False, default=False
    )
    is_admin = db.Column(
        db.Boolean,  # admin layer credential, controls only layers not users
        index=False,
        unique=False,
        nullable=False,
        default=False,
    )
    is_staff = db.Column(
        db.Boolean, index=False, unique=False, nullable=False, default=False
    )
    is_superuser = db.Column(
        db.Boolean,  # super user credential, controls both users and layer tables
        index=False,
        unique=False,
        nullable=False,
        default=False,
    )

    def __repr__(self):
        return "<User {}>".format(self.username)
        # return '<User %r>' % self.username

    @hybrid_property
    def password(self):
        """ password getter """
        # print('\n PASSWORD getter called\n') # debug call

        return self.password_

    @password.setter
    def password(self, plaintext):  # this should the same with hybrid propery name
        """Create hashed password. -- setter"""
        # print('\n PASSWORD SETTER called\n') # debug call

        if plaintext.split(":")[0] != "pbkdf2":  # avoid re-hasing hashed value
            print("\n HASHED called\n")
            self.password_ = generate_password_hash(plaintext)

    def verify_password(self, plaintext):
        """Check hashed password."""

        return check_password_hash(self.password_, plaintext)

    def emailr(self):
        return "e-mail: %r" % self.email  # on user.email: return user.email
        # return self.email

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_email(value):
        return User.query.filter_by(email=value).first()


class Layers(db.Model):
    """Model for theme layers in Postgress."""

    __tablename__ = "layers"
    __bind_key__ = "db1"  # PG

    id = db.Column(
        db.Integer, primary_key=True
    )  # primary keys are required by SQLAlchemy
    #
    layer_id = db.Column(
        "layer_id", db.String(128), index=False, unique=True, nullable=False, default=""
    )  # id_???
    #
    title = db.Column("title", db.String(128), nullable=True)  # :: "Natuur monumenten"
    #
    category = db.Column("category", db.String(128), nullable=True)
    #
    layer_type = db.Column(
        db.String(64), nullable=True, default="themelayer:true"
    )  # temp solution!

    meta_name = db.Column("meta_name", db.String(128), nullable=True)
    meta_kind = db.Column("meta_kind", db.String(128), nullable=True)
    meta_org = db.Column(
        "meta_org", db.String(256), nullable=True, default="mijnDatalab"
    )

    meta_updated = db.Column(
        "meta_updated", db.String(128), nullable=True, default='getDate("year")'
    )
    #
    visible = db.Column("visible", db.Boolean, nullable=False, default=False)
    #
    opacity = db.Column("opacity", db.DECIMAL(1, 1), nullable=False, default=0.9)
    #
    isqueryable = db.Column("isqueryable", db.Boolean, default=True)
    #
    isgeojson = db.Column("isgeojson", db.Boolean, default=False, nullable=False)
    isPopup = db.Column("isPopup", db.Boolean, default=True)
    #
    # isbaselayer = db.Column('isbaselayer', db.Boolean, default=False)
    # isLufo = db.Column('isbaselayer', db.Boolean, default=False)
    #
    layer_name = db.Column(
        "layer_name", db.String(128), nullable=True, default="topp:mylayer_???"
    )
    #
    # _popup_attributes --> attribute list in Js :  make list of layer field as addable to this field, 1) ajax call to get fields
    _popup_attributes = db.Column("_popup_attributes", db.String(250), nullable=True)
    #
    _search_fields = db.Column("_search_fields", db.String(250), nullable=True)
    #
    projection = db.Column(
        "projection", db.String(100), default="EPSG:28992", nullable=False
    )
    #
    url = db.Column(
        "url",
        db.String(500),
        default="https://mijndatalab.nl/geoserver/topp/wms?",
        nullable=False,
    )
    #
    legend_url = db.Column(
        "legend_url",
        db.String(600),
        nullable=True,
        default="/wms?SERVICE=WMS&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&LAYER=+lyr.get(layerName)+&format=image/png",
    )
    #
    server_type = db.Column(
        "server_type", db.String(50), default="geoserver", nullable=False
    )
    #
    closed_dataset = db.Column(
        "closed_dataset", db.Boolean, nullable=False, default=True
    )
    #
    published = db.Column("published", db.Boolean, nullable=False, default=False)
    #
    created_at = db.Column(
        "created_at", db.DateTime, nullable=False, default=datetime.utcnow
    )
    updated_at = db.Column(
        "updated_at", db.DateTime, nullable=False, default=datetime.utcnow
    )
    #
    # baselayer= 01, luchtfoto = 100 , thema = 1000
    ordering = db.Column(db.Integer, index=True, nullable=False, unique=True, default=1)

    authkey = db.Column("authkey", db.String(64), nullable=True)  #  "f....-....-...."
    #
    def __str__(self):
        return "Volgorde: {} || {} (Gesloten dataset: {})".format(
            self.ordering, self.title, self.is_closed_dataset
        )

    #
    def get_absolute_url(self):
        return reverse("webservice:theme-detail", kwargs={"slug": self.slug})

    #
    @property
    def popup_attributes(self):
        attributes = self._popup_attributes

        if not attributes:
            return ""
        result = []

        for attr in attributes.split():
            result.append("'{}'".format(attr))

        return "popupAttributes: [{}]".format(", ".join(result))

    #
    @property
    def search_fields(self):
        search_fields = self._search_fields

        if not search_fields:
            return ""
        result = []

        for attr in search_fields.split():
            result.append("'{}'".format(attr))

        return "search_fields: [{}]".format(", ".join(result))

    #
    @property
    def myid(self):
        return "id: {}".format(self.layer_id)

    #
    @property
    def sldDiv(self):
        return "sld_div_{}".format(self.layer_id)

    #
    @property
    def layer_type_str(self):
        """
 
         if self.layer_type == 'theme_layer':
             return "themelayer:true"
         elif self.layer_type == 'base_registration':
             return "basisreg:true"
         elif self.layer_type == 'base_layer':
             return "isBaseLayer:true"
         elif self.layer_type == 'lucht_foto':
             return "isLufo:true"
         """

        return self.layer_type.js_type

    #
    @property
    def infoDiv(self):
        return "info_div_{}".format(self.layer_id)

    #
    @property
    def sld(self):
        return "sld_{}".format(self.layer_id)

    #
    @property
    def legend(self):
        return "lgn_{}".format(self.layer_id)

    #
    @property
    def filterid(self):
        return "flt_{}".format(self.layer_id)

    #
    @property
    def filterdataid(self):
        return "data_{}".format(self.layer_id)

    #
    @property
    def datazoekid(self):
        return "zoek_data_{}".format(self.layer_id)

    #
    @property
    # def params(self):
    #     return "{{'layers': '{0}'}}".format(self.layer_name)
    def params(self):
        if self.closed_dataset == True:
            return "{{ 'layers': '{0}', 'authkey' : '{1}' }}".format(
                self.layer_name, self.authkey
            )
        else:
            return "{{'layers': '{0}'}}".format(self.layer_name)

    #
    @property
    def source(self):
        # TODO: check server_type case.

        if self.layer_id != "osm":
            return """
     new ol.source.TileWMS({{
     projection: '{0}',
     url: '{1}',
     params: {2},
     serverType: '{3}'
 }})""".format(
                self.projection, self.url, self.params, self.server_type
            )
        else:
            return "new ol.source.OSM()"  # if OSM

    @property
    def isExternal(self):
        # get 'mijndatalab' from https://mijndatalab.nl/geoserver/topp
        host = self.url.split("//")[1].split(".")[0]
        # host  == 'mijndatalab' and False or True

        if host == "mijndatalab":
            return False
        else:
            return True

    @property
    def is_published(self):
        return self.published

    #
    @property
    def is_closed_dataset(self):
        return self.closed_dataset


# EOF
