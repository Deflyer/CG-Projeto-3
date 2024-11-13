from OpenGL.GL import *
from config_screen import *
from drawings import *
from vertexes import *
from vertexes import *
import keyboard as kb
import glm


# Configuring the screen used to show the objects with textures.
window = init_window()
print("foi 1")
non_emissor_object, emisssor_object = create_program()
print("ah bom")


# Getting all the vertexes and textures used in our project.
index_vertexes = {}
textures_coord_list = []
start = 0

# Creating the shrek.
#print("nossa")
#shrek, coords_shrek, textures_shrek = get_vertexes_shrek()
#print(start)
#index_vertexes['shrek'] = [start]
# We use a different method to read from an obj file, so different save
#for value in coords_shrek:
#    index_vertexes['shrek'].append(start + value)
#start = len(shrek) + start

# Creating the bathroom.
#bathroom, coords_bathroom, textures_bathroom = get_vertexes_bathroom()
#index_vertexes['bathroom'] = [start]
#for value in coords_bathroom:
#    index_vertexes['bathroom'].append(index_vertexes['bathroom'][-1] + value)
#start = len(bathroom) + start

# Creating the house.
house, coords_house, textures_house, normals_house = get_vertexes_house()
index_vertexes['house'] = [start]
for value in coords_house:
    index_vertexes['house'].append(index_vertexes['house'][-1] + value)
start = len(house) + start

# Creating the sky.
#sky, coords_sky, textures_sky = get_vertexes_sky()
#index_vertexes['sky'] = [start]
#for value in coords_sky:
#    index_vertexes['sky'].append(index_vertexes['sky'][-1] + value)
#start = len(sky) + start

# Creating the drawer.
#drawer, coords_drawer, textures_drawer = get_vertexes_drawer()
#index_vertexes['drawer'] = [start]
#for value in coords_drawer:
#    index_vertexes['drawer'].append(index_vertexes['drawer'][-1] + value)
#start = len(drawer) + start

# Creating the vase.
#vase, coords_vase, textures_vase = get_textures_vase()
#index_vertexes['vase'] = [start]
#for value in coords_vase:
#    index_vertexes['vase'].append(index_vertexes['vase'][-1] + value)
#start = len(vase) + start

# Creating the rose.
#rose, coords_rose, textures_rose = get_textures_rose()
#index_vertexes['rose'] = [start]
#for value in coords_rose:
#    index_vertexes['rose'].append(index_vertexes['rose'][-1] + value)
#start = len(rose) + start

# Creating the bed.
#bed, coords_bed, textures_bed = get_textures_bed()
#index_vertexes['bed'] = [start]
#for value in coords_bed:
#    index_vertexes['bed'].append(index_vertexes['bed'][-1] + value)
#start = len(bed) + start

# Creating the ground.
#ground, coords_ground, textures_ground = get_textures_ground()
#index_vertexes['ground'] = [start]
#for value in coords_ground:
#    index_vertexes['ground'].append(index_vertexes['ground'][-1] + value)
#start = len(ground) + start

# Creating the plant1.
#plant1, coords_plant1, textures_plant1, positions1 = get_vertexes_plant1()
#index_vertexes['plant1'] = [start]
#for value in coords_plant1:
#    index_vertexes['plant1'].append(index_vertexes['plant1'][-1] + value)
#start = len(plant1) + start

# Creating the plant2.
#plant2, coords_plant2, textures_plant2, positions2 = get_vertexes_plant2()
#index_vertexes['plant2'] = [start]
#for value in coords_plant2:
#    index_vertexes['plant2'].append(index_vertexes['plant2'][-1] + value)
#start = len(plant2) + start

# Creating the bird.
#bird, coords_bird, textures_bird = get_vertexes_bird()
#index_vertexes['bird'] = [start]
#for value in coords_bird:
#    index_vertexes['bird'].append(index_vertexes['bird'][-1] + value)
#start = len(bird) + start

# Joining everyone
#vertexes_temp = np.concatenate((shrek, bathroom))
#vertexes_temp = np.concatenate((vertexes_temp, house))
#vertexes_temp = np.concatenate((vertexes_temp, sky))
#vertexes_temp = np.concatenate((vertexes_temp, drawer))
#vertexes_temp = np.concatenate((vertexes_temp, vase))
#vertexes_temp = np.concatenate((vertexes_temp, rose))
#vertexes_temp = np.concatenate((vertexes_temp, bed))
#vertexes_temp = np.concatenate((vertexes_temp, ground))
#vertexes_temp = np.concatenate((vertexes_temp, plant1))
#vertexes_temp = np.concatenate((vertexes_temp, plant2))
#vertexes_temp = np.concatenate((vertexes_temp, bird))


vertexes = np.zeros(len(house), [("position", np.float32, 3)])
#vertexes = house
vertexes['position'] = house

#textures_temp = textures_shrek + textures_bathroom + textures_house + textures_sky + textures_drawer + textures_vase + textures_rose + textures_bed + textures_ground + textures_plant1 + textures_plant2 + textures_bird
textures = np.zeros(len(textures_house), [("position", np.float32, 2)])
#textures['position'] = textures_house

normals = np.zeros(len(normals_house), [("position", np.float32, 3)])
normals['position'] = normals_house
#-----------------------------------------------------------------------------------

# Sending and rendering the objects.

print(non_emissor_object.ID)
send_data_to_gpu(non_emissor_object, vertexes, textures, normals)
render_window(window)

# Activating the keyboard and mouse handler function and initializing an auxiliar variable.
glfw.set_key_callback(window,kb.key_event)
#glfw.set_cursor_pos_callback(window, kb.mouse_event)

#-----------------------------------------------------------------------------------

# Getting GPU variables.

loc_color = get_loc_color(non_emissor_object.ID)
mat_view, loc_view = get_view(non_emissor_object.ID)
mat_projection, loc_projection = get_projection(non_emissor_object.ID)
loc_model = glGetUniformLocation(non_emissor_object.ID, "model")

#-----------------------------------------------------------------------------------
sky_rotation_angle = 0.0

# Code main loop.
while not glfw.window_should_close(window):
    # Reading user interactions.
    glfw.poll_events()

    kb.bird_angle = (kb.bird_angle + kb.bird_speed) % 360
    sky_rotation_angle = (sky_rotation_angle + 0.1) % 360

    # Activating the polygon view mode.
    if kb.polyMode:
        glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
    else:
        glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)

    # Clearing screen and loading a new solid background.
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glClearColor(1.0, 1.0, 1.0, 1.0)
    non_emissor_object.setFloat("material.shininess", 32.0)

    non_emissor_object.setVec3("dirLight.direction", -0.2, -1.0, -0.3)
    non_emissor_object.setVec3("dirLight.ambient", 0.8, 0.05, 0.05)
    non_emissor_object.setVec3("dirLight.diffuse", 0.4, 0.4, 0.4)
    non_emissor_object.setVec3("dirLight.specular", 0.5, 0.5, 0.5)
    non_emissor_object.setVec3("spotLight.position", kb.camera.Position)
    non_emissor_object.setVec3("spotLight.direction", kb.camera.Front)
    non_emissor_object.setVec3("spotLight.ambient", 0.0, 0.0, 0.0)
    non_emissor_object.setVec3("spotLight.diffuse", 0, 1.0, 0)
    non_emissor_object.setVec3("spotLight.specular", 1.0, 1.0, 1.0)
    non_emissor_object.setFloat("spotLight.constant", 1.0)
    non_emissor_object.setFloat("spotLight.linear", 0.09)
    non_emissor_object.setFloat("spotLight.quadratic", 0.032)
    non_emissor_object.setFloat("spotLight.cutOff", glm.cos(glm.radians(12.5)))
    non_emissor_object.setFloat("spotLight.outerCutOff", glm.cos(glm.radians(15.0)))   

    # Drawing the objects.
    #draw_bathroom(loc_model, loc_color, index_vertexes)
    #draw_plant1(loc_model, loc_color,index_vertexes, positions1)
    #draw_plant2(loc_model, loc_color,index_vertexes, positions2)
    draw_house(loc_model, loc_color, index_vertexes)
    #draw_shrek(loc_model, loc_color, index_vertexes)
    #draw_sky(loc_model, loc_color, index_vertexes, sky_rotation_angle)
    #draw_drawer(loc_model, loc_color, index_vertexes)
    #draw_vase(loc_model, loc_color, index_vertexes)
    #draw_rose(loc_model, loc_color, index_vertexes)
    #draw_bed(loc_model, loc_color, index_vertexes)
    #draw_ground(loc_model, loc_color, index_vertexes)
    #draw_bird(loc_model, loc_color, index_vertexes)

    mat_view, loc_view = get_view(non_emissor_object.ID)
    glUniformMatrix4fv(loc_view, 1, GL_TRUE, mat_view)

    mat_projection, loc_projection = get_projection(non_emissor_object.ID)
    glUniformMatrix4fv(loc_projection, 1, GL_TRUE, mat_projection)    

    # Displaying the next frame.
    glfw.swap_buffers(window)

glfw.terminate()