print("""
       __________
        /\____;;___\\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
""")

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_or_right = input("what path do you choose right or left? ").lower()
if left_or_right == "left":
    swim_or_wait = input("do you prefer swim or wait? ").lower()
    if swim_or_wait == "wait":
        door = input("Which door do you choose; red, yellow or blue? ")
        if door == "yellow":
            print('You win!!')
        elif door == "red":
            print("Burned by fire... Game over")
        elif door == "blue":
            print("Eaten by beasts.. Game Over")
        else:
            print("Game over")
    else:
        print("attacked by trout... Game Over")
else:
    print("fall into a hole... Game over")

