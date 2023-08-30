def calculate_result(masse, poussee, vent, stabilite, gravite):
    if None in (masse, poussee, vent, stabilite, gravite):
        raise ValueError("All input values are mandatory")

    result = ((poussee + vent) * masse + gravite ** 2) / stabilite
    return result

try:
    masse = float(input("masse: "))
    poussee = float(input("poussee: "))
    vent = float(input("vent: "))
    stabilite = float(input("stabilite: "))
    gravite = float(input("gravite: "))
    
    result = calculate_result(masse, poussee, vent, stabilite, gravite)
    print("Result:", result)
except ValueError as e:
    print("Error:", e)
