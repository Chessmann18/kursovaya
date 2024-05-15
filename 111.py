def calculate_rental_cost(hours, car_type):
    if car_type == "такси":
        cost_per_hour = 10
    elif car_type == "микроавтобус":
        cost_per_hour = 15
    elif car_type == "автобус":
        cost_per_hour = 20
    else:
        return "Неверно указан тип автомобиля"

    total_cost = hours * cost_per_hour
    return total_cost

# Ввод данных от пользователя
hours = int(input("Введите количество часов аренды: "))
car_type = input("Введите тип автомобиля (такси, микроавтобус, автобус): ")

# Вызов функции для расчета стоимости аренды
rental_cost = calculate_rental_cost(hours, car_type)

if isinstance(rental_cost, str):
    print(rental_cost)
else:
    print(f"Стоимость аренды автомобиля типа {car_type} на {hours} часов составит {rental_cost} ")