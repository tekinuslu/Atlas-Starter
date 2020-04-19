from datetime import datetime

from werkzeug.security import generate_password_hash

from app import User, app, db

# This is for SQLite


def mydb_init():
    # try:
    db.create_all()
    # if "--init" in sys.argv:
    #        db.create_all()

    superuser = User(
        firstname="Tekin",
        lastname="Uslu",
        username="tekin",
        password_=generate_password_hash("test"),
        email="info@mijndatalab.nl",
        date_joined=datetime(2019, 12, 25),
        is_admin=True,
        is_superuser=True,
    )
    admin = User(
        firstname="Michiel",
        lastname="de Ruyter",
        username="mdruyter",
        password_=generate_password_hash("test"),
        email="info@mijndatalab.nl",
        date_joined=datetime.utcnow(),
        is_admin=True,
        is_superuser=False,
    )
    normal = User(
        firstname="Sally",
        lastname="Almond",
        username="sally",
        password_=generate_password_hash("test"),
        email="info@mijndatalab.nl",
        date_joined=datetime.utcnow(),
        is_admin=False,
        is_superuser=False,
    )

    db.session.add(superuser)
    db.session.commit()
    db.session.add(admin)
    db.session.commit()
    db.session.add(normal)
    db.session.commit()
    # else:
    # print


# db.session.rollback()
# db.drop_all()


if __name__ == "__main__":

    dbfile = app.config["SQLALCHEMY_DATABASE_URI"].split("/")[-1]

    try:
        # if not os.path.isfile(dbfile):
        mydb_init()
        print("\n")
        print("Done creating sqlite table: {}".format(User.__tablename__))
        print("\n")
        print("To check type: sqlite3 {}".format(dbfile))
        print("\n")
    # else:
    #  print("\n")
    #  print("Warning: DB file %s already exists! Delete it and try again " % dbfile )
    #  print("\n")

    #  except (IOError, detail):
    except OSError as err:
        print("OS error: {0}".format(err))

#  except Exception as e:
#    print("type error: " + str(e))
#    print(traceback.format_exc())

#  if len( sys.argv ) < 2:
#    print 'Usage: %s datapath' % sys.argv[ 0 ]
#    exit()
#
#  pdb.set_trace()
#
#  datapath= sys.argv[ 1 ]


# EOF
