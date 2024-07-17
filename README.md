<p align="center">
  <img src="https://github.com/dhhruv/Chrome-Dino-Runner/blob/master/assets/DinoWallpaper.png" width="97" height="97">
  <h2 align="center" style="margin-top: -4px !important;">A Replica of the hidden Dinosaur Game from Chrome Browser Offline mode controlled by EMG signal</h2>



### About:

-	This project used a game developed by other users, Dino Runner (an offline game from Google), and replaced the input that allowed the dinosaur's actions to be controlled.
In the case of the previously developed project, clicking on the space bar made the dinosaur jump. In the case of the project I developed, the dinosaur jumps after detecting a muscle contraction via the electromyographic signal.

-	The  signal was collected via the BITalino (r)evolution Board and processed by filtering, rectifying, smoothing and calculating the RMS in real time.
Thresold logic was then developed. When the calculated RMS was higher than a certain thresold, it was assumed that a muscle contraction had been detected and the dinosaur would jump.

### Game Logic:

![DinoRun_Logic](https://github.com/user-attachments/assets/5d4c0f50-d765-445d-a9b0-393c323db65e)



https://github.com/user-attachments/assets/32c20932-5339-4ba2-82b1-ee8a1067ac5a





### Input:

| Control              | Actions                                                       |
|--------------------- |---------------------------------------------------------------|
|Muscle contraction    |  Jump                           




