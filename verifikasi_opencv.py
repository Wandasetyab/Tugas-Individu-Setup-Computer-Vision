# verifikasi_opencv.py
# Script sederhana untuk verifikasi instalasi OpenCV
# Jalankan di Python interpreter atau sebagai file: python verifikasi_opencv.py

import cv2

print("OpenCV berhasil diimport!")
print("Versi OpenCV:", cv2.__version__)

# Contoh fungsi sederhana (opsional, dari tutorial lanjutan)
# img = cv2.imread('gambar_contoh.jpg')  # Uncomment jika ada gambar
# if img is not None:
#     print("Gambar berhasil dibaca!")
# else:
#     print("Gagal membaca gambar. Pastikan path benar.")