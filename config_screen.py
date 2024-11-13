# File containing functions that configure the screen that will be used to show our project.

import glfw
from OpenGL.GL import *
import glm
import numpy as np
import keyboard as kb
from shader_m import Shader


HEIGHT = 1080
WIDTH = 1920
WINDOW_NAME = 'Project 2'
QTT_TEXTURES = 4

def init_window():
    '''
    Instantiates a GLFW window.
    '''
    
    glfw.init()
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window = glfw.create_window(WIDTH, HEIGHT, WINDOW_NAME, None, None)
    glfw.make_context_current(window)
    glfw.set_cursor_pos_callback(window, kb.mouse_callback)
    glfw.set_scroll_callback(window, kb.scroll_callback)

    # tell GLFW to capture our mouse
    glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)
    glEnable(GL_DEPTH_TEST)

    glfw.show_window(window)

    return window

def create_program():
    '''
    Requests GPU slots for the program and shaders to then compile and attach
    these shaders to this program slot.
    '''

    lightingShader = Shader("6.multiple_lights.vs", "6.multiple_lights.fs")
    lightCubeShader = Shader("6.light_cube.vs", "6.light_cube.fs")

    return lightingShader, lightCubeShader

def send_data_to_gpu(program, vertexes, textures):
    '''
    Requests GPU slots to program data and then sends this data to this slot.
    '''
    cubeVAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertexes.nbytes, vertexes, GL_STATIC_DRAW)

    glBindVertexArray(cubeVAO)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * glm.sizeof(glm.float32), None)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * glm.sizeof(glm.float32), ctypes.c_void_p(3 * glm.sizeof(glm.float32)))
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 8 * glm.sizeof(glm.float32), ctypes.c_void_p(6 * glm.sizeof(glm.float32)))
    glEnableVertexAttribArray(2)

    # second, configure the light's VAO (VBO stays the same the vertices are the same for the light object which is also a 3D cube)
    lightCubeVAO = glGenVertexArrays(1)
    glBindVertexArray(lightCubeVAO)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    # note that we update the lamp's position attribute's stride to reflect the updated buffer data
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * glm.sizeof(glm.float32), None)
    glEnableVertexAttribArray(0)

def render_window(window):
    '''
    Render a already created window.
    '''

    glfw.show_window(window)
    glEnable(GL_DEPTH_TEST)

def get_loc_color(program):
    '''
    Returns the color variable localized in the GPU.
    '''

    return glGetUniformLocation(program, "color")

def get_view(program):
    '''
    Returns the transformation matrix variable localized in the GPU.
    '''

    return view_matrix(), glGetUniformLocation(program, "view")

def get_model(program):
    '''
    Returns the transformation matrix variable localized in the GPU.
    '''

    return glGetUniformLocation(program, "model")

def get_projection(program):
    '''
    Returns the transformation matrix variable localized in the GPU.
    '''

    return projection_matrix(), glGetUniformLocation(program, "projection")

def view_matrix():
    mat_view = glm.lookAt(kb.cameraPos, kb.cameraPos + kb.cameraFront, kb.cameraUp)
    mat_view = np.array(mat_view)
    return mat_view

def projection_matrix():
    # perspective parameters: fovy, aspect, near, far
    mat_projection = glm.perspective(glm.radians(45.0), WIDTH/HEIGHT, 0.1, 1000.0)
    
    mat_projection = np.array(mat_projection)    
    return mat_projection