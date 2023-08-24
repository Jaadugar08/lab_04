class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing


def get_match_list(match_list):
    print("Match List:")
    for match in match_list:
        print(f"{match.location} - {match.team1} vs {match.team2} - {match.timing}")


def search_match_by_team(match_list, team_name):
    print(f"Matches for team {team_name}:")
    for match in match_list:
        if match.team1 == team_name or match.team2 == team_name:
            print(f"{match.location} - {match.team1} vs {match.team2} - {match.timing}")


def search_match_by_location(match_list, location):
    print(f"Matches in {location}:")
    for match in match_list:
        if match.location == location:
            print(f"{match.location} - {match.team1} vs {match.team2} - {match.timing}")


def search_match_by_timing(match_list, timing):
    print(f"Matches with timing {timing}:")
    for match in match_list:
        if match.timing == timing:
            print(f"{match.location} - {match.team1} vs {match.team2} - {match.timing}")


def main():
    match_list = [
        Match("Mumbai", "India", "Sri Lanka", "DAY"),
        Match("Delhi", "England", "Australia", "DAY-NIGHT"),
        Match("Chennai", "India", "South Africa", "DAY"),
        Match("Indore", "England", "Sri Lanka", "DAY-NIGHT"),
        Match("Mohali", "Australia", "South Africa", "DAY-NIGHT"),
        Match("Delhi", "India", "Australia", "DAY"),
    ]

    print("Select the search option:")
    print("1. List of all the matches of a Team")
    print("2. List of Matches on a Location")
    print("3. List of Matches based on timing")

    option = int(input("Enter your option: "))

    if option == 1:
        team_name = input("Enter the team name: ")
        search_match_by_team(match_list, team_name)
    elif option == 2:
        location = input("Enter the location: ")
        search_match_by_location(match_list, location)
    elif option == 3:
        timing = input("Enter the timing: ")
        search_match_by_timing(match_list, timing)
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()=
