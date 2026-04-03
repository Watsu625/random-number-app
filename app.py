import streamlit as st
import random
import time

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="เครื่องสุ่มตัวเลข", page_icon="🎲")

# ส่วนหัวของเว็บ
st.title("🎲 เครื่องสุ่มตัวเลข 3 หลัก")
st.write("กดปุ่มด้านล่างเพื่อทำการสุ่มตัวเลข 3 หลักครับ!")

st.divider()

# สร้างปุ่มกดสำหรับสุ่ม
if st.button("กดเพื่อสุ่มตัวเลขเลย!", type="primary"):
    
    with st.spinner('กำลังสุ่มตัวเลข...'):
        time.sleep(1) # หน่วงเวลาเล็กน้อยให้ดูน่าลุ้น
        
        # สุ่มตัวเลข 3 หลักเพียงครั้งเดียว
        digit1 = random.randint(0, 9)
        digit2 = random.randint(0, 9)
        digit3 = random.randint(0, 9)
        result = f"{digit1}{digit2}{digit3}"
        
        # แสดงผลลัพธ์
        st.subheader("🎯 ผลการสุ่มของคุณคือ:")
        st.markdown(f"<h1 style='text-align: center; color: green;'>[ {result} ]</h1>", unsafe_allow_html=True)
            
    st.balloons() # ปล่อยลูกโป่งฉลอง

