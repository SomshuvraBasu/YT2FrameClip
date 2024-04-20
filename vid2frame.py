import cv2
import os

def time_to_seconds(time_str):
    # Convert time string in format 'mm:ss' to seconds
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

def extract_frames(video_path, output_folder, start_time, end_time):
    try:
        # Create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Open the video file
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        start_frame = int(start_time * fps)
        end_frame = int(end_time * fps)

        # Set the frame position to the start frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        # Read until reaching the end frame
        while cap.isOpened() and cap.get(cv2.CAP_PROP_POS_FRAMES) < end_frame:
            # Read a frame
            ret, frame = cap.read()
            if not ret:
                break

            # Save frame as an image
            frame_filename = f"frame_{int(cap.get(cv2.CAP_PROP_POS_FRAMES)):04d}.jpg"
            frame_path = os.path.join(output_folder, frame_filename)
            cv2.imwrite(frame_path, frame)

        # Release the video capture object
        cap.release()
        print(f"Frames extracted from {start_time} to {end_time} and saved to '{output_folder}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    video_path = input("Enter the path of the video file: ")
    start_time_str = input("Enter the start timestamp in format 'mm:ss': ")
    end_time_str = input("Enter the end timestamp in format 'mm:ss': ")
    start_time = time_to_seconds(start_time_str)
    end_time = time_to_seconds(end_time_str)
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_folder = os.path.join(os.path.dirname(video_path), f"{video_name}_frames_from_{start_time_str}_to_{end_time_str}")

    extract_frames(video_path, output_folder, start_time, end_time)
