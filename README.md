# OpenCV_Trial

i start this repository as i was interested in the library OpenCV and his aplications, obviusly the way more easy to learn this concept was apply to some games, as is a concept that is quite funny for me.

Some problems that i encounter was the way that some games render their windows size imagen.

And the time that would consume really to take all the imagens and train the model properly.

At the start the model was working just fine but the FPS was down to 6, that was not optimal, by the end of the time i decide to remake all the program following a tutorial about open CV and Threading, the firstone help me to tidy up the code and reorganize using clases and the secondone make it jump from 6 fps to 300 fps.

I was used to clases but not to multi-threading but is a topic that i would start to pay more attention as its clear how much power it gives you.

As it's right now the model capture really good whatever imagen of a enemy until certain distance (i can guess this is caused for the mayority of imagens have been taken in that range of distnce) this is obvius when you see we work with a really small dataset about a 100 positives and 100 negatives, something rasonable would be more like 500 and 500.

Other thing that im not happy with is the stages of training or the -maxFalseAlarmRate as 0.3 in this case i think is leading to overfitting, but as i say tune this model properly would take few days and im quite happy with it working as it is. 

Have Been a good learning.


