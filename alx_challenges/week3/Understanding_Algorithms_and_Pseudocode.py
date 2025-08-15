#Challenge
# You’re cleaning your closet and have a giant pile of dirty clothes! Unfortunately, the washing machine only washes a limited number of clothes at a time. To maximize efficiency, you need to sort the clothes into separate piles based on color (lights, darks) before washing.
# Write the algorithm, pseudocode the solution and anaylze the complexity ### Bonus Challenge:
# Can you modify the pseudocode to sort the clothes by type (shirts, pants, socks) as well as color? How would this change the complexity?
# Lists to hold sorted clothes
pile_lights = []
pile_darks = []

# Function to sort clothes into light and dark piles
def clothes_colors(clothes):
    for item in clothes:
        if item["color"] == "light":
            pile_lights.append(item)
        elif item["color"] == "dark":
            pile_darks.append(item)
    return pile_lights, pile_darks

# Collect clothes from user
clothes = []
num = int(input("How many clothes do you want to sort? "))
for i in range(num):
    name = input(f"Enter the name of cloth #{i+1}: ")
    color = input(f"Enter the color of '{name}' (light/dark): ").strip().lower()
    if color not in ["light", "dark"]:
        print("Invalid color. Please enter 'light' or 'dark'.")
        continue
    clothes.append({"name": name, "color": color})

# Sort clothes and display results
lights, darks = clothes_colors(clothes)
print("\nLight-colored clothes:", [item["name"] for item in lights])
print("Dark-colored clothes:", [item["name"] for item in darks])