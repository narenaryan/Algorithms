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
    console.log(tstring);
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

llist = new LinkedList();
console.log(llist.isEmpty())
llist.push(2);
llist.push(52);
llist.push(13);
llist.traverse();
console.log(llist.search(52))
console.log(llist.search(12))
console.log(llist.isEmpty())
