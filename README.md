# QR Code Generator 🧾➡️📱

This project is a simple and customizable **QR Code Generator** built using Python. 
It takes a URL (or any string data) and generates a high-quality QR code image with a specified border, size, and color scheme.

## 📌 Features

- ✅ Generate QR codes from any URL or text
- 🎨 Customize:
  - Border thickness
  - Box size (pixel density)
  - Fill and background colors
- 🖼 Save as `.png` image file
- 🔒 High error correction (`30%` of code can be restored if damaged)

## 🛠 Technologies Used

- **Python 3.x**
- **qrcode** Python library
- **Pillow** for image processing (via `qrcode[pil]`)

## Install dependency
- pip install qrcode[pil]

## Usage
-python qr_code.py

