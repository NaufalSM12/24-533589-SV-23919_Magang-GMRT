import numpy as np
import matplotlib.pyplot as plt

def h_forwardkinematik(panjang_a1, panjang_a2, sudut_q1, sudut_q2):

    q1_rad = np.deg2rad(sudut_q1)
    q2_rad = np.deg2rad(sudut_q2)

    # 2. Matriks Transformasi dari frame 0 (pangkal) ke frame 1 (lutut)
    # Ini adalah matriks standar untuk rotasi lalu translasi (pergeseran)
    T_0_1 = np.array([
        [np.cos(q1_rad), -np.sin(q1_rad), panjang_a1 * np.cos(q1_rad)],
        [np.sin(q1_rad),  np.cos(q1_rad), panjang_a1 * np.sin(q1_rad)],
        [0,               0,              1]
    ])
    
    # Ambil posisi (x,y) dari kolom terakhir matriks untuk menentukan posisi lutut
    posisi_lutut = T_0_1[:2, 2]

    # 3. Matriks Transformasi dari frame 1 (lutut) ke frame 2 (ujung kaki)
    T_1_2 = np.array([
        [np.cos(q2_rad), -np.sin(q2_rad), panjang_a2 * np.cos(q2_rad)],
        [np.sin(q2_rad),  np.cos(q2_rad), panjang_a2 * np.sin(q2_rad)],
        [0,               0,              1]
    ])

    # 4. Matriks Transformasi total dari pangkal ke ujung kaki
    # Didapat dengan mengalikan matriks T_0_1 dengan T_1_2
    T_0_2 = T_0_1 @ T_1_2 

    # Ambil posisi (x,y) dari kolom terakhir matriks total
    posisi_ujung = T_0_2[:2, 2]

    return posisi_lutut, posisi_ujung

def display_gambar(pos_lutut, pos_ujung):
    """
    Fungsi untuk membuat visualisasi/gambar dari posisi robot.
    """
    pangkal = [0, 0] # Titik awal selalu di (0,0)
    
    plt.figure(figsize=(8, 8))
    # Gambar link femur (a1) dari pangkal ke lutut
    plt.plot([pangkal[0], pos_lutut[0]], [pangkal[1], pos_lutut[1]], 'r-o', linewidth=3, markersize=8, label='Femur (a1)')
    # Gambar link tibia (a2) dari lutut ke ujung kaki
    plt.plot([pos_lutut[0], pos_ujung[0]], [pos_lutut[1], pos_ujung[1]], 'g-o', linewidth=3, markersize=8, label='Tibia (a2)')

    # Beri tanda pada setiap titik penting
    plt.plot(pangkal[0], pangkal[1], 'ko', markersize=10, label='Pangkal (Coxa)')
    plt.plot(pos_lutut[0], pos_lutut[1], 'ko', markersize=10, label='Lutut')
    plt.plot(pos_ujung[0], pos_ujung[1], 'bo', markersize=10, label='Ujung Kaki')

    #Dsiplay gambar
    plt.title('Visualisasi Kinematik Maju Robot 2-DOF')
    plt.xlabel('Sumbu X')
    plt.ylabel('Sumbu Y')
    plt.legend()
    plt.grid(True)
    plt.axis('equal') # Membuat skala sumbu X dan Y sama agar tidak distorsi
    plt.show()


# --- Program Utama Dimulai Di Sini ---
if __name__ == "__main__":
    # Meminta input dari pengguna
    a1 = float(input("Panjang femur (a1): "))
    a2 = float(input("Panjang tibia (a2): "))
    q1 = float(input("Sudut servo 1 (q1): "))
    q2 = float(input("Sudut servo 2 (q2): "))

    # Panggil fungsi untuk menghitung posisi
    posisi_lutut_hasil, posisi_ujung_hasil = h_forwardkinematik(a1, a2, q1, q2)

    # Tampilkan hasil perhitungan ke terminal
    print(f"\n--- Hasil Perhitungan ---")
    print(f"Posisi Sendi Lutut\t: ({posisi_lutut_hasil[0]:.2f}, {posisi_lutut_hasil[1]:.2f})")
    print(f"Posisi Ujung Kaki\t: ({posisi_ujung_hasil[0]:.2f}, {posisi_ujung_hasil[1]:.2f})")

    # Panggil fungsi untuk menampilkan gambar robot
    display_gambar(posisi_lutut_hasil, posisi_ujung_hasil)