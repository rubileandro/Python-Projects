def main():
    protein_calc()


def protein_calc():
    print(
        "Welcome to PyProtein! Let's calculate your daily protein requirement.\n")
    # valid body weight check
    while True:
        try:
            body_weight_kg = float(input("What is your body weight in Kg? "))
            if 30 <= body_weight_kg <= 635:
                break
            else:
                print("Please enter a body weight between 30kg and 635kg.")
        except ValueError:
            print("Please enter a valid number for your body weight.")

    body_weight_lb = int(body_weight_kg * 2.20462)
    # Assuming 1 gram per pound of body weight
    protein_requirement = body_weight_lb

    print(f"Your daily protein requirement is {protein_requirement} grams per day. \n"
          f"Ideally, the amount of protein in each meal should be spaced more or less evenly throughout the day.\n")

    food_emoji(protein_requirement)


def food_emoji(protein_required):
    food_options = {
        "beef": {"emoji": "🥩", "protein": 40, "label": "beef steaks (each serving is 170g)"},
        "egg": {"emoji": "🍳", "protein": 6, "label": "single eggs (each serving is 1 large egg ~57g)"},
        "chicken": {"emoji": "🍗", "protein": 12, "label": "chicken drumsticks (each serving is 113g)"},
        "fish": {"emoji": "🐟", "protein": 28, "label": "fish fillets servings (each serving is 142g)"},
        "tofu": {"emoji": "⬜️", "protein": 10, "label": "tofu steaks (each serving is 113g)"},
        "milk": {"emoji": "🥛", "protein": 8, "label": "glasses of milk (each serving is 240ml)"},
        "nuts": {"emoji": "🥜", "protein": 7, "label": "servings of nuts (peanuts) (each serving is 28g)"},
        "yogurt": {"emoji": "🍶", "protein": 15, "label": "servings of Greek yogurt (each serving is 150g)"},
        "cheese": {"emoji": "🧀", "protein": 7, "label": "servings of cheese (Cheddar) (each serving is 28g)"},
        "protein shake": {"emoji": "🥤", "protein": 20, "label": "servings of protein shakes (Whey) (each serving is 25g)"},
    }

    while True:
        food_choice = input(f"Which food item would you like to see as an example to meet your protein requirement? "
                            f"\nOptions: {', '.join(food_options.keys())}: ").lower()

        if food_choice in food_options:
            food_info = food_options[food_choice]
            num_servings = int(protein_required / food_info["protein"])
            print(f"You would need about {num_servings} {food_info['label']} "
                  f"to meet your protein requirement of {protein_required}.")

            total_emojis_to_print = min(num_servings, 100)

            for i in range(total_emojis_to_print):
                print(food_info["emoji"], end='')
                # emoji per line
                if (i + 1) % 10 == 0:
                    print()

            if num_servings > 100:
                print(f"\n(Displayed a sample of 100 {food_info['label']} for brevity.)")

            # Exception handling loop
            while True:
                try:
                    another = input("\nWould you like to check another food item? (yes/no): ").strip().lower()
                    if another in ['yes', 'no']:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            if another == 'yes':
                continue
            else:
                print("Goodbye! Thank you for using PyProtein.")
                break

        else:
            print("Invalid choice. Please select a valid food option.")


if __name__ == '__main__':
    main()
