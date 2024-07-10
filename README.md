# OTOBOOK

OTOBOOK adalah  Program PKM-KC PENS (Politeknik Elektronika Negeri Surabaya) program kami membuat sebuah aplikasi yang menggunakan OCR, klasifikasi teks, dan summarization untuk mendeteksi dan mengelola informasi dari buku perpustakaan.

## Instalasi

1. **Instalasi Tesseract:**

   - Windows:
     Unduh installer dari [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
     Ikuti petunjuk instalasi.

   - Linux:
     ```bash
     sudo apt install tesseract-ocr
     ```

   - macOS:
     ```bash
     brew install tesseract
     ```

2. **Setup Lingkungan Python:**

   ```bash
   mkdir OTOBOOK
   cd OTOBOOK
   python -m venv venv
   source venv/bin/activate  # Untuk Windows gunakan venv\Scripts\activate

**Installasi**
pip install -r requirements.txt
