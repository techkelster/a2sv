class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        self.history = [*self.history[:self.cur + 1], url]
        self.cur += 1

    def back(self, steps: int) -> str:
        while self.cur > 0 and steps > 0:
            self.cur -= 1
            steps -= 1
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        while self.cur < len(self.history) - 1 and steps > 0:
            self.cur += 1
            steps -= 1
        return self.history[self.cur]
