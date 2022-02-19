def draw_line(tickLength, tickLabel = ' '):
    line = '-' * tickLength
    if tickLabel:
        line += ' ' + tickLabel
    print(line)

def draw_interval(centerLength):
    if centerLength > 0:
        draw_interval(centerLength - 1)
        draw_line(centerLength)
        draw_interval(centerLength - 1)

def draw_ruler(numInches, majorLength):
    draw_line(majorLength, '0')
    for j in range(1, 1 + numInches):
        draw_interval(majorLength - 1)
        draw_line(majorLength, str(j))


if __name__ == "__main__":
    draw_ruler(2, 4)