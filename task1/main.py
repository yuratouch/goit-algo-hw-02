import queue
import random
import time

request_queue = queue.Queue()

def generate_unique_id():
    return random.randint(10000, 99999)

def generate_request():
    request_id = generate_unique_id()
    request = f"Заявка {request_id}"
    request_queue.put(request)
    print(f"Заявку {request} додано в чергу обробки.")


def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Заявку {request} передано в обробку.")
    else:
        print("Черга пуста.")

def main():
    while True:
        user_input = input("Введіть 'g' для створення нової заявки, 'p' для передачі заявки в обробку або 'q' для виходу: ").lower()
        if user_input == 'g':
            generate_request()
        elif user_input == 'p':
            process_request()
        elif user_input == 'q':
            print("Завершення програми")
            break
        else:
            print("Невідома команда")

if __name__ == "__main__":
    main()