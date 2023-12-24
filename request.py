from queue import Queue
import random
import time

# Функція для генерації заявок
def generate_request(q):
    request_id = random.randint(1, 9999)
    q.put(request_id)
    print(f"Заявка {request_id} додана до черги.")

# Функція для обробки заявок
def process_request(q):
    if not q.empty():
        request = q.get()
        print(f"Заявка {request} оброблена.")
    else:
        print("Черга пуста.")

queue = Queue()

# Головний цикл програми
try:
    while True:
        generate_request(queue)    
        process_request(queue)     
        time.sleep(1)              
except KeyboardInterrupt:
    print("Програма завершена.")