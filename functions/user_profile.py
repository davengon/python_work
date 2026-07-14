def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

new_profile = build_profile("David", "Gonzalez", age=30, favorite_color="Maroon", favorite_fruit="Cherry")
print(new_profile)