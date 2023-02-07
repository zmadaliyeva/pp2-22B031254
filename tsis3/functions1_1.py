#ounces = int(input())grams = int (input())ounces = 28.3495231 * gramsprint(ounces)
def ounces_to_grams(weight):
    new = weight * 20.3495
    return new

weight_in_ounces = int(input())

weight_in_grams = ounces_to_grams(weight_in_ounces)

print(f"{weight_in_grams}g")