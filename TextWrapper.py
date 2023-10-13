def wrap(string, max_width):
    para = ''
    while len(string) > 0:
        if len(string) < max_width:
            para += string + '\n'
            string = ''
        para += string[:max_width] + '\n'
        string = string[max_width:]
        
    return para
(* def wrapbuiltin(string, max_width):
  return textwrap.fill(string, max_width) *)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
