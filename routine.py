def prepare_diet():
    print("Welcome to the Diet Planner!")
    print("Let's start by gathering some information.")

    goal = input("What is your goal? Bodybuilding, Weight Gaining, or Weight Losing? ").lower()
    if goal not in ['bodybuilding', 'weight gaining', 'weight losing']:
        print("Invalid goal. Please choose one of the provided options.")
        return

    diet_type = input("What type of diet do you prefer? (e.g., Vegetarian, Non-vegetarian, Vegan): ").lower()
    if diet_type not in ['vegetarian', 'non-vegetarian', 'vegan']:
        print("Invalid diet type. Please choose one of the provided options.")
        return

    if goal == 'bodybuilding':
        diet_plan = prepare_bodybuilding_diet(diet_type)
    elif goal == 'weight gaining':
        diet_plan = prepare_weight_gaining_diet(diet_type)
    elif goal == 'weight losing':
        diet_plan = prepare_weight_losing_diet(diet_type)

    print("\nHere's your personalized diet plan:")
    for meal, foods in diet_plan.items():
        print(f"\n{meal.capitalize()}:")
        for food in foods:
            print(f"- {food}")

    print("\nAdvice:")
    if goal == 'bodybuilding':
        print("Focus on high-protein foods and adequate calorie intake to support muscle growth.")
    elif goal == 'weight gaining':
        print("Increase calorie intake with nutrient-dense foods to support weight gain.")
    elif goal == 'weight losing':
        print("Create a calorie deficit by choosing foods that are low in calories but high in nutrients.")

def prepare_bodybuilding_diet(diet_type):
    if diet_type == 'vegetarian':
        diet_plan = {
            'breakfast': ['Scrambled eggs', 'Whole grain toast', 'Fruit smoothie'],
            'mid-morning snack': ['Greek yogurt with nuts and berries'],
            'lunch': ['Quinoa salad with chickpeas and vegetables'],
            'afternoon snack': ['Protein shake with almond milk'],
            'dinner': ['Grilled tofu with brown rice and steamed vegetables']
        }
    elif diet_type == 'non-vegetarian':
        diet_plan = {
            'breakfast': ['Egg whites omelette with spinach', 'Whole wheat bread'],
            'mid-morning snack': ['Cottage cheese with fruit'],
            'lunch': ['Grilled chicken breast with sweet potato and broccoli'],
            'afternoon snack': ['Turkey slices with whole grain crackers'],
            'dinner': ['Salmon fillet with quinoa and asparagus']
        }
    elif diet_type == 'vegan':
        diet_plan = {
            'breakfast': ['Vegan protein smoothie with almond milk'],
            'mid-morning snack': ['Mixed nuts and seeds'],
            'lunch': ['Lentil soup with whole grain bread'],
            'afternoon snack': ['Hummus with raw vegetables'],
            'dinner': ['Stir-fried tempeh with brown rice and mixed vegetables']
        }
    return diet_plan

def prepare_weight_gaining_diet(diet_type):
    if diet_type == 'vegetarian':
        diet_plan = {
            'breakfast': ['Oatmeal with nuts and dried fruits', 'Avocado toast'],
            'mid-morning snack': ['Banana with peanut butter'],
            'lunch': ['Bean burritos with guacamole and salsa'],
            'afternoon snack': ['Trail mix with dried fruits and dark chocolate'],
            'dinner': ['Vegetable stir-fry with tofu and quinoa']
        }
    elif diet_type == 'non-vegetarian':
        diet_plan = {
            'breakfast': ['Protein pancakes with berries', 'Eggs with whole grain toast'],
            'mid-morning snack': ['Greek yogurt with honey and granola'],
            'lunch': ['Chicken and rice bowl with vegetables'],
            'afternoon snack': ['Beef jerky with cheese and crackers'],
            'dinner': ['Grilled steak with baked potato and green beans']
        }
    elif diet_type == 'vegan':
        diet_plan = {
            'breakfast': ['Smoothie bowl with plant-based protein powder'],
            'mid-morning snack': ['Chia seed pudding with coconut milk'],
            'lunch': ['Quinoa salad with black beans and avocado'],
            'afternoon snack': ['Nut butter sandwich with banana'],
            'dinner': ['Vegan pasta with tofu and tomato sauce']
        }
    return diet_plan

def prepare_weight_losing_diet(diet_type):
    if diet_type == 'vegetarian':
        diet_plan = {
            'breakfast': ['Greek yogurt with berries', 'Whole grain cereal with almond milk'],
            'mid-morning snack': ['Apple slices with almond butter'],
            'lunch': ['Vegetable soup with whole grain bread'],
            'afternoon snack': ['Edamame with sea salt'],
            'dinner': ['Roasted vegetables with quinoa']
        }
    elif diet_type == 'non-vegetarian':
        diet_plan = {
            'breakfast': ['Scrambled eggs with spinach', 'Whole wheat toast'],
            'mid-morning snack': ['Cottage cheese with pineapple'],
            'lunch': ['Grilled chicken salad with vinaigrette'],
            'afternoon snack': ['Turkey and cheese roll-ups'],
            'dinner': ['Baked fish with steamed vegetables']
        }
    elif diet_type == 'vegan':
        diet_plan = {
            'breakfast': ['Fruit salad with nuts'],
            'mid-morning snack': ['Rice cakes with avocado'],
            'lunch': ['Chickpea salad with lemon tahini dressing'],
            'afternoon snack': ['Vegetable sticks with hummus'],
            'dinner': ['Stir-fried tofu with mixed vegetables']
        }
    return diet_plan

prepare_diet()
