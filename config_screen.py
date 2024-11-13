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
    
def send_data_to_gpu(program, vertexes, textures, normals):
    '''
    Configura os buffers para os dados de vértices, texturas e normais carregados do arquivo OBJ,
    adaptados ao shader que utiliza aPos, aNormal e aTexCoords.
    '''
    
    # Extrair dados do modelo
    program.use()
    if glGetProgramiv(program.ID, GL_LINK_STATUS) == GL_FALSE:
        print("Shader program não foi linkado corretamente.")
        return

    # Gerar e ligar VAO (se não estiver já feito)
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)
    # Gerar buffers para cada tipo de dado
    buffers = glGenBuffers(3)
    # Configurar buffer de vértices para `aPos`
    glBindBuffer(GL_ARRAY_BUFFER, buffers[0])
    glBufferData(GL_ARRAY_BUFFER, vertexes.nbytes, vertexes, GL_STATIC_DRAW)
    stride = vertexes.strides[0]
    offset = ctypes.c_void_p(0)
    loc_position = glGetAttribLocation(program.ID, "aPos")

    glEnableVertexAttribArray(loc_position)
    glVertexAttribPointer(loc_position, 3, GL_FLOAT, False, stride, offset)
    print("aqui foi")
    # Configurar buffer de coordenadas de textura para `aTexCoords`
    glBindBuffer(GL_ARRAY_BUFFER, buffers[1])
    glBufferData(GL_ARRAY_BUFFER, textures.nbytes, textures, GL_STATIC_DRAW)
    loc_texture_coord = glGetAttribLocation(program.ID, "aTexCoords")
    glEnableVertexAttribArray(loc_texture_coord)
    glVertexAttribPointer(loc_texture_coord, 2, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

    # Configurar buffer de normais para `aNormal`
    glBindBuffer(GL_ARRAY_BUFFER, buffers[2])
    glBufferData(GL_ARRAY_BUFFER, normals.nbytes, normals, GL_STATIC_DRAW)
    loc_normal = glGetAttribLocation(program.ID, "aNormal")
    glEnableVertexAttribArray(loc_normal)
    glVertexAttribPointer(loc_normal, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

    # Desvincula o buffer para evitar alterações acidentais
    glBindBuffer(GL_ARRAY_BUFFER, 0)


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