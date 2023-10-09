if __name__ == '__main__':
    me = []
    N = int(input())
    for i in range(N):
        com = input().split()
        if len(com) == 1:
            if com[0] == "print":
                print(me)
            elif com[0] == "pop":
                me.pop()
            elif com[0] == "sort":
                me.sort()
            else:
                me.reverse()
        elif len(com) == 2:
            if com[0] == "remove":
                me.remove(int(com[1]))
            else:
                me.append(int(com[1]))
        else:
            me.insert(int(com[1]), int(com[2]))
            
