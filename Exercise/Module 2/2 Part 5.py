
talent = float(input("Enter talents: "))
tp = float((talent * 20)*32)*13.3
pound = float(input("Enter pounds: "))
pl = float(pound*32)*13.3
lot = float(input("Enter lots: "))
lg = float(lot*13.3)

total_grams = tp + pl + lg

kg = int(total_grams // 1000)
g = (total_grams % 1000)

print(f"The weight in modern units is {kg} kg {g:.2f} g")