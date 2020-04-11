$(document).ready(function () {
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var myObj = JSON.parse(this.responseText);
        //console.log(myObj);
		populateVueData(myObj,stopOnloading())
    }
    if (this.readyState == 4 && this.status != 200){
    	console.log("error in getting data:"+str(this.status))
    }
	};
	xmlhttp.open("GET", "/static/js/result.js", true);
	xmlhttp.send();
})
function populateVueData(datain,callback){
	//console.log("here")
	var example1 = new Vue({
		el: '#data1',
		data: {
		items: datain
		}
	})
	callback
}
function stopOnloading(){
	$("#onLoading").addClass("d-none");
	$("#BaseCont").removeClass("d-none");
	$("body").addClass("loadnormal");
	$("body").removeClass("loadbg");
}

