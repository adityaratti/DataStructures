class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head_ref):
    temp = head_ref
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next


def push(head_ref, new_data):
    new_node = Node(new_data)
    new_node.next = head_ref
    head_ref = new_node
    return head_ref

def insertion_sort(head_ref):
    sorted = None
    current = head_ref

    while current is not None:
        next = current.next
        sorted = sorted_insert(sorted, current)
        current = next

    head_ref = sorted
    return head_ref

def sorted_insert(head_ref, new_node):
    current = head_ref
    if head_ref is None or head_ref.data >= new_node.data:
        new_node.next = head_ref
        head_ref = new_node
    else:
        while current.next is not None and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    return head_ref

a = None
a = push(a, 5)
a = push(a, 20)
a = push(a, 1)
a = push(a, 15)
a = push(a, 17)
a = push(a, 2)

print("Linked List before sorting")
printList(a)

a = insertion_sort(a)

print("\nLinked List after insertion sorting")
printList(a)


def partition(start, end):
    if start == end or start is None or end is None:
        return start

    pivot_prev = start
    current = start
    pivot = end.data

    while start != end:
        if start.data < pivot:
            pivot_prev = current
            current.data, start.data = start.data, current.data
            current = current.next

        start = start.next

    current.data, end.data = end.data, current.data

    return pivot_prev



def quick_sort(start,end):
    if start == end:
        return
    pivot_prev=partition(start,end)

    quick_sort(start, pivot_prev)

    if pivot_prev is not None and pivot_prev == start:
        quick_sort(pivot_prev.next, end)
    elif pivot_prev is not None and pivot_prev.next is not None:
        quick_sort(pivot_prev.next.next, end)


a = None
a = push(a, 5)
a = push(a, 20)
a = push(a, 1)
a = push(a, 15)
a = push(a, 17)
a = push(a, 2)

print("\nLinked List before sorting")
printList(a)

start = a
while a.next is not None:
    a = a.next

end = a

quick_sort(start, end)

print("\nLinked List after quick sorting")
printList(start)

def oddEvenList(head: Node) -> Node:
    odd = head
    even = head.next

    if odd is None or even is None:
        return head
    while even is not None:
        if (odd is None or even is None or even.next is None):
            break
        next_p = odd.next
        odd.next = even.next
        even.next = even.next.next
        odd = odd.next
        odd.next = next_p
        even = even.next
    return head

a = None
a = push(a, 5)
a = push(a, 20)
a = push(a, 1)
a = push(a, 15)
a = push(a, 17)
a = push(a, 2)

print("\nLinked List before odd even arrange")
printList(a)

a = oddEvenList(a)
print("\nLinked List after odd even arrange")
printList(a)