def introduction():
    print("Welcome to the treasure hunt game !!")
    print("your goal is simple, you'll have to earn 3 keys in order to be able to open our wonderful treasure room.")
    print("You'll go through various challenges which will test your abilities !")
    print("good luck..")
    return


def compose_equipe():
    n = 0
    lc = 0
    n = int(input("Enter the number of player ! reminder, it must be between 1 and 3 : "))
    while n < 1 or n > 3:
        print("Error, the number of player must be between 1 and 3.")
        n = int(input("Enter the number of player ! reminder, it must be between 1 and 3 : "))
    team = []
    for i in range(n):
        print(f"Enter the player {i+1} information :")
        name = input("name : ")
        profession = input("profession : ")
        is_leader = str(input("Is this person the leader ? (Yes/No): "))
        if is_leader == "Yes" or is_leader == "yes" or is_leader == "Y" or is_leader == "y":
            if lc < 1:
                leader = True
                lc += 1
        else :
            leader = False

        player = {'name':name,'profession':profession,'leader':leader,'keys':0}
        team.append(player)

    if lc == 0:
        print("there is no leader to this team, so, the first player of the team will be declared the leader")
        team[0]['leader'] = True
    return team

def challenge_menu():
    print("menu : ")
    print("1. mathematics challenges")
    print("2. logic challenges")
    print("3. chance challenges")
    print("4. pere fouras' riddle")

    c = int(input("Select which task you wanna perform first : "))
    return c

def choose_player(team):
    for i in range(len(team)):
        if team[i]['leader'] == True:
            status="Leader"
        else :
            status="member"
        print(f"{i+1}. {team[i]['name']} {team[i]['profession']} - {status}")

    n = int(input("Enter the number of the player you'd like to select : "))
    while n < 0 or n > len(team):
        n = int(input("Enter the number of the player you'd like to select : "))

    for i in range(len(team)):
        if n-1 == i :
            return team[i]