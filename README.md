Nama : Ghaisan Nabil Iradat
NPM : 2506619051
Kelas : PBP A

1. Iya saya menggunakan <section>, ini sangat membantu saya untuk memilah section halaman yang ingin di-inisiate yang sesuai dengan apa yang kita inginkan dan terlihat lebih rapih 

2. Membuat @media pada css sehingga dapat mengubah layout halaman web saat dibuka pada device HP

3. Saat ini belum ada batasan saat mengintegrasikan kreatifitas saya ke dalam web portofolio ini, dan mungkin kedepannya jikalau memungkinkan, tambahan animasi pada web serta perbaikan pada tugas1 saat ini

## TUGAS 2 ##
1. Alur ketika user membuka web adalah -> urls proyek -> urls aplikasi -> views -> models -> template -> output 
urls proyek ==> menentukan untuk request yang diterima akan didistribusikan kemana
urls aplikasi ==> mendistribusikan views yang harus ditangani
views ==> menerima request
models ==> integrate dengan database
template ==> menampilkan output kepada user

2. untuk jangka panjang, ketika ingin menambahkan sebuah data ataupun fitur baru, developer hanya menambahkan pada model dan views tanpa harus generate ulang pada template

3. 
makemigrations ==> membuat file migration berdasarkan models
migrate ==> mengaplikasikan file migration ke sebuah database

dengan contoh saat mengisi bagian models sebelumnya (karena menambah education), ketika menjalankan makemigrations django akan mengupdate bagian education dan
membuat file migration yang baru. Dan ketika menjalankan migrate file migration tersebut akan diterapkan pada database.


## TUGAS 3 ##
1. Dengan menggunakan modelform, proses pembuatan UI akan efisien daripada menulis langsung pada file html secara manual. Django dapat membuat struktur forms langsung terhubung ke models, dan dengan menggunakan tag {% csrf_token %} setiap distribution data di django, memiliki pertahanan dari serangan web. Tanpa adanya token csrf ini, akan memungkinkan terjadi penyerangan terhadap web tersebut.

2. JSON lebih akurat dibandingkan XML karena json memiliki payload lebih kecil, sehingga penggunaannya akan jauh lebih ringan dan lebih cepat serta datanya akan jauh lebih ringkas dan readable.

3. Alur pengembalian data, saat user mengakses URL, Django akan mendistribusi ke views yang sesuai dengan request. Views disini berperan sebagai logic application untuk memproses data dan menentukan respon apa yang di-inginkan(sesuai dengan request). Lalu views akan mengarah kepada models untuk mengumpulkan data yang melewati serialization dan ditaruh dalam bentuk HttpResponse. 

Membutuhkan serialization untuk membaca objek python menjadi format JSON sehingga data data yang dipindah sebelumnya dapat dibaca dengan baik.

declare ai :https://claude.ai/chat/21511b8d-b675-4034-890f-4f65eab71aa6

## TUGAS 5 ##
1. Debouncing digunakan untuk menunda suatu eksekusi terhadap pada sebuah fungsi, sehingga user akan berhenti melakukan interact selama waktu tertentu. Debouncing ini sangat penting untuk fitur searching langsung, dimana AJAX akan melakukan reaksi tiap user mengetik pada saat melakukan pencarian. Dimana akan menerima apa yang diminta (search) akan loading sehingga AJAX akan mengirim permintaan user ke dalam server.

2. await berfungsi sebagai command untuk javascript suapaya dapat menghentikan sementara pengeksekusian baris kode setelahnya yang berada di dalam fungsi fetch(). Jika tidak menggunakan await, outcome yang dihasilkan tidak berisi data yang diinginkan. Pada saat baris kode setelahnya membaca baris tersebut, akan outcome eror.

3. Serangan XSS merupakan sebuah serangan keamanan yang memengaruhi sebuah database, dimana penyerang akan memasukkan sebuah script yang dimana, pada saat script tersebut terbaca pada sebuah situs, akan me-compile script tersebut yang mengakibatkan pencurian data user.

Data yang ditampilkan melalui AJAX/JavaScript lebih rentan karena ketika data diambil secara manual, JavaScript yang menjadi "frontend" menjadi tanggung jawabnya dan diubah menjadi HTML, dan perlindungan yang secara otomatis diberikan oleh django akan hilang. Dan django sendiri memiliki sistem perlindungan sendiri yang dinamakan Django Template Language, sehingga tiap teks yang diubah menjadi HTML akan melindungi serangan XSS tersebut.

## TUGAS 6 ##
1. REST(Representational State Transfer) adalah sebuah arsitektur perangkat lunak yang menggunakan HTTP untuk merancang web API, dan pertukaran data pada resource. Sebuah API yang mengembalikan JSON belum cukup untuk menyebut API sebagai RESTful karena belum menggunakan data sebagai resource yang telah di-identifikasi oleh URL (contohnya **/api/v1/experience/**) yang menggunakan HTTP method (**GET, POST, PUT, PATCH, DELETE**) untuk define suatu function dan juga menukarkan data secara konsisten.

--> Perbedaan antara PUT dan PATCH:
a. PUT -> Digunakan ketika mengganti keseluruhan pada suatu objek sehingga user harus mengirimkan keseluruhan field yang telah di-inisiasi oleh serializer
b. PATCH -> Digunakan ketika memperbaharui sebagian dengan partial=True pada serializer, sehingga user hanya mengirimkan filed yang ingin diubah tanpa harus mengubah field lainnya.

2. Peran serializer pada DRF(Django REST Framework) mengubah model ataupun queryset yang dimana dikerjakan dua arah dan diubah menjadi primitive data type Python yang dapat dikonfersi menjadi JSON terutama pada HTTP method GET. Selain itu, serializer juga melakukan deserialization untuk validasi input dan menyimpannya ke dalam database pada HTTP method POST, PUT, DAN PATCH

Keuntungannya dibandingkan menggunakan dictionary secara manual, akan mevalidasi keseluruhannya menggunakan ModelForm secara individual. Dan dengan menggunakan Serializer akan menghilangkan code duplicate yang menyatukan sebuah struktur dan terhadap aturan validasi input pada satu tempat terstruktur, serializer menyediakan keamanan melalui fields dan juga menghasilkan error output per field dengan status 400 Bad Request

3.
a. Authentication adalah sebuah proses yang memverifikasi suatu request yang menggunakan DRF dan diproses oleh authentication_classes untuk mengisi objek request.user
b. Authorization adalah sebuah proses yang memeriksa hak akses suatu pengguna yang diproses oleh permission_classes untuk mengizinkan ataupun menolak API view sebelum objek dijalankan

mengapa hak akses wajib diperiksa dengan permission class di server adalah untuk menyembunyikan tombol tambah, edit, dan hapus pada template HTML (experience, project) maupun pada JavaScript yang berfungsi untuk UI/UX, Permission class pada sisi server diperlukan untuk lapisan defense agar menolak hal hal yang mencurigakan/ilegal dengan output statsu 403 Forbidden

4. Pada saat API menggunakan SessionAuthentication, browser akan memberikan cookie sessionid pada tiap request. Tanpa adanya verification token CSRF, pihak ketiga dapat menfaatkan sessionid tersebut untuk mengirimkan request perubahan data tanpa sepengetahuan pemilik. Oleh karena itu, DRF memeriksa token CSRF untuk seluruh method HTTP (POST, PUT, PATCH, DELETE) yang telah diproses authentication 

force_authenticate tidak cukup untu mengujinya karena melewatkan mekanisme sessionid dan juga tidak memeriksa middleware CSRF, maka dari itu, harus diuji menggunakan APIClient yang dikombinasikan dengan client.login supaya dapat melakukan mekanisme yang lenkap dan pengujian yang menyeluruh

AI DISCLOSURE: 
    Saya menggunakan Gemini dan Claude untuk membantu saya dalam mengerjakan tugas ini, saya me-strategikan prompting dengan menganalisis perubahan antara project dan experience dalam implementasi code sehingga menerapkan Django REST Framework dengan optimal.

    Saya menggunakannya yang paling banyak pada bagian:
    1. api_views
        penerapan syntaxnya untuk bagian experience dan implementasinya
    2. tests_api
        membuat function testing
    3. hal lainnya yang dibutuhkan untuk pengecekan apakah terdapat kesalahan dalam implementasinya dan arahan untuk solve error pada kasus tertentu