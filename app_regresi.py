
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Aplikasi Regresi Linear",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Aplikasi Regresi Linear")
st.write("Aplikasi sederhana untuk menghitung regresi linear antara jam belajar dan nilai ujian.")

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([55, 60, 65, 70, 75, 78, 85, 90])

m, c = np.polyfit(x, y, 1)

y_prediksi = m * x + c
residual = y - y_prediksi
jumlah_galat = np.sum(residual)

st.subheader("1. Persamaan Regresi Linear")
st.latex(f"y = {m:.2f}x + {c:.2f}")

st.write(f"Koefisien kemiringan (m): **{m:.4f}**")
st.write(f"Konstanta (c): **{c:.4f}**")

st.subheader("2. Data Pengamatan")

data = pd.DataFrame({
    "Jam Belajar": x,
    "Nilai Ujian": y,
    "Prediksi": y_prediksi,
    "Residual": residual
})

st.dataframe(data, use_container_width=True)

st.subheader("3. Grafik Regresi Linear")

fig, ax = plt.subplots()

ax.scatter(x, y, label="Data asli")
ax.plot(x, y_prediksi, label="Garis regresi")

ax.set_xlabel("Jam Belajar")
ax.set_ylabel("Nilai Ujian")
ax.set_title("Regresi Linear Jam Belajar dan Nilai Ujian")
ax.legend()
ax.grid(True)

st.pyplot(fig)

st.subheader("4. Prediksi Nilai Ujian")

jam_belajar = st.number_input(
    "Masukkan jumlah jam belajar:",
    min_value=0.0,
    max_value=100.0,
    value=9.0,
    step=1.0
)

hasil_prediksi = m * jam_belajar + c

st.success(f"Prediksi nilai ujian: {hasil_prediksi:.2f}")

st.subheader("5. Perhitungan Residual")

st.write("Residual adalah selisih antara nilai asli dan nilai prediksi.")
st.write(f"Jumlah galat (residual): **{jumlah_galat:.10f}**")

st.info(
    "Jumlah residual mendekati nol karena metode regresi linear "
    "kuadrat terkecil dengan konstanta menghasilkan jumlah residual "
    "yang secara matematis sama dengan nol."
)
