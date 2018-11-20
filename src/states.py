class States:
    def __init__(self):
        self.total_open = 0
        self.max_rep = 0
        self.current_rep = 0

    def add_rep(self, n):
        self.current_rep += n
        if self.current_rep > self.max_rep:
            self.max_rep = self.current_rep
