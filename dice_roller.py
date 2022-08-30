import random
def main():
  print('You rolled a die')
  
  dice_rolls = 2
  l = random.randint(1,6)
  print(f"You rolled a {l}")
  
  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    print(f'You rolled a {roll}')

if __name__== "__main__":
  main()
