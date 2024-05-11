import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit_plotly_mapbox_events import plotly_mapbox_events
import plotly.express as px
import pandas as pd


with st.sidebar:
    Pilihan= option_menu('KeliLink',['Home','Pesanan Saya','Riwayat'],icons=['house','basket2','card-list'],default_index=0)
    

if(Pilihan=='Home'):
    choice= st.selectbox('', ['🔎Cari makanan dan minuman'])
    col1,col2,col3=st.columns(3)
    with col1:
        image = Image.open('sate.jpg')
        st.image(image)
    with col2:
        image = Image.open('seblak.jpeg')
        st.image(image)
    with col3:
        image = Image.open('siomay.jpg')
        st.image(image)
    
    col1,col2,col3= st.columns(3)
    with col1:
        st.button('💰Dompetmu: Rp. 100.000')
    with col2:
        st.button('🪙Poin: 1.000')
    
    Menu = option_menu(
        menu_title= '',
        options=['Terdekat', 'Populer','Banyak Diskon'],
        icons= ['award-fill','database-fill-down'],
        menu_icon="cast", 
        default_index=0,
        orientation="horizontal",
    )
    if Menu== "Terdekat":
        df = pd.DataFrame({
            'lat': [-7.283001],
            'lon': [112.796328],
            'hover': [1],
            'color_1': [3],
            'color_2': [5],
            'color_3': [3]
        })
        mapbox = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="hover", zoom=12, height=600)
        mapbox.update_layout(mapbox_style="carto-positron")
        mapbox.update_layout(margin={"r":0, "t":0, "l":0, "b":0})
        mapbox_events = plotly_mapbox_events(
            mapbox,
            click_event=True,
            select_event=True,
            hover_event=True,
            override_height=600
        )
        plot_name_holder_clicked = st.empty()
        plot_name_holder_selected = st.empty()
        plot_name_holder_hovered = st.empty()
    
    if Menu== "Populer":
        col1,col2,col3=st.columns(3)
        with col1:
            image = Image.open('sate.jpg')
            st.image(image)
            st.write('Sate ayam Pak Mus')
            st.write('⭐5.0')
            but=st.button('Selengkapnya>')
        with col2:
            image = Image.open('seblak.jpeg')
            st.image(image)
            st.write('Seblak Bandung Teh Lilis')
            st.write('⭐4.9')
            but1=st.button('Selengkapnya>>')
        with col3:
            image = Image.open('siomay.jpg')
            st.image(image)
            st.write('Siomay Ikan Bu Rika')
            st.write('⭐4.9')
            but2=st.button('Selengkapnya>>>')

if (Pilihan=='Pesanan Saya'):
    st.header('Pesanan Saya🍟')
    st.subheader('📍Martabak Mas Bro')
    col1,col2,col3=st.columns(3)
    with col1:
        image=Image.open('martabak.jpg')
        st.image(image)
    with col2:
        st.write('')
        st.subheader('Rp. 28.000')
        st.button('Pesan lagi')
        st.button('Beri Penilian')
    
        
        
