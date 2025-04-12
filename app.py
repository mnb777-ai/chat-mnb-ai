import streamlit as st
from transformers import pipeline

# تصميم الواجهة
st.set_page_config(page_title="Chat MNB AI", page_icon="🤖")
st.title("مرحبًا بك في Chat MNB AI!")

# الدردشة النصية
user_input = st.text_input("اكتب سؤالك هنا...")
if user_input:
    chatbot = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")
    response = chatbot(user_input, max_length=100)[0]['generated_text']
    st.success(response)

# تحميل الصور
uploaded_image = st.file_uploader("أرفع صورة لتحليلها", type=["jpg", "png"])
if uploaded_image:
    st.image(uploaded_image, caption="تم تحميل الصورة!", width=300)
    st.write("جارٍ التحليل...")

# زر الاشتراك
if st.button("🆓 ترقية إلى Pro"):
    st.write("انتقل إلى: [https://buy.stripe.com/test_123](https://buy.stripe.com/test_123)")
