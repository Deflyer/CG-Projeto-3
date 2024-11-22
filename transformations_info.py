import glm
import keyboard as kb
import random
import math

def get_positions():
    return [
        glm.vec3(-2.80, -0.80, -6.80),  # rose
        glm.vec3(kb.bird_radius * math.cos(kb.bird_angle), 50.0, kb.bird_radius * math.sin(kb.bird_angle)), # bird
        glm.vec3(2.70, -0.95, -7.80),   # drawer
        glm.vec3(2.70, -1.0, -20.0),    # bed
        glm.vec3(20.0, 2.2, -6.0),      # bathroom
        glm.vec3(0.0, -1.0, 0.0),       # ground
        glm.vec3(0.0, -1.0, -10.0),     # house
        glm.vec3(0.0, -45, 0.0),        # sky
        glm.vec3(-2.80, -0.80, -6.80),  # vase
        glm.vec3(-1.0, -2.0, -1.0),     # plant2
        glm.vec3(-1.0, -2.0, -1.0),     # plant1
        glm.vec3(0.0, -1.0, 2.0)        # shrek
    ]

# Function to compute scales dynamically
def get_scales():
    return [
        glm.vec3(0.05, kb.rose_scale_y, 0.05),  # rose
        0.05,  # bird
        0.75,  # drawer
        0.035,  # bed
        0.003,  # bathroom
        70.0,   # ground
        0.5,    # house
        1.0,    # sky
        0.005,  # vase
        0.05,   # plant2
        0.05,   # plant1
        2.8     # shrek
    ]

def get_rotations():
    return [
        0.0,  # rose
        - ( (360 * kb.bird_angle) / (2 * math.pi) ),  # bird
        180.0,  # drawer
        0.0,  # bed
        200.0,  # bathroom
        0.0,  # ground
        180.0,  # house
        kb.sky_rotation_angle,  # sky
        0.0,  # vase
        0.05,  # plant2
        0.05,  # plant1
        0.05   # shrek
    ]

def get_position(idx):
    return get_positions()[idx]

def get_scale(idx):
    # Dynamically fetch scales
    return get_scales()[idx]

def get_rotation(idx):
    return get_rotations()[idx]

def get_lights_positions():
    # Positions of the point lights
    pointLightPositions = [
        glm.vec3(-2.80, -0.80, -6.80),
        glm.vec3(2.3, -3.3, -4.0),
        glm.vec3(-4.0, 2.0, -12.0),
        glm.vec3(0.0, 0.0, -3.0)
    ]
    return pointLightPositions

def get_positions_plants():
    positions1 = []
  
    exclusion_zones = [
    (-8, -30, 6, 60),
    (5, -9, 25, -2),             
    ]
    
    # Calcula posições fixas para as plantas
    for i in range(3):
        min_radius = 14 * (i + 1)
        max_radius = 14 * (i + 2)
        num_plants = 120 + 50 * i
        angle_step = 360 / num_plants
        for j in range(num_plants):
            angle_rad = math.radians(j * angle_step + random.uniform(-10, 10))
            radius = random.uniform(min_radius, max_radius)  
            t_x = radius * math.cos(angle_rad)
            t_y = -1.0                
            t_z = radius * math.sin(angle_rad) 
            angle = random.uniform(0, 360)
            s_x = random.uniform(0.5, 0.7) + 0.2*i   
            s_y = s_x                     
            s_z = random.uniform(0.5, 0.7) + 0.2*i
            valid = True
            for zone in exclusion_zones:
                x_min, z_min, x_max, z_max = zone
                if (x_min <= t_x <= x_max) and (z_min <= t_z <= z_max):
                    valid = False
            if valid:
                positions1.append((t_x, t_y, t_z, angle, s_x, s_y, s_z))

    positions2 = []
    
    # Calcula posições fixas para as plantas
    for i in range(3):
        min_radius = 3 * (i + 1)
        max_radius = 3 * (i + 2)
        num_plants = 10
        angle_step = (360 / num_plants) + random.uniform(0, 45)
        for j in range(num_plants):
            angle_rad = math.radians(j * angle_step + random.uniform(-10, 10))
            radius = random.uniform(min_radius, max_radius)
            t_x = radius * math.cos(angle_rad)
            t_y = -1.0                         
            t_z = radius * math.sin(angle_rad)
            angle = random.uniform(0, 360)
            s_x = random.uniform(0.01, 0.02) + 0.005*i
            s_y = s_x                        
            s_z = random.uniform(0.01, 0.02) + 0.005*i
            valid = True
            for zone in exclusion_zones:
                x_min, z_min, x_max, z_max = zone
                if (x_min <= t_x <= x_max) and (z_min <= t_z <= z_max):
                    valid = False
            if valid:
                positions2.append((t_x, t_y, t_z, angle, s_x, s_y, s_z))
    return [positions1, positions2]