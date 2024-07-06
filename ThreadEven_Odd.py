import threading
import time

# Function to print even numbers
def print_even():
    for i in range(2, 21, 2):
        print(f"Even Thread: {i}")
        time.sleep(0.1)  # Adding a small delay for illustration

# Function to print odd numbers
def print_odd():
    for i in range(1, 20, 2):
        print(f"Odd Thread: {i}")
        time.sleep(0.1)  # Adding a small delay for illustration

# Creating threads
even_thread = threading.Thread(target=print_even)
odd_thread = threading.Thread(target=print_odd)

# Starting threads
even_thread.start()
odd_thread.start()

# Waiting for threads to complete (optional)
even_thread.join()
odd_thread.join()

# This line ensures "Main Thread" prints last, demonstrating all threads have completed
print("Main Thread: All threads have finished execution")