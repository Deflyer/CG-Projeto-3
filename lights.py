import glm

import keyboard as kb

# Valores difusos
diffuse_values = [
    (1.0, 0.1, 0.1),  # rose
    (1.0, 0.5, 0.0),  # bird
    (0.7, 0.3, 0.0),  # drawer
    (0.3, 0.1, 0.0),  # bed
    (0.1, 0.2, 1.0),  # bathroom
    (0.4, 0.4, 0.4),  # ground
    (0.2, 0.2, 0.6),  # house
    (0.1, 0.1, 0.4),  # sky
    (0.3, 0.1, 0.0),  # vase
    (0.2, 0.7, 0.2),  # plant2
    (0.1, 0.5, 0.1),  # plant1
    (1.0, 0.9, 0.5),  # lamp
    (0.5, 0.7, 1.0),  # lantern
    (0.5, 0.7, 1.0),  # magic ball
    (0.1, 0.3, 0.6),  # magic ball stand
    (0.0, 1.0, 0.0),  # shrek
]

# Valores especulares
specular_values = [
    (0.5, 0.2, 0.2),  # rose
    (0.6, 0.2, 0.2),  # bird
    (0.3, 0.2, 0.0),  # drawer
    (0.1, 0.1, 0.1),  # bed
    (0.1, 0.1, 1.0),  # bathroom
    (0.3, 0.3, 0.3),  # ground
    (0.3, 0.3, 0.6),  # house
    (0.1, 0.1, 0.3),  # sky
    (0.5, 0.5, 0.5),  # vase
    (0.2, 0.5, 0.2),  # plant2
    (0.3, 0.6, 0.3),  # plant1
    (0.7, 0.6, 0.3),  # lamp
    (0.6, 0.7, 1.0),  # lantern
    (0.5, 0.7, 1.0),  # magic ball
    (0.1, 0.3, 0.6),  # magic ball stand
    (0.0, 1.0, 0.0),  # shrek
]

def aplicar_luz_param(lightingShader, pointLightPositions, idx):

    # directional light
    lightingShader.setVec3("dirLight.direction", -0.2, -1.0, -0.3)
    lightingShader.setVec3("dirLight.ambient", 0.5, 0.5, 0.5)
    lightingShader.setVec3("dirLight.diffuse", diffuse_values[idx][0] *  0.5, diffuse_values[idx][1] *  0.5, diffuse_values[idx][2] *  0.5)
    lightingShader.setVec3("dirLight.specular", specular_values[idx][0] *  0.5, specular_values[idx][1] *  0.5, specular_values[idx][2] *  0.5)
    lightingShader.setFloat("dirLight.normal_correction", 1)

    # point light 1
    lightingShader.setVec3("pointLights[0].position", pointLightPositions[0])
    lightingShader.setVec3("pointLights[0].ambient", 0.8 * kb.ambient * kb.is_lamp_on, (0.7)* kb.ambient * kb.is_lamp_on, (0.3)* kb.ambient * kb.is_lamp_on)
    lightingShader.setVec3("pointLights[0].diffuse", diffuse_values[idx][0] *  kb.is_lamp_on * kb.diffuse, diffuse_values[idx][1] *  kb.is_lamp_on * kb.diffuse, diffuse_values[idx][2] *  kb.is_lamp_on * kb.diffuse)
    lightingShader.setVec3("pointLights[0].specular", specular_values[idx][0] *  kb.is_lamp_on * kb.specular, specular_values[idx][1] *  kb.is_lamp_on * kb.specular, specular_values[idx][2] *  kb.is_lamp_on * kb.specular)
    lightingShader.setFloat("pointLights[0].normal_correction", 1)
    lightingShader.setFloat("pointLights[0].constant", 1.0)
    lightingShader.setFloat("pointLights[0].linear", 0.0009)
    lightingShader.setFloat("pointLights[0].quadratic", 0.00032)

    # point light 2
    lightingShader.setVec3("pointLights[1].position", pointLightPositions[1])
    lightingShader.setVec3("pointLights[1].ambient", 0.3 * kb.ambient * kb.is_ball_on, 0.3 * kb.ambient * kb.is_ball_on, 0.9 * kb.ambient * kb.is_ball_on)
    lightingShader.setVec3("pointLights[1].diffuse", diffuse_values[idx][0] * kb.diffuse * kb.is_ball_on, diffuse_values[idx][1] * kb.diffuse * kb.is_ball_on, diffuse_values[idx][2] * kb.diffuse * kb.is_ball_on)
    lightingShader.setVec3("pointLights[1].specular", specular_values[idx][0] * kb.specular * kb.is_ball_on, specular_values[idx][1] * kb.specular * kb.is_ball_on, specular_values[idx][2] * kb.specular * kb.is_ball_on)
    lightingShader.setFloat("pointLights[1].normal_correction", 1)
    lightingShader.setFloat("pointLights[1].constant", 1.0)
    lightingShader.setFloat("pointLights[1].linear", 0.09)
    lightingShader.setFloat("pointLights[1].quadratic", 0.032)

    # point light 3
    lightingShader.setVec3("pointLights[2].position", pointLightPositions[2])
    lightingShader.setVec3("pointLights[2].ambient", 0.9 * kb.ambient * kb.is_fire_on, 0.3 * kb.ambient * kb.is_fire_on, 0.3 * kb.ambient * kb.is_fire_on)
    lightingShader.setVec3("pointLights[2].diffuse", diffuse_values[idx][0] * kb.diffuse * kb.is_fire_on, diffuse_values[idx][1] * kb.diffuse * kb.is_fire_on, diffuse_values[idx][2] * kb.diffuse * kb.is_fire_on)
    lightingShader.setVec3("pointLights[2].specular", specular_values[idx][0] * kb.specular * kb.is_fire_on, specular_values[idx][1] * kb.specular * kb.is_fire_on, specular_values[idx][2] * kb.specular * kb.is_fire_on)
    lightingShader.setFloat("pointLights[2].normal_correction", 1)
    lightingShader.setFloat("pointLights[2].constant", 1.0)
    lightingShader.setFloat("pointLights[2].linear", 0.02)
    lightingShader.setFloat("pointLights[2].quadratic", 0.0032)