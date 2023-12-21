class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = {}
        self.ttl = timeToLive
        self.token_self = deque()

    def generate(self, tokenId: str, currentTime: int) -> None:
        endTime = currentTime + self.ttl
        self.tokens[tokenId] = endTime
        self.token_self.append((endTime, tokenId))

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens:
            return
        if self.tokens[tokenId] <= currentTime:
            while self.token_self and self.token_self[0][0] <= currentTime:
                exp, tok = self.token_self.popleft()
                del self.tokens[tok]
            return
        idx = 0
        while self.token_self[idx][1] != tokenId:
            idx += 1
        del self.token_self[idx]
        del self.tokens[tokenId]
        self.generate(tokenId, currentTime)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.token_self and self.token_self[0][0] <= currentTime:
                exp, tok = self.token_self.popleft()
                del self.tokens[tok]
        return len(self.token_self)


        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)