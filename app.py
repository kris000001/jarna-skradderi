import streamlit as st
import streamlit.components.v1 as components
import backend

# 1. Page Configuration set to WIDE layout for laptop screens
st.set_page_config(page_title="Järna Kemtvätt", layout="wide")

# 2. Injecting Custom CSS
custom_css = """
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,600&family=Inter:wght@300;400;600&display=swap');

    /* Hide Streamlit UI */
    header {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}

    /* Apply Medium Matte Gray Background with Depth and Texture */
    .stApp {
        background-color: #5c6068; 
        background-image: 
            radial-gradient(circle at 50% 0%, rgba(192, 158, 90, 0.15) 0%, transparent 60%),
            linear-gradient(135deg, rgba(255,255,255,0.03) 25%, transparent 25%),
            linear-gradient(225deg, rgba(255,255,255,0.03) 25%, transparent 25%),
            linear-gradient(45deg, rgba(255,255,255,0.03) 25%, transparent 25%),
            linear-gradient(315deg, rgba(255,255,255,0.03) 25%, transparent 25%);
        background-size: 100% 100%, 40px 40px, 40px 40px, 40px 40px, 40px 40px;
        background-position: 0 0, 0 0, 0 20px, 20px -20px, -20px 0px;
        font-family: 'Inter', sans-serif !important;
        color: #f0f2f5;
    }

    /* Constrain the main container slightly on ultra-wide screens */
    .block-container {
        max-width: 1150px !important;
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
    }

    /* Apply Elegant Font to Headings */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Playfair Display', serif !important;
        color: #ffffff !important;
    }

    /* --- CLEAN, HIGH-VISIBILITY TAB NAVIGATION --- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        justify-content: center;
    }

    .stTabs button[data-baseweb="tab"] {
        background-color: #484b52 !important;
        border: 1px solid #6b6f78 !important;
        border-radius: 8px 8px 0 0 !important;
        padding: 12px 32px !important;
    }
    
    .stTabs button[data-baseweb="tab"] div, 
    .stTabs button[data-baseweb="tab"] span,
    .stTabs button[data-baseweb="tab"] p {
        font-family: 'Inter', sans-serif !important;
        font-size: 1.3rem !important; 
        font-weight: 600 !important;
        color: #c5c8ce !important; 
    }
    
    /* When a tab is actively selected */
    .stTabs button[aria-selected="true"] {
        background-color: #484b52 !important;
        border-bottom: 4px solid #c09e5a !important; /* Tailor Gold accent */
    }
    
    .stTabs button[aria-selected="true"] div,
    .stTabs button[aria-selected="true"] span,
    .stTabs button[aria-selected="true"] p {
        color: #ffffff !important; 
    }

    /* --- IMAGE AESTHETICS --- */
    [data-testid="stImage"] img {
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.4);
        transition: transform 0.3s ease;
    }
    [data-testid="stImage"] img:hover {
        transform: scale(1.02);
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- CUSTOM BRAND HEADER ---
st.markdown("""
<div style='text-align: center; padding-top: 1rem; padding-bottom: 2rem;'>
    <h1 style='font-size: 4rem; color: #ffffff; margin-bottom: 0;'>Järna Kemtvätt</h1>
    <h3 style='font-size: 1.3rem; color: #c09e5a; margin-top: 5px; font-family: "Inter", sans-serif; font-weight: 400; letter-spacing: 4px;'>SKRÄDDERI & KEMTVÄTT</h3>
</div>
""", unsafe_allow_html=True)

# Navigation tabs updated
tab_main, tab_about, tab_contact = st.tabs(["Hem", "Om Oss", "Omdömen & Kontakt"])

# --- INTERFACE 1: MAIN ---
with tab_main:
    st.header("Välkommen till oss!")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Get images from backend, but filter out "imgClose"
    backend_images = [img for img in backend.get_images() if "imgClose" not in str(img)]
    
    # Combine backend images with the two new ones
    home_images = backend_images + ["imgKeys.jpg", "imgMachines.jpg"]
    
    # Create a dynamic grid that puts images in rows of 3
    cols = st.columns(3)
    for index, img_path in enumerate(home_images):
        with cols[index % 3]:
            st.image(img_path, use_container_width=True)
            st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
        
    st.markdown("<br><hr style='border: 1px solid #6b6f78;'><br>", unsafe_allow_html=True)

    # Layout for Hours & Small Map side-by-side
    col_info, col_map = st.columns([1, 1], gap="large")
    
    with col_info:
        st.subheader("Öppettider & Adress")
        address = backend.get_address()
        st.write(f"📍 **Adress:** {address}")
        
        hours = backend.get_hours()
        st.write("**Öppettider:**")
        for day, time in hours.items():
            st.write(f"- **{day}:** {time}")

    with col_map:
        st.subheader("Hitta Hit")
        map_html = """
        <iframe 
            width="100%" 
            height="270" 
            style="border:0; border-radius: 12px; box-shadow: 0 6px 15px rgba(0,0,0,0.3);" 
            loading="lazy" 
            allowfullscreen
            src="https://maps.google.com/maps?q=Storgatan%201A,%20153%2030%20J%C3%A4rna&t=&z=15&ie=UTF8&iwloc=&output=embed">
        </iframe>
        """
        components.html(map_html, height=280)

# --- INTERFACE 2: ABOUT US ---
with tab_about:
    st.markdown("<br>", unsafe_allow_html=True)
    
    about_html = """<div style="max-width: 850px; margin: 0 auto; background-color: #484b52; padding: 50px 60px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.25); border-top: 4px solid #c09e5a; text-align: center;">
<div style="font-size: 3rem; color: #c09e5a; margin-bottom: 10px; line-height: 1;">❝</div>
<p style="font-family: 'Playfair Display', serif; font-size: 1.35rem; color: #e4e6eb; line-height: 1.8; margin-bottom: 25px; font-weight: 400;">Jag heter <strong>X</strong> och jag har jobbat som skräddare i över 35 år, där jag har sytt allt från kostymer, klänningar, kjolar och kappor från grunden i väldigt hög kvalitet. Jag kan serva alla sorters symaskiner. Jag har flera års erfarenhet inom skomakeri och även nyckeltillverkning.</p>
<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; margin: 30px 0;">
<div style="background-color: #383a40; padding: 10px 18px; border-radius: 20px; border: 1px solid #c09e5a; color: #ffffff; font-family: 'Inter', sans-serif; font-size: 1.05rem; font-weight: 500;">✂️ Skrädderi</div>
<div style="background-color: #383a40; padding: 10px 18px; border-radius: 20px; border: 1px solid #c09e5a; color: #ffffff; font-family: 'Inter', sans-serif; font-size: 1.05rem; font-weight: 500;">👔 Kemtvätt</div>
<div style="background-color: #383a40; padding: 10px 18px; border-radius: 20px; border: 1px solid #c09e5a; color: #ffffff; font-family: 'Inter', sans-serif; font-size: 1.05rem; font-weight: 500;">🔑 Nyckeltillverkning</div>
<div style="background-color: #383a40; padding: 10px 18px; border-radius: 20px; border: 1px solid #c09e5a; color: #ffffff; font-family: 'Inter', sans-serif; font-size: 1.05rem; font-weight: 500;">👞 Skomakeri</div>
</div>
<p style="font-family: 'Playfair Display', serif; font-size: 1.35rem; color: #e4e6eb; line-height: 1.8; margin-bottom: 30px; font-weight: 400;">På Järna Kemtvätt och Skrädderi erbjuder vi tjänster inom skrädderi, kemtvätt, nyckeltillverkning och skomakeri. Vi prioriterar kvalitet och strävar efter att nöja alla våra kunder.</p>
<hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(192, 158, 90, 0), rgba(192, 158, 90, 0.75), rgba(192, 158, 90, 0)); margin: 30px 0;">
<p style="font-family: 'Playfair Display', serif; font-size: 1.5rem; color: #c09e5a; font-style: italic; font-weight: 600; margin-bottom: 0;">Du är alltid välkommen till Järna Kemtvätt och Skrädderi.</p>
</div>"""

    st.markdown(about_html, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

# --- INTERFACE 3: REVIEWS & CONTACT ---
with tab_contact:
    st.header("Vad Våra Kunder Säger")
    
    reviews = backend.get_reviews()
    for review in reviews:
        card_html = f"""<div style="background-color: #484b52; padding: 22px; border-radius: 10px; box-shadow: 0 6px 18px rgba(0,0,0,0.25); border-left: 5px solid #c09e5a; margin-bottom: 20px;">
<div style="font-size: 1.15rem; color: #ffffff; margin-bottom: 8px;">{review['rating']} <strong>{review['name']}</strong></div>
<div style="font-family: 'Playfair Display', serif; font-style: italic; color: #d0d3dc; font-size: 1.25rem;">"{review['text']}"</div>
</div>"""
        st.markdown(card_html, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.header("Kontakta Oss")
    st.write("📞 **Ring oss:** 08-551 704 40")
    st.write("✉️ **E-post:** jarnakemtvattskradderi@gmail.com")