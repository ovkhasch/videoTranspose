import cv2
import numpy as np

def transform_video(input_file, output_file):
    # Read the input video
    cap = cv2.VideoCapture(input_file)
    if not cap.isOpened():
        print("Error opening video file")
        return

    # Get input video properties
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Prepare the output video writer
    out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_count, frame_height))

    # Initialize a numpy array to store output frames
    input_frames = np.zeros((frame_count, frame_height, frame_width, 3), dtype=np.uint8)

    # Process each frame
    for frame_idx in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break
        # Assign pixels to the correct position in the output frames
        input_frames[frame_idx] = frame

    output_frames = input_frames.transpose(2, 1, 0, 3)
    print(frame_width, frame_height, frame_count)
    print("Dimensions of input_frames:", input_frames.shape)
    print("Dimensions of output_frames:", output_frames.shape)

    # Write output frames to the output video
    for i in range(frame_width):
        out_frame = output_frames[i]
        out.write(out_frame)

    # Release resources
    cap.release()
    out.release()

# Example usage
transform_video('taurus_littrow_valley_360p30.mp4', 'output.mp4')
