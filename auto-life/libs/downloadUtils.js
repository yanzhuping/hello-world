const callback = arguments[arguments.length - 1]
function getFile(url) {
	var xhr=new XMLHttpRequest();
	xhr.responseType="blob"
	xhr.onreadystatechange=function(){
		if(xhr.readyState==4&&xhr.status==200){
			blobToDataURL(xhr.response,callback)
		}
	}
	xhr.open("GET",url);
	xhr.send();
}
function blobToDataURL(blob, callback) {
    var a = new FileReader();
    a.onload = function (e) { callback(e.target.result); }
    a.readAsDataURL(blob);
}


