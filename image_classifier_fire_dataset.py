import os

"""
Drop this program in the top level directory of the dataset (the same level with the 'the_wildfire_dataset.csv')

LABELS FOR THE IMAGES:
1 - Both_smoke_and_fire
2 - Smoke_from_fires
3 - Fire_confounding_elements
4 - Forested_areas_without_confounding_elements
5 - Smoke_confounding_elements
"""

# Gets the current working directory that the python file is located in 
currentDir = str(os.getcwd()) + '/the_wildfire_dataset/the_wildfire_dataset/'

# Changes the text colors in the console to make it easier to read
class bcolors:
    FAIL = '\033[91m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

# Print the menu to allow the user to select individual folders or all at once
def main():
    while True:
        # Prints the menu for the user
        print("Which data category would you like to classify? (please make a selection)")
        print("1. Test dataset")
        print("2. Train dataset")
        print("3. Val dataset")
        print("4. Exit")
        
        usr_choice = str(input("\n>:"))
        
        try:
            match usr_choice:
                # Test dataset
                case "1":
                    fileWriter("test", "test_classified.csv")
                
                # Train dataset
                case "2":
                    fileWriter("train", "train_classified.csv")
                
                # Val dataset
                case "3":
                    fileWriter("val", "val_classified.csv")
                
                # Terminates the program
                case "4":
                    break

                # Raises an exception if the user made an invalid choice
                case _:
                    raise Exception
        
        # Prints the error message to the user
        except:
            print(Exception(bcolors.FAIL + "Please choose a valid option\n" + bcolors.ENDC))



def fileWriter(folderName, fileName):
    # Creates the working directory
    workingDir = currentDir + "/" + folderName

    # Collects all of the image names for each folder
    bothSmokeAndFireImages = os.listdir(workingDir + "/fire/Both_smoke_and_fire")
    smokeFromFiresImages = os.listdir(workingDir + "/fire/Smoke_from_fires")
    fireConfoundingElementsImages = os.listdir(workingDir + "/nofire/Fire_confounding_elements")
    forestedAreasWithoutConfoundingElementsImages = os.listdir(workingDir + "/nofire/Forested_areas_without_confounding_elements")
    smokeConfoundingElementsImages = os.listdir(workingDir + "/nofire/Smoke_confounding_elements")

    # Writes all file names with their appropriate label
    with open(fileName, 'w') as file:
        file.write("Label,Image file name\n")

        # Writes Both_smoke_and_fire folder contents with the label '1'
        for img in bothSmokeAndFireImages:
            file.write("1," + img + "\n")

        # Writes Smoke_from_fires folder contents with the label '2'    
        for img in smokeFromFiresImages:
            file.write("2," + img + "\n")

        # Writes Fire_confounding_elements folder contents with the label '3'
        for img in fireConfoundingElementsImages:
            file.write("3," + img + "\n")

        # Writes Forested_areas_without_confounding_elements folder contents with the label '4'
        for img in forestedAreasWithoutConfoundingElementsImages:
            file.write("4," + img + "\n")
    
        # Writes Smoke_confounding_elements folder contents with the label '5'
        for img in smokeConfoundingElementsImages:
            file.write("5," + img + "\n")

    # Prints the conformation
    print(bcolors.OKGREEN + "File written succefully\n" + bcolors.ENDC)


# Checks if the program is the main file of if it was called from a different program
if __name__ == '__main__':
    main()
