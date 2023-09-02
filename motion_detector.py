import cv2
import pandas
from datetime import datetime

# Initialize variables
first_frame = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns=["Start", "End"])

# Open the video capture device (webcam)
video = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture device
    check, frame = video.read()

    status = 0

    # Convert the frame to grayscale and apply Gaussian blur for noise reduction
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # If it's the first frame, initialize it and continue
    if first_frame is None:
        first_frame = gray
        continue

    # Calculate the absolute difference between the current frame and the first frame
    delta_frame = cv2.absdiff(first_frame, gray)

    # Apply a binary threshold to create a motion mask
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Find contours in the thresholded frame
    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:  # Adjust this threshold as needed
            continue

        status = 1

        # Draw bounding boxes around moving objects
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Update the status list
    status_list.append(status)
    status_list = status_list[-2:]

    # Record start and end times when motion is detected
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    # Display various frames for debugging
    cv2.imshow("Gray", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)

    # Press 'q' to exit the loop
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

# Print status list and recorded times
print(status_list)
print(times)

# Create a DataFrame and save motion event times to a CSV file
for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End": times[i + 1]}, ignore_index=True)

df.to_csv("Times.csv")

# Release the video capture device and close OpenCV windows
video.release()
cv2.destroyAllWindows()
