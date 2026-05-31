
# Cars dictionary exercise
cars = {
    "car_1": {"brand": "Toyota", "year": 2018, "price": 15000},
    "car_2": {"brand": "Honda", "year": 2021, "price": 20000},
    "car_3": {"brand": "Ford", "year": 2023, "price": 25000}
}

# Task 1: Print outer key with brand and price
for key, value in cars.items():
    print(f"{key}: Brand: {value['brand']}, Price: {value['price']} ")

print()  # blank line for separation

# Task 2: Print only cars newer than 2020
for key, value in cars.items():
    if value['year'] > 2020:
        print(key)
