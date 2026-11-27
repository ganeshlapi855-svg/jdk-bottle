def calculate_material(bottles, material_per_bottle):
    if bottles <= 0 or material_per_bottle <= 0:
        raise ValueError("Values must be positive")

    total_grams = bottles * material_per_bottle
    total_kg = total_grams / 1000
    return total_kg


if __name__ == "__main__":
    bottles = int(input("Enter Number of Bottles: "))
    material = float(input("Enter Raw Material per Bottle (grams): "))

    try:
        total = calculate_material(bottles, material)
        print("\n------ BOTTLE PRODUCTION DETAILS ------")
        print("Number of Bottles:", bottles)
        print("Material per Bottle:", material, "grams")
        print("Total Raw Material Required:", total, "kg")
    except ValueError as e:
        print("Error:", e)        