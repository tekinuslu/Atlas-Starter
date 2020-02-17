

// LINK for layers
//var myurl = 'https://mijndatalab.nl/atlas-starter/layersc';
var myurl = geocadtek.appConfig["server"] + geocadtek.appConfig["apppath"] +'/layersc';
console.log(myurl);


var myjson = {};

// AJAX async calls -- put in a function for proper use.
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


function callbackFuncWithData(data,status,jqxhr)
{
  //myjson = data["layer"];
  myjson = data;
  //alert(jqxhr.responseText);
}


//debugger;


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



//EOF
