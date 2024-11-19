import glm

positions = [
    glm.vec3( 0.0,  0.0,  0.0), # rose
    glm.vec3( 1.0,  1.0,  1.0)  # drawer
]

def get_position(idx):
    return positions[idx]

def get_lights_positions():
    # positions of the point lights
    pointLightPositions = [
        glm.vec3( 0.7,  0.2,  2.0),
        glm.vec3( 2.3, -3.3, -4.0),
        glm.vec3(-4.0,  2.0, -12.0),
        glm.vec3( 0.0,  0.0, -3.0)
    ]

    return pointLightPositions