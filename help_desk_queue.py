# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    # Delete the following line and implement your Queue class
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new = Node(value)

        if self.front == None:
            self.front = new
            self.rear = new
        else:
            self.rear.next = new
            self.rear = new

    def dequeue(self):
        if self.front == None:
            return None

        value = self.front.value
        self.front = self.front.next

        if self.front == None:
            self.rear = None

        return value

    def peek(self):
        if self.front == None:
            return None

        return self.front.value

    def print_queue(self):
        current = self.front

        while current != None:
            print("- " + current.value)
            current = current.next
    


def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()
    

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            queue.enqueue(name)
            
            
            print(f"{name} added to the queue.")

        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            name = queue.dequeue()

            if name == None:
                print("No customers waiting")
            else:
                print(f"Helped: {name}")


        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            name = queue.peek()

            if name == None:
                print("No customers waiting")
            else:
                print(f"Next customer: {name}")


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_queue()
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()