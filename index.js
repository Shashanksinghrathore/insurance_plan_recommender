var express = require("express");
var path = require('path');
var shelljs = require("shelljs");
var app =  express();

//var http = require('http').Server(app);
app.set('port',(process.env.PORT || 5000));
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/public'));

//route to upload files. It used upload method defined above to upload the files via multer
app.get("/",function(req,res){
	res.render("home");
});

app.get("/policies",function(req,res){
	res.render("policies");
});

// app.get("/test",function(req,res){
// 	res.render("test");
// });

app.get("/final",function(req,res){
	res.render("final");
});

var Server = app.listen(app.get('port'), function(){
	console.log('listening on *:');
});
