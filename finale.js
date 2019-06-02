
'use strict';
var express = require('express');
const bodyParser = require("body-parser");
var app = express();
var port = 3000;
var fs = require('fs');

var dyn = {
    "dict":[]
  };

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.use(bodyParser.urlencoded({
    extended: true
}));

app.use(bodyParser.json());

var k = 0;
var j_buf = {};
var p_buf = {};
var mut = 0;

app.post('/', (req, res) => {
  k = k+1;
  res.json({
    response: 'ok',
    body: '1'
  });
  if(k%2 == 0){
    p_buf = req.body;
    dyn.dict.push(j_buf);
    dyn.dict.push(p_buf);
    console.log(dyn);
    j_buf = {};
    j_buf = {};
  }
  else{-
    
    j_buf = req.body;
  }

  if(k%3 == 0)
  {
    dyn = { "dict":[] };
  }
  
});

app.get(`/`, function(request, response){
  var dyn_json = {
    "dict":[]
  };
  mut = 1;
  fs.readFile('geez.txt', 'utf-8' ,function(err, buf) {
  console.log(buf);
  var val = buf;
  var index = 0;
  var d = val.split("\n");
  console.log(d);
  var i = 0;
  for(i = 0;i<1;i++)
  {
    var a = [];
    a[0] =  d[index].split(" ")[0];
    a[1] =  d[index].split(" ")[1];
    a[2] =  d[index].split(" ")[2];
    a[3] =  d[index++].split(" ")[3];
    console.log(a[0]);
    dyn_json.dict.push({"app_id": a[0],
      "consumption" : a[1]
     });
    dyn_json.dict.push({"app_id": a[2],
      "consumption" : a[3]
     });
  }

  console.log(dyn_json);
  response.json(dyn_json)
  console.log("putting last data");
  console.log(d[2]);
  
  });
    
});

app.listen(port, function(){
    console.log('Express app listening on port ' + port);
});
