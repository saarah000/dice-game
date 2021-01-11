import random
import time
userpass = True
rounds = 0

def login(userpass): #login
    while userpass == True:
        login.player1 = input("Player 1, please enter your username: ")
        pass1 = input("Please enter your password: ")
        if pass1 == str("Hello123"):
            print("Welcome,",login.player1)
        else:
            print("Error. You are not an authorised player. Please try again.")#try again
            login.player1 = input("Player 1, please enter your username: ")
            pass1 = input("Please enter your password: ")
            if pass1 != ("Hello123"):
                print("Error. You are not an authorised player.")
                quit()

        login.player2 = input("Player 2 please enter your username: ")
        pass2 = input("Please enter your password: ")
        if pass2 == str("Pas5word"):
            print("Welcome,",login.player2)
        else:
            print("Error. You are not an authorised player. Please try again.")
            login.player2 = input("Player 2 please enter your username: ")
            pass2 = input("Please enter your password: ")
            if pass1 != ("Pas5word"):
                print("Error. You are not an authorised player.")
                quit()
        return login.player1, login.player2
        userpass = False

def play1():
    global score1
    time.sleep(2)
    print(" ")
    print(login.player1,",it is your turn:")
    time.sleep(3)
    play1.roll1 = random.randint(1,6)
    print("You rolled a",play1.roll1)#roll first die
    time.sleep(3)
    play1.roll2 = random.randint(1,6)
    print("You rolled a",play1.roll2)#roll second die
    time.sleep(2)
    points1 = int(play1.roll1 + play1.roll2)#add points up
    if (points1 % 2) == 0:#if even number
            time.sleep(2)
            print("Your total points are",points1,". Even number, add 10 points!")
            points1 = points1 + 10#add 10 points
            score1 = score1 + points1 
            if play1.roll1 == play1.roll2:#if doubles rolled
                time.sleep(2)
                print("You scored doubles! Roll again!")
                play1.roll6 = random.randint(1,6)
                print("You rolled a",play1.roll6)
                score1 = score1 + play1.roll6#add third roll
                return
            else:
                time.sleep(2)
            print ("Your current score is" ,score1)
    else:#if odd number
        time.sleep(2)
        print("Your total points are",points1,". Odd number, you lose 5 points :(")
        points1 = points1 - 5
        score1 = score1 + points1
        if play1.roll1 == play1.roll2:#if doubles rolled
            time.sleep(2)
            print("You scored doubles! Roll again!")
            play1.roll6 = random.randint(1,6)
            print("You rolled a",play1.roll6)
            score1 = score1 + play1.roll6#add third roll
            return
        else:
            time.sleep(2)
        print("Your current score is" ,score1)
    return score1

def play2():
    global score2
    time.sleep(2)
    print(" ")
    print(login.player2,",it is your turn:")
    time.sleep(3)
    play2.roll3 = random.randint(1,6)
    print("You rolled a",play2.roll3)#roll first die
    time.sleep(3)
    play2.roll4 = random.randint(1,6)
    print("You rolled a",play2.roll4)#roll second die
    time.sleep(2)
    points2 = int(play2.roll3 + play2.roll4)#add points up
    if (points2 % 2) == 0:#if even number
        time.sleep(2)
        print("Your total points are",points2,". Even number, add 10 points!")
        points2 = points2 + 10#add 10 points
        score2 = score2 + points2
        if play2.roll3 == play2.roll4:#if doubles rolled
                time.sleep(2)
                print("You scored doubles! Roll again!")
                play2.roll5 = random.randint(1,6)
                print("You rolled a",play2.roll5)
                score2 = score2 + play2.roll5#add third roll
        else:
                time.sleep(2)
        print("Your current score is", score2)
    else:#if odd number
        time.sleep(2)
        print("Your total points are",points2,". Odd number, you lose 5 points :(")#take away 5 points
        points2 = points2 - 5
        score2 = score2 + points2
        if play2.roll3 == play2.roll4:#if doubles rolled
            time.sleep(2)
            print("You scored doubles! Roll again!")
            play2.roll5 = random.randint(1,6)
            print("You rolled a",play2.roll5)
            score2 = score2 + play2.roll5#add third roll
            return
        else:
            time.sleep(2)
        print ("Your current score is" ,score2)
    return score2

player1, player2 = login(userpass)
score1 = 0
score2 = 0
points1 = play1()
points2 = play2()
for i in range (1,5):
    play1()
    play2()
    score1 = play1()
    score2 = play2()
    if score1 <=  0:
        print("Your score is below 0. Game Over.")
        quit()
    elif score2 <= 0:
        print("Your score is below 0. Game Over.")
        quit()
    else:
        ()
    print(login.player1,", your current total score is",score1)
    print(login.player2,", your current total score is",score2)
    rounds = rounds + 1
    while rounds >= 5:
        if score1 > score2:
            print(login.player1, "wins with a score of", score1)
            winner1 = [login.player1,score1]
            high_scores = open("Leaderboard.txt","a")
            high_scores.append(winner1)
            high_scores.close()
        elif score1< score2:
            print(login.player2, "wins with a score of",score2)
            winner2 = [login.player2,score2]
            high_scores = open("Leaderboard.txt","a")
            high_scores.append(winner2)
            high_scores.close()
        elif score1 == score2:
            roll7 = random.randint(1,6)
            roll8 = random.randint(1,6)
            if roll7 > roll8:
                print(login.player1,"wins")
                winner1 = [login.player1,score1]
                high_scores = open("Leaderboard.txt","a")
                high_scores.append(winner1)
                high_scores.close()
            else:
                print(login.player2,"wins")
                winner2 = [login.player2,score2]
                high_scores = open("Leaderboard.txt","a")
                high_scores.append(winner2)
                high_scores.close()
        break
    else:
        break

high_scores = open("Leaderboard.txt","r")
print(high_scores.readlines())
