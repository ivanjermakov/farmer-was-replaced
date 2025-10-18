def water():
    if entity not in water_list:
        return
    if num_items(Items.Water) == 0:
        return
    if get_water() < watering_target - 0.25/2:
        use_item(Items.Water)

def plant_select():
    global pumpkin_only
    hay_count = num_items(Items.Hay)
    wood_count = num_items(Items.Wood)
    carrot_count = num_items(Items.Carrot)
    pumpkin_count = num_items(Items.Pumpkin)
    power_count = num_items(Items.Power)
    cacti_count = num_items(Items.Cactus)
    total_count = wood_count + carrot_count + pumpkin_count
    avg_count = total_count / 3
    if pumpkin_only and pumpkin_count > 1.25 * carrot_count:
        pumpkin_only = False
    elif not pumpkin_only and pumpkin_count < 0.75 * carrot_count:
        pumpkin_only = True
        pumpkin_start = get_time()

    if pumpkin_only:
        plant_pumpkin()
    elif hay_count < wood_count:
        plant_hay()
    elif wood_count < avg_count:
        plant_wood()
    elif carrot_count < avg_count:
        plant_carrot()
    #elif power_count < avg_count:
    #    plant_power()
elif cacti_count < 1000:
    plant_cacti()
else:
    plant_power()

def plant_hay():
    if ground != Grounds.Grassland:
        till()

def plant_wood():
    if (x + y) % 2 == 0:
        plant(Entities.Tree)
        return
    plant_hay()

def plant_carrot():
    if ground == Grounds.Grassland:
        till()
    plant(Entities.Carrot)

def plant_pumpkin():
    if ground == Grounds.Grassland:
        till()
    plant(Entities.Pumpkin)

def plant_power():
    if ground == Grounds.Grassland:
        till()
    plant(Entities.Sunflower)

def plant_cacti():
    if ground == Grounds.Grassland:
        till()
    plant(Entities.Cactus)

clear()    
x = 0
y = 0
entity = None
ground = None
watering_target = 0.25
pumpkin_only = False
pumpkin_start = 0
water_list = [Entities.Carrot, Entities.Sunflower, Entities.Tree]

def operate(id):
    global x
    global y
    global entity
    global ground

    while True:
        x = get_pos_x()
        y = get_pos_y()
        entity = get_entity_type()
        ground = get_ground_type()

        strip_width = get_world_size() / 4
        if y >= id * strip_width and y < (id + 1) * strip_width:
            if entity == Entities.Pumpkin:
                pumpkin_phase = (get_time() - pumpkin_start) % 20
                if pumpkin_only and pumpkin_phase > 10:
                    harvest()
            elif can_harvest():
                harvest()
            plant_select()
            water()

            if (x + y) % 3 == 1 and num_items(Items.Weird_Substance) < 1000:
                use_item(Items.Weird_Substance)
        else:
            move(North)
            continue

        if get_pos_x() == get_world_size() - 1:
            move(North)
        if True:
            move(East)
