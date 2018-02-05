
var newNum = "";
var prevNum = 0;
var result = 0;
var prevOpr = "+";


function calculator(){
	var numbers = document.getElementsByClassName("num");
	for(var i=0; i<numbers.length; i++){
		numbers[i].addEventListener('click', function(event){
			var x = event.target || event.srcElement;
			numVal = x.value;
			newNum += numVal;
			var screen = document.getElementById("screen-number");
			screen.innerHTML = newNum ;
			console.log(newNum);
		});
	}

	var operators = document.getElementsByClassName("operator");
	for(var i=0; i<operators.length; i++){
		operators[i].addEventListener('click', function(event){
			var y = event.target || event.srcElement;
			oprVal = y.value;
			console.log(prevOpr);			
			var screen = document.getElementById("screen-number");			

			 if (prevOpr == "/" && newNum == "0") {  // exception 01 : Divide by zero
						newNum = "";
						prevNum = 0;
						result = 0;
						prevOpr = "+";
						alert("Do not divide by zero!");
						screen.innerHTML = result;
					}

			else {


			switch(prevOpr) {
				case "+" : 
					result = parseInt(result) + parseInt(newNum);
					newNum = "";
					screen.innerHTML = result ;
					prevOpr = oprVal;
					//console.log("plus");
					break;

				case "-" : 
					result = parseInt(result) - parseInt(newNum);
					newNum = "";
					screen.innerHTML = result ;
					prevOpr = oprVal;
					//console.log("minus");
					break;

				case "*" : 
					result = parseInt(result) * parseInt(newNum);
					newNum = "";
					screen.innerHTML = result ;
					prevOpr = oprVal;
					//console.log("multiply");
					break;

				case "/" : 
					result = parseInt(result) / parseInt(newNum);
					newNum = "";
					screen.innerHTML = parseInt(result);
					prevOpr = oprVal;
					//console.log("divide");
					break;

				case "=" : 
					result = parseInt(newNum);
					newNum = "";
					screen.innerHTML = result;
					prevOpr = oprVal;
					//console.log("equals");
					break;
					

				default:
					return true;
			}


			if (isNaN(result)){		// exception 02 : double-clicking operators
					newNum = "";
					prevNum = 0;
					result = 0;
					prevOpr = "+";
					alert("Do not double-click operators!");
					screen.innerHTML = result;
			}

		}

		});
	}
}


