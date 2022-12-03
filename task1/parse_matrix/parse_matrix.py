
def parse_matrix(raw: str) -> list[int]:
    out = []
    lasdigit = ''
    last = False
    for i in raw:
        if i.isnumeric() :
            if last:
                lasdigit = lasdigit + i
                last = True
            else:
                lasdigit = i
                last = True
        else:
            if last :
                out.append(int(lasdigit))
                last = False
                lasdigit = ''
    if last:
        out.append(int(lasdigit))
    return out