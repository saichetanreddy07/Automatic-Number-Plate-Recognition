## Automatic-Number-Plate-Recognition using EasyOCR

# 1. Introduction
Number plate recognition is an essential task in many modern-day applications, such as automatic toll collection, traffic monitoring, and vehicle identification. This project focuses on developing a system that uses Optical Character Recognition (OCR) to extract and identify vehicle license plate numbers from images.

# Project Group Members
This project was completed as a collaborative effort by the following team members:

-	B V SAI CHETAN REDDY   
- K VISHNU VARDHAN      
-	Y KASHYAP MADHAV                            

# 3. Objectives
The main objectives of this project are:

-	To accurately detect and recognize vehicle number plates from images.
-	To extract and interpret characters from number plates using OCR technology.
-	To create a user-friendly system that can be integrated into broader traffic management systems.

# 4. Technology Stack

•	Programming Language: Python

•	Libraries and Tools:

  -	OpenCV: For image processing and pre-processing of the input images.
  -	EasyOCR: For character recognition from the number plate.
  -	NumPy: For array manipulations and numerical operations.

# 5. Methodology

## 5.1 Image Acquisition
The system takes input images either through a live video feed or as pre-stored image files. The input is processed to identify and localize the number plate.

## 5.2 Image Preprocessing
Various image preprocessing techniques are applied to improve the quality of the number plate area. This includes:
- 	### Grayscale Conversion:
    Converting the image to grayscale for easier processing.
-   ### Thresholding:
    Binarizing the image for better contrast between the plate and the background.
-   ### Edge Detection:
     Using techniques like Canny edge detection to identify the boundaries of the plate.

## 5.3 Number Plate Detection
The number plate is localized using contour detection and bounding box techniques. Once detected, the plate area is cropped from the image for further processing.

## 5.4 OCR for Character Recognition
EasyOCR is used to extract characters from the number plate. The OCR model processes the cropped image of the number plate and converts the detected characters into text.

## 5.5 Post-Processing
Post-processing involves cleaning and formatting the OCR output to ensure accuracy. Any non-alphanumeric characters detected due to noise are removed, and corrections are made if necessary.

## 6. Results
-	The system successfully detects and extracts characters from vehicle number plates.
-	The OCR model provides an accuracy rate of approximately [mention accuracy percentage] on test datasets.
-	The system can handle varying lighting conditions and orientations of the number plates to a certain extent.

## 7. Challenges and Future Work
### Challenges:
- Handling skewed or angled number plates.
- Detecting plates in poor lighting conditions or with obstructions.

### Future Enhancements:
- Implementing a deep learning-based approach to improve detection accuracy.
- Adding real-time detection capability with faster processing.


## 8. Conclusion
The number plate recognition system built using EasyOCR and OpenCV provides an efficient solution for vehicle identification. The system achieves its goal of extracting and recognizing characters from vehicle number plates, demonstrating the practical application of OCR technology in real-world scenarios.
