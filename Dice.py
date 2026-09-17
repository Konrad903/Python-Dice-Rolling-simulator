from random import *
def roll():
 no=randint(1,6)
 if(no==1):
    print("       [---------]\n" \
    "       |         |\n" \
    "       |    o    |\n" \
    "       |         |\n" \
    "       [---------]")
 if(no==2):
    print("       [---------]\n" \
    "       |o        |\n" \
    "       |         |\n" \
    "       |        o|\n" \
    "       [---------]")
 if(no==3):
    print("       [---------]\n" \
    "       |o        |\n" \
    "       |    o    |\n" \
    "       |        o|\n" \
    "       [---------]")
 if(no==4):
    print("       [---------]\n" \
    "       |o       o|\n" \
    "       |         |\n" \
    "       |o       o|\n" \
    "       [---------]")
 if(no==5):
    print("       [---------]\n" \
    "       |o       o|\n" \
    "       |    o    |\n" \
    "       |o       o|\n" \
    "       [---------]")
 if(no==6):
    print("       [---------]\n" \
    "       |o       o|\n" \
    "       |o       o|\n" \
    "       |o       o|\n" \
    "       [---------]")
roll()
ans=input(" 'Would you like to roll again\nType 'y' or 'n' ")
if(ans=='y'):
   roll()
else:
   print('\n')