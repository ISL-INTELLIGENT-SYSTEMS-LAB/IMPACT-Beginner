import os
import shutil

""" 
    This script is used to sort the images into their respective folders so that they can be used for training the model.
    
    Simply place this file in the same directory as the images folder and run it.
"""


def main():
    """
        This function calls the labelIdentifier function on each of the three files that contain the image names and their labels
    """
    
    with open('test-set-v2.1.txt', 'r') as file:
        labelIdentifier(file)
        
    with open('train-set-v2.1.txt', 'r') as file:
        labelIdentifier(file)
        
    with open('val-set-v2.1.txt', 'r') as file:
        labelIdentifier(file)
        
        
def labelIdentifier(file):
    """
        This function takes in a file and sorts the images into their respective folders based on their labels
    """
    basepath = os.getcwd()
    
    
    for line in file:
        image, label = line.split()
        
        if label == '0':
            imageMover(image, os.path.join(basepath, r'images/Arm cover'))
        elif label == '1':
            imageMover(image, os.path.join(basepath, r'images/Other rover part'))
        elif label == '2':
            imageMover(image, os.path.join(basepath, r'images/Artifact'))
        elif label == '3':
            imageMover(image, os.path.join(basepath, r'images/Nearby surface'))
        elif label == '4':
            imageMover(image, os.path.join(basepath, r'images/Close-up rock'))
        elif label == '5':
            imageMover(image, os.path.join(basepath, r'images/DRT'))
        elif label == '6':
            imageMover(image, os.path.join(basepath, r'images/DRT spot'))
        elif label == '7':
            imageMover(image, os.path.join(basepath, r'images/Distant landscape'))
        elif label == '8':
            imageMover(image, os.path.join(basepath, r'images/Drill hole'))
        elif label == '9':
            imageMover(image, os.path.join(basepath, r'images/Night sky'))
        elif label == '10':
            imageMover(image, os.path.join(basepath, r'images/Floats'))
        elif label == '11':
            imageMover(image, os.path.join(basepath, r'images/Layers'))
        elif label == '12':
            imageMover(image, os.path.join(basepath, r'images/Light-toned veins'))
        elif label == '13':
            imageMover(image, os.path.join(basepath, r'images/Mastcam cal target'))
        elif label == '14':
            imageMover(image, os.path.join(basepath, r'images/Sand'))
        elif label == '15':
            imageMover(image, os.path.join(basepath, r'images/Sun'))
        elif label == '16':
            imageMover(image, os.path.join(basepath, r'images/Wheel'))
        elif label == '17':
            imageMover(image, os.path.join(basepath, r'images/Wheel joint'))
        elif label == '18':
            imageMover(image, os.path.join(basepath, r'images/Wheel tracks'))
        else:
            imageMover(image, os.path.join(basepath, r'images/Unknown'))
        

def imageMover(image, destination):
    """
        This function takes in an image and moves them to their appropriate destination folder
    """
    os.makedirs(destination, exist_ok=True)
    
    try:
        shutil.move(os.path.join(os.getcwd(), r'images/', image) , destination)
        print(f'Moved %s to %s' % (image, destination))
    except:
        pass
        

# Calls the main function if this file is run directly
if __name__ == '__main__':
    main()