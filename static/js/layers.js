var vectorLayer, vectorSource;

 // get curent time
 function getDate(param){
 	// define a current time
 	var currentTime = new Date()
 	// returns the month (from 0 to 11)
 	var month = currentTime.getMonth() + 1
 	// returns the day of the month (from 1 to 31)
 	var day = currentTime.getDate()
 	// returns the year (four digits)
 	var year = currentTime.getFullYear()

 	if(param == 'month'){ // get month
 		return month + '/' + year;
 	} else if(param == 'day'){ // get day
 		return day + '/' + year;
 	} else if(param == 'year'){ //get year
 		return year;
 	} else if (param == 'full'){
 		return day + '/' + month + '/' + year
 	}
 }

// //add BRT PDOk Panden
// var brt_pdok = new ol.layer.Tile({
// 	id: "brtpdok",
// 	sld: "sldID_brt",
// 	sldDiv: "sld_div_brt",
// 	infoDiv: "info_div_brt_pdok",
// 	// metadata attributen
// 	meta_naam: "BRT (Basisregistratie Topografie) - <a target='_blank' href='https://pdok.nl'>PDOK</a>",
// 	meta_soort: "Basisregistratie",
// 	meta_org: "<a href='https://data.overheid.nl/data/dataset/brt-achtergrondkaart' target='_blank'>Kadaster</a>",
// 	meta_bijgewerkt: '01/02/2018',
// 	// metadata attributen
// 	title: "BRT Topografie",
// 	visible: true,
// 	isBaseLayer: true,
// 	opacity: 0.9,
// 	source: new ol.source.TileWMS({
// 		url: "https://geodata.nationaalgeoregister.nl/wmsc?",
// 		params: {'layers': 'brtachtergrondkaartpastel'}
// 	})
// });



// LINK for layers
//var myurl = 'https://mijndatalab.nl/atlas-starter/layers';
//var myurl = geocadtek.appConfig["server"] + '/atlas-starter/layers';
var myurl = geocadtek.appConfig["server"] + geocadtek.appConfig["apppath"] +'/layers';
console.log(myurl);

var myjson = {};

// AJAX async calls -- will be put in a function for proper use.
//
// aaa = $.getJSON(myurl, callbackFuncWithData);
var senddata;

$.ajax({
    url: myurl,
    dataType: 'json',
    data: senddata,
    async: false,
    success: callbackFuncWithData
});


//function callbackFuncWithData(data)
function callbackFuncWithData(data,status,jqxhr)
{
  //myjson = data["layer"];
  myjson = data;
  //alert(jqxhr.responseText);
}


//debugger;


// marker layers
vectorSource = new ol.source.Vector({});

vectorLayer = new ol.layer.Vector({
	title: "Marker Layer",
	source: vectorSource
});

var layerList = [];

jQuery(myjson.layer).each(function (index){
            //console.log(myjson.layer[index].title);
            myjson.layer[index].source = eval(myjson.layer[index].source); // enable source object

            // "Basisreg:true" --> Basisreg: true
            c=myjson.layer[index].layer_type.split(':');
            c=JSON.parse('{"' +  c[0] + '":' + eval(c[1]) + '}' )
            myjson.layer[index] = $.extend(myjson.layer[index],c)

             layerList.push(  new ol.layer.Tile( myjson.layer[index] ) );
//            return false; // This will stop the execution of jQuery each loop.
});

             layerList.push(vectorLayer);
//debugger;





//EOF
