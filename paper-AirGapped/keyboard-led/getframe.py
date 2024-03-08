import cv2, sys

filepath = sys.argv[1]
destination = sys.argv[2]

def extract_frames(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_filename = f"{output_folder}/frame_{frame_count:04d}.jpg"
        cv2.imwrite(frame_filename, frame)
        
        frame_count += 1
    
    cap.release()
    cv2.destroyAllWindows()

input_video_path = filepath
output_frame_folder = destination
extract_frames(input_video_path, output_frame_folder)
