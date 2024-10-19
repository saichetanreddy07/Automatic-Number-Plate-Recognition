import cv2
import numpy as np
import imutils
import easyocr

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])

# Function to map the state code to the full state name
def get_state_from_code(code):
    state_codes = {
        'KA': 'Karnataka',
        'MH': 'Maharashtra',
        'DL': 'Delhi',
        'TN': 'Tamil Nadu',
        'GJ': 'Gujarat',
        'UP': 'Uttar Pradesh',
        # Add more state codes as needed
    }
    return state_codes.get(code, "Unknown State")

# Function to extract the place of registration from the number plate text
def extract_registration_place(text):
    if len(text) > 2 and text[0:2].isalpha():
        state_code = text[0:2].upper()
        return get_state_from_code(state_code)
    return "Unknown"

# Open the camera (0 is usually the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, img = cap.read()

    # Check if the frame is captured correctly
    if not ret:
        print("Failed to capture image")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Noise reduction
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)

    # Edge detection
    edged = cv2.Canny(bfilter, 30, 200)

    # Find contours
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:  # We assume the number plate has 4 corners
            location = approx
            break

    if location is not None:
        # Create a mask for the number plate region
        mask = np.zeros(gray.shape, np.uint8)
        new_image = cv2.drawContours(mask, [location], 0, 255, -1)
        new_image = cv2.bitwise_and(img, img, mask=mask)

        # Extract coordinates for the number plate
        (x, y) = np.where(mask == 255)
        (x1, y1) = (np.min(x), np.min(y))
        (x2, y2) = (np.max(x), np.max(y))
        cropped_image = gray[x1:x2 + 1, y1:y2 + 1]

        # Perform OCR on the cropped image
        result = reader.readtext(cropped_image)

        if result:
            text = result[0][-2]  # Get the detected text
            accuracy = result[0][-1]  # Get the accuracy/confidence score

            # Extract the place of registration from the detected number plate
            registration_place = extract_registration_place(text)

            # Print the number plate, accuracy, and place of registration
            print(f"Detected Number Plate: {text}")
            print(f"Accuracy: {accuracy * 100:.2f}%")
            print(f"Place of Registration (State): {registration_place}")

            # Display the detected text on the image
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, text, (approx[0][0][0], approx[1][0][1] + 60), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

            # Display the accuracy as a percentage
            cv2.putText(img, f'Accuracy: {accuracy*100:.2f}%', (approx[0][0][0], approx[1][0][1] + 100), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

            # Draw a rectangle around the detected number plate
            cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0, 255, 0), 3)

    # Display the resulting frame
    cv2.imshow('Number Plate Detection', img)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
