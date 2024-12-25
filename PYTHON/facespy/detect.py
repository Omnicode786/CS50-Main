import cv2
from PIL import Image
import os

# Check if the image exists at the given path
image_path = r"C:\Users\lkj\OneDrive\Desktop\CS50\PYTHON\facespy\faces.jpg"  # Raw string path

if not os.path.exists(image_path):
    print("Error: The image file does not exist at the specified path.")
    exit()

# Load the image
image = cv2.imread(image_path)

# Check if the image was loaded correctly
if image is None:
    print(f"Error: Could not open or read the image {image_path}.")
    exit()

# Convert to grayscale (required for face detection)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load the pre-trained face detector (Haar Cascade classifier)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Check if faces were found and print the result
if len(faces) > 0:
    print(f"Found {len(faces)} face(s)")

    # Create a copy of the original image to draw rectangles on
    output_image = image.copy()

    # Loop through the faces and draw rectangles around them
    for idx, (x, y, w, h) in enumerate(faces):
        # Draw rectangle (green color)
        cv2.rectangle(output_image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Extract each face
        face_image = image[y:y+h, x:x+w]
        
        # Convert face image to PIL for saving
        face_pil_image = Image.fromarray(cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB))

        # Save the face image with a unique filename
        face_filename = os.path.join(os.path.dirname(image_path), f"detected_face_{idx+1}.jpg")
        face_pil_image.save(face_filename)
        print(f"Saved face {idx+1} as {face_filename}")

    # Save the new image with detected faces (output image with rectangles drawn)
    output_filename = os.path.join(os.path.dirname(image_path), "detected_faces.jpg")
    cv2.imwrite(output_filename, output_image)
    print(f"Saved output image with all faces as {output_filename}")

else:
    print("No faces found in the image.")
