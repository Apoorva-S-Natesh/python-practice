import threading
import time


def print_numbers():
	for i in range(1, 6):
		time.sleep(2)
		print(f"Number: {i}")


def print_char():
	for i in "banana":
		time.sleep(1)
		print(f"Character: {i}")

#Daemon thread
def background_task():
	while True:
		print("Background task running...")
		time.sleep(1)

#create a thread
thread1 = threading.Thread(target=print_numbers, name="numbers")
thread2 = threading.Thread(target=print_char, name="characters")

thread = threading.Thread(target=background_task)
thread.daemon = True #setingthread thread as daemon
thread.start()

thread1.start()
thread2.start()

print(f"is {thread1.name} alive? {thread1.is_alive()}")
print(f"is {thread1.name} alive? {thread2.is_alive()}")
thread1.join() # waits until thread completes
thread2.join()
print(f"is thread1 alive? {thread1.is_alive()}")
print(f"is thread2 alive? {thread2.is_alive()}")
print("Thread has completed, continuig the program.")


'''
####### threads list ###
def simple_tasks(task_name):
	print(f"Starting {task_name}")
	time.sleep(1)
	print(f"ending {task_name}")

print("enter task names:")
tasks = input().split(", ")
threads = []

for task in tasks:
	thread = threading.Thread(target=simple_tasks, args=(task,))
	threads.append(thread)
	thread.start()

for thread in threads:
	thread.join()

'''