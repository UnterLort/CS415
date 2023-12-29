# @Kyle Stewart @team_points.py version 1

def compute_team_points(rosters, player_points):
    # Make an empty dictionary
    team_points = {}

    # Add each team to the dictionary
    for team, players in rosters.items():
        # Make the total points 0
        total_points = 0
        # Add each player in the roster of the current team
        for player, points in player_points:
            # Check if the player's name is in the roster of the current team
            if player in players:
                # Add the points scored by that player to the total points for the current team
                total_points += points

        # Add the team name and total points to the dictionary
        team_points[team] = total_points

    # Return team points
    return team_points


# List what is in the dictionary rosters
rosters = {
    'Storm': ['Jewell Loyd'],
    'Mercury': ['Skylar Diggins-Smith', 'Diana Taurasi'],
    'Liberty': ['Natasha Howard', 'Breanna Stewart'],
    'Aces': []
}
# Make a list called player points that tracks the points
player_points = [
    ('Breanna Stewart', 34), ('Jewell Loyd', 24), ('Natasha Howard', 15), ('Diana Taurasi', 22)
]

# Calculates the total points with player points and the rosters
team_points = compute_team_points(rosters, player_points)
print(team_points)
