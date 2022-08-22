# Prediktor Gaji Ilmuwan Data (selama COVID-19)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

- Membuat aplikasi web yang akan memperkirakan gaji ilmuwan data (MAE~\$20k) untuk membantu ilmuwan data memahami dengan lebih baik berapa gaji yang mereka akan terima selama pandemi COVID-19
- Melakukan web scrapping terhadap data pekerjaan dari Glassdoor menggunakan Selenium dan Chromedriver
- Melakukan feature engineer dari teks pada deskripis pekerjaan untuk menghitung berapa nilai yang perusahaan berikan bagi mereka yang memiliki kemampuan seperti Python, R, AWS, Hadoop, dan kemampuan lainnya, dan juga pengetahuan lain yang dibutuhkan seperti pengetahuan Algoritma dan Statistik
- Optimasi linear, lasso, dan Random Forest Regressor menggunakan GridsearchCV untuk mencapai model terbaik
- Membuat aplikasi web bagi user untuk memasukkan data dan menerima perkiraan/hasil prediksi, menggunakan Streamlit dan Heroku.

## Motivasi

Selama pandemi COVID-19, penerimaan pegawai mencapai tingkat terendahnya yang baru. Industri teknologi juga terdampak olehnya, dan bersamaa dengan itu, ilmuwan data pun ikut terkena dampaknya. Kemampuan untuk mendapatkan pekerjaan yang baik saat ini, dengan gaji yang proporsional dengan kemampuan yang dimiliki menjadi sangat penting. Di waktu yang sama, kondisi ini sangatlah berbeda dibandingkan dengan kondisi ketika situasi normal. Web aplikasi ini memberi jalan untuk membantu memperkirakan berapa gaji yang dapat diterima oleh seseorang saat ini, berdasarkan kemampuan yang dimiliki, dan juga berdasarkan perusahaan yang merekrut mereka.

## Teknologi yang Digunakan

Sebagian besar pekerjaan dalam projek ini menggunakan Selenium 3.141.0, Numpy 1.18.3, Pandas 1.0.4, Joblib 0.15.1, Scikit_Learn 0.23.1 dan Streamlit 0.61.0.

## Environment yang Digunakan

Kode untuk web scrap dan streamlit dijalankan pada environment Atom sebagai IDE. Pembersihan data, Exploratory Data Analysis, dan pembuatan model dijalankan pada environment Jupyter Notebook.

## Model yang Digunakan

Perbandingan dilakukan dengan membuat model regresi linear (MAE ~25K), regresi lasso (MAE ~22K) dan random forest (MAE ~23K). GridSearchCV membantu mengidentidikasi hyperparameter yang optimal untuk melakukan tuning pada setiap model ini, sehingga didapatkan model terbaik yaitu model regresi lasso dengan MAE ~20K.

## Hasil EDA

Sejumlah hasil menarik dari EDA:

![Plot1](/images/plot1.png)

![Plot2](/images/plot2.png)

![Plot3](/images/plot3.png)

![Plot4](/images/plot4.png)

## Antar Muka Aplikasi Web

Aplikasi web dibangun menggunakan Streamlit dan di-deploy menggunakan Heroku. Aplikasinya dapat diakses di [sini](https://gaji-ilmuwan-data.herokuapp.com/)

![DSS1](/images/DSStreamlit1.png)

![DSS2](/images/DSStreamlit2.png)
