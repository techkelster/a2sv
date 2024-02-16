class Solution:
    def simplifyPath(self, path: str) -> str:
        answer = []
        path = path.split("/") 
        for dira in path:
            if dira == "..":
                if answer:
                    answer.pop()
            elif dira == '.' or dira == "":
                continue
            else:
                answer.append(dira)
        return "/" + "/".join(answer)

        