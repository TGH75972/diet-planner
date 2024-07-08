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
        diet_plan, nutrients = prepare_bodybuilding_diet(diet_type)
    elif goal == 'weight gaining':
        diet_plan, nutrients = prepare_weight_gaining_diet(diet_type)
    elif goal == 'weight losing':
        diet_plan, nutrients = prepare_weight_losing_diet(diet_type)

    print("\nHere's your personalized diet plan:")
    for meal, foods in diet_plan.items():
        print(f"\n{meal.capitalize()}:")
        for food in foods:
            print(f"- {food}")

    print("\nNutrient Information:")
    for nutrient, value in nutrients.items():
        print(f"{nutrient.capitalize()}: {value} grams")

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
    
    nutrients = calculate_nutrients(diet_plan)
    return diet_plan, nutrients

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
    
    nutrients = calculate_nutrients(diet_plan)
    return diet_plan, nutrients

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
    
    nutrients = calculate_nutrients(diet_plan)
    return diet_plan, nutrients

def calculate_nutrients(diet_plan):
    nutrients = {'protein': 0, 'carbs': 0, 'fat': 0}

    for meal, foods in diet_plan.items():
        for food in foods:
            if food.lower() in food_nutrients:
                nutrients['protein'] += food_nutrients[food.lower()]['protein']
                nutrients['carbs'] += food_nutrients[food.lower()]['carbs']
                nutrients['fat'] += food_nutrients[food.lower()]['fat']

    return nutrients

food_nutrients = {
    'scrambled eggs': {'protein': 13.0, 'carbs': 1.5, 'fat': 11.0},
    'whole grain toast': {'protein': 2.5, 'carbs': 48.0, 'fat': 1.5},
    'fruit smoothie': {'protein': 2.0, 'carbs': 34.0, 'fat': 0.5},
    'greek yogurt with nuts and berries': {'protein': 10.0, 'carbs': 20.0, 'fat': 5.0},
    'quinoa salad with chickpeas and vegetables': {'protein': 12.0, 'carbs': 42.0, 'fat': 6.0},
    'protein shake with almond milk': {'protein': 20.0, 'carbs': 8.0, 'fat': 3.0},
    'grilled tofu with brown rice and steamed vegetables': {'protein': 15.0, 'carbs': 50.0, 'fat': 10.0},
    'egg whites omelette with spinach': {'protein': 14.0, 'carbs': 2.0, 'fat': 0.5},
    'whole wheat bread': {'protein': 4.0, 'carbs': 12.0, 'fat': 1.0},
    'cottage cheese with fruit': {'protein': 10.0, 'carbs': 5.0, 'fat': 2.0},
    'grilled chicken breast with sweet potato and broccoli': {'protein': 30.0, 'carbs': 35.0, 'fat': 5.0},
    'turkey slices with whole grain crackers': {'protein': 20.0, 'carbs': 22.0, 'fat': 4.0},
    'salmon fillet with quinoa and asparagus': {'protein': 25.0, 'carbs': 30.0, 'fat': 10.0},
    'vegan protein smoothie with almond milk': {'protein': 20.0, 'carbs': 10.0, 'fat': 5.0},
    'mixed nuts and seeds': {'protein': 6.0, 'carbs': 8.0, 'fat': 15.0},
    'lentil soup with whole grain bread': {'protein': 12.0, 'carbs': 45.0, 'fat': 2.0},
    'hummus with raw vegetables': {'protein': 5.0, 'carbs': 15.0, 'fat': 6.0},
    'stir-fried tempeh with brown rice and mixed vegetables': {'protein': 20.0, 'carbs': 60.0, 'fat': 10.0},
    'oatmeal with nuts and dried fruits': {'protein': 8.0, 'carbs': 60.0, 'fat': 10.0},
    'avocado toast': {'protein': 3.0, 'carbs': 15.0, 'fat': 10.0},
    'banana with peanut butter': {'protein': 4.0, 'carbs': 30.0, 'fat': 10.0},
    'bean burritos with guacamole and salsa': {'protein': 15.0, 'carbs': 60.0, 'fat': 15.0},
    'trail mix with dried fruits and dark chocolate': {'protein': 6.0, 'carbs': 45.0, 'fat': 20.0},
    'vegetable stir-fry with tofu and quinoa': {'protein': 20.0, 'carbs': 50.0, 'fat': 10.0},
    'protein pancakes with berries': {'protein': 10.0, 'carbs': 30.0, 'fat': 5.0},
    'eggs with whole grain toast': {'protein': 12.0, 'carbs': 15.0, 'fat': 10.0},
    'greek yogurt with honey and granola': {'protein': 15.0, 'carbs': 50.0, 'fat': 8.0},
    'chicken and rice bowl with vegetables': {'protein': 25.0, 'carbs': 60.0, 'fat': 10.0},
    'beef jerky with cheese and crackers': {'protein': 20.0, 'carbs': 15.0, 'fat': 15.0},
    'grilled steak with baked potato and green beans': {'protein': 30.0, 'carbs': 50.0, 'fat': 15.0},
    'smoothie bowl with plant-based protein powder': {'protein': 20.0, 'carbs': 40.0, 'fat': 10.0},
    'chia seed pudding with coconut milk': {'protein': 8.0, 'carbs': 20.0, 'fat': 10.0},
    'quinoa salad with black beans and avocado': {'protein': 12.0, 'carbs': 50.0, 'fat': 15.0},
    'nut butter sandwich with banana': {'protein': 8.0, 'carbs': 45.0, 'fat': 15.0},
    'vegan pasta with tofu and tomato sauce': {'protein': 20.0, 'carbs': 70.0, 'fat': 10.0},
    'greek yogurt with berries': {'protein': 10.0, 'carbs': 20.0, 'fat': 5.0},
    'whole grain cereal with almond milk': {'protein': 8.0, 'carbs': 50.0, 'fat': 5.0},
    'apple slices with almond butter': {'protein': 2.0, 'carbs': 25.0, 'fat': 10.0},
    'vegetable soup with whole grain bread': {'protein': 8.0, 'carbs': 40.0, 'fat': 2.0},
    'edamame with sea salt': {'protein': 11.0, 'carbs': 13.0, 'fat': 5.0},
    'roasted vegetables with quinoa': {'protein': 12.0, 'carbs': 50.0, 'fat': 5.0},
    'scrambled eggs with spinach': {'protein': 12.0, 'carbs': 2.0, 'fat': 10.0},
    'whole wheat toast': {'protein': 4.0, 'carbs': 20.0, 'fat': 2.0},
    'cottage cheese with pineapple': {'protein': 10.0, 'carbs': 15.0, 'fat': 2.0},
    'grilled chicken salad with vinaigrette': {'protein': 25.0, 'carbs': 10.0, 'fat': 15.0},
    'turkey and cheese roll-ups': {'protein': 20.0, 'carbs': 5.0, 'fat': 10.0},
    'baked fish with steamed vegetables': {'protein': 25.0, 'carbs': 10.0, 'fat': 5.0},
    'fruit salad with nuts': {'protein': 5.0, 'carbs': 30.0, 'fat': 10.0},
    'rice cakes with avocado': {'protein': 3.0, 'carbs': 25.0, 'fat': 10.0},
    'chickpea salad with lemon tahini dressing': {'protein': 15.0, 'carbs': 40.0, 'fat': 10.0},
    'vegetable sticks with hummus': {'protein': 5.0, 'carbs': 20.0, 'fat': 8.0},
    'stir-fried tofu with mixed vegetables': {'protein': 20.0, 'carbs': 20.0, 'fat': 10.0}
}

if __name__ == "__main__":
    prepare_diet()
