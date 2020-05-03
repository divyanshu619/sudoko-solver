import cv2
import pytesseract
import numpy as np

# Read image from which text needs to be extracted
img = cv2.imread("download.jpg")

# Preprocessing the image starts

# Convert the image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Performing OTSU threshold
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Specify structure shape and kernel size.
# Kernel size increases or decreases the area
# of the rectangle to be detected.
# A smaller value like (10, 10) will detect
# each word instead of a sentence.
kernel_len = np.array(img).shape[1]//220
ver_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_len))
hor_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_len, 1))

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
image_1 = cv2.erode(thresh1, ver_kernel, iterations=1)
vertical_lines = cv2.dilate(image_1, ver_kernel, iterations=1)

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
image_1 = cv2.erode(thresh1, hor_kernel, iterations=1)
horizontal_lines = cv2.dilate(image_1, hor_kernel, iterations=1)

# Appplying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
# rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
# erosion = cv2.erode(dilation, rect_kernel, iterations=1)
# rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
# opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, rect_kernel)
# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("original", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Creating a copy of image
im2 = img.copy()

# A text file is created and flushed
file = open("recognized.txt", "w+")
file.write("")
file.close()

# Looping through the identified contours
# Then rectangular part is cropped and passed on
# to pytesseract for extracting text from it
# Extracted text is then written into the text file
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Drawing a rectangle on copied image
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Cropping the text block for giving input to OCR
    cropped = im2[y:y + h, x:x + w]
    # cv2.imshow("original", rect)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Open the file in append mode
    file = open("recognized.txt", "a")

    # Apply OCR on the cropped image
    text = pytesseract.image_to_string(cropped)

    # Appending the text into file
    file.write(text)
    file.write("\n")

    # Close the file
    file.close()
