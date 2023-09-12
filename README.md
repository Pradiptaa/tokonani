# Tautan aplikasi Adaptable: https://tokonani.adaptable.app/

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
---
<p> Dimulai dengan membuat sebuah direktori lokal baru pada komputer dan membuat repositori baru pada github, lalu menghubungkan keduanya. Dilanjutkan dengan membuat virtual environment dengan "python venv", lalu membuat dependencies dan menginstall seluruh dependencies yang diperlukan. Setelah itu mengubah konfigurasi pada proyek django, dan proyek django sudah siap untuk dijalankan.
<br> Selanjutnya adalah menambahkan direktori bernama "main" di dalam direktori awal. Lalu dilanjutkan dengan membuat html yang dinamakan "main.html" dan melakukan perubahan "models.py" sesuai dengan ketentuan soal dalam direktori main dan menjalankan perintah untuk migration. Setelah itu dilakukan perubahan di dalam "views.py" untuk ditampilkan pada html. 
<br> Setelah itu dilakukan konfigurasi routing url dengan membuat "urls.py" pada direktori main dan dibuat sedemikian hingga dapat dihubungkan dengan konfigurasi pada file "urls.py" pada direktori awal. 
<br> Setelah hal-hal diatas dilakukan, dilanjutkan dengan app deployment yang dilakukan pada "Adaptable.io", dan melakukan, add, commit, dan push pada GitHub.
</p>

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
---
request | response 
--- | ---

## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
---
<p> Virtual environment digunakan karena virtual environment memungkinkan pengguna untuk membuat environment yang terisolasi untuk proyeknya. Virtual environment juga memudahkan pengguna untuk mengelola kebutuhan proyek seperti pip yang mudah untuk di-install, upgrade, ataupun uninstall. Virtual environment juga memudahkan pengguna untuk menyebarkan proyeknya. Virtual environment juga menyediakan environment yang mudah dan bersih untuk development dan testing.
<br> Aplikasi web berbasis Django dapat dibuat dengan tidak menggunakan virtual environment, tetapi ini bukan best-practice karena dapat menyebabkan tidak terorganisirnya proyek yang dapat menimbulkan beberapa masalah.
</p>

### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
---
<p> <strong>MVC</strong>: Konsep arsitektur yang digunakan untuk merancang aplikasi web dan membaginya menjadi tiga komponen utama yaitu Model, View, dan Controller. Model mewakili data dan logika dari aplikasi tersebut, View bertanggung jawab untuk menampilkan data kepada pengguna, dan Controller bertanggung jawab dalam alur aplikasi.
<br> <strong>MVT</strong>: Konsep arsitektur yang digunakan untuk merancang aplikasi web dan membagi menjadi tiga komponen yaitu Model, View, Template. Model dan View pada MVT serupa dengan yang ada pada MVC, tetapi Template adalah bagian yang membedakan, Template ini berisikan logika tampilan bagian interaktif. Template memisahkan tampilan logika dengan tampilan dari View.
<br> <strong>MVVM</strong>: Konsep arsitektur yang digunakan untuk merancang aplikasi web dan membagi menjadi tiga komponen yaitu Model, View, ViewModel. Model dan View pada MVT serupa dengan yang ada pada MVC, tetapi ViewModel adalah pembeda dari MVVM. ViewModel ini mengubah data model menjadi format yang dapat ditampilkan pada View.
</p>