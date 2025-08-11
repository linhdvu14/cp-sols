''' Robot Programming Strategy 
https://codingcompetitions.withgoogle.com/codejam/round/00000000000516b9/0000000000134c90
'''
def repeat_to_length(s, wanted):
    return (s * (wanted//len(s) + 1))[:wanted]


def solve(moves):
    LEN = 500*256
    seen = [set() for _ in range(LEN)]

    for move in moves:
        move = repeat_to_length(move, LEN)
        for i, c in enumerate(move):
            seen[i].add(c)

    out = ''
    for i, s in enumerate(seen):
        if len(s) == 3:
            return 'IMPOSSIBLE'
        if len(s) == 2:
            if 'R' not in s:
                out += 'S'
            elif 'P' not in s:
                out += 'R'
            elif 'S' not in s:
                out += 'P'

        if len(s) == 1:
            if 'R' in s:
                out += 'P'
            elif 'P' in s:
                out += 'S'
            elif 'S' in s:
                out += 'R'
            return out

    return 'IMPOSSIBLE'


def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())

    for t in range(T):
        A = int(stdin.readline().strip())
        moves = []
        for _ in range(A):
            moves.append(stdin.readline().strip())
        out = solve(moves)
        print('Case #{}: {}'.format(t+1, out))
 

if __name__ == '__main__':
    main()