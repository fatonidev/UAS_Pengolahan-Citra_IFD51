# Informasi Mata Kuliah

Berikut adalah informasi terkait mata kuliah yang diambil:

| Keterangan        | Detail                                 |
|-------------------|----------------------------------------|
| **Mata Kuliah**    | Pengolahan Citra Digital               |
| **Kelas**          | IFD51                                  |
| **Prodi**          | S1 PJJ Informatika                     |
| **Nama Mahasiswa** | Ahmad Fatoni                           |
| **NIM**            | 200401010148                           |
| **Dosen**          | Alun Sujjada, S.Kom., M.T              |

---

# Jawaban UAS_Pengolahan Citra_IFD51

1.  
![1_Hasil_robert_sobel](1_Hasil_robert_sobel.png)
Gambar ini menunjukkan proses deteksi tepi menggunakan dua metode yaitu Roberts dan Sobel, yang keduanya merupakan teknik dalam pemrosesan citra untuk mengekstrak informasi tepi dari suatu gambar grayscale. Berikut adalah analisis hasil yang diperoleh.

**a. Gambar Original (Citra Asli)**
Gambar ini menampilkan proses deteksi tepi pada sebuah citra grayscale menggunakan dua metode, yaitu Roberts dan Sobel. Deteksi tepi adalah teknik penting dalam pemrosesan citra yang bertujuan untuk mengekstrak informasi batas atau kontur suatu objek berdasarkan perubahan intensitas piksel. Gambar asli yang ditampilkan menunjukkan siluet pohon dengan banyak cabang yang bercabang-cabang, yang menciptakan tantangan tersendiri dalam deteksi tepi karena adanya variasi intensitas dan detail halus dalam struktur objek.a metode yang digunakan harus cukup sensitif terhadap perubahan halus dalam intensitas gambar.
**b. Hasil dengan Operator Roberts**
Pada gambar kedua, hasil deteksi tepi menggunakan operator Roberts terlihat. Operator ini bekerja dengan menghitung perbedaan intensitas piksel dalam arah diagonal menggunakan filter konvolusi 2x2. Dari hasil yang ditampilkan, terlihat bahwa metode Roberts menghasilkan tepi yang cukup tajam dan tipis, namun dengan banyak noise yang muncul dalam bentuk bintik-bintik kecil di sekitar gambar. Hal ini disebabkan oleh sensitivitas tinggi metode Roberts terhadap perubahan kecil dalam intensitas gambar. Dengan demikian, metode ini cenderung kurang optimal untuk gambar yang memiliki tekstur kompleks seperti cabang-cabang pohon yang halus, karena beberapa detail mungkin hilang atau terganggu oleh noise.
**c. Hasil dengan Operator Sobel**
gambar ketiga menunjukkan hasil deteksi tepi menggunakan operator Sobel. Berbeda dengan Roberts, metode Sobel menghitung gradien intensitas dalam dua arah utama, yaitu horizontal dan vertikal, dengan menggunakan filter konvolusi 3x3. Hasilnya terlihat lebih halus dan lebih jelas dibandingkan dengan metode Roberts. Noise yang muncul juga lebih sedikit, sehingga garis-garis tepi dari cabang pohon tampak lebih menyatu dan lebih mudah diidentifikasi. Karena Sobel menangkap perubahan intensitas dalam dua arah, metode ini lebih efektif dalam mendeteksi tepi pada gambar dengan struktur kompleks dan perubahan gradien yang lebih lembut.

Dari perbandingan kedua metode ini, dapat disimpulkan bahwa operator Roberts lebih cocok untuk gambar dengan perubahan intensitas yang tajam dan kontras tinggi, sementara operator Sobel lebih baik untuk menangkap tepi pada gambar dengan variasi intensitas yang lebih kompleks. Dalam kasus gambar pohon ini, metode Sobel lebih direkomendasikan karena memberikan hasil deteksi tepi yang lebih bersih, lebih halus, dan lebih sedikit noise, sehingga lebih sesuai untuk objek yang memiliki banyak detail seperti cabang-cabang pohon yang saling bertumpuk.

