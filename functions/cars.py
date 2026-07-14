def stored_cars(manufacturer, model_name, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model_name"] = model_name
    return car_info

new_car = stored_cars('subaru', 'outback', color='blue', tow_package=True)
print(new_car)