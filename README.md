Swap X and time axis of a video

* Read the input video and extract frames.
* For each frame, iterate over its pixels and place them in the output frames where the new X-coordinate is the frame index of the input video, and the Y-coordinate remains the same.
* The width of the output video is equal to the number of frames in the input video, and its height is the same as the input video's height.
* The number of frames in the output video is equal to the width of the input video.
* Write these frames to create the output video.
