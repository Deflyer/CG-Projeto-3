# File used to handle keyboard events.
# Most of the logic is from the code of our professor

import math
import glfw
import glm
from camera import Camera, Camera_Movement

polyMode = False
tree_scale = 1
shrek_step = 0
shrek_side_step = 0
person_step = 0
person_speed = 0
cameraPos   = glm.vec3(0.0,  0.0,  1.0)
cameraFront = glm.vec3(0.0,  0.0, -1.0)
cameraUp    = glm.vec3(0.0,  1.0,  0.0)
skyfix    = glm.vec3(0.0,  -72.0,  0.0)
firstMouse = True
yaw = -90.0 
pitch = 0.0
camera = Camera(glm.vec3(0.0, 0.0, 3.0))
lastX = 1920 / 2.0
lastY = 1080 / 2.0
firstMouse = True

# Geometric transformations auxiliar variables.
rose_scale_y = 0.05
bird_speed = 0.00
bird_radius = 80.0
bird_angle = 0.0

def key_event(window,key,scancode,action,mods):
    global polyMode
    global cameraPos
    global cameraFront
    global cameraUp
    global shrek_step
    global shrek_side_step
    global rose_scale_y
    global bird_speed

    cameraSpeed = 0.4

    exclusion_zones = [
        (-8, -30, 6, 1),
        (5, -9, 25, -2),             
        ]
    
    if key == 87 and (action==1 or action==2): # tecla W
        valid = True
        nova_pos = cameraPos + cameraSpeed * cameraFront
        if glm.length(nova_pos + skyfix) >= 96 or nova_pos[1] < -0.5:
             print(glm.length(nova_pos + skyfix))
             print(nova_pos)
             print(cameraPos)
             valid = False
        if valid:
            cameraPos = nova_pos
    
    if key == 83 and (action==1 or action==2): # tecla S
        valid = True
        nova_pos = cameraPos - cameraSpeed * cameraFront
        if glm.length(nova_pos +skyfix) >= 96 or nova_pos[1] < -0.5:
             valid = False
        if valid:
            cameraPos = nova_pos
    
    if key == 65 and (action==1 or action==2): # tecla A
        valid = True
        nova_pos = cameraPos - glm.normalize(glm.cross(cameraFront, cameraUp)) * cameraSpeed
        if glm.length(nova_pos + skyfix) >= 96 or nova_pos[1] < -0.5:
             valid = False
        if valid:
            cameraPos = nova_pos
        
    if key == 68 and (action==1 or action==2): # tecla D
        valid = True
        nova_pos = cameraPos + glm.normalize(glm.cross(cameraFront, cameraUp)) * cameraSpeed
        if glm.length(nova_pos +skyfix) >= 96 or nova_pos[1] < -0.5:
             valid = False
        if valid:
            cameraPos = nova_pos

    if key == 73 and (action==1 or action==2): # tecla I
        valid = True
        for zone in exclusion_zones:
                x_min, z_min, x_max, z_max = zone
                if (x_min <= shrek_side_step <= x_max) and (z_min <= shrek_step + 1.9 <= z_max):
                    valid = False
        if(shrek_side_step **2  + (shrek_step - 0.5) ** 2 >= 3600):
             valid = False
        if valid:
            shrek_step -= 0.5 
        
    if key == 75 and (action==1 or action==2): # tecla K
        valid = True
        for zone in exclusion_zones:
                x_min, z_min, x_max, z_max = zone
                if (x_min <= shrek_side_step <= x_max) and (z_min <= shrek_step + 2.1 <= z_max):
                    valid = False
        if(shrek_side_step **2  + (shrek_step + 0.5) ** 2 >= 3600):
             valid = False
        if valid:
            shrek_step += 0.5 

    if key == 74 and (action==1 or action==2): # tecla J
        valid = True
        for zone in exclusion_zones:
                x_min, z_min, x_max, z_max = zone
                if (x_min <= shrek_side_step -0.5 <= x_max) and (z_min <= shrek_step + 2 <= z_max):
                    valid = False
        if((shrek_side_step - 0.5) **2  + (shrek_step) ** 2 >= 3600):
             valid = False
        if valid:
            shrek_side_step -= 0.5 

    if key == 76 and (action==1 or action==2): # tecla L
        valid = True
        for zone in exclusion_zones:
                x_min, z_min, x_max, z_max = zone
                if (x_min <= shrek_side_step +0.5 <= x_max) and (z_min <= shrek_step + 2 <= z_max):
                    valid = False
        if((shrek_side_step + 0.5) **2  + (shrek_step) ** 2 >= 3600):
             valid = False
        if valid:
            shrek_side_step += 0.5 

    if key == 80 and action == glfw.PRESS: 
        polyMode = not polyMode

    if key == 265 and action == glfw.PRESS: # tecla seta pra cima (rosa cresce).
        aux = rose_scale_y + 0.01
        rose_scale_y = min(aux, 0.13)

    if key == 264 and action == glfw.PRESS: # tecla seta pra baixo (rosa diminui).
        aux = rose_scale_y - 0.01
        rose_scale_y = max(aux,0.05)

    if key == 262 and action == glfw.PRESS: # tecla seta pra direita.
        aux = bird_speed + 0.01
        bird_speed = min(aux, 0.05)

    if key == 263 and action == glfw.PRESS: # tecla seta pra esquerda.
        aux = bird_speed - 0.01
        bird_speed = max(aux, 0.0)

def mouse_callback(window, xpos: float, ypos: float) -> None:
    global lastX, lastY, firstMouse

    if (firstMouse):

        lastX = xpos
        lastY = ypos
        firstMouse = False

    xoffset = xpos - lastX
    yoffset = lastY - ypos # reversed since y-coordinates go from bottom to top

    lastX = xpos
    lastY = ypos

    camera.ProcessMouseMovement(xoffset, yoffset)

def scroll_callback(window, xoffset: float, yoffset: float) -> None:

    camera.ProcessMouseScroll(yoffset)