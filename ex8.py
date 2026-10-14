import random


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class CarWash:
    def __init__(self, wash_time):
        self.wash_rate = wash_time
        self.current_car = None
        self.time_remaining = 0

    def tick(self):
        if self.current_car is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_car = None

    def busy(self):
        return self.current_car is not None

    def start_next(self, car):
        self.current_car = car
        self.time_remaining = self.wash_rate


class Car:
    def __init__(self, time):
        self.timestamp = time

    def wait_time(self, current_time):
        return current_time - self.timestamp


def new_car_arrives():
    return random.randrange(1, 11) == 10


def simulation():
    print("Предположения симуляции (Вариант 1):")
    print("1. Симуляция длится 120 минут (7200 секунд).")
    print("2. Каждую минуту (с вероятностью 10%) приезжает новая машина.")
    print("3. Время на мойку одной машины составляет 10 минут.")

    wash_time = 10
    num_minutes = 120

    car_wash = CarWash(wash_time)
    car_queue = Queue()
    waiting_times = []

    for current_minute in range(num_minutes):
        if new_car_arrives():
            car_queue.enqueue(Car(current_minute))

        if (not car_wash.busy()) and (not car_queue.is_empty()):
            next_car = car_queue.dequeue()
            waiting_times.append(next_car.wait_time(current_minute))
            car_wash.start_next(next_car)

        car_wash.tick()

    if waiting_times:
        avg_wait = sum(waiting_times) / len(waiting_times)
    else:
        avg_wait = 0

    print(f"Среднее время ожидания: {avg_wait:.2f} мин. Машин осталось в очереди: {car_queue.size()}")


simulation()