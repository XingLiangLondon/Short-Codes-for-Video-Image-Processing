cam = cv2.VideoCapture("C:/Users/user/Documents/Dunhill Project/Project Data/Test/BM1c.MOV")
# Get video/camera input details
lengthVideo = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
print("Video Length",lengthVideo)
widthVideo  = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Video Width", widthVideo)
heightVideo = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Video Height",heightVideo)

# fps for video input with a stream header (need nb_frames field) 
fpsVideo = int(cam.get(cv2.CAP_PROP_FPS)) 
print("FPS", fpsVideo)
