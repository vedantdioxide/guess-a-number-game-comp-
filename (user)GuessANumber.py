import random 
guess=0


def computer_guess(x):
   low = 1
   high = x 
   feedback = ''
   while feedback != 'c':
      guess = random.randint(low,high)
      if low != high:
        guess = random.randint(low,high)
      else :
          low = high
   
      feedback = input(f'Is {guess} too high (H), too low (L),correct (C)').lower()
      if feedback == 'h':
            high = guess - 1
      elif feedback == 'l':
            low = guess + 1
        
   print(f'yayyyy!!!! you have guessed the {guess} correctly')

computer_guess(3)