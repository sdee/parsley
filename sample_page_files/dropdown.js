function showDropdown(dropdownElement, hiddenElement, callingElement, IEtopOffset, IErightOffset) {
	$(hiddenElement).value="";
	$(callingElement).value="";
	$(callingElement).blur();
	
	var IE = document.all?true:false
	if (IE) {
		$(dropdownElement).style.top = IEtopOffset;
		if (IErightOffset != '') {
			$(dropdownElement).style.right = "0px";
		}
	}
	
	$(dropdownElement).style.display = "block";
}


function selectItem(hiddenElement, value, textElement, text, dropdownElement) {
	$(hiddenElement).value=value;
	if (textElement != '') {
		$(textElement).value=text;
		$(dropdownElement).style.display = "none";
	}
}

function fetchProduce(url, hiddenElement1, hiddenElement2) {
	var qs;
	qs = "";
	if ($(hiddenElement1).value != "") {
		qs = hiddenElement1 + "=" + $(hiddenElement1).value;
	} else {
		return;
	}
	if (hiddenElement2 != "") {
		if ($(hiddenElement2).value != "") {
			qs = qs + "&" + hiddenElement2 + "=" + $(hiddenElement2).value;
		} else {
			return;
		}
	}
	window.location.href = url + "?" + qs;
}

function findPos(obj) {
	var curleft = curtop = 0;
	if (obj.offsetParent) {
		curleft = obj.offsetLeft
		curtop = obj.offsetTop
		while (obj = obj.offsetParent) {
			curleft += obj.offsetLeft
			curtop += obj.offsetTop
		}
	}
	return [curleft,curtop];
}