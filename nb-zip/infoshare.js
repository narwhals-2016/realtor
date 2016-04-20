
// function to pull zip code - neighborhood pairs off infoshare.org



myChildren = $('#Area2LB').children;
var myArray = [];
var myString = "";
for (i = 0; i < myChildren.length; i ++){
	myString = myChildren[i].text
	myArray.push(myString)
};
console.log(myArray)