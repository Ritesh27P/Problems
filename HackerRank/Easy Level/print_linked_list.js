function printLinkedList(head) {
    while (true) {
        console.log(head.data)
        if (head.next){
            head = head.next
        }else {
            break
        }
    } 
}