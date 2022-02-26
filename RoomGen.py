'''
Code used to generate 3d(ish) ASCII rooms 
'''
import random

def ascii_room(depth: int, width: int, height: int, top_down: bool) -> str:
    output = ''
    if top_down:
        output += depth * ('_') + (width + 2) * (' ') + depth * ('_') + '\n'
    else:
        for i  in range(depth):
            output += (''.join([wall_lines(j) for j in range(i)])) + '\\' + 2 * (depth - i) * (' ') + (width) * (' ') + '/' + (''.join([wall_lines(j) for j in range(i)]))[::-1] + '\n'

    for i in range(height):
        output += (''.join([wall_lines(j) for j in range(depth)])) + '|' + width * ('#') + '|' + (''.join([wall_lines(j) for j in range(depth)]))[::-1] + '\n'

    for i  in range(depth, 0, -1):
        output += (''.join([wall_lines(j) for j in range(i - 1)])) + '/' + 2 * (depth - i) * (' ') + (width + 2) * (' ') + '\\' + (''.join([wall_lines(j) for j in range(i - 1)]))[::-1] + '\n'

    return output

def wall_lines(i: int):
    if i % 2 == 0:
        return '|'
    return ' '

def texture(apply_to: str, c: str, p: int) -> str: # c is a char texture, p is probability of c appearing, [0 <= p <= 100]
    output = apply_to
    for i in range(len(output) - 1):
        if(output[i : i+1] == ' '):
            if random.randrange(100) <= p:
                output = output[:i] + c + output[i + 1:]
    return output

def __main__():
    r = texture(ascii_room(4, 50, 10, False), '.', 5)
    print(r)
    with open("room.txt", "w") as f:
        f.write(r)

if __name__ == '__main__':
    __main__()