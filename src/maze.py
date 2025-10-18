def right():
    global heading
    if heading == North and can_move(East):
        heading = East
        move(heading)
        return True
    if heading == East and can_move(South):
        heading = South
        move(heading)
        return True
    if heading == South and can_move(West):
        heading = West
        move(heading)
        return True
    if heading == West and can_move(North):
        heading = North
        move(heading)
        return True
    return False

def left():
    global heading
    if heading == North and can_move(West):
        heading = West
        move(heading)
        return True
    if heading == East and can_move(North):
        heading = North
        move(heading)
        return True
    if heading == South and can_move(East):
        heading = East
        move(heading)
        return True
    if heading == West and can_move(South):
        heading = South
        move(heading)
        return True
    return False

def straight():
    global heading
    if heading == North and can_move(North):
        heading = North
        move(heading)
        return True
    if heading == East and can_move(East):
        heading = East
        move(heading)
        return True
    if heading == South and can_move(South):
        heading = South
        move(heading)
        return True
    if heading == West and can_move(West):
        heading = West
        move(heading)
        return True
    return False

def back():
    global heading
    if heading == North and can_move(South):
        heading = South
        move(heading)
        return True
    if heading == East and can_move(West):
        heading = West
        move(heading)
        return True
    if heading == South and can_move(North):
        heading = North
        move(heading)
        return True
    if heading == West and can_move(East):
        heading = East
        move(heading)
        return True
    return False

def solve(r):
    while get_entity_type() != Entities.Treasure:
        if num_drones() == 1:
            return
        if r:
            if right():
                pass
            elif straight():
                pass
            elif left():
                pass
            elif back():
                pass
            else:
                if left():
                    pass
                elif straight():
                    pass
                elif right():
                    pass
                elif back():
                    pass

        harvest()

def solve_r():
    return solve(True)


heading = North
maze_size = 12
substance = maze_size * 2**(num_unlocked(Unlocks.Mazes) - 1)

while True:
    clear()
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, substance)
    heading = North

    spawn_drone(solve_r)
    solve(False)
