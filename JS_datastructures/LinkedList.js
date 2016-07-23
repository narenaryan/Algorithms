function LinkedList() {
    this.head = null
}

LinkedList.prototype.isEmpty = function() {
    return this.head == null
}

LinkedList.prototype.push = function(val) {
    var node = {
        val: val,
        next: null
    };
    if (this.head === null) {
        this.head = node;
    } else {
        var start = this.head;
        while (start.next !== null) {
            start = start.next;
        }
        start.next = node;
    }
}

LinkedList.prototype.traverse = function(val) {
    start = this.head;
    tstring = "";
    while (start.next) {
        tstring += start.val + "=>";
        start = start.next;
    }
    tstring += start.val;
    console.log(tstring)
}

LinkedList.prototype.search = function(elem) {
    start = this.head;
    while (start.next !== null) {
        if (elem === start.val) {
            return start
        }
        start = start.next;
    }
    return -1
}

// Reverse a linked list
LinkedList.prototype.reverse = function(start) {
    if (start.next == null) {
        console.log(start.val)
        return;
    } else {
        this.reverse(start.next)
        console.log(start.val)
    }

}

// Check a linked list is palindrome or not
LinkedList.prototype.isPalindrome = function() {
    start = this.head
    var temp = []
    while (start.next !== null) {
        temp.push(start.val)
				start = start.next
    }
		temp.push(start.val)
		console.log(temp)
    for (var i = 0, j = temp.length - 1; i <= j; i++, j--) {
        if (temp[i] !== temp[j]) {
            return false
        }
    }
    return true
}

llist = new LinkedList();
console.log(llist.isEmpty())
llist.push(2);
llist.push(52);
llist.push(2);
llist.traverse();

console.log(llist.search(52))
console.log(llist.search(12))
console.log(llist.isEmpty())
llist.reverse(llist.head)
console.log(llist.isPalindrome())
