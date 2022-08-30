import random
def main():
  #print('You rolled a die')
  
  dice_rolls = 2
  dice_sum = 0
  
  #l = random.randint(1,6)
  #print(f"You rolled a {l}")
  
  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    print(f'You rolled a {roll}')
    dice_sum = dice_sum + rol
    
  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()
