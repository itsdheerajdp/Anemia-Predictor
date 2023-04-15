import cv2 as cv

cam_port = 0
cam = cv.VideoCapture(cam_port)

while True:
    # Read the next frame from the camera
    result, image = cam.read()
    if not result:
        print("No image detected. Please try again.")
        continue

    # Show the current frame
    cv.imshow("Camera", image)

    # Wait for a key press
    key = cv.waitKey(1) & 0xFF

    # If the 'c' key is pressed, capture the image
    if key == ord("c"):
        cv.imshow("Prediction", image)
        cv.imwrite("predict.png", image)
        cv.waitKey(0)
        cv.destroyWindow("Prediction")
        break

# Clean up the camera resources
cam.release()
cv.destroyAllWindows()
