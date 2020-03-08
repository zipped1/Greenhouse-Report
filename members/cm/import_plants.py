import bpy
import os
import glob
import random


# Get OBJ files
directory_im = "C:/Users/Carla/OneDrive/Uniunterlagen/Master/Systems_engineering_meets_life_sciences/obj_files/"
size = 10  # To change the size just change this line. The rest is proportional
plantsRow = 6 

nrPlants = 42
all_files = glob.glob(directory_im + "*.obj")
files = random.choices(all_files, k=nrPlants)
counter = 0


for f in files:
    print("______________________________________________________")
    
    # Place each plant in the scene
    head, tail = os.path.split(f)
    collection_name = tail.replace('.obj', '')
    bpy.ops.import_scene.obj(filepath=f,
     use_split_groups = True, global_clight_size = size)

    # Move each plant in an own collection
    myCol = bpy.data.collections.new(collection_name)
    bpy.context.scene.collection.children.link(myCol)
    
    # Calculate were to position the plant
    xpos = (counter % plantsRow) * (size / 4)
    ypos = (counter // plantsRow) *  (size / 2)
    
    # Remove the link to the main context
    for ob in bpy.context.selected_objects:
        myCol.objects.link(ob)
        bpy.context.collection.objects.unlink(ob)
        ob.location.x = xpos 
        ob.location.y = ypos 
    
    # Place the pipe
    length = size / 2.5
    bpy.ops.mesh.primitive_cylinder_add(radius = size / 200,
     depth = length, location = (xpos, ypos + (size / 30),
     length / 2))
    cube = bpy.context.selected_objects[0]
    myCol.objects.link(cube)
    bpy.context.collection.objects.unlink(cube)
    
    bpy.ops.mesh.primitive_plane_add(size=size / 4,
     location = (xpos + (size / 30), ypos, 0))
    plane = bpy.context.selected_objects[0]
    
    myCol.objects.link(plane)
    bpy.context.collection.objects.unlink(plane)
    counter += 1