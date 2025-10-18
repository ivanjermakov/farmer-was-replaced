import main
import cacti

def operate1():
    return operate_fn(1)
def operate2():
    return operate_fn(2)
def operate3():
    return operate_fn(3)
def operate3():
    return operate_fn(3)
def operate4():
    return operate_fn(4)
def operate5():
    return operate_fn(5)
def operate6():
    return operate_fn(6)
def operate7():
    return operate_fn(7)


operate_fn = main.operate
if True:
    operate_fn = cacti.operate

clear()
spawn_drone(operate1)
spawn_drone(operate2)
spawn_drone(operate3)
spawn_drone(operate4)
spawn_drone(operate5)
spawn_drone(operate6)
spawn_drone(operate7)
operate_fn(0)
