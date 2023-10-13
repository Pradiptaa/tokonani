# Nama: Pradipta Arya Pramudita - 2206083685
# Kelas: PBP F
---
## Tautan aplikasi Adaptable: https://tokonani.adaptable.app/main/
---
## ---Tugas 2---
---
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
---
<p> Dimulai dengan membuat sebuah direktori lokal baru pada komputer dan membuat repositori baru pada github, lalu menghubungkan keduanya. Dilanjutkan dengan membuat virtual environment dengan "python venv", lalu membuat dependencies dan menginstall seluruh dependencies yang diperlukan. Setelah itu mengubah konfigurasi pada proyek django, dan proyek django sudah siap untuk dijalankan. 
</p>
<p> Selanjutnya adalah menambahkan direktori bernama "main" di dalam direktori awal. Lalu dilanjutkan dengan membuat html yang dinamakan "main.html" dan melakukan perubahan "models.py" sesuai dengan ketentuan soal dalam direktori main dan menjalankan perintah untuk migration. Setelah itu dilakukan perubahan di dalam "views.py" untuk ditampilkan pada html. 
</p>
<p> Setelah itu dilakukan konfigurasi routing url dengan membuat "urls.py" pada direktori main dan dibuat sedemikian hingga dapat dihubungkan dengan konfigurasi pada file "urls.py" pada direktori awal. 
</p>
<p> Setelah hal-hal diatas dilakukan, dilanjutkan dengan app deployment yang dilakukan pada "Adaptable.io", dan melakukan, add, commit, dan push pada GitHub.
</p>

---

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
---
<img src="/Assets/BaganPBP.jpg">

---

### Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
---
<p> Virtual environment digunakan karena virtual environment memungkinkan pengguna untuk membuat environment yang terisolasi untuk proyeknya. Virtual environment juga memudahkan pengguna untuk mengelola kebutuhan proyek seperti pip yang mudah untuk di-install, upgrade, ataupun uninstall. Virtual environment juga memudahkan pengguna untuk menyebarkan proyeknya. Virtual environment juga menyediakan environment yang mudah dan bersih untuk development dan testing.
</p>
<p> Aplikasi web berbasis Django dapat dibuat dengan tidak menggunakan virtual environment, tetapi ini bukan best-practice karena dapat menyebabkan tidak terorganisirnya proyek yang dapat menimbulkan beberapa masalah.
</p>

---

### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
---
<p> <strong>MVC</strong>: Konsep arsitektur yang digunakan untuk merancang aplikasi web dan membaginya menjadi tiga komponen utama yaitu Model, View, dan Controller. Model mewakili data dan logika dari aplikasi tersebut, View bertanggung jawab untuk menampilkan data kepada pengguna, dan Controller bertanggung jawab dalam alur aplikasi.
</p>
<p> <strong>MVT</strong>: Konsep arsitektur yang digunakan untuk merancang aplikasi web dan membagi menjadi tiga komponen yaitu Model, View, Template. Model dan View pada MVT serupa dengan yang ada pada MVC, tetapi Template adalah bagian yang membedakan, Template ini berisikan logika tampilan bagian interaktif. Template memisahkan tampilan logika dengan tampilan dari View.
</p>
<p> <strong>MVVM</strong>: Konsep arsitektur yang digunakan untuk merancang aplikasi web dan membagi menjadi tiga komponen yaitu Model, View, ViewModel. Model dan View pada MVVM serupa dengan yang ada pada MVC dan MVT, tetapi ViewModel adalah pembeda dari MVVM. ViewModel ini mengubah data model menjadi format yang dapat ditampilkan pada View.
</p>

---
## ---Tugas 3---
---
### Apa perbedaan antara form POST dan form GET dalam Django?
---
<p> form POST bekerja dengan mengirim data sebagai bagian dari request body http, yang berarti data tidak dapat dilihat melalui URL, yang membuatnya lebih aman dari GET. Sementara itu, form GET bekerja dengan mengirim form sebagai query string yang terlihat melalu URL. Pengguna dapat melihat dan mengubah parameter dalam URL, sehingga form GET tidak aman untuk data-data sensitif.
</p>

---
### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
---
<p> <strong> XML </strong> dirancang untuk pertukaran data dengan fokus pada fleksibilitas dan sifat deskriptif. Sementara <strong> JSON </strong> digunakan untuk pertukaran serial data yang ringan dan mudah digunakan dalam pengembangan. Lalu dengan <strong> HTML </strong> secara khusus digunakan untuk menentukan struktur dan presentasi sebuah web. Penggunaan ketiganya bergantung pada kebutuhan dan konteks penggunaannya. 
</p>

---
### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
---
<p> Hal pertama yang membuat JSON sering digunakan dalam pertukaran data antara aplikasi web modern adalah karena JSON memiliki syntax yang sederhana bagi kedua manusia dan mesin. Alasan lain adalah karena struktur JSON yang ringan sehingga payload lebih kecil dibandingkan dengan format lain seperti XML. Efisiensi ini penting untuk mengurangi waktu transfer data dan penggunaan bandwidth. JSON juga dapat merepresentasikan struktur data yang kompleks termasuk nested objects dan arrays. Fleksibilitas ini membuat JSON cocok untuk serialisasi beragam tipe data.
</p>

---
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
---
<p> Diawali dengan menambah file python baru untuk membuat struktur dari form yang akan menerima data produk. Lalu dilanjut dengan membuat fungsi baru pada "views.py" yang akan menerima parameter request dan menghasilkan form yang berfungsi untuk menambah data. Setelah itu, modifikasi fungsi "show_main" yang sudah ada. Kemudian dilakukan penambahan path untuk mengakses fungsi baru yang sudah ada. Lalu membuat berkas HTML baru yang berfungsi untuk memunculkan form yang sudah dibuat, dan modifikasi main.html untuk menambahkan button. 
</p>
<p> Selanjutnya ditambahkan fungsi lain bernama "show_xml" untuk mengembalikan data dalam bentuk XML, dan dilanjutkan dengan menambah path baru untuk show_xml tersebut. Hal yang hampir sama juga dilakukan untuk mengembalikan data dalam bentuk JSON. Setelah itu, dilakukan juga penambahan fungsi untuk mengembalikan data berdasarkan ID dalam bentuk XML dan JSON. Lalu dilanjutkan dengan penambahan path-path baru pada "urls.py" sesuai dengan fungsi-fungsi baru yang telah dibuat.
</p>

---
### Screenshot dari hasil akses URL pada Postman
---
<strong> 1. HTML </strong>
<img src="/Assets/HTMLresponse.png">
<strong> 2. XML </strong>
<img src="/Assets/XMLresponse.png">
<strong> 3. JSON </strong>
<img src="/Assets/JSONresponse.png">
<strong> 4. XML by ID </strong>
<img src="/Assets/XMLIDresponse.png">
<strong> 5. JSON by ID </strong>
<img src="/Assets/JSONIDresponse.png">

---
## ---Tugas 4---
---
### Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
---
<p> Django UserCreationForm adalah sebuah built-in form yang disediakan oleh Django untuk membantu dalam proses user registration pada sebuah aplikasi web. Beberapa kelebihan dari penggunaan Django UserCreationForm adalah UserCreationForm mudah digunakan dan terintegrasi dengan sistem authentication Django. Namun, UserCreationForm juga memiliki kekurangan yaitu keterbatasan dalam fungsionalitas dan belum tentu cocok untuk semua aplikasi. </p>

---
###  Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
---
<p> Dalam konteks Django, authentication atau autentikasi adalah proses verifikasi identitas pengguna yang bertujuan untuk mengetahui pengguna yang biasanya menggunakan username dan password. Sementara authorization atau otorisasi adalah proses memutuskan apa saja hal yang diizinkan kepada pengguna setelah melakukan autentikasi. proses otorisasi bertujuan untuk mengontrol akses bagi pengguna ke bagian-bagian yang sudah ditentukan. </p>
<p> Kedua hal ini (autentikasi dan otorisasi) penting adanya karena dengan menggabungkan keduanya, developer dapat memastikan bahwa pengguna hanya dapat mengakses dan melakukan tindakan sesuai dengan peran dan haknya, sehingga meningkatkan keamanan dan integritas aplikasi. </p>

---
###  Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
---
<p>Cookies adalah salah satu mekanisme yang digunakan untuk menyimpan data dari sisi pengguna. Django menggunakan cookies untuk mengelola data sesi pengguna dengan menyimpan data seperti ID sesi dan preferensi pengguna. Django juga memungkinkan untuk mengubah konfigurasi cookies pada berbagai aspek seperti lamanya cookies, domain, dan lain-lain.</p>

---
###  Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
---
<p> Penggunaan cookies memiliki beberapa risiko yang harus diwaspadai seperti pencurian data yang terjadi jika cookies mengandung data-data sensitif seperti informasi pribadi pengguna. Penggunaan cookies juga terancam oleh serangan Cross-Site Request Forgery (CSRF). Serangan ini dapat memaksa pengguna untuk membuat permintaan HTTP yang tidak disengaja yang mengandung kode-kode autentikasi yang berpotensi mendapatkan akses tanpa izin. </p>

---
###  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
---
<p> Pengimplementasian diawali dengan import modul-modul yang diperlukan, lalu membuat function baru yang menerima request dari browser ke server untuk register. Dilanjutkan dengan membuat suatu file HTML ang akan menampilkan form register yang sudah dibuat. Lalu menambahkan path url untuk function tersebut. Ulangi langkah-langkah sebelumnya untuk function authentication dan login. Langkah yang sama juga dilakukan pada function logout. </p>
<p> Pada HTML, dilakukan hal-hal yang berbeda, logout hanya membutuhkan hyperlink pada file "main.html". Otorisasi dialkukan dengan menggunakan modul login_required untuk membatasi akses. Dilanjutkan dengan membuat akun dan memasukkan data-data. Lalu menambahkan kode untuk menghubungkan suatu item dengan user. Kemudian melakukan beberapa perubahan pada "create_product pada "views.py" agar Django mengenali bahwa objek dimiliki User tersebut. Fungsi "show_main" juga berubah untuk hanya menunjukkan produk yang dimiliki user tersebut. Terakhir, hal yang dilakukan adalah untuk makemigrattions serta migrate dan git add, commit, push. </p>

---
## ---Tugas 5---
---
### Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
---
<p>
<strong> Universal Selector (*): </strong> Universal selector adalah selector yang digunakan setiap element pada halaman web. Selector ini dapat digunakan saat menerapkan suatu sttyle terhadap setiap elemen pada halaman web. Uiversal selector bermanfaat untuk melakukan penerapan style secara global, debugging, melakukan reset default, dan menerapkan baseline konsisten.
</p>
<p> 
<strong> Type selector: </strong> Type selector adalah selector yang memilih semua elemen dengan HTML tag spesifik. Selector ini dapat digunakan saat menerapkan suatu style kepada semua elemen dengan HTML tag yang spesifik (headings, paragraph, dll). Selector ini memiliki manfaat untuk semantic styling, simplisitas, dan menerapkan konsistensi.
</p>
<p>
<strong> Class Selector: </strong> Class selector adalah selector yang digunakan untuk memilih elemn dari HTML berdasarkan value "class" yang didefiniskan terhadap masing-masing elemen. Selector ini digunakan ketika melakukan styling terhadap beberapa elemen dengan karakteristik visual yang sama, membuat style customization untuk komponen individual atau widget pada halaman web, dan untuk penerapan style pada elemen-elemen dengan HTML berbeda.
</p>
<p>
<strong> ID Selector: </strong> ID selector digunakan saat ingin memilih suatu HTML berdasarkan atribut ID yang dimiliki. ID selector diawali dengan "#" diikuti dengan ID nya. ID selector digunakan ketika melakukan styling terhadap suatu elemen spesifik, membuat anchors untuk in-page navigation, dan menerapkan fungsionalitas JavaScript pada elemen spesifik.
</p>

---
### Jelaskan HTML5 Tag yang kamu ketahui.
---
<p> <strong> header: </strong> Mendefinisikan kontainer untuk konten pengantar pada bagian atas halaman web
</p>
<p> <strong> nav: </strong> Mewakili bagian dari halaman web yang berisi link untuk navigasi
</p>
<p> <strong> main: </strong> Menenetukan konten utama dari dokumen
</p>
<p> <strong> section: </strong> Mendefinisikan pengelompokan tematis konten dalam dokumen
</p>
<p> <strong> footer: </strong> Mendefinisikan kontainer untuk konten pengantar pada bagian bawah halaman web
</p>

---
### Jelaskan perbedaan antara margin dan padding.
---
Aspek | Margin | Padding
--- | --- | ---
Tujuan | Mengatur ruang kosong di luar border elemen dan mengatur ruang kosong antar border elemen dengan elemen lainnya | Mengatur ruang kosong antara elemen dengan bordernya
Pengaruh thd Ukuran | Tidak mengubah ukuran elemen, hanya mengubah posisi | Mengubah ukuran elemen
Penggunaan | Membuat ruang kosong antar elemen, membuat margin antar page, melakukan centering, mengatur layout dari elemen block-level | Membuat ruang kosong antar konten pada elemen, membuat button, containers dengan internal spacing, mengatur layout dari inline dan inline-block elements 

---
###  Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
---
Aspek | CSS Tailwind | Bootstrap
--- | --- | ---
Approach | Utility-first approach yang berfokus pada penggunaan utility (class-class kecil yang menyediakan gaya atau fungsi tertentu) untuk membangun komponen dan tampilan. | Component-Based approach yang memisahkan fungsionalitas menjadi komponen-komponen tersendiri
Costumization | Dapat diubah detail sesuai keinginan dan kebutuhan pengguna | Dapat dibuah tetapi ada batasan
Kasus | Proyek yang membutuhkan desain dan kontrol terhadap style yang digunakan | Proyek yang memiliki desain konsisten dan standar

---
###  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
---
<p> - Hal pertama yang dilakukan adalah membuat file-file css baru untuk setiap html dalam main, lalu modifikasi file-file html dalam main untuk disambung dengan file-file css.
</p>
<p> - Kedua saya mencari color pallete yang cocok untuk penerapan css nya, kemudian saya modifikasi setiap file css.
</p>
<p> - Trial error untuk setiap komponen </p>

---
## --- Tugas 6 ---
---
### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
---
<p> Dalam synchronous programming, tindakan dilakukan secara berturut-turut, satu demi satu, dan jika tindakan sebelumnya belum selesai, dilakukan dengan penundaan. Ini memudahkan penulisan dan pemahaman program, tetapi bisa terasa lambat jika tindakan memerlukan waktu lama atau terjadi kesalahan. </p>
<p> Sementara dalam asynchronous programming, tindakan dapat berjalan bersamaan tanpa penundaan, membuat program lebih cepat dan responsif. Namun, ini membuat penulisan dan pemahaman program lebih kompleks karena alur eksekusi tidak mengikuti urutan kode. </p>

---
### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
---
<p>Paradigma event-driven programming mengatur alur program berdasarkan peristiwa seperti interaksi pengguna, sensor, atau pesan dari program lain, yang membuat program lebih responsif. Sebagai contoh, dalam paradigma ini, sebuah form web dapat mengirim data ke server tanpa perlu me-refresh halaman menggunakan XMLHttpRequest dan menanggapi peristiwa seperti klik, tekan, atau ubah dengan menampilkan hasil di elemen HTML tanpa harus terus-menerus menjalankan kode.</p>

---
### Jelaskan penerapan asynchronous programming pada AJAX.
---
<p>Asynchronous programming dalam konteks AJAX adalah metode yang memungkinkan aplikasi web berkomunikasi dengan server tanpa menunggu respons. Pendekatan ini meningkatkan efisiensi dan responsifitas aplikasi web karena tak perlu me-refresh halaman web saat ada permintaan data. Pada asynchronous programming dalam AJAX, JavaScript berfungsi sebagai bahasa pemrograman utama untuk mengirim dan menerima data dari server secara asinkron. Selain itu, JavaScript juga dapat mengubah tampilan antarmuka pengguna sesuai dengan data yang diterima atau dikirim, menciptakan pengalaman pengguna yang lebih dinamis dan interaktif.</p>

---
### Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
---
* Fetch API lebih ringan dan kompatibel dengan browser modern, sedangkan jQuery cocok untuk browser lama.
* Fetch API menggunakan Promise untuk mengelola respon asinkron, menghindari "callback hell," sementara jQuery menggunakan callback yang lebih fleksibel.
* jQuery menyediakan metode lebih sederhana untuk tugas-tugas seperti pengiriman data JSON, sedangkan Fetch API memberikan lebih banyak kontrol dalam permintaan dan respons Ajax.
* Fetch API memiliki metode bawaan untuk mengubah respons menjadi berbagai tipe data, sedangkan jQuery memerlukan penentuan jenis data di awal dengan opsi dataType.

---
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
---
<p>Dimulai dengan membuat container-container untuk card pada seluruh html. Lalu membuat fungsi baru pada views untuk get product dalam bentuk JSON. Setelah itu membuat fungsi getProduct pada JavaScript di main.html untuk mendapatkan product dalam bentuk JSON. Dilanjutkan dengan membuat fungsi untuk menampilkan seluruh product pada cards. Lalu membuat fungsi untuk mengubah tabel agar sesuai dengan AJAX. Lalu membuat modal sebagai tempat menambahkan product baru beserta button nya. Setelah itu membuat fungsi untuk menambahkan product saat button ditekan dan membuat event listener agar mendeteksi hal tersebut. Terakhir membuat function-function untuk menyesuaikan button/fitur yang sudah dibuat pada tugas-tugas sebelumnya. </p>
