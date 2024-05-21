import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit_plotly_mapbox_events import plotly_mapbox_events
import plotly.express as px
import pandas as pd
import numpy as np

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
        options=['Terdekat', 'Populer','Banyak Diskon','Voucher'],
        icons= ['pin-map','bag-heart','bag-check','postcard'],
        menu_icon="cast", 
        default_index=0,
        orientation="horizontal",
    )
    if 'button_clicked' not in st.session_state:
        st.session_state.button_clicked = False
    if 'jumlahst' not in st.session_state:
        st.session_state.jumlahst = 0
    if 'jumlahes' not in st.session_state:
        st.session_state.jumlahes = 0
    if 'jumlahst1' not in st.session_state:
        st.session_state.jumlahst1 = 0
    if 'jumlahes1' not in st.session_state:
        st.session_state.jumlahes1 = 0
    if 'jumlahst2' not in st.session_state:
        st.session_state.jumlahst2 = 0
    if 'jumlahes2' not in st.session_state:
        st.session_state.jumlahes2 = 0
    if 'checkout_clicked' not in st.session_state:
        st.session_state.checkout_clicked = False
    if 'pay_clicked' not in st.session_state:
        st.session_state.pay_clicked = False
    if 'pop1_clicked' not in st.session_state:
        st.session_state.pop1_clicked = False
    if 'pop11_clicked' not in st.session_state:
        st.session_state.pop11_clicked = False
    if 'pop12_clicked' not in st.session_state:
        st.session_state.pop12_clicked = False
    if 'pop13_clicked' not in st.session_state:
        st.session_state.pop13_clicked = False
    if 'dis1_clicked' not in st.session_state:
        st.session_state.dis1_clicked = False
    if 'dis11_clicked' not in st.session_state:
        st.session_state.dis11_clicked = False
    if 'dis12_clicked' not in st.session_state:
        st.session_state.dis12_clicked = False
    if 'dis13_clicked' not in st.session_state:
        st.session_state.dis13_clicked = False
    if 'dis2_clicked' not in st.session_state:
        st.session_state.dis2_clicked = False
    if 'dis21_clicked' not in st.session_state:
        st.session_state.dis21_clicked = False
    if 'dis22_clicked' not in st.session_state:
        st.session_state.dis22_clicked = False
    if 'dis23_clicked' not in st.session_state:
        st.session_state.dis23_clicked = False
        
    def on_button_click():
        st.session_state.button_clicked = True
    def on_checkout_click():
        st.session_state.checkout_clicked = True
    def on_pay_click():
        st.session_state.pay_clicked = True
    def on_pop1_click():
        st.session_state.pop1_clicked = True
    def on_pop11_click():
        st.session_state.pop11_clicked = True
    def on_pop12_click():
        st.session_state.pop12_clicked = True
    def on_pop13_click():
        st.session_state.pop13_clicked = True
    def on_dis1_click():
        st.session_state.dis1_clicked = True
    def on_dis11_click():
        st.session_state.dis11_clicked = True
    def on_dis12_click():
        st.session_state.dis12_clicked = True
    def on_dis13_click():
        st.session_state.dis13_clicked = True
    def on_dis2_click():
        st.session_state.dis2_clicked = True
    def on_dis21_click():
        st.session_state.dis21_clicked = True
    def on_dis22_click():
        st.session_state.dis22_clicked = True
    def on_dis23_click():
        st.session_state.dis23_clicked = True

    
    if Menu== "Terdekat":    
        df = pd.DataFrame(
            np.random.randn(400, 2) / [100, 100] + [-7.281763,112.795482],
            columns=['lat', 'lon'])
        st.map(df)

        but = st.button('Pilih', on_click=on_button_click)
        if st.session_state.button_clicked:
            st.header('Menu')
            col1, col2 = st.columns(2)
            with col1:
                st.subheader('Makanan')
                image = Image.open('sate.jpg') 
                st.image(image)
                st.subheader('Minuman')
                image1 = Image.open('esteh.jpg') 
                st.image(image1)
            with col2:
                st.write('')
                st.write('')
                st.write('')
                st.write('Sate Ayam')
                st.session_state.jumlahst = st.number_input("Jumlah", min_value=0, value=st.session_state.jumlahst)
                level= st.selectbox('Pilih Level', ['Pedas','Tidak'])
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.write('Es Teh')
                st.session_state.jumlahes = st.number_input("Jumlah  ", min_value=0, value=st.session_state.jumlahes)
            but1 = st.button('Checkout', on_click=on_checkout_click)
            if st.session_state.checkout_clicked:
                harga= 15000*st.session_state.jumlahst
                harga2=3000*st.session_state.jumlahes
                Ongkir= 4000
                layanan= 9000
                total= harga+Ongkir+layanan+harga2
                st.write(f"Harga Sate=Rp{harga}")
                st.write(f"Harga Es Teh=Rp{harga2}")
                st.write(f"Biaya Pengiriman=Rp{Ongkir}")
                st.write(f"Biaya Layanan=Rp{layanan}")
                st.write(f"Total=Rp{total}")
                but2 = st.button('Bayar', on_click=on_pay_click)
                if st.session_state.pay_clicked:
                    st.success("Pembayaran Berhasil")
            

                
        
    
    if Menu== "Populer":
        col1,col2,col3=st.columns(3)
        with col1:
            image = Image.open('sate.jpg')
            st.image(image)
            st.write('Sate ayam Pak Mus')
            st.write('⭐5.0')
            but=st.button('Selengkapnya', on_click=on_pop1_click)
            if st.session_state.pop1_clicked:
                df = pd.DataFrame(
                    np.random.randn(1, 2) / [100, 100] + [-7.281763,112.795482],
                    columns=['lat', 'lon'])
                st.map(df)
                but = st.button('Pilih', on_click=on_pop11_click)
                if st.session_state.pop11_clicked:
                    st.header('Menu')
                    st.subheader('Makanan')
                    st.write('Sate Ayam')
                    image = Image.open('sate.jpg') 
                    st.image(image)
                    st.session_state.jumlahst1 = st.number_input("Jumlah", min_value=0, value=st.session_state.jumlahst1)
                    level= st.selectbox('Pilih Level', ['Pedas','Tidak'])
                    st.subheader('Minuman')
                    st.write('Es Teh')
                    image1 = Image.open('esteh.jpg') 
                    st.image(image1)
                    st.session_state.jumlahes1 = st.number_input("Jumlah  ", min_value=0, value=st.session_state.jumlahes1)
                    but1 = st.button('Checkout', on_click=on_pop12_click)
                    if st.session_state.pop12_clicked:
                        harga= 15000*st.session_state.jumlahst1
                        harga2=3000*st.session_state.jumlahes1
                        Ongkir= 4000
                        layanan= 9000
                        total= harga+Ongkir+layanan+harga2
                        st.write(f"Harga Sate=Rp{harga}")
                        st.write(f"Harga Es Teh=Rp{harga2}")
                        st.write(f"Biaya Pengiriman=Rp{Ongkir}")
                        st.write(f"Biaya Layanan=Rp{layanan}")
                        st.write(f"Total Harga=Rp{total}")
                        but2 = st.button('Bayar', on_click=on_pop13_click)
                        if st.session_state.pop13_clicked:
                            st.success("Pembayaran Berhasil")
            
        with col2:
            image = Image.open('seblak.jpeg')
            st.image(image)
            st.write('Seblak Bandung Teh Lilis')
            st.write('⭐4.9')
            but1=st.button('Selengkapnya  ')
        with col3:
            image = Image.open('siomay.jpg')
            st.image(image)
            st.write('Siomay Ikan Bu Rika')
            st.write('⭐4.9')
            but2=st.button('Selengkapnya   ')
            
    if (Menu=='Banyak Diskon'):
        col1,col2,col3=st.columns(3)
        with col1:
            image = Image.open('sate.jpg')
            st.image(image)
            st.write('Sate ayam Pak Mus')
            st.write('Diskon 40%')
            but= st.button('Selengkapnya', on_click=on_dis1_click)
            if st.session_state.dis1_clicked:
                df = pd.DataFrame(
                    np.random.randn(1, 2) / [100, 100] + [-7.281763,112.795482],
                    columns=['lat', 'lon'])
                st.map(df)
                but1=st.button('Pilih', on_click=on_dis11_click)
                if st.session_state.dis11_clicked:
                    st.header('Menu')
                    st.subheader('Makanan')
                    st.write('Sate Ayam')
                    image = Image.open('sate.jpg') 
                    st.image(image)
                    st.session_state.jumlahst2 = st.number_input("Jumlah", min_value=0, value=st.session_state.jumlahst2)
                    level= st.selectbox('Pilih Level', ['Pedas','Tidak'])
                    st.subheader('Minuman')
                    st.write('Es Teh')
                    image1 = Image.open('esteh.jpg') 
                    st.image(image1)
                    st.session_state.jumlahes2 = st.number_input("Jumlah  ", min_value=0, value=st.session_state.jumlahes2)
                    diskon= st.checkbox("Gunakan Voucher")
                    harga= 15000*st.session_state.jumlahst2
                    harga2=3000*st.session_state.jumlahes2
                    Ongkir= 4000
                    layanan= 9000
                    but2=st.button('Checkout', on_click=on_dis12_click)
                    if st.session_state.dis12_clicked:
                        if diskon:
                            diskon= harga+harga2-((harga+harga2)*(40/100))
                            total1= harga+harga2+Ongkir+layanan-((harga+harga2)*(40/100))
                            total= harga+Ongkir+layanan+harga2
                            st.write(f"Harga Sate=Rp{harga}")
                            st.write(f"Harga Es Teh=Rp{harga2}")
                            st.write(f"Biaya Pengiriman=Rp{Ongkir}")
                            st.write(f"Biaya Layanan=Rp{layanan}")
                            st.write(f"Total Harga=Rp{total}")
                            st.write(f"Diskon Voucher=Rp{diskon}")
                            st.write(f"Total Harga setelah diskon=Rp{total1}")
                        else:
                            total= harga+Ongkir+layanan+harga2
                            st.write(f"Harga Sate=Rp{harga}")
                            st.write(f"Harga Es Teh=Rp{harga2}")
                            st.write(f"Biaya Pengiriman=Rp{Ongkir}")
                            st.write(f"Biaya Layanan=Rp{layanan}")
                            st.write(f"Total Harga=Rp{total}")

                        but2 = st.button('Bayar', on_click=on_dis13_click)
                        if st.session_state.dis13_clicked:
                            st.success("Pembayaran Berhasil")
                
        with col2:
            image = Image.open('seblak.jpeg')
            st.image(image)
            st.write('Seblak Bandung Teh Lilis')
            st.write('Diskon 20% ✅Geratis Ongkir')
            but1= st.button('Selengkapnya ', on_click=on_dis2_click)
            if st.session_state.dis2_clicked:
                df = pd.DataFrame(
                    np.random.randn(1, 2) / [100, 100] + [-7.284589,112.801882],
                    columns=['lat', 'lon'])
                st.map(df)
            
        with col3:
            image = Image.open('siomay.jpg')
            st.image(image)
            st.write('Siomay Ikan Bu Rika')
            st.write('✅Geratis Ongkir')
            but2=st.button('Selengkapnya>>>')
            
    if (Menu== 'Voucher'):
        st.header('Voucher Makanan')
        col1,col2,col3=st.columns(3)
        with col1:
            image = Image.open('v1.png')
            st.image(image)
            but1=st.button('Klaim  ')
            if but1:
                st.success("Voucher berhasil diklaim")
        with col2:
            image = Image.open('v2.png')
            st.image(image)
            but2= st.button('Klaim ')
            if but2:
                st.success("Voucher berhasil diklaim")
        with col3:
            image = Image.open('v3.png')
            st.image(image)
            but3= st.button('Klaim   ')
            if but3:
                st.success("Voucher berhasil diklaim")
                
        st.header('Voucher Geratis Ongkir')
        col1,col2,col3=st.columns(3)
        with col1:
            image = Image.open('v6.png')
            st.image(image)
            but4=st.button('Klaim          ')
            if but4:
                st.success("Voucher berhasil diklaim")
        with col2:
            image = Image.open('v4.png')
            st.image(image)
            but5= st.button('Klaim    ')
            if but5:
                st.success("Voucher berhasil diklaim")
        with col3:
            image = Image.open('v5.png')
            st.image(image)
            but6= st.button('Klaim       ')
            if but6:
                st.success("Voucher berhasil diklaim")


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


    
        
        
