import streamlit as st
import qrcode
from io import BytesIO
import uuid
from PIL import Image
from gtts import gTTS
import base64

#--------------------------
#QR GENERATION FUNCTION
#--------------------------
def generate_qr(data):
    qr=qrcode.QRCode(version=1,box_size=10,border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black",back_color="white")
    return img
#------------------------
#STREAMLIT UI
#------------------------
st.set_page_config(page_title="Metro Ticket Booking",page_icon="")
st.title("Metro tickets booking Sysytem with QR Code+Auto voice")
stations=["Ameerpet","Miyapur","LB nagar","KPHP","JNTU"]
name=st.text_input("Enter passenger name")
source=st.selectbox("Source station",stations)
destination=st.selectbox("Destination stations",stations)
no_of_tickets=st.number_input("Number of Tickets",min_value=1,value=1)
price_per_ticket=30
total_amount=no_of_tickets*price_per_ticket
st.info(f"Total Amount:rs{total_amount}")
#-----------------------------
#BOOKING BUTTON
#-----------------------------
if st.button("Book Tickets"):
    if name.strip()=="":
        st.error("Please enter passenger name.")
    elif source==destination:
        st.error("source and destination cannot be the same")
    else:
        #Generating bookin ID
        booking_id=str(uuid.uuid4())[:8]
        #QRCode Generation
        qr_data=(
            f"BookingID:{booking_id}\n"
            f"Name:{name}\nFrom:{source}\nto:{destination}\n Tickets:{no_of_tickets}"
            )
        qr_img=generate_qr(qr_data)
        buf=BytesIO()
        qr_img.save(buf,format="PNG")
        qr_bytes=buf.getvalue()
        #SHOW SUCCESS AND DETAILS
        st.success("Tickets Booking succesfullu!!!!")
        st.write("Ticket details")
        st.write(f"**Booking ID:** {booking_id}")
        st.write(f"**passenger:** {name}")
        st.write(f"**From:** {source}")
        st.write(f"**To:** {destination}")
        st.write(f"**Tickets:** {no_of_tickets}")
        st.write(f"Amount paid:** {total_amount}")
        st.image(qr_bytes,width=250)

