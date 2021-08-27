STARTING_POINT = [(20,20), (19,20), (18,20)]
MOVE_SPEED = 1

positions = STARTING_POINT
x, y = STARTING_POINT[0]

ms = 0
while ms < 11: # 10칸 이동 좌표 Test
    ms += 1
    if ms == 1:
        print(STARTING_POINT)
    
    print([(x, y-ms)] + positions[:-1])