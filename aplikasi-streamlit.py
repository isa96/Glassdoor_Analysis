import streamlit as st
import joblib
import numpy as np
import pandas as pd
import sklearn

df = pd.read_csv("gaji_ilmuwan_data_us_bersih.csv")

st.title("Memprediksi Gaji Ilmuwan Data (Selama Pandemi Covid-19)")

model = joblib.load("model.pkl")

st.markdown(
    "## Setiap Kolom Wajib Diisi.")

st.subheader("Detail Perusahaan: \n Cek situs Glassdoor untuk nilai pastinya, jika ragu-ragu.")

rating = st.slider("Rating perusahaan berdasarkan penilaian Glassdoor",
                    min_value=0.0, max_value=5.0, step=0.1)
age = st.number_input('Umur Perusahaan', step=1.0, min_value=0.0)
num_comp = st.number_input("Jumlah pesaing yang melamar", step=1.0, min_value=0.0)

st.subheader("Detail mengenai pekerjaan:")

jobhq = st.radio(
        "Apakah lokasi bekerja di kantor utama? (0 untuk Tidak, 1 untuk Iya)",options=[0,1])

job_type_num = st.selectbox("Jenis pekerjaaan",options=df['job_type'].unique())

def number_simplifier(role):
    if role == "data scientist":
        return 3
    elif role == "data engineer":
        return 2
    elif role == "analyst":
        return 1
    elif role == "director":
        return 4
    elif role == "manager":
        return 5
    elif role == "mle":
        return 6
    elif role == "na":
        return 7
    elif role == "research":
        return 8
    elif role == "sw":
        return 9

job_type_num1 = number_simplifier(job_type_num)


def senior_simplifier(title):
    if title == "Senior":
        return 1
    else:
        return 2


seniority_num = st.radio("Jabatan Senior?", options=["Senior", "Tidak Senior"])
seniority_num1 = senior_simplifier(seniority_num)

len_desc = st.number_input("Jumlah kata deskripsi pekerjaan", step=1.0)

st.subheader("Keahlian Anda:")

python_req = st.radio("Python (0 untuk Tidak, 1 untuk Iya)", options=[0,1])
r_req = st.radio("R (0 untuk Tidak, 1 untuk Iya)", options=[0,1])
aws_req = st.radio("AWS (0 untuk Tidak, 1 untuk Iya)", options=[0,1])
spark_req = st.radio("Spark (0 untuk Tidak, 1 untuk Iya)", options=[0,1])
hadoop_req = st.radio("Hadoop (0 untuk Tidak, 1 untuk Iya)", options=[0,1])
docker_req = st.radio("Docker (0 untuk Tidak, 1 untuk Iya)", options=[0,1])
sql_req = st.radio("SQL (0 untuk Tidak, 1 untuk Iya)", options=[0,1])
linux_req = st.radio("Linux (0 untuk Tidak, 1 untuk Iya)", options=[0,1])
flask_req = st.radio("Flask (0 untuk Tidak, 1 untuk Iya)", options=[0,1])
django_req = st.radio("Django (0 untuk Tidak, 1 untuk Iya)", options=[0,1])
tensorflow_req = st.radio("Tensorflow (0 untuk Tidak, 1 untuk Iya)", options=[0,1])
keras_req = st.radio("Keras (0 untuk Tidak, 1 untuk Iya)", options=[0,1])
pytorch_req = st.radio("Pytorch (0 untuk Tidak, 1 untuk Iya)", options=[0,1])
tableau_req = st.radio("Tableau (0 untuk Tidak, 1 untuk Iya)", options=[0,1])
algo_req = st.radio("Pengetahuan Algoritma (0 untuk Tidak, 1 untuk Iya)", options=[0,1])
stats_req = st.radio("Pengetahuan Statistik (0 untuk Tidak, 1 untuk Iya)", options=[0,1])

features = [rating, jobhq, age, num_comp, python_req, r_req, aws_req,spark_req,hadoop_req,docker_req,
            sql_req,linux_req,flask_req,django_req,tensorflow_req,keras_req,pytorch_req,tableau_req,algo_req,
            stats_req, job_type_num1, seniority_num1, len_desc]

final_features = np.array(features).reshape(1,-1)

if st.button('Prediksi'):
    prediction = model.predict(final_features)
    st.balloons()
    st.success(f'Prediksi gaji Anda dalam Dolar AS {round(prediction[0],3)*1000} ')
