class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
        self.best_score = max(self.scores)
        self.latest_score = self.scores[-1]
        self.sorted = self.scores[:]
        self.sorted.sort()
        self.sorted.reverse()

    def latest(self):
        return self.latest_score

    def personal_best(self):
        return self.best_score

    def personal_top(self):
        return self.sorted[:3]

    def report(self):
        latest = self.latest()
        best = self.personal_best()
        if latest == best:
            return "Your latest score was {}. That's your personal best!".format(latest)
        else:
            return "Your latest score was {}. That's {} short of your personal best!".format(latest, best - latest)
