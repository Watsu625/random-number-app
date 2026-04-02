import streamlit as st
import random
import time

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="เครื่องสุ่มตัวเลข", page_icon="🎲")

# ส่วนหัวของเว็บ
st.title("🎲 เครื่องสุ่มตัวเลข 3 หลัก")
st.write("กดปุ่มด้านล่างเพื่อทำการสุ่มตัวเลข 3 หลัก จำนวน 3 ครั้งครับ!")

st.divider() # เส้นคั่น

# สร้างปุ่มกดสำหรับสุ่ม
if st.button("กดเพื่อสุ่มตัวเลขเลย!", type="primary"):
    
    # ทำให้มีแอนิเมชันหมุนๆ ตอนกำลังสุ่ม
    with st.spinner('กำลังสุ่มตัวเลข... รอลุ้นเลย!'):
        time.sleep(1) # หน่วงเวลาหลอกๆ ให้ดูน่าตื่นเต้น
        
        # สุ่ม 3 ครั้ง
        for i in range(1, 4):
            digit1 = random.randint(0, 9)
            digit2 = random.randint(0, 9)
            digit3 = random.randint(0, 9)
            result = f"{digit1}{digit2}{digit3}"
            
            time.sleep(0.5)
            # แสดงผลตัวเลขให้ตัวใหญ่และสวยงาม
            st.success(f"👉 ผลการสุ่มครั้งที่ {i}: **[ {result} ]**")
            
    st.balloons() # ปล่อยลูกโป่งฉลองเมื่อสุ่มเสร็จ!

