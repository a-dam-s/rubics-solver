MOVE_MAP = {0: 'U', 1: "U'", 2: 'U2', 3: 'D', 4: "D'", 5: 'D2', 6: 'L', 7: "L'", 8: 'L2', 9: 'R', 10: "R'", 11: 'R2', 12: 'F', 13: "F'", 14: 'F2', 15: 'B', 16: "B'", 17: 'B2'}

def is_solved(state: int) -> bool:
    return state in SOLVED_STATES

def is_same_piece(piece1: str, piece2: str) -> bool:
    return sorted(piece1) == sorted(piece2)

def get_piece(state: int, index: int) -> int:
    state >>= 5*(7-index)
    state %= 32
    return state

def get_orientation(piece: int) -> int:
    return piece % 4

def get_position(piece: int) -> int:
    return piece >> 2



def convert_colors_to_code(colors: str) -> int:
    colors = colors.lower()
    if len(colors) != 24:
        return -1
    allowed = "wygbro"
    if not all(ch in allowed for ch in colors):
        return -1
    pieces = ["" for _ in range(8)]
    pieces[0] = colors[0] + colors[4] + colors[17]
    pieces[1] = colors[1] + colors[16] + colors[13]
    pieces[2] = colors[2] + colors[12] + colors[9]
    pieces[3] = colors[3] + colors[8] + colors[5]
    pieces[4] = colors[20] + colors[6] + colors[11]
    pieces[5] = colors[21] + colors[10] + colors[15]
    pieces[6] = colors[22] + colors[14] + colors[19]
    pieces[7] = colors[23] + colors[18] + colors[7]

    solved = ["wbo", "wbr", "wgr", "wgo", "ygo", "ygr", "ybr", "ybo"]

    total_orientation = 0

    result = 0
    for p in pieces:
        for t in solved:
            if is_same_piece(p, t):
                orientation = 0 if p[0] in "wy" else (1 if p[1] in "wy" else 2)
                total_orientation += orientation
                result *= 32
                result += solved.index(t)*4 + orientation
                break
        else:
            return -1
    if (total_orientation%3 != 0):
        print("This scramble is unslovable!")
        return -1
    return result

SOLVED_STATES = {convert_colors_to_code("wwwwooooggggrrrrbbbbyyyy"),
              convert_colors_to_code("wwwwggggrrrrbbbbooooyyyy"),
              convert_colors_to_code("wwwwrrrrbbbbooooggggyyyy"),
              convert_colors_to_code("wwwwbbbbooooggggrrrryyyy"),
              convert_colors_to_code("yyyyrrrrggggoooobbbbwwww"),
              convert_colors_to_code("yyyyggggoooobbbbrrrrwwww"),
              convert_colors_to_code("yyyyoooobbbbrrrrggggwwww"),
              convert_colors_to_code("yyyybbbbrrrrggggoooowwww"),
              convert_colors_to_code("ggggooooyyyyrrrrwwwwbbbb"),
              convert_colors_to_code("ggggyyyyrrrrwwwwoooobbbb"),
              convert_colors_to_code("ggggrrrrwwwwooooyyyybbbb"),
              convert_colors_to_code("ggggwwwwooooyyyyrrrrbbbb"),
              convert_colors_to_code("rrrrggggyyyybbbbwwwwoooo"),
              convert_colors_to_code("rrrryyyybbbbwwwwggggoooo"),
              convert_colors_to_code("rrrrbbbbwwwwggggyyyyoooo"),
              convert_colors_to_code("rrrrwwwwggggyyyybbbboooo"),
              convert_colors_to_code("bbbbrrrryyyyoooowwwwgggg"),
              convert_colors_to_code("bbbbyyyyoooowwwwrrrrgggg"),
              convert_colors_to_code("bbbboooowwwwrrrryyyygggg"),
              convert_colors_to_code("bbbbwwwwrrrryyyyoooogggg"),
              convert_colors_to_code("oooobbbbyyyyggggwwwwrrrr"),
              convert_colors_to_code("ooooyyyyggggwwwwbbbbrrrr"),
              convert_colors_to_code("ooooggggwwwwbbbbyyyyrrrr"),
              convert_colors_to_code("oooowwwwbbbbyyyyggggrrrr"),
              }

def cw(piece: int) -> int:
    o = get_orientation(piece)
    piece &= 0b111100
    return piece | ((o+1)%3)

def ccw(piece: int) -> int:
    o = get_orientation(piece)
    piece &= 0b111100
    return piece | ((o-1)%3)

def reverse_move(m: int) -> int:
    if m % 3 == 2:
        return m
    elif m % 3 == 0:
        return m + 1
    return m - 1

u=0
up=1
u2=2
l=3
lp=4
l2=5
f=6
fp=7
f2=8
r=9
rp=10
r2=11
b=12
bp=13
b2=14
d=15
dp=16
d2=17

def move(state: int, m: int) -> int:
    p_7 = state % 32
    state >>= 5
    p_6 = state % 32
    state >>= 5
    p_5 = state % 32
    state >>= 5
    p_4 = state % 32
    state >>= 5
    p_3 = state % 32
    state >>= 5
    p_2 = state % 32
    state >>= 5
    p_1 = state % 32
    state >>= 5
    p_0 = state % 32

    s_0 = 0
    s_1 = 0
    s_2 = 0
    s_3 = 0
    s_4 = 0
    s_5 = 0
    s_6 = 0
    s_7 = 0
    
    match m:
        case 0: # u
            s_0 = p_3
            s_1 = p_0
            s_2 = p_1
            s_3 = p_2
            s_4 = p_4
            s_5 = p_5
            s_6 = p_6
            s_7 = p_7
        case 1: # up
            s_0 = p_1
            s_1 = p_2
            s_2 = p_3
            s_3 = p_0
            s_4 = p_4
            s_5 = p_5
            s_6 = p_6
            s_7 = p_7
        case 2: # u2
            s_0 = p_2
            s_1 = p_3
            s_2 = p_0
            s_3 = p_1
            s_4 = p_4
            s_5 = p_5
            s_6 = p_6
            s_7 = p_7
        case 3: # d
            s_0 = p_0
            s_1 = p_1
            s_2 = p_2
            s_3 = p_3
            s_4 = p_7
            s_5 = p_4
            s_6 = p_5
            s_7 = p_6
        case 4: # dp
            s_0 = p_0
            s_1 = p_1
            s_2 = p_2
            s_3 = p_3
            s_4 = p_5
            s_5 = p_6
            s_6 = p_7
            s_7 = p_4
        case 5: # d2
            s_0 = p_0
            s_1 = p_1
            s_2 = p_2
            s_3 = p_3
            s_4 = p_6
            s_5 = p_7
            s_6 = p_4
            s_7 = p_5
        case 6: # l
            s_0 = ccw(p_7)
            s_1 = p_1
            s_2 = p_2
            s_3 = cw(p_0)
            s_4 = ccw(p_3)
            s_5 = p_5
            s_6 = p_6
            s_7 = cw(p_4)
        case 7: # lp
            s_0 = ccw(p_3)
            s_1 = p_1
            s_2 = p_2
            s_3 = cw(p_4)
            s_4 = ccw(p_7)
            s_5 = p_5
            s_6 = p_6
            s_7 = cw(p_0)
        case 8: # l2
            s_0 = p_4
            s_1 = p_1
            s_2 = p_2
            s_3 = p_7
            s_4 = p_0
            s_5 = p_5
            s_6 = p_6
            s_7 = p_3
        case 9: # r
            s_0 = p_0
            s_1 = cw(p_2)
            s_2 = ccw(p_5)
            s_3 = p_3
            s_4 = p_4
            s_5 = cw(p_6)
            s_6 = ccw(p_1)
            s_7 = p_7
        case 10: # rp
            s_0 = p_0
            s_1 = cw(p_6)
            s_2 = ccw(p_1)
            s_3 = p_3
            s_4 = p_4
            s_5 = cw(p_2)
            s_6 = ccw(p_5)
            s_7 = p_7
        case 11: # r2
            s_0 = p_0
            s_1 = p_5
            s_2 = p_6
            s_3 = p_3
            s_4 = p_4
            s_5 = p_1
            s_6 = p_2
            s_7 = p_7
        case 12: # f
            s_0 = p_0
            s_1 = p_1
            s_2 = cw(p_3)
            s_3 = ccw(p_4)
            s_4 = cw(p_5)
            s_5 = ccw(p_2)
            s_6 = p_6
            s_7 = p_7
        case 13: # fp
            s_0 = p_0
            s_1 = p_1
            s_2 = cw(p_5)
            s_3 = ccw(p_2)
            s_4 = cw(p_3)
            s_5 = ccw(p_4)
            s_6 = p_6
            s_7 = p_7
        case 14: # f2
            s_0 = p_0
            s_1 = p_1
            s_2 = p_4
            s_3 = p_5
            s_4 = p_2
            s_5 = p_3
            s_6 = p_6
            s_7 = p_7
        case 15: # b
            s_0 = cw(p_1)
            s_1 = ccw(p_6)
            s_2 = p_2
            s_3 = p_3
            s_4 = p_4
            s_5 = p_5
            s_6 = cw(p_7)
            s_7 = ccw(p_0)
        case 16: # bp
            s_0 = cw(p_7)
            s_1 = ccw(p_0)
            s_2 = p_2
            s_3 = p_3
            s_4 = p_4
            s_5 = p_5
            s_6 = cw(p_1)
            s_7 = ccw(p_6)
        case 17: # b2
            s_0 = p_6
            s_1 = p_7
            s_2 = p_2
            s_3 = p_3
            s_4 = p_4
            s_5 = p_5
            s_6 = p_0
            s_7 = p_1
        case _:
            return -1
    final = 0

    final += s_0
    final <<= 5
    final += s_1
    final <<= 5
    final += s_2
    final <<= 5
    final += s_3
    final <<= 5
    final += s_4
    final <<= 5
    final += s_5
    final <<= 5
    final += s_6
    final <<= 5
    final += s_7
    
    return final
