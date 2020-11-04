

def get_name():
    """
    this function the name of the robot from the user and return it.
    """
    name = input("What do you want to name your robot? ")
    print(f'{name}: Hello kiddo!')
    return name


def get_input(name):
    """
    this function accept commands from user input
    """
    coordinates = {
        "x": 0,
        "y": 0
    }
    direction = ['north']
    while True:
        command = input(f"{name}: What must I do next? ")
        move_command = command.split(" ")
        if command.upper() == 'OFF':
            print(f'{name}: Shutting down..')
            break
        elif command.upper() == 'HELP':
            help = get_help()
            print(help)
        elif move_command[0].upper() == "FORWARD":
            coordinates = forward_command(name, int(move_command[1]), coordinates, direction)
        elif move_command[0].upper() == 'BACK':
            coordinates = back_command(name, int(move_command[1]), coordinates, direction)
        elif command.upper() == 'RIGHT':
            coordinates = right_command(name, command, coordinates, direction)
        elif command.upper() == 'LEFT':
            coordinates = left_command(name, command, coordinates, direction)
        elif move_command[0].upper() == "SPRINT":
            sprint_command(name, int(move_command[1]), coordinates, direction)

        else:
            print(f"{name}: Sorry, I did not understand '{command}'.")
            return get_input(name)
        tracking_position(name, coordinates)


def get_help():
    """
    this function helps the user with information to operate the robot.
    """
    help = """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
    """
    return help
"""
SPRINT - give a short burst of speed
"""


def forward_command(name, steps, coordinates, direction):
    """
    this function deals with the movement of the function to the forward direction
    """
    old_coordinates = coordinates.copy()
    if direction[0] == 'north':
        coordinates['y'] += steps
    elif direction[0] == 'south':
        coordinates['y'] -= steps
    elif direction[0] == 'west':
        coordinates['x'] -= steps
    elif direction[0] == 'east':
        coordinates['x'] += steps
    store = limit_area(name, coordinates)
    if store is True:
        print(f' > {name} moved forward by {steps} steps.')
        return coordinates
    else:
        return old_coordinates


def tracking_position(name, coordinates):
    """
        this function tracks the location of the robot using coordinates.
    """
    print(f' > {name} now at position ({coordinates["x"]},{coordinates["y"]}).')


def back_command(name, steps, coordinates, direction):
    """
        this function deals with the movement of the function to the back direction.
    """
    old_coordinates = coordinates.copy()
    if direction[0] == 'south':
        coordinates['y'] += steps
    elif direction[0] == 'north':
        coordinates['y'] -= steps
    elif direction[0] == 'west':
        coordinates['x'] += steps
    elif direction[0] == 'east':
        coordinates['x'] -= steps
    store = limit_area(name, coordinates)
    if store is True:
        print(f' > {name} moved back by {steps} steps.')
        return coordinates
    else:
        return old_coordinates


def right_command(name, steps, coordinates, direction):
    """
        this function deals with the movement of the function to the right direction.
    """
    old_coordinates = coordinates.copy()
    print(f' > {name} turned right.')
    if direction[0] == 'north':
        direction[0] = 'east'
    elif direction[0] == 'east':
        direction[0] = 'south'
    elif direction[0] == 'south':
        direction[0] = 'west'
    elif direction[0] == 'west':
        direction[0] = 'north'
    store = limit_area(name, coordinates)
    if store is True:
        return coordinates
    else:
        return old_coordinates


def left_command(name, step, coordinates, direction):
    """
        this function deals with the movement of the function to the left direction.
    """
    old_coordinates = coordinates.copy()
    print(f' > {name} turned left.')
    if direction[0] == 'north':
        direction[0] = 'west'
    elif direction[0] == 'west':
        direction[0] = 'south'
    elif direction[0] == 'south':
        direction[0] = 'east'
    elif direction[0] == 'east':
        direction[0] = 'north'
    store = limit_area(name, coordinates)
    if store is True:
        return coordinates
    else:
        return old_coordinates


def limit_area(name, coordinates):
    """
        this function provide the robot with a safe area to operate on.
    """
    check = ((-200 < coordinates['y'] < 200) and (-100 < coordinates['x'] < 100))
    if check:
        return True
    else:
        print(f"{name}: Sorry, I cannot go outside my safe zone.")
        return False


def sprint_command(name, steps, coordinates, direction):
    """
        this function improves the speed of the function by sprinting
    """
    print(f' > {name} moved forward by {steps} steps.')
    coordinates['y'] += steps
    if steps == 1:
        return 1
    else:
        return sprint_command(name, steps - 1, coordinates, direction)


def robot_start():
    """This is the entry function, do not change"""
    name = get_name()
    get_input(name)


if __name__ == "__main__":
    robot_start()
