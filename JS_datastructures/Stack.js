
function Stack(){
	this.top = -1;
	this.arr = [];
}

Stack.prototype.push = function(val){
	this.arr.push(val);
	this.top += 1;
}

Stack.prototype.pop = function(val){
	if (this.top == -1) {
		throw "Stack is empty";
	}
	this.top -= 1;
	return this.arr.pop();
}

Stack.prototype.isEmpty = function(){
	return this.arr.length == 0;
}

Stack.prototype.peek = function(){
	if (this.top == -1) {
		throw "Stack is empty";
	}
	return this.arr[this.arr.length - 1];
}

function isStringbalanced(testString){
	myStack = new Stack();
	var isBalanced = true;

	for (var i in testString) {
		if (testString[i] == "("){
			myStack.push("(");
		} else if (testString[i] == ")") {
			  if (myStack.isEmpty()) {
			     isBalanced = false;
		    } else {
					elem = myStack.pop()
					if (elem != "("){
						isBalanced = false;
					}
				}
		}
	}

	if (!myStack.isEmpty()){
		isBalanced = false
	}
	return isBalanced
}

testString1 = "()((a+b)-c)";
testString2 = "()()())";



console.log(isStringbalanced(testString1)?"Balanced":"Not Balanced");
console.log(isStringbalanced(testString2)?"Balanced":"Not Balanced");

/* myStack = new Stack()
myStack.push(2)
myStack.push(12)
myStack.push(76)
console.log(myStack.peek())
myStack.pop()
console.log(myStack.peek())
myStack.pop()
myStack.pop()
myStack.peek() */
