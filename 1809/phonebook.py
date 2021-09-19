def validate_code(p):
    if len(p) != 16:
        return False
    if p[0:3] != '+7-':
        return False
    if p[6] != '-' or p[10] != '-' or p[13] != '-':
        return False
    ap = p[3:6] + p[7:10]+p[11:13]+p[14:]
    digits = '0123456789'
    for sym in ap:
        if not sym in digits:
            return False
    return True