import os

def generate_negative_description_file():
    with open("neg.txt", "w") as f:
        for filename in os.listdir("negative"):
            f.write("Negative\\"+ filename + "\n")

generate_negative_description_file()

# Cmd codes to train the cascade classifier model:

# Run the marker
#C:\Users\Julio\Desktop\new_project_read_imagen>C:\Users\Julio\Desktop\opencv\build\x64\vc15\bin\opencv_annotation.exe --annotations=pos.txt --images=Positive  
# Run Create sample
#C:\Users\Julio\Desktop\new_project_read_imagen>C:\Users\Julio\Desktop\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec 
# Run Training
#C:\Users\Julio\Desktop\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data Cascade\ -vec pos.vec -bg neg.txt -w 24 -h 24 -numPos 100 -nunNeg 200 -numStages 12 -maxFalseAlarmRate 0.3 -minHitRate 0.999   

