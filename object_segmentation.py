import cv2
from ultralytics import YOLO

#load the yolov8 segmentatin model
model=YOLO('yolov8n-seg.pt')


#intialize the video capture object
cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("Error: Could not open video.")
    exit()
    
    
    
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Perform object segmentation on the frame
        results = model(frame)

        # Annotate the frame with the segmentation results
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("Object Segmentation", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
    
    