# Configures all the needed components of our screen.

from glfw.GLFW import *

WIDTH = 1920
HEIGHT = 1080

def init_window():

    glfwInit()
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3)
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3)
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE)

    window = glfwCreateWindow(WIDTH, HEIGHT, "Project 3", None, None)
    glfwMakeContextCurrent(window)

    return window