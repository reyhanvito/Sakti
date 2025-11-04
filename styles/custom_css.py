import streamlit as st

def load_custom_css():
    st.markdown("""
    <style>
    /* ===================================
    🔤 FONT & RESET GLOBAL
    ==================================== */
    body {
        background-color: #f9fafb !important;
        font-family: "Segoe UI", "Roboto", sans-serif !important;
        color: #1f2937 !important;
    }

    /* ===================================
    🧭 SIDEBAR PREMIUM MODERN
    ==================================== */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #cc383c 0%, #7a0d0f 100%) !important;
        color: #f9fafb !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: flex-start !important;
        text-align: center !important;
        height: 100vh !important;
        padding: 10px 0 20px 0 !important;
        border-right: 1px solid rgba(255,255,255,0.08) !important;
        box-shadow: 3px 0 12px rgba(0,0,0,0.25) !important;
        animation: slideInLeft 0.6s ease !important;
        overflow-y: auto !important;
    }

    /* 🖼️ LOGO */
    section[data-testid="stSidebar"] img {
        width: 144px !important;
        height: auto !important;
        margin: 0 auto 8px auto !important;
        display: block !important;
        filter: drop-shadow(0 0 4px rgba(255,215,0,0.45)) !important;
        animation: fadeInDown 0.8s ease !important;
        transition: transform 0.3s ease, filter 0.3s ease !important;
    }

    section[data-testid="stSidebar"] img:hover {
    transform: scale(1.05);
    filter: drop-shadow(0 0 8px rgba(255,215,0,0.55));
    }

    /* 🏷️ TITLE MENU */
    .sidebar-title {
        font-size: 17px !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        letter-spacing: 1.3px !important;
        color: #FFD700 !important;
        border-bottom: 1px solid rgba(255,255,255,0.15) !important;
        padding-bottom: 6px !important;
        margin-bottom: 26px !important;
        width: 98% !important;
        text-align: center !important;
        animation: fadeInDown 0.8s ease !important;
    }

    /* 🔘 MENU NAVIGASI */
    div[role="radiogroup"] {
        display: flex !important;
        flex-direction: column !important;
        gap: 14px !important;
        width: 100% !important;
        align-items: center !important;
        animation: fadeInUp 0.8s ease !important;
    }

    div[role="radiogroup"] > label {
        position: relative !important;
        width: 110% !important;
        padding: 12px 16px !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        background: rgba(255,255,255,0.06) !important;
        color: #f9fafb !important;
        cursor: pointer !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        text-align: center !important
        line-height: 1.4 !important;
        align-items: center !important;;
        justify-content: center !important;
        transition: all 0.25s ease-in-out !important;
        box-shadow: inset 0 2px 6px rgba(0,0,0,0.05) !important;
    }

    /* Hilangkan bullet default radio */
    div[role="radiogroup"] > label > div:first-child {
        display: none !important;
    }

    /* Warna teks tetap terang */
    div[role="radiogroup"] > label * {
        color: inherit !important;
        opacity: 1 !important;
    }

    /* Hover */
    div[role="radiogroup"] > label:hover {
        background: rgba(255,215,0,0.18) !important;
        border-color: rgba(255,215,0,0.35) !important;
        transform: translateY(-2px) !important;
    }

    /* Aktif */
    div[role="radiogroup"] > label[data-checked="true"] {
        background: linear-gradient(135deg, #FFD700, #FFCC33) !important;
        color: #0b2f25 !important;
        font-weight: 700 !important;
        box-shadow: 0 6px 16px rgba(255,215,0,0.25) !important;
    }

    /* Bar emas di kiri menu aktif */
    div[role="radiogroup"] > label[data-checked="true"]::before {
        content: "" !important;
        position: absolute !important;
        left: 0 !important;
        top: 0 !important;
        bottom: 0 !important;
        width: 6px !important;
        background: #e5b100 !important;
        border-radius: 14px 0 0 14px !important;
    }

    /* 🎚️ SCROLLBAR CUSTOM */
    section[data-testid="stSidebar"]::-webkit-scrollbar {
        width: 6px !important;
    }
    section[data-testid="stSidebar"]::-webkit-scrollbar-thumb {
        background: rgba(255,255,255,0.2) !important;
        border-radius: 6px !important;
    }
    section[data-testid="stSidebar"]::-webkit-scrollbar-thumb:hover {
        background: rgba(255,255,255,0.4) !important;
    }

    /* ===================================
    📌 HEADER UTAMA (TITLE)
    ==================================== */
    .header-container {
        text-align: center;
        padding: 40px 15px 25px 15px;
        background: linear-gradient(135deg, #cc383c, #7a0d0f);
        border-radius: 0 0 20px 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        margin-bottom: 30px;
        animation: fadeInDown 0.8s ease;
    }
    .header-title {
        font-size: 34px;
        font-weight: 800;
        color: #ffd700;
        margin: 0;
    }
    .header-sub {
        font-size: 17px;
        margin-top: 10px;
        font-weight: 500;
        letter-spacing: 0.6px;
        color: #f5f5f5;
    }
    .header-sub .sub-highlight {
        color: #ffd700;
        font-weight: 700;
    }
    .header-sub .sub-normal {
        color: #d9d9d9;
        font-weight: 400;
    }
    .header-sub .separator {
        margin: 0 8px;
        color: #a0a0a0;
        font-weight: 300;
    }

    /* ===================================
    🔘 TOMBOL & INPUT
    ==================================== */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #ffd700, #ffb300);
        color: #004d40;
        font-size: 15px;
        font-weight: bold;
        padding: 10px 26px;
        border-radius: 10px;
        border: none;
        box-shadow: 0px 4px 10px rgba(255,215,0,0.4);
        transition: all 0.3s ease-in-out;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(135deg, #ffb300, #ffd700);
        transform: translateY(-2px);
        box-shadow: 0px 6px 15px rgba(0,0,0,0.25);
    }
    textarea {
        background-color: #ffffff !important;
        color: #333 !important;
        border-radius: 10px !important;
        border: 1px solid #d1d5db !important;
        padding-left: 15px !important;
        font-size: 15px !important;
    }
    textarea::placeholder {
        color: #9ca3af !important;
    }

    /* ===================================
    🎬 ANIMASI HALUS
    ==================================== */
    @keyframes slideInLeft {
        0% { transform: translateX(-220px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    @keyframes fadeInDown {
        0% { transform: translateY(-12px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(8px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)
