import qrcode
import cv2
import os
from PIL import Image

def encode_text_to_qr(text, filename, format='png'):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        
        if format.lower() == 'png':
            img.save(filename + ".png")
            print(f"QR code generated and saved as {filename}.png")
        elif format.lower() == 'jpg':
            img.save(filename + ".jpg")
            print(f"QR code generated and saved as {filename}.jpg")
        else:
            print("Error: Invalid format specified. Only 'png' and 'jpg' formats are supported.")
    except Exception as e:
        print(f"Error occurred: {e}")

def encode_image_to_qr(image_path, filename, format='png'):
    try:
        img = cv2.imread(image_path)
        if img is None:
            print("Error: Invalid image path.")
            return
        
        detector = cv2.QRCodeDetector()
        data, _, _ = detector.detectAndDecode(img)

        if not data:
            print("Error: No QR code detected in the provided image.")
            return

        encode_text_to_qr(data, filename, format)
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    while True:
        print("\n1. Convert URL or text to QR code")
        print("2. Convert image to QR code")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            data = input("Enter the URL or text to encode: ")
            filename = input("Enter the filename for the QR code image (without extension): ")
            format_choice = input("Choose the format (PNG/JPG, default=PNG): ").lower()
            encode_text_to_qr(data, filename, format_choice)
        elif choice == '2':
            image_path = input("Enter the path to the image file: ")
            filename = input("Enter the filename for the QR code image (without extension): ")
            format_choice = input("Choose the format (PNG/JPG, default=PNG): ").lower()
            encode_image_to_qr(image_path, filename, format_choice)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
