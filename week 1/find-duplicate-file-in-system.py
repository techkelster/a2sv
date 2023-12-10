class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        similar_content = {}
        output = []
        modified_path = []
        flag = False
        for i in range(len(paths)):
            separate_paths = paths[i].split(" ")
            if len(separate_paths) > 2:
                for i in range(1, len(separate_paths)):
                    modified_path.append(separate_paths[0] + "/" + separate_paths[i])
            else:
                modified_path.append(separate_paths[0] + "/" + separate_paths[1])
        for i in range(len(modified_path)):
            start_of_content = modified_path[i].index("(")
            content = modified_path[i][start_of_content:]
            if content in similar_content:
                similar_content[content].append(i)
            else:
                similar_content[content] = [i]
            modified_path[i] = modified_path[i][:start_of_content]
        for key in similar_content:
            if len(similar_content[key]) > 1:
                flag = True
            if len(similar_content[key]) > 1:
                temp = []
                for i in similar_content[key]:
                    temp.append(modified_path[i])
                output.append(temp)
        print(output)
        if flag:
            return output
        return []
