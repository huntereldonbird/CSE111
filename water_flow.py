

def water_column_height(tower_height, tank_height):

    h = tower_height + (3 * tank_height) / 4


    return h

def pressure_gain_from_water_height(height):

    P = ((998.2) * (9.80665) * height) / 1000

    return P


def pressure_lost_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):

    P = ((friction_factor * -1) * pipe_length * 998.2 * (fluid_velocity * fluid_velocity)) / (2000 * pipe_diameter)

    return P