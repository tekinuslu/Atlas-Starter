
from app import Layers, app, db

## This is for SQLite


def mydb_init():

    db.create_all()

    #   tmp = Layers(
    #       layer_id= ,
    #       layer_name= ,
    #       title= ,
    #       category=,
    #       meta_name=,
    #       meta_kind=,
    #       meta_org=,
    #       meta_updated=,
    #       visible=True,
    #       opacity=,
    #       isqueryable=True,
    #       #_popup_attributes=NULL,
    #       #_search_fields=NULL,
    #       projection=,
    #       url=,
    #       server_type='geoserver',
    #       closed_dataset=False,
    #       published=True,
    #       #created_at='2019-11-22 19:53:57',
    #       #updated_at='2019-11-22 19:53:57',
    #       ordering=,
    #       layer_type=,
    #       legend_url=' ',
    #       isgeojson=False,
    #       #authkey=NULL,
    #       isPopup=False,
    #       )

    brt = Layers(
        layer_id="brtpdok2",
        layer_name="brtachtergrondkaartpastel",
        title="BRT Topografie",
        category="BaseMap",
        meta_name="BRT (Basisregistratie Topografie) - <a target="
        "_blank"
        " href="
        "https://pdok.nl"
        ">PDOK</a>",
        meta_kind="Basisregistratie",
        meta_org="<a href="
        "https://data.overheid.nl/data/dataset/brt-achtergrondkaart"
        " target="
        "_blank"
        ">Kadaster</a>",
        meta_updated="01/02/2018",
        visible=True,
        opacity=0.9,
        isqueryable=True,
        # _popup_attributes=NULL,
        # _search_fields=NULL,
        projection="EPSG:28992",
        url="https://geodata.nationaalgeoregister.nl/wmsc?",
        server_type="geoserver",
        closed_dataset=False,
        published=True,
        # created_at='2019-11-22 19:53:57',
        # updated_at='2019-11-22 19:53:57',
        ordering=1,
        layer_type="isBaseLayer:true",
        legend_url=" ",
        isgeojson=False,
        # authkey=NULL,
        isPopup=False,
    )

    # OPEN LAYERS MAP
    osm = Layers(
        layer_id="osm",
        layer_name="Openstreet Map",
        title="OSM Open Street Map",
        category="BaseMap",
        meta_name="<a target="
        "_blank"
        " href="
        "https://www.openstreetmap.org"
        ">OSM</a> (OpenStreetMap)",
        meta_kind="Achtergrond kaart",
        meta_org="Vrijwilligers",
        meta_updated="01/01/2020",
        # meta_updated= 'getDate(''full'') + '' (Dagelijks)''',
        visible=False,
        opacity=0.9,
        isqueryable=False,
        # _popup_attributes=NULL,
        # _search_fields=NULL,
        projection="EPSG:28992",
        url="https://mijndatalab.nl/geoserver/topp/wms?",
        server_type="geoserver",
        closed_dataset=False,
        published=True,
        # created_at='2019-11-22 19:53:57',
        # updated_at='2019-11-22 19:53:57',
        ordering=2,
        layer_type="isBaseLayer:true",
        legend_url=" ",
        isgeojson=False,
        # authkey=NULL,
        isPopup=False,
    )

    # BASISREGISTRATIES
    bag = Layers(
        layer_id="id_bag_basigreg",
        layer_name="bag:bag",
        title="BAG",
        category="Basisregistratie",
        meta_name="Basisregistratie Adressen en Gebouwen (BAG)",
        meta_kind="Basisregistratie",
        meta_org="PDOK",
        meta_updated="01/01/2020",
        # meta_updated= 'getDate("year")',
        visible=True,
        opacity=0.9,
        isqueryable=True,
        # _popup_attributes=NULL,
        # _search_fields=NULL,
        projection="EPSG:28992",
        url="https://geodata.nationaalgeoregister.nl/bag/wms?",
        server_type="geoserver",
        closed_dataset=False,
        published=True,
        # created_at='2019-11-22 19:53:57',
        # updated_at='2019-11-22 19:53:57',
        ordering=103,
        layer_type="basisreg:true",
        legend_url="https://geodata.nationaalgeoregister.nl/bag/ows?service=WMS&request=GetLegendGraphic&format=image%2Fpng&width=20&height=20&layer=bag",
        isgeojson=False,
        # authkey=NULL,
        isPopup=True,
    )

    bgt = Layers(
        layer_id="id_bgt_basigreg",
        layer_name="bgtterugmeldingen",
        title="BGT Terugmeldingen",
        category="Basisregistratie",
        meta_name="BGT Terugmeldingen",
        meta_kind="Basisregistratie",
        meta_org="PDOK",
        meta_updated="01/01/2020",
        # meta_updated= 'getDate("year")',
        visible=False,
        opacity=0.9,
        isqueryable=True,
        # _popup_attributes=NULL,
        # _search_fields=NULL,
        projection="EPSG:28992",
        url="https://geodata.nationaalgeoregister.nl/terugmeldingen/bgt/v2/wms?",
        server_type="geoserver",
        closed_dataset=False,
        published=True,
        # created_at='2019-11-22 19:53:57',
        # updated_at='2019-11-22 19:53:57',
        ordering=113,
        layer_type="basisreg:true",
        legend_url="https://geodata.nationaalgeoregister.nl/terugmeldingen/bgt/v2/wms?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=bgtterugmeldingen&format=image/png&STYLE=terugmeldingen_style",
        isgeojson=False,
        # authkey=NULL,
        isPopup=True,
    )

    kad = Layers(
        layer_id="id_kadaster_basisreg",
        layer_name="CP.CadastralParcel",
        title="Kadastrale kaart v4",
        category="Kadaster",
        meta_name="Kadastrale kaart v4",
        meta_kind="Basisregistratie",
        meta_org="PDOK",
        meta_updated="01/01/2020",
        # meta_updated= 'getDate("year")',
        visible=False,
        opacity=0.9,
        isqueryable=True,
        _popup_attributes="",
        _search_fields="",
        projection="EPSG:28992",
        url="https://geodata.nationaalgeoregister.nl/inspire/cp/wms?",
        server_type="geoserver",
        closed_dataset=False,
        published=True,
        # created_at='2019-11-22 19:53:57',
        # updated_at='2019-11-22 19:53:57',
        ordering=115,
        layer_type="basisreg:true",
        legend_url="https://geodata.nationaalgeoregister.nl/inspire/cp/ows?service=WMS&request=GetLegendGraphic&format=image%2Fpng&width=20&height=20&layer=CP.CadastralParcel",
        isgeojson=False,
        # authkey=NULL,
        isPopup=True,
    )

    #
    # Luchtfotos
    #

    lucht1 = Layers(
        layer_id="lufo2019NL",
        layer_name="Actueel_ortho25",
        title="Luchtfoto 2019 - NL",
        category="Luchtfoto",
        meta_name="Luchtfoto 2019 25cm Netherlands",
        meta_kind="Raster kaart",
        meta_org="Geo Informatie <a href="
        "https://www.pdok.nl/introductie/-/article/luchtfoto-pdok"
        " target="
        "_blank"
        ">PDOK</a>",
        meta_updated="2019",
        visible=False,
        opacity=0.7,
        isqueryable=True,
        _popup_attributes="",
        _search_fields="",
        projection="EPSG:28992",
        url="https://geodata.nationaalgeoregister.nl/luchtfoto/rgb/wms?",
        server_type="mapserver",
        closed_dataset=False,
        published=True,
        ordering=100,
        layer_type="isLufo:true",
        legend_url="",
        isgeojson=False,
        isPopup=True,
    )

    lucht2 = Layers(
        layer_id="lufo2019NL_IR",
        layer_name="Actueel_ortho25IR",
        title="Luchtfoto 2019 IR - NL",
        category="Luchtfoto",
        meta_name="Luchtfoto 2019 Infrarood 25cm Netherlands",
        meta_kind="Raster kaart",
        meta_org="Geo Informatie <a href="
        "https://www.pdok.nl/introductie/-/article/luchtfoto-pdok"
        " target="
        "_blank"
        ">PDOK</a>",
        meta_updated="2019",
        visible=False,
        opacity=0.7,
        isqueryable=True,
        _popup_attributes="",
        _search_fields="",
        projection="EPSG:28992",
        url="https://geodata.nationaalgeoregister.nl/luchtfoto/infrarood/wms?",
        server_type="mapserver",
        closed_dataset=False,
        published=True,
        ordering=101,
        layer_type="isLufo:true",
        legend_url="",
        isgeojson=False,
        isPopup=True,
    )

    #
    # Thematic layers
    #

    nat = Layers(
        layer_id="id_bnatmomu",
        layer_name="beschermdenatuurmonumenten",
        title="Natuur monumenten",
        category="",
        meta_name="Beschermde natuurmonumenten  - <a target="
        "_blank"
        " href="
        "https://pdok.nl"
        ">PDOK</a>",
        meta_kind="Thema kaart",
        meta_org="<a href="
        "https://www.geobasisregistraties.nl/basisregistraties/adressen-en-gebouwen"
        " target="
        "_blank"
        "> natuurmonumenten </a>",
        meta_updated="01/01/2020",
        # meta_updated='getDate(''full'') +'' (Dagelijks)''',
        visible=False,
        opacity=0.7,
        isqueryable=True,
        _popup_attributes="",
        _search_fields="",
        projection="EPSG:28992",
        url="https://geodata.nationaalgeoregister.nl/beschermdenatuurmonumenten/wms",
        server_type="NA",
        closed_dataset=False,
        published=True,
        # created_at='2019-11-22 19:53:57',
        # updated_at='2019-11-22 19:53:57',
        ordering=1001,
        layer_type="themelayer:true",
        legend_url="https://geodata.nationaalgeoregister.nl/beschermdenatuurmonumenten/wms?SERVICE=WMS&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&LAYER=beschermdenatuurmonumenten&format=image/png",
        isgeojson=False,
        # authkey=NULL,
        isPopup=True,
    )

    bomen = Layers(
        layer_id="id_bomen",
        layer_name="rivm_084_20170314_gm_Bomenkaart",
        title="Bomen in Nederland",
        category="",
        meta_name="Bomen in Nederland  - <a target="
        "_blank"
        " href="
        "https://nationaalgeoregister.nl"
        ">NGR</a>",
        meta_kind="Thema kaart",
        meta_org="MijnDatalab",
        meta_updated="01/01/2020",
        # meta_updated='getDate("year")',
        visible=False,
        opacity=0.7,
        isqueryable=True,
        # _popup_attributes=NULL,
        # _search_fields=NULL,
        projection="EPSG:28992",
        url="https://geodata.rivm.nl/geoserver/wms?",
        server_type="geoserver",
        closed_dataset=False,
        published=True,
        # created_at='2019-11-22 19:53:57',
        # updated_at='2019-11-22 19:53:57',
        ordering=1002,
        layer_type="themelayer:true",
        legend_url="https://geodata.rivm.nl/geoserver/ows?service=WMS&request=GetLegendGraphic&format=image%2Fpng&width=20&height=20&layer=rivm_084_20170314_gm_Bomenkaart",
        isgeojson=False,
        # authkey=NULL,
        isPopup=True,
    )

    rce = Layers(
        layer_id="id_rvim_mon",
        layer_name="rce_rijksmonumenten_2019",
        title="RCE Rijksmonumenten",
        category="",
        meta_name="Rijksmonumenten - <a target="
        "_blank"
        " href="
        "https://nationaalgeoregister.nl"
        ">NGR</a>",
        meta_kind="Thema kaart",
        meta_org="<a href="
        "https://nationaalgeoregister.nl/geonetwork/srv/dut/catalog.search#/metadata/6f84efeb-fc1d-4565-a721-80735ea57dbd"
        " target="
        "_blank"
        ">Rijks monumenten - 2019</a>",
        meta_updated="01/07/2019",
        visible=False,
        opacity=0.7,
        isqueryable=True,
        _popup_attributes="",
        _search_fields="",
        projection="EPSG:28992",
        url="https://geodata.rivm.nl/geoserver/wms?",
        server_type="geoserver",
        closed_dataset=False,
        published=True,
        # created_at='2019-11-22 19:53:57',
        # updated_at='2019-11-22 19:53:57',
        ordering=1003,
        layer_type="themelayer:true",
        legend_url="https://geodata.rivm.nl/geoserver/ows/wms?SERVICE=WMS&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&LAYER=rce_rijksmonumenten_2019&format=image/png",
        isgeojson=False,
        # authkey=NULL,
        isPopup=True,
    )

    hiden1 = Layers(
        layer_id="id_gashid",
        layer_name="prv_atlas:Aardgasvelden_in_productie",
        title="Gas fields in production - closedDATA from DB",
        category="",
        meta_name="Hidden Layer - <a target="
        "_blank"
        " href="
        "https://mijndatalab.nl"
        ">mijndatalab</a>",
        meta_kind="Thema kaart",
        meta_org="<a href="
        "https://www.pdok.nl/"
        " target="
        "_blank"
        ">Aardgasvelden_in_productie</a>",
        meta_updated="01/01/2020",
        # meta_updated='getDate(''full'') +'' (Dagelijks)''',
        visible=False,
        opacity=0.7,
        isqueryable=True,
        _popup_attributes="",
        _search_fields="",
        projection="EPSG:28992",
        url="https://mijndatalab.nl/geoserver/prv_atlas/wms?",
        server_type="geoserver",
        closed_dataset=True,
        published=True,
        # created_at='2019-11-22 19:53:57',
        # updated_at='2019-11-22 19:53:57',
        ordering=1004,
        layer_type="themelayer:true",
        legend_url="https://mijndatalab.nl/geoserver/prv_atlas/ows?service=WMS&request=GetLegendGraphic&format=image%2Fpng&width=20&height=20&layer=Aardgasvelden_in_productie",
        isgeojson=False,
        authkey="fd4c1482-db2a-4566-b3a4-685e14c8602c",
        isPopup=True,
    )

    #  template = Layers(
    #      layer_id= ,
    #      layer_name= ,
    #      title= ,
    #      category='',
    #      meta_name=,
    #      meta_kind=,
    #      meta_org=,
    #      meta_updated=,
    #      visible=True,
    #      opacity=,
    #      isqueryable=True,
    #      _popup_attributes='',
    #      _search_fields='',
    #      projection=,
    #      url=,
    #      server_type='geoserver',
    #      closed_dataset=False,
    #      published=True,
    #      #created_at='2019-11-22 19:53:57',
    #      #updated_at='2019-11-22 19:53:57',
    #      ordering=,
    #      layer_type=,
    #      legend_url=' ',
    #      isgeojson=False,
    #      #authkey=NULL,
    #      isPopup=True,
    #      )

    ####

    db.session.add(brt)
    db.session.add(osm)
    db.session.add(bag)
    db.session.add(bgt)
    db.session.add(kad)
    db.session.add(lucht1)
    db.session.add(lucht2)
    db.session.add(nat)
    db.session.add(bomen)
    db.session.add(rce)
    db.session.add(hiden1)
    db.session.commit()


# db.session.rollback()
# db.drop_all()


if __name__ == "__main__":

    dbfile = app.config["SQLALCHEMY_DATABASE_URI"].split("/")[-1]

    try:
        # if not os.path.isfile(dbfile)=
        mydb_init()
        print("\n")
        print("Done creating sqlite table= {}".format(Layers.__tablename__))
        print("\n")
        print("To check type= sqlite3 {}".format(dbfile))
        print("\n")
    # else=
    #  print("\n")
    #  print("Warning= DB file %s already exists! Delete it and try again " % dbfile )
    #  print("\n")

    #  except (IOError, detail)=
    except OSError as err:
        print("OS error= {0}".format(err))

#  except Exception as e=
#    print("type error= " + str(e))
#    print(traceback.format_exc())

#  if len( sys.argv ) < 2=
#    print 'Usage= %s datapath' % sys.argv[ 0 ]
#    exit()
#
###  pdb.set_trace()
#
#  datapath= sys.argv[ 1 ]


# EOF
