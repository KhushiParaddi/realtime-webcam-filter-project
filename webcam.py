import cv2

# Start webcam
cap = cv2.VideoCapture(0)

# Mode variable (controls filter)
mode = 0

print("Press keys to change filters:")
print("0 - Normal")
print("1 - Grayscale")
print("2 - Blur")
print("3 - Edge Detection")
print("4 - Brightness Adjustment")
print("ESC - Exit")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to access webcam")
        break

    # Apply filters based on mode
    if mode == 0:
        output = frame

    elif mode == 1:
        # Convert to grayscale
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    elif mode == 2:
        # Apply Gaussian blur
        output = cv2.GaussianBlur(frame, (15, 15), 0)

    elif mode == 3:
        # Edge detection
        output = cv2.Canny(frame, 100, 200)

    elif mode == 4:
        # Increase brightness and contrast
        output = cv2.convertScaleAbs(frame, alpha=1.3, beta=40)

    # Display the result
    cv2.imshow("Real-Time Webcam Filters", output)

    # Detect key press
    key = cv2.waitKey(1) & 0xFF

    if key == ord('0'):
        mode = 0
    elif key == ord('1'):
        mode = 1
    elif key == ord('2'):
        mode = 2
    elif key == ord('3'):
        mode = 3
    elif key == ord('4'):
        mode = 4
    elif key == 27:  # ESC key
        break

# Release resources
cap.release()
cv2.destroyAllWindows()