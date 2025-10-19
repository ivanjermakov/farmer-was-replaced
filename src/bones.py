threshold = 100

def play():
    clear()
    change_hat(Hats.Brown_Hat)
    change_hat(Hats.Dinosaur_Hat)
    ws = get_world_size()
    dir = North
    tx = 0
    ty = 0
    apples = 0
    while True:
        x = get_pos_x()
        y = get_pos_y()

        if get_entity_type() == Entities.Apple:
            tx, ty = measure()
            apples += 1

        if apples == threshold:
            for _ in range(10):
                move(North)
                move(West)
            apples += 1
        elif apples < threshold:
            if x < tx:
                if move(East):
                    dir = East
                elif move(North):
                    dir = North
                elif move(South):
                    dir = South
                elif move(West):
                    dir = West
                else:
                    break
                continue
            if x > tx:
                if move(West):
                    dir = West
                elif move(North):
                    dir = North
                elif move(South):
                    dir = South
                elif move(East):
                    dir = East
                else:
                    break
                continue
            if y < ty:
                if move(North):
                    dir = North
                elif move(East):
                    dir = East
                elif move(West):
                    dir = West
                elif move(South):
                    dir = South
                else:
                    break
                continue
            if y > ty:
                if move(South):
                    dir = South
                elif move(East):
                    dir = East
                elif move(West):
                    dir = West
                elif move(North):
                    dir = North
                else:
                    break
                continue
        else:
            if x == 0 and y == 0:
                dir = North
            if x == 0 and y == ws - 1:
                dir = South
            if dir == South:
                if y == 0:
                    dir = North
                else:
                    if not move(dir):
                        break
                continue
            if y % 2 == 0 and x == ws - 1:
                if not move(dir):
                    break
                continue
            if y % 2 == 1 and x == 1 and y != ws - 1:
                if not move(dir):
                    break
                continue
            if y % 2 == 0:
                if not move(East):
                    break
                continue
            if y % 2 == 1:
                if not move(West):
                    break
                continue
    change_hat(Hats.Brown_Hat)

while True:
    play()

