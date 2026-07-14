def make_sandwich(*ingredients):
    print("Making your sandwich with the following ingredients: ")
    for ingredient in ingredients:
        print(f"*- {ingredient}" )

make_sandwich("Bread", "Cheese", "Tomato", "Turkey")
make_sandwich("Bread", "Peanut Butter", "Jelly")
make_sandwich("Bread", "Butter")