#  MAGIC BALL 8 LOOK ABSP13 FOR PREVIOUS VERSION

# USING LIST

import random

MyMistake = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(MyMistake[random.randint(0, len(MyMistake) - 1)]) # Example version

print(random.choice(MyMistake)) # My version