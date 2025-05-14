#Write to check if a person is buying oranges at 100 rs and later selling it at 120 rs. Find that he has profit or loss?
B=int(input("Enter the buying price : "))
S=int(input("Enter the selling price : "))
if B>S:
    print("You made loss of Rs.",B-S)
else:
    print("You made profit of Rs.",S-B)