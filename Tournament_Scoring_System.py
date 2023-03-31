import PySimpleGUI as sg
sg.theme("darkAmber")

#Dictionary to store team and individual scores
teams = {}
individuals = {}

#Function to add teams
def add_team():
    team = sg.PopupGetText("Enter team name:")
    teams[team] = []

    #Uses loop to collect team members
    for i in range(5):
        member = sg.PopupGetText("Enter team member {} name:".format(i + 1))
        teams[team].append(member)

    #Getting how many events per player
    try:
        numEvents = int(sg.PopupGetText("How many events per player? Enter a number between 1-5"))
    except ValueError:
        sg.popup("Only enter a number between 1-5")
                    

    #Uses loop to collect scores for events
    for i in range(numEvents):
        score = sg.PopupGetText("Enter score for event {}:".format(i + 1))

        #Catches invalid inputs 
        try:
            score = int(score)
            if score >= 0:
                teams[team].append(score)
            else:
                sg.Popup("Invalid score. Please enter a positive number")  
        except ValueError:
            sg.Popup("Invalid score. Please enter a valid number")

#Function to add individuals
def add_individual():
    individual = sg.PopupGetText("Enter individual player name:")
    individuals[individual] = []

    #Getting how many events per player
    try:
        numEvents = int(sg.PopupGetText("How many events per player? Enter a number between 1-5"))
    except ValueError:
        sg.popup("Only enter a number between 1-5")

    #Loop for 5 events getting scores
    for i in range(numEvents):
        score = sg.PopupGetText("Enter score for event {} for {}:".format(i + 1, individual))

        #Catches invalid inputs
        try:
            score = int(score)
            if score >= 0:
                individuals[individual].append(score)
            else:
                sg.Popup("Invalid score. Please enter a positive number")  
        except ValueError:
            sg.Popup("Invalid score. Please enter a valid number.")

#Main layout
layout = [
    [sg.Text("Enter as team or individual:", font=("Helvetica", 20))],
    [sg.Button("Team", font=("Helvetica", 16)), sg.Button("Individual", font=("Helvetica", 16))]
]

#Creates main window
window = sg.Window("Tournament Scoring System", layout, size=(400, 200))

#Selection. Individual or Team 
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Team":
        for i in range(5):
            add_team()
        break
    elif event == "Individual":
        for i in range(20):
            add_individual()
        break

#Calculates the total score of each team then append to list
for team, scores in teams.items():
    total_score = sum(scores[5:])
    teams[team].append(total_score)

#Calculate the total score of each individual then append to list
for individual, scores in individuals.items():
    total_score = sum(scores)
    individuals[individual].append(total_score)

#Sorts teams from highest to lowest score
sorted_teams = sorted(teams.items(), key=lambda x: x[1][-1], reverse=True)

#Creates the team leaderboard
team_leaderboard = "Team Leaderboard:\n\n"
for i, (team, scores) in enumerate(sorted_teams):
    team_leaderboard += "{}. {} ({})\n".format(i + 1, team, scores[-1])

#Sorts individual participants from highest to lowest score
sorted_individuals = sorted(individuals.items(), key=lambda x: x[1][-1], reverse=True)

#Creates the individual leaderboard 
individual_leaderboard = "Individual Leaderboard:\n\n"
for i, (individual, scores) in enumerate(sorted_individuals):
    individual_leaderboard += "{}. {} ({})\n".format(i + 1, individual, scores[-1])



with open("scoresData", "w") as file:

    #display the team leaderboard and appends sorted teams to file
    if event == "Team":
        sg.popup(team_leaderboard)
        file.write(str(sorted_teams))

    #display the individual leaderboard and appends sorted individuals to file
    elif event == "Individual":
        sg.popup(individual_leaderboard)
        file.write(str(sorted_individuals))

