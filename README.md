# OpenCV_Trial
# ABOUTS

I start this repository as i was interested in the library OpenCV and his aplications, obviusly the way more easy to learn this concept was apply to some games, as is a concept that is quite funny for me.

Some problems that i encounter:
- Some games do not resize their windows they proyect it, so you can not use win32gui.FindWindow to capture the window and you need to record the full screen. (is a problem when you use just one screen)
- Some games eat the key inputs when you are in game so its dificult to have keybindings for your programs, i know i could go arround this... but time would start to be a problem
- The time that actually gets to tune the model to a optimal standars.
- The size of the dataset that i use.

* about a 60 positives and 80 negatives, something rasonable would be more like 500 and 500, the problem comes with after taking the pictures actually you need manually to draw the circles with "opencv_annotation", then create the samples with "opencv_createsamples" to then train the cascade "opencv_traincascade"

# DEVELOPMENT

At the start the model was working just fine but the FPS was down to 6, that was not optimal, by the end i decide to remake all the program following a tutorial about openCV and Threading, the firstone help me to tidy up the code and reorganize using clases and the secondone make it jump from 6 fps to 200 fps.

I was used to clases but not to multi-threading but is a topic that i would start to pay more attention as its clear how much power it gives you.
                                         
# PROGRAM

As it's right now the model capture really good whatever imagen of a enemy until certain distance (i can guess this is caused for the mayority of imagens have been taken in that range of distnce) this is obvius when you see we work with a really small dataset 

Other thing that im not happy with is the stages of training or the -maxFalseAlarmRate as 0.3 in this case i think is leading to overfitting, but as i say tune this model properly would take few days and im quite happy with it working as it as i dont gonna have future uses for it.



# Without Threading
<img = https://github.com/kylekk76/OpenCV_Trial/blob/main/without_threading.png>
# With Threading
<img = https://github.com/kylekk76/OpenCV_Trial/blob/main/with_threading.png>
