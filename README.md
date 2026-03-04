# Praktik Setup Lingkungan Computer Vision untuk Machine Learning

**Nama:** Wanda Setya Budi  
**NIM:** 231001008  
**Mata Kuliah:** Machine Learning  
**Tanggal:** 04 Maret 2026 

**Deskripsi:** Repository ini berisi hasil praktik dari video tutorial "#1 Computer Vision | Pengenalan konsep, tool, library & pemrograman"[](https://youtu.be/sdATJ5sBeIs). Saya mempraktikkan setup lingkungan kerja dari nol menggunakan Anaconda, membuat virtual environment, menginstal Python 3.12 dan OpenCV, serta verifikasi hasil. Dokumentasi ini menjelaskan langkah-langkah secara detail, beserta analisis singkat.

## Langkah-Langkah Praktik

### 1. Pembukaan dan Persiapan
- Download dan instal Anaconda dari website resmi (anaconda.com).
- Anaconda adalah platform distribusi Python yang lengkap untuk Data Science dan Machine Learning.
- Setelah instalasi, buka Anaconda Navigator (versi GUI) atau Anaconda Prompt (versi command line).

### 2. Analisis: Navigator vs Prompt
- Navigator: Mudah untuk pemula, tapi lebih berat dan kurang detail log.
- Prompt: Lebih ringan, hemat RAM, dan memberikan log proses detail untuk debugging error. Saya sarankan gunakan Prompt.

### 3. Penjelasan Istilah dan Konsep dari Video
- **Virtual Environment**: Ini seperti kotak mainan terpisah di komputer. Kita buat ruang khusus ini supaya program dan library untuk Computer Vision tidak campur aduk dengan proyek lain, biar nggak rusak atau bentrok.
- **Conda-forge**: Repositori komunitas seperti 'Play Store' untuk library. Fungsinya menyediakan ribuan library yang selalu update dan stabil, termasuk OpenCV untuk Computer Vision.
- **Anaconda Cheat Sheet**: 'Kamus saku' daftar perintah conda. Berguna untuk cek sintaks cepat, seperti `create`, `activate`, atau `install`, agar tidak salah ketik.
- Lainnya dari video: Pilih Python 3.12 karena performa lebih baik (hingga 25% lebih cepat), error handling lebih informatif, dan stabil untuk library CV. Verifikasi instalasi penting untuk cek error, seperti solusi DLL load failed dengan `opencv-python-headless`.

### 4. Praktik Setup (Python 3.12 & OpenCV)
- Buka Anaconda Prompt.
- Buat environment baru: `conda create -n ENV_BELAJAR python=3.12`
- Aktifkan: `conda activate ENV_BELAJAR`
- Instal OpenCV: `pip install opencv-python` (dari Conda-forge jika perlu channel: `conda install -c conda-forge opencv`).
- Alasan Python 3.12: Peningkatan performa, pesan error lebih baik, f-strings fleksibel, type hinting canggih, dan stabil untuk OpenCV.

### 5. Verifikasi Hasil
- Masuk Python interpreter: `python`
- Ketik: `import cv2`
- Ketik: `print(cv2.__version__)` (Hasil: Misalnya 4.13.0, tanpa error).
- Jika error DLL load failed (umum di Windows): Ganti instal dengan `pip install opencv-python-headless`.

### 6. Hasil yang Didapat
- Environment siap 100% untuk praktikum Machine Learning selanjutnya.
- Library OpenCV terinstal sukses, siap untuk operasi seperti pemrosesan gambar, deteksi objek, dll.

### Analisis Singkat Kode yang Diimplementasikan
- `conda create -n ENV_BELAJAR python=3.12`: Membuat environment isolasi agar tidak konflik dengan proyek lain. Python 3.12 dipilih untuk kecepatan dan debugging mudah di CV.
- `conda activate ENV_BELAJAR`: Aktifkan environment, batasi perubahan ke sistem global – penting untuk ML karena library sering update.
- `pip install opencv-python`: Instal library inti CV untuk gambar/video. Stabil di 3.12, tapi gunakan headless jika error grafis.
- `import cv2` dan `print(cv2.__version__)`: Verifikasi sukses, langkah awal untuk coding CV seperti `cv2.imread()` di tutorial lanjutan.

## File Pendukung
- `verifikasi_opencv.py`: Script Python untuk test OpenCV.

Repository ini juga mendukung video presentasi saya di YouTube: [Link YouTube Kamu].

Terima kasih!
