def operate(id):
    x = 0
    y = 0
    entity = None
    ground = None
    watering_target = 0.25
    pumpkin_only = False
    pumpkin_start = 0
    water_list = [Entities.Carrot, Entities.Sunflower]
    ws = get_world_size()
    last_harvest = get_time()

    while True:
        x = get_pos_x()
        y = get_pos_y()
        entity = get_entity_type()
        ground = get_ground_type()

        strip_width = get_world_size() / max_drones()
        if y >= id * strip_width and y < (id + 1) * strip_width:
            if entity == Entities.Cactus:
                m = measure()
                m_east = measure(East)
                m_west = measure(West)
                m_north = measure(North)
                m_south = measure(South)
                if m_east != None and m > m_east:
                    swap(East)
                elif m_west != None and m < m_west:
                    swap(West)
                elif m_north != None and m > m_north:
                    swap(North)
                elif m_south != None and m < m_south:
                    swap(South)
                if id == 0 and get_time() - last_harvest > 20:
                    if can_harvest():
                        harvest()
                        last_harvest = get_time()

            elif can_harvest():
                harvest()

            if ground == Grounds.Grassland:
                till()
            plant(Entities.Cactus)
        else:
            move(North)
            continue

        if get_pos_x() == get_world_size() - 1:
            move(North)
        move(East)
