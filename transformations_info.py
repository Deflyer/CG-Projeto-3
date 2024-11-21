import glm

positions = [
    glm.vec3( -2.80, -0.80, -6.80), # rose
    glm.vec3(  2.70,  -1.0, -20.0),  # bird
    glm.vec3(  2.70, -0.95, -7.80), # drawer
    glm.vec3(  2.70,  -1.0, -20.0),  # bed
    glm.vec3(  20.0,   2.2, -6.0),  # bathroom
    glm.vec3( 0.0,   -1.0,   0.0),  # ground
    glm.vec3(  0.0,  -1.0,  -10.0),  # house
    glm.vec3( 0.0, -45, 0.0),  # sky
    glm.vec3( -2.80, -0.80, -6.80),  # vase
    glm.vec3( -1.0,  -2.0,  -1.0),  # plant2
    glm.vec3( -1.0,  -2.0,  -1.0),  # plant1
    glm.vec3( -1.0,  -2.0,  -1.0)  # plant1
]

scales = [
    0.05, # rose
    0.05, # vazio------------
    0.75, # drawer
    0.035, # bed
    0.003, # bathroom
    70.0, # vazio------------
    0.5, # house
    1.0, # sky
    0.005, # vase
    0.05, # vazio------------
    0.05, # vazio------------
    0.05, # vazio------------
]

rotations = [
    0.0, # rose
    0.05, # vazio------------
    180.0, # drawer
    0.0, # bed
    200.0, # bathroom
    0.0, # vazio------------
    180.0, # house
    0.0, # sky (tem q rotacionar)
    0.0, # vase
    0.05, # vazio------------
    0.05, # vazio------------
    0.05, # vazio------------
]

def get_position(idx):
    return positions[idx]

def get_scale(idx):
    return scales[idx]

def get_rotation(idx):
    return rotations[idx]

def get_lights_positions():
    # positions of the point lights
    pointLightPositions = [
        glm.vec3( 0.0,  0.0,  0.5),
        glm.vec3( 2.3, -3.3, -4.0),
        glm.vec3(-4.0,  2.0, -12.0),
        glm.vec3( 0.0,  0.0, -3.0)
    ]

    return pointLightPositions