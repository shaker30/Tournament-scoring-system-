class TournamentManager:
    def __init__(self):
        self.teams = {}  # Format: {team_name: [member_names]}
        self.individuals = []  # List of individual participant names
        self.events = {}  # Format: {event_name: {"type": "team/individual", "participants": [], "scores": {}}}
        self.team_limit = 4
        self.individual_limit = 20

    def register_team(self, team_name, member_names):
        if len(self.teams) < self.team_limit and team_name not in self.teams:
            self.teams[team_name] = member_names
            return True
        return False

    def register_individual(self, name):
        if len(self.individuals) < self.individual_limit and name not in self.individuals:
            self.individuals.append(name)
            return True
        return False

    def add_event(self, event_name, event_type):
        if event_name not in self.events:
            self.events[event_name] = {"type": event_type, "participants": [], "scores": {}}
            return True
        return False

    def record_score(self, event_name, participant, score):
        if event_name in self.events:
            self.events[event_name]["scores"][participant] = score
            return True
        return False

    def calculate_rankings(self, event_name):
        scores = self.events[event_name]["scores"]
        # Sorting participants based on scores in descending order
        rankings = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return rankings

# Example usage
tournament_manager = TournamentManager()
tournament_manager.register_team("Team A", ["Alice", "Bob", "Charlie", "David", "Eve"])
tournament_manager.register_individual("Zara")
tournament_manager.add_event("Math Quiz", "individual")
tournament_manager.record_score("Math Quiz", "Zara", 95)

# To calculate and print rankings for an event
rankings = tournament_manager.calculate_rankings("Math Quiz")
print(rankings)
