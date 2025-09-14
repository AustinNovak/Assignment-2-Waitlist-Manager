# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None


# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
        print(f"Added {name} to the front of the waitlist.")

    def add_end(self, name):
        new_node = Node(name)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Added {name} to the end of the waitlist.")

    def remove(self, name):
        current = self.head
        prev = None
        while current:
            if current.name == name:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                print(f"Removed {name} from the waitlist.")
                return
            prev = current
            current = current.next
        print(f"{name} not found in the waitlist.")

    def print_list(self):
        if self.head is None:
            print("The waitlist is empty")
            return
        current = self.head
        while current:
            print(f"- {current.name}")
            current = current.next


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove(name)

        elif choice == "4":
            print("Current waitlist:")
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")


# Call the waitlist_generator function to start the program
if __name__ == "__main__":
    waitlist_generator()


'''
Design Memo (200–300 words):

How does your list work?
This waitlist is implemented as a singly linked list. Each customer is
represented as a Node, which stores the customer’s name and a pointer to
the next Node. The LinkedList class maintains a reference to the head node,
allowing traversal through the entire list. Adding to the front updates the
head pointer immediately, while adding to the end requires traversing to
the final node and linking in the new Node. Removal searches the list until
a match is found, then adjusts pointers so the list remains intact.

What role does the head play?
The head is the entry point to the list. It identifies where the list begins,
and all traversals, searches, and insertions start from it. If the head is
None, the list is empty. When removing or inserting at the front, the head
must be updated carefully because it defines the first Node.

When might a real engineer need a custom list like this?
Engineers might use a custom list like this when they need more control than
normal arrays or lists give. For example, it’s helpful when people are being
added and removed a lot, like a waitlist with VIPs and regular customers.
Linked lists are also good when memory is tight, since arrays can be harder
to resize. Plus, linked lists are the base for other structures like
queues and stacks, so learning them now is important for building more
complex systems later.
'''
