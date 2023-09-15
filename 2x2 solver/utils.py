MOVE_MAP = {0: 'U', 1: "U'", 2: 'U2', 3: 'D', 4: "D'", 5: 'D2', 6: 'L', 7: "L'", 8: 'L2', 9: 'R', 10: "R'", 11: 'R2', 12: 'F', 13: "F'", 14: 'F2', 15: 'B', 16: "B'", 17: 'B2'}

def is_solved(state: int) -> bool:
    return state == 4576531228 # solved state!

def is_same_piece(piece1: str, piece2: str) -> bool:
    return sorted(piece1) == sorted(piece2)

def get_piece(state: int, index: int) -> int:
    state >>= 5*(7-index)
    state %= 32
    return state

def get_orientation(piece: int) -> int:
    return piece % 4

def get_position(piece: int) -> int:
    return piece // 4

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

    result = 0
    for p in pieces:
        for t in solved:
            if is_same_piece(p, t):
                multiplier = 0 if p[0] in "wy" else (1 if p[1] in "wy" else 2)
                result *= 32
                result += solved.index(t)*4 + multiplier
                break
        else:
            return -1
        
    return result

def cw(piece: int) -> int:
    o = get_orientation(piece)
    piece &= 0b111100
    return piece | ((o+1)%3)

def ccw(piece: int) -> int:
    o = get_orientation(piece)
    piece &= 0b111100
    return piece | ((o-1)%3)

def reverse_move(m: int) -> int:
    if m % 3 == 0:
        return m+1
    elif m % 3 == 1:
        return m-1
    return m

def move(state: int, m: int) -> int:
    p = [-1 for _ in range(8)]
    for i in range(8):
        p[7-i] = state % 32
        state >>= 5
    
    match m:
        case 0: # u
            result = [p[3], p[0], p[1], p[2], p[4], p[5], p[6], p[7]]
        case 1: # up 
            result = [p[1], p[2], p[3], p[0], p[4], p[5], p[6], p[7]]
        case 2: # u2
            result = [p[2], p[3], p[0], p[1], p[4], p[5], p[6], p[7]]
        case 3: # d
            result = [p[0], p[1], p[2], p[3], p[7], p[4], p[5], p[6]]
        case 4: # dp
            result = [p[0], p[1], p[2], p[3], p[5], p[6], p[7], p[4]]
        case 5: # d2
            result = [p[0], p[1], p[2], p[3], p[6], p[7], p[4], p[5]]
        case 6: # l
            result = [ccw(p[7]), p[1], p[2], cw(p[0]), ccw(p[3]), p[5], p[6], cw(p[4])]
        case 7: # lp
            result = [ccw(p[3]), p[1], p[2], cw(p[4]), ccw(p[7]), p[5], p[6], cw(p[0])]
        case 8: # l2
            result = [p[4], p[1], p[2], p[7], p[0], p[5], p[6], p[3]]
        case 9: # r
            result = [p[0], cw(p[2]), ccw(p[5]), p[3], p[4], cw(p[6]), ccw(p[1]), p[7]]
        case 10: # rp
            result = [p[0], cw(p[6]), ccw(p[1]), p[3], p[4], cw(p[2]), ccw(p[5]), p[7]]
        case 11: # r2
            result = [p[0], p[5], p[6], p[3], p[4], p[1], p[2], p[7]]
        case 12: # f
            result = [p[0], p[1], cw(p[3]), ccw(p[4]), cw(p[5]), ccw(p[2]), p[6], p[7]]
        case 13: # fp
            result = [p[0], p[1], cw(p[5]), ccw(p[2]), cw(p[3]), ccw(p[4]), p[6], p[7]]
        case 14: # f2
            result = [p[0], p[1], p[4], p[5], p[2], p[3], p[6], p[7]]
        case 15: # b
            result = [cw(p[1]), ccw(p[6]), p[2], p[3], p[4], p[5], cw(p[7]), ccw(p[0])]
        case 16: # bp
            result = [cw(p[7]), ccw(p[0]), p[2], p[3], p[4], p[5], cw(p[1]), ccw(p[6])]
        case 17: # b2
            result = [p[6], p[7], p[2], p[3], p[4], p[5], p[0], p[1]]
        case _:
            return -1
    final = 0
    for i in range(8):
        final <<= 5
        final += result[i]
    return final


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