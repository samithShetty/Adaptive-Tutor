import os
import random

def generateEquation(topic):
    image_folder_path = os.getcwd() + "\\imageProblems"
     # Get a list of image file names in the folder
    image_files = [f for f in os.listdir(image_folder_path) if f.lower().endswith(('.png')) and f.startswith(topic)]

    # Select a random image file
    random_image_file = random.choice(image_files)

    # Create a full file path to the selected image
    image_path = os.path.join(image_folder_path, random_image_file)
    #print(image_path)
    return image_path

def ImageAnswer(imagePath):
    imagePath = imagePath.split('\\')[-1]
    if imagePath == "Discrete_Probability_1.png":
        return 0.41
    elif imagePath == "Discrete_Probability_2.png":
        return 0.5
    elif imagePath == "Discrete_Probability_3.png":
        return 0.83
    elif imagePath == "Discrete_Probability_4.png":
        return 0.17
    elif imagePath == "Discrete_Probability_5.png":
        return 150
    elif imagePath == "Discrete_Probability_6.png":
        return 0.01
    elif imagePath == "Discrete_Probability_7.png":
        return 0.99
    elif imagePath == "Discrete_Probability_8.png":
        return 0.39
    elif imagePath == "Discrete_Probability_9.png":
        return 0.78
    elif imagePath == "Discrete_Probability_10.png":
        return 0.56
    elif imagePath == "Discrete_Probability_11.png":
        return 12
    elif imagePath == "Continuous_Random_Variables_1.png":
        return 675
    elif imagePath == "Continuous_Random_Variables_2.png":
        return 19
    elif imagePath == "Continuous_Random_Variables_3.png":
        return 0.5948
    elif imagePath == "Continuous_Random_Variables_4.png":
        return 0.8023
    elif imagePath == "Continuous_Random_Variables_5.png":
        return 0.3028
    elif imagePath == "Continuous_Random_Variables_6.png":
        return 0.5222
    elif imagePath == "Continuous_Random_Variables_7.png":
        return 84.5
    elif imagePath == "Continuous_Random_Variables_8.png":
        return 23
    elif imagePath == "Continuous_Random_Variables_9.png":
        return 19.88
    elif imagePath == "Continuous_Random_Variables_10.png":
        return 116.45
    elif imagePath == "Continuous_Random_Variables_11.png":
        return 20
    elif imagePath == "Sampling_Distribution_1.png":
        return 0.8802
    elif imagePath == "Sampling_Distribution_2.png":
        return 0.6898
    elif imagePath == "Sampling_Distribution_3.png":
        return 0.3
    elif imagePath == "Sampling_Distribution_4.png":
        return 0.0228
    elif imagePath == "Sampling_Distribution_5.png":
        return 280


def main():
    topic = input("Enter Topic: ")
    imagePath = generateEquation(topic)
    print(imagePath, ImageAnswer(imagePath))
    

if __name__ == "__main__":
    main()