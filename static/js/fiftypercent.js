// author : Mima 
// Email : mima@fiftypercent-magazine.org
// Any adivce will be very preciouse to me. please feel free to send me any tip or advice.

const STANDARDSIZE = 1920;

//const PROPERTY_VALUE= ['.width', 'height', 'top', 'left']
//const PROPERTIES = {0 : [158, 170, 235, 133], 1 : [158, 170, 980, 1700]};
var properties = {}
// all Icons
var icons = document.getElementsByClassName("icon");

// todo: find different solution to fetch the original properties of the icon elements.
function setProperty() {
	for(var i=0; i<icons.length; i++){
		var property = []
		property.push(parseInt(icons[i].style.width, 10));
		property.push(parseInt(icons[i].style.height, 10));
		property.push(parseInt(icons[i].style.top, 10));
		property.push(parseInt(icons[i].style.left, 10));

		properties[i] =  property
	}
}
setProperty()

function setIcon() {
	var changeRatio = STANDARDSIZE / $(window).width();
	for(var i=0;i<icons.length;i++) {
		icons[i].style.width = properties[i][0] / changeRatio +'px';
		icons[i].style.height = properties[i][1] / changeRatio +'px';
		icons[i].style.top = properties[i][2] / changeRatio +'px';
		icons[i].style.left = properties[i][3] / changeRatio +'px';
	};
};

window.onload = setIcon;
window.onresize = setIcon;
