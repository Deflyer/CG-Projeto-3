# Handles vertexes and textures aggregating funtionalities.

import glm
from utils import *

def get_vertexes_textures():

    vet = []
    textures = []
    vet_idx = {}

    vertexes_aux_1 = load_obj_to_glm_array('./objects/rose/rose.obj')
    vet.append({'inicio': 0, 'tam': int(len(vertexes_aux_1)/8)})
    texture_aux = loadTexture("./objects/rose/rose_texture.jpg")
    textures.append(texture_aux)
    vet_idx['rose'] = 0
    
    vertexes_aux_2 = load_obj_to_glm_array('./objects/bird/bird.obj')
    ini = vet[0]['inicio'] + vet[0]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_2)/8)})
    texture_aux = loadTexture("./objects/bird/bird_texture.jpg")
    textures.append(texture_aux)
    vet_idx['bird'] = 1

    vertexes_aux_3 = load_obj_to_glm_array('./objects/drawer/drawer.obj')
    ini = vet[1]['inicio'] + vet[1]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_3)/8)})
    texture_aux = loadTexture("./objects/drawer/drawer_texture.png")
    textures.append(texture_aux)
    vet_idx['drawer'] = 2

    vertexes_aux_4 = load_obj_to_glm_array('./objects/bed/bed.obj')
    ini = vet[2]['inicio'] + vet[2]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_4)/8)})
    texture_aux = loadTexture("./objects/bed/bed_texture.png")
    textures.append(texture_aux)
    vet_idx['bed'] = 3

    vertexes_aux_5 = load_obj_to_glm_array('./objects/bathroom/bathroom.obj')
    ini = vet[3]['inicio'] + vet[3]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_5)/8)})
    texture_aux = loadTexture("./objects/bathroom/bathroom_texture.png")
    textures.append(texture_aux)
    vet_idx['bathroom'] = 4

    vertexes_aux_6 = load_obj_to_glm_array('./objects/ground/ground.obj')
    ini = vet[4]['inicio'] + vet[4]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_6)/8)})
    texture_aux = loadTexture("./objects/ground/ground_texture.jpg")
    textures.append(texture_aux)
    vet_idx['ground'] = 5

    vertexes_aux_7 = load_obj_to_glm_array('./objects/house/house.obj')
    ini = vet[5]['inicio'] + vet[5]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_7)/8)})
    texture_aux = loadTexture("./objects/house/house_texture.jpg")
    textures.append(texture_aux)
    vet_idx['house'] = 6

    vertexes_aux_8 = load_obj_to_glm_array('./objects/sky/sky.obj')
    ini = vet[6]['inicio'] + vet[6]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_8)/8)})
    texture_aux = loadTexture("./objects/sky/sky_texture.jpg")
    textures.append(texture_aux)
    vet_idx['sky'] = 7

    vertexes_aux_9 = load_obj_to_glm_array('./objects/vase/vase.obj')
    ini = vet[7]['inicio'] + vet[7]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_9)/8)})
    texture_aux = loadTexture("./objects/vase/vase_texture.png")
    textures.append(texture_aux)
    vet_idx['vase'] = 8

    vertexes_aux_10 = load_obj_to_glm_array('./objects/plant/plant1.obj')
    ini = vet[8]['inicio'] + vet[8]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_10)/8)})
    texture_aux = loadTexture("./objects/plant/plant1_texture.png")
    textures.append(texture_aux)
    vet_idx['plant1'] = 9

    vertexes_aux_11 = load_obj_to_glm_array('./objects/plant/plant2.obj')
    ini = vet[9]['inicio'] + vet[9]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_11)/8)})
    texture_aux = loadTexture("./objects/plant/plant2_texture.png")
    textures.append(texture_aux)
    vet_idx['plant2'] = 10

    vertexes_aux_12 = load_obj_to_glm_array('./objects/lamp/lamp.obj')
    ini = vet[10]['inicio'] + vet[10]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_12)/8)})
    texture_aux = loadTexture("./objects/lamp/lamp_texture.png")
    textures.append(texture_aux)
    vet_idx['lamp'] = 11

    vertexes_aux_13 = load_obj_to_glm_array('./objects/lantern/lantern.obj')
    ini = vet[11]['inicio'] + vet[11]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_13)/8)})
    texture_aux = loadTexture("./objects/lantern/lantern_texture.jpg")
    textures.append(texture_aux)
    vet_idx['lantern'] = 12

    vertexes_aux_14 = load_obj_to_glm_array('./objects/magic_ball/ball.obj')
    ini = vet[12]['inicio'] + vet[12]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_14)/8)})
    texture_aux = loadTexture("./objects/magic_ball/ball_texture.jpg")
    textures.append(texture_aux)
    vet_idx['magic_ball'] = 13

    vertexes_aux_15 = load_obj_to_glm_array('./objects/magic_ball/stand.obj')
    ini = vet[13]['inicio'] + vet[13]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_15)/8)})
    texture_aux = loadTexture("./objects/magic_ball/stand_texture.jpg")
    textures.append(texture_aux)
    vet_idx['magic_ball_stand'] = 14

    vertexes_aux_16 = load_obj_to_glm_array('./objects/shrek/shrek.obj')
    ini = vet[14]['inicio'] + vet[14]['tam']
    vet.append({'inicio': ini, 'tam': int(len(vertexes_aux_16)/8)})
    texture_aux = loadTexture("./objects/shrek/shrek_texture.jpg")
    textures.append(texture_aux)
    texture_aux = loadTexture("./objects/shrek/leather_texture.jpg")
    textures.append(texture_aux)
    vet_idx['shrek'] = 15

    combined_vertices = glm.array(glm.float32, *vertexes_aux_1[:], *vertexes_aux_2[:], *vertexes_aux_3[:], *vertexes_aux_4[:], 
                                  *vertexes_aux_5[:], *vertexes_aux_6[:], *vertexes_aux_7[:], *vertexes_aux_8[:], *vertexes_aux_9[:],
                                  *vertexes_aux_10[:], *vertexes_aux_11[:], *vertexes_aux_12[:], *vertexes_aux_13[:], *vertexes_aux_14[:],
                                  *vertexes_aux_15[:], *vertexes_aux_16[:])
    
    return combined_vertices, textures, vet, vet_idx