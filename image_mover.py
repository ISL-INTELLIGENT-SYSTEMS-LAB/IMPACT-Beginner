import os
import shutil

# This script is used to sort the images into their respective folders so that they can be used for training the model

# The following lists are used to store the images
armCover = []
otherRoverPart = []
artifact = []
nearbySurface = []
closeUpRock = []
drt = []
drtSpot = []
distantLandscape = []
drillHole = []
nightSky = []
floats = []
layers = []
lightTonedVeins = []
mastcamCalTarget = []
sand = []
sun = []
wheel = []
wheelJoint = []
wheelTracks = []

# This list is used to store images that are not labeled correctly
trash = []


def main():
    """
        This function calls the labelIdentifier function on each of the three files and then calls 
        the image_mover function on each of the lists to move the images to their appropriate folders
    """
    
    with open('test-set-v2.1.txt', 'r') as f:
        labelIdentifier(f)
        
    with open('train-set-v2.1.txt', 'r') as f:
        labelIdentifier(f)
        
    with open('val-set-v2.1.txt', 'r') as f:
        labelIdentifier(f)
        
        
    image_mover(armCover, os.getcwd() +'\\images\\Arm cover')
    image_mover(otherRoverPart, os.getcwd() +'\\images\\Other rover part')
    image_mover(artifact, os.getcwd() +'\\images\\Artifact')
    image_mover(nearbySurface, os.getcwd() +'\\images\\Nearby surface')
    image_mover(closeUpRock, os.getcwd() +'\\images\\Close-up rock')
    image_mover(drt, os.getcwd() +'\\images\\DRT')
    image_mover(drtSpot, os.getcwd() +'\\images\\DRT spot')
    image_mover(distantLandscape, os.getcwd() +'\\images\\Distant landscape')
    image_mover(drillHole, os.getcwd() +'\\images\\Drill hole')
    image_mover(nightSky, os.getcwd() +'\\images\\Night sky')
    image_mover(floats, os.getcwd() +'\\images\\Float')
    image_mover(layers, os.getcwd() +'\\images\\Layers')
    image_mover(lightTonedVeins, os.getcwd() +'\\images\\Light-toned veins')
    image_mover(mastcamCalTarget, os.getcwd() +'\\images\\Mastcam cal target')
    image_mover(sand, os.getcwd() +'\\images\\Sand')
    image_mover(sun, os.getcwd() +'\\images\\Sun')
    image_mover(wheel, os.getcwd() +'\\images\\Wheel')
    image_mover(wheelJoint, os.getcwd() +'\\images\\Wheel joint')
    image_mover(wheelTracks, os.getcwd() +'\\images\\Wheel tracks')
    image_mover(trash, os.getcwd() +'\\images\\_Trash')


def image_mover(list, destination):
    """
        This function takes in a list of images and moves them to their appropriate destination folder
    """
    
    os.makedirs(destination, exist_ok=True)
    
    for image in list:
        try:
            shutil.move(os.getcwd() + '\\images\\' + image, destination)
            print('Moved ' + image + ' to ' + destination)
        except:
            pass
        

def labelIdentifier(f):
    """
        This function takes in a file and sorts the images into their respective lists
    """
    
    for line in f:
        image, label = line.split()
        
        if label == '0':
            armCover.append(image)
        elif label == '1':
            otherRoverPart.append(image)
        elif label == '2':
            artifact.append(image)
        elif label == '3':
            nearbySurface.append(image)
        elif label == '4':
            closeUpRock.append(image)
        elif label == '5':
            drt.append(image)
        elif label == '6':
            drtSpot.append(image)
        elif label == '7':
            distantLandscape.append(image)
        elif label == '8':
            drillHole.append(image)
        elif label == '9':
            nightSky.append(image)
        elif label == '10':
            floats.append(image)
        elif label == '11':
            layers.append(image)
        elif label == '12':
            lightTonedVeins.append(image)
        elif label == '13':
            mastcamCalTarget.append(image)
        elif label == '14':
            sand.append(image)
        elif label == '15':
            sun.append(image)
        elif label == '16':
            wheel.append(image)
        elif label == '17':
            wheelJoint.append(image)
        elif label == '18':
            wheelTracks.append(image)
        else:
            trash.append(image)
    
# Calls the main function if this file is run directly
if __name__ == '__main__':
    main()