import streamlit as st
from datetime import date, timedelta
from docxtpl import DocxTemplate
import os
import csv
from email.message import EmailMessage
import smtplib

# ---- Load Custom CSS (aman untuk deploy) ----
try:
    from styles.custom_css import load_custom_css

    load_custom_css()
except Exception:
    st.markdown(
        "<style>body {background-color: white;}</style>", unsafe_allow_html=True
    )

# ----------------- KONFIGURASI HALAMAN -----------------
st.set_page_config(page_title="SAKTI", page_icon="💼", layout="wide")
load_custom_css()

LOG_FILE = "kunjungan_log.csv"


# ----------------- FUNGSI UTILITAS -----------------
def tulis_log(nama_pemohon, nama_tahanan, tanggal_kunjungan, tanggal_surat):
    """Menyimpan log ke file CSV"""
    header = ["Nama Pemohon", "Nama Tahanan", "Tanggal Kunjungan", "Tanggal Surat"]
    data = [nama_pemohon, nama_tahanan, tanggal_kunjungan, tanggal_surat]

    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(data)


# ----------------- HEADER -----------------
st.markdown(
    """
<div class="header-container">
    <div class="header-title">SAKTI – Sistem Administrasi Kunjungan Tahanan Terintegrasi</div>
    <div class="header-sub">
        <span class="sub-highlight">Kejaksaan Negeri Banyumas</span>
        <span class="separator">|</span>
        <span class="sub-normal">Bidang Pidana Umum</span>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ----------------- SIDEBAR -----------------
with st.sidebar:
    st.image("logo_pidum.png")
    st.markdown("<h3 class='sidebar-title'>Menu</h3>", unsafe_allow_html=True)
    menu = st.radio("", ["SAKTI", "Login Admin"], label_visibility="collapsed", index=0)

# ============================================================
# ======================== MENU SAKTI ========================
# ============================================================
if menu == "SAKTI":
    st.markdown(
        """
    <div style="
        background:#ffffff;
        border-radius:18px;
        padding:26px 30px;
        box-shadow:0 8px 22px rgba(0,0,0,0.07);
        border:1px solid #e5e7eb;
        margin-top:10px;
        margin-bottom:24px;
        animation: fadeInUp 0.6s ease-in-out;
    ">
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
        <div style="
        background:linear-gradient(135deg,#cc383c,#7a0d0f);
        color:#fff;
        padding:10px;
        border-radius:10px;
        font-size:18px;
        box-shadow:0 2px 5px rgba(0,0,0,0.2);
        ">💳</div>
        <h4 style="margin:0;color:#7a0d0f;font-size:20px;font-weight:800;">
        Panduan Pengisian Sistem Administrasi Kunjungan Tahanan Terintegrasi (SAKTI)
        </h4>
    </div>
    <hr style="border:none; border-top:1px solid #e5e7eb; margin:18px 0;">
    """,
        unsafe_allow_html=True,
    )

    # ----------------- DATA TAHANAN -----------------
    tahanan_options = {
        "Aji Maulana bin Sodikin": {
            "alias": "Aji",
            "tempat_lahir": "Cilacap",
            "tanggal_lahir": "26 Februari 1999",
            "jenis_kelamin": "Laki-laki",
            "kewarganegaraan": "WNI",
            "alamat": (
                "Jl. Poso No. 62 A Desa Mujur Lor Rt 004 / Rw 002, "
                "Kec. Kroya, Kab. Cilacap, Prov. Jawa Tengah (KTP). "
                "Domisili: Desa Pageralang Rt 003 / Rw 003, Kec. Kemranjen, Kab. Banyumas."
            ),
            "agama": "Islam",
            "pendidikan": "SD",
            "tanggal_kunjungan": date(2025, 11, 2),
            "batas_hari": 20,
        },
        "Fikich Probo Sutrisno als Botak bin (alm) Ngadino": {
            "alias": "Botak",
            "tempat_lahir": "Cilacap",
            "tanggal_lahir": "29 Januari 1999",
            "jenis_kelamin": "Laki-laki",
            "kewarganegaraan": "WNI",
            "alamat": (
                "Jl. Derpawisa Rt 001 / Rw 001 Desa Karangasem, Kec. Sampang, Kab. Cilacap, Prov. Jawa Tengah (KTP). "
                "Domisili: Desa Mujur Lor, Dusun Rawaseser Rt 06 / Rw 04, Kec. Kroya, Kab. Cilacap, Prov. Jawa Tengah."
            ),
            "agama": "Islam",
            "pendidikan": "SMP",
            "tanggal_kunjungan": date(2025, 11, 3),
            "batas_hari": 20,
        },
        "Timothy Ricky Widjaja bin Agus Widjaja": {
            "alias": "Timothy",
            "tempat_lahir": "Purwokerto",
            "tanggal_lahir": "18 Maret 1998",
            "jenis_kelamin": "Laki-laki",
            "kewarganegaraan": "WNI",
            "alamat": (
                "Jalan Brigjend Katamso No. 223, Rt 05 Rw 01, Kelurahan Purwokerto Lor, "
                "Kec. Purwokerto Timur, Kab. Banyumas, Prov. Jawa Tengah."
            ),
            "agama": "Islam",
            "pendidikan": "SMA (Kelas 1)",
            "tanggal_kunjungan": date(2025, 11, 4),
            "batas_hari": 20,
        },
        "Kevin Richy Triyanto bin Kuswandi": {
            "alias": "Kevin",
            "tempat_lahir": "Banyumas",
            "tanggal_lahir": "10 November 1992",
            "jenis_kelamin": "Laki-laki",
            "kewarganegaraan": "WNI",
            "alamat": (
                "Desa Pliken Rt 001 Rw 009, Kec. Kembaran, Kab. Banyumas, Prov. Jawa Tengah."
            ),
            "agama": "Islam",
            "pendidikan": "SD",
            "tanggal_kunjungan": date(2025, 11, 5),
            "batas_hari": 20,
        },
        "Kusman bin Setu (Alm)": {
            "alias": "Kusman",
            "tempat_lahir": "Banyumas",
            "tanggal_lahir": "26 Oktober 1985",
            "jenis_kelamin": "Laki-laki",
            "kewarganegaraan": "WNI",
            "alamat": (
                "Desa Somakaton Rt 006 Rw 001, Kec. Somagede, Kab. Banyumas, Prov. Jawa Tengah."
            ),
            "agama": "Islam",
            "pendidikan": "SD (Lulus)",
            "tanggal_kunjungan": date(2025, 11, 6),
            "batas_hari": 20,
        },
    }
    # ----------------- FILTER 20 HARI -----------------
    today = date.today()
    filtered_tahanan = {
        nama: data
        for nama, data in tahanan_options.items()
        if today <= data["tanggal_kunjungan"] + timedelta(days=data["batas_hari"])
    }

    if not filtered_tahanan:
        st.warning("⚠️ Semua data tahanan telah melewati batas 20 hari kunjungan.")
        st.stop()

    # ----------------- FORM -----------------
    with st.form("form_sakti"):
        st.markdown("### Pilih Tahanan", unsafe_allow_html=True)
        nama_tahanan = st.selectbox("Nama Tahanan", list(filtered_tahanan.keys()))
        data_tahanan = filtered_tahanan[nama_tahanan]

        st.markdown("### Data Pemohon (Pengunjung)", unsafe_allow_html=True)
        nama_pemohon = st.text_input("Nama Pemohon")
        alamat_pemohon = st.text_area("Alamat Pemohon")
        pekerjaan_pemohon = st.text_input("Pekerjaan Pemohon", "Belum / Tidak Bekerja")
        hubungan = st.text_input("Hubungan dengan Tahanan")
        keperluan = st.text_input("Keperluan Kunjungan", "Besuk Tahanan")
        tanggal_kunjungan = st.date_input("Tanggal Berlaku", value=today)

        # 📸 Ambil Foto KTP Langsung
        foto_ktp = st.camera_input("📷 Ambil Foto KTP Langsung")

        submit_sakti = st.form_submit_button("🚀 Generate & Kirim ke Admin")

    # ----------------- PROSES -----------------
    if submit_sakti:
        if not foto_ktp:
            st.error("❌ Mohon ambil foto KTP terlebih dahulu.")
            st.stop()

        # Email admin & kredensial Gmail dari secrets
        email_admin = st.secrets.get("EMAIL_ADMIN", "pidumbanyumas@gmail.com")
        sender_email = st.secrets["EMAIL_USER"]
        app_password = st.secrets["EMAIL_PASS"]

        # ==================== HITUNG UMUR (VERSI TAHANAN INDONESIA) ====================

        def parse_tanggal_lahir_indonesia(tanggal_str):
            """Konversi string tanggal lahir format Indonesia ke objek date"""
            bulan_mapping = {
                "januari": 1,
                "februari": 2,
                "maret": 3,
                "april": 4,
                "mei": 5,
                "juni": 6,
                "juli": 7,
                "agustus": 8,
                "september": 9,
                "oktober": 10,
                "november": 11,
                "desember": 12,
            }

            try:
                bagian = tanggal_str.strip().split()
                if len(bagian) != 3:
                    return None
                hari = int(bagian[0])
                bulan = bulan_mapping.get(bagian[1].lower())
                tahun = int(bagian[2])
                if not bulan:
                    return None
                return date(tahun, bulan, hari)
            except Exception:
                return None

        tgl_lahir_obj = parse_tanggal_lahir_indonesia(data_tahanan["tanggal_lahir"])

        if tgl_lahir_obj:
            umur_tahanan = (
                today.year
                - tgl_lahir_obj.year
                - ((today.month, today.day) < (tgl_lahir_obj.month, tgl_lahir_obj.day))
            )
        else:
            umur_tahanan = "-"
        # ----------------- NOMOR SURAT OTOMATIS -----------------
        NOMOR_SURAT_FILE = "nomor_surat.txt"

        def get_next_nomor_surat():
            """Membaca dan menaikkan nomor surat otomatis."""
            nomor_terakhir = 0
            if os.path.exists(NOMOR_SURAT_FILE):
                try:
                    with open(NOMOR_SURAT_FILE, "r") as f:
                        nomor_terakhir = int(f.read().strip() or 0)
                except Exception:
                    nomor_terakhir = 0

            nomor_baru = nomor_terakhir + 1
            with open(NOMOR_SURAT_FILE, "w") as f:
                f.write(str(nomor_baru))

            return nomor_baru

        # Panggil fungsi untuk dapatkan nomor urut
        nomor_urut = get_next_nomor_surat()

        # Format nomor surat resmi
        nomor_surat = f"B-{nomor_urut}/M.3.39/Es.2/{today.month}/{today.year}"

        # Context untuk surat
        context = {
            "nomor_surat": nomor_surat,
            "nama_tahanan": nama_tahanan,
            "alias_tahanan": data_tahanan.get("alias", "-"),
            "tempat_lahir": data_tahanan.get("tempat_lahir", "-"),
            "tanggal_lahir": data_tahanan.get("tanggal_lahir", "-"),
            "umur": umur_tahanan if umur_tahanan != "-" else "",
            "jenis_kelamin": data_tahanan.get("jenis_kelamin", "-"),
            "kewarganegaraan": data_tahanan.get("kewarganegaraan", "-"),
            "alamat_tahanan": data_tahanan.get("alamat", "-"),
            "agama": data_tahanan.get("agama", "-"),
            "pendidikan": data_tahanan.get("pendidikan", "-"),
            "nama_pemohon": nama_pemohon or "-",
            "pekerjaan_pemohon": pekerjaan_pemohon or "-",
            "alamat_pemohon": alamat_pemohon or "-",
            "hubungan": hubungan or "-",
            "keperluan": keperluan or "-",
            "tanggal_kunjungan": tanggal_kunjungan.strftime("%d %B %Y"),
            "tanggal_surat": today.strftime("%d %B %Y"),
        }

        # Buat surat izin (Word)
        surat_path = f"Surat_Izin_Kunjungan_{nama_pemohon or 'Pemohon'}.docx"
        doc = DocxTemplate("Surat_Template.docx")
        doc.render(context)
        doc.save(surat_path)

        # Simpan foto KTP sementara
        ktp_path = f"KTP_{nama_pemohon or 'Pemohon'}.jpg"
        with open(ktp_path, "wb") as f:
            f.write(foto_ktp.getbuffer())

        # Kirim email
        subject = f"Surat Izin Kunjungan - {nama_tahanan}"
        body = (
            f"Yth. Admin Bidang Pidana Umum,\n\n"
            f"Berikut surat izin kunjungan atas nama {nama_pemohon or 'Pemohon'} "
            f"untuk tahanan {nama_tahanan}.\n"
            f"Tanggal Berlaku: {tanggal_kunjungan.strftime('%d %B %Y')}.\n\n"
            f"Terlampir surat izin dan foto KTP pemohon.\n\n"
            f"Hormat kami,\nSAKTI – Kejaksaan Negeri Banyumas"
        )

        with st.spinner("📨 Mengirim surat & KTP ke admin..."):
            try:
                msg = EmailMessage()
                msg["From"] = sender_email
                msg["To"] = email_admin
                msg["Subject"] = subject
                msg.set_content(body)

                # Tambahkan 2 lampiran (surat + foto)
                for file_path in [surat_path, ktp_path]:
                    with open(file_path, "rb") as f:
                        data = f.read()
                        file_name = os.path.basename(file_path)
                        msg.add_attachment(
                            data,
                            maintype="application",
                            subtype="octet-stream",
                            filename=file_name,
                        )

                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                    smtp.login(sender_email, app_password)
                    smtp.send_message(msg)

                # Simpan log kunjungan
                tulis_log(
                    nama_pemohon,
                    nama_tahanan,
                    tanggal_kunjungan.strftime("%d %B %Y"),
                    today.strftime("%d %B %Y"),
                )

                st.success(f"✅ Surat & foto KTP berhasil dikirim ke {email_admin}")
            except Exception as e:
                st.error(f"❌ Gagal mengirim email: {e}")
            finally:
                for file in [surat_path, ktp_path]:
                    if os.path.exists(file):
                        os.remove(file)

elif menu == "Login Admin":
    st.markdown("## 🔐 Login Admin")

    # Kredensial admin
    ADMIN_USER = st.secrets.get("ADMIN_USER", "admin")
    ADMIN_PASS = st.secrets.get("ADMIN_PASS", "12345")

    # Jika belum login
    if not st.session_state.get("admin_logged_in"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == ADMIN_USER and password == ADMIN_PASS:
                st.session_state["admin_logged_in"] = True
                st.success("✅ Login berhasil! Menampilkan log kunjungan...")
                st.rerun()  # langsung reload halaman agar tabel muncul tanpa refresh manual
            else:
                st.error("❌ Username atau password salah.")

    # Jika sudah login, tampilkan data log
    elif st.session_state.get("admin_logged_in"):
        st.markdown("### 📋 Log Kunjungan Tahanan")

        if os.path.exists(LOG_FILE):
            import pandas as pd

            df = pd.read_csv(LOG_FILE)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("Belum ada log kunjungan yang tercatat.")

        # Tombol logout
        if st.button("Logout"):
            st.session_state["admin_logged_in"] = False
            st.success("✅ Anda telah logout.")
            st.rerun()
