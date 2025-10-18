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

        if apples == 10:
            for _ in range(10):
                move(North)
                move(West)
            apples += 1
        elif apples < 10:
            if x < tx and dir != West:
                if not move(East):
                    break
                dir = East
                continue
            if x > tx and dir != East:
                if not move(West):
                    break
                dir = West
                continue
            if y < ty and dir != South:
                if not move(North):
                    break
                dir = North
                continue
            if y > ty and dir != North:
                if not move(South):
                    break
                dir = South
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
