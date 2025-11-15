susu_savings = {"Akosua":200, "Ama":150, "Adwoa":300}
print("="*20, "Current Balance", "="*20)

for name, amount in susu_savings.items():
    print(f"{name}: {amount}")
print("="*40)
print("UPDATE SAVINGS")
print()
woman_name = input("Enter woman's name: ")
new_amount = int(input("Enter new amount: "))
susu_savings[woman_name] = new_amount
print(f"\n {woman_name}'s savings updated to: {new_amount}")

print("="*50)
print("UPDATED SUSU SAVINGS: ")
print("="*50)
for name, amount in susu_savings.items():
    print(f"{name}: {amount}")