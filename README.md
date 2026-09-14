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

declare ai :https://claude.ai/chat/21511b8d-b675-4034-890f-4f65eab71aa6