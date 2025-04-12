import os
import openai
import streamlit as st
from dotenv import load_dotenv
import whisper
import tempfile
from diffusers import StableDiffusionPipeline

# تحميل مفاتيح API
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# إعداد واجهة المستخدم
st.set_page_config(page_title="MNB AI Pro", layout="wide")
st.title("🚀 MNB AI - مدعوم بـ OpenAI")

# شريط جانبي للإعدادات
with st.sidebar:
    st.header("الإعدادات ⚙️")
    api_key = st.text_input("أدخل مفتاح OpenAI API", type="password")
    if api_key:
        openai.api_key = api_key

# تبويبات للوظائف
tab1, tab2, tab3 = st.tabs(["💬 الدردشة الذكية", "🎨 توليد الصور", "🎤 تحويل الصوت"])

# تبويب الدردشة مع OpenAI
with tab1:
    st.subheader("محادثة مع الذكاء الاصطناعي")
    chat_input = st.text_area("اكتب رسالتك...")
    
    if st.button("إرسال", key="chat_btn"):
        if not openai.api_key:
            st.error("الرجاء إدخال مفتاح API في الشريط الجانبي")
        else:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": chat_input}],
                temperature=0.7
            )
            st.success(response.choices[0].message.content)

# تبويب توليد الصور
with tab2:
    st.subheader("توليد صور بالذكاء الاصطناعي")
    image_prompt = st.text_input("وصف الصورة المطلوبة")
    
    if st.button("توليد الصورة", key="image_btn"):
        pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0")
        image = pipe(image_prompt).images[0]
        st.image(image, caption=image_prompt)

# تبويب تحويل الصوت
with tab3:
    st.subheader("تحويل الصوت إلى نص")
    audio_file = st.file_uploader("ارفع ملف صوتي", type=["mp3", "wav", "ogg"])
    
    if audio_file and st.button("تحويل إلى نص", key="audio_btn"):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(audio_file.read())
            model = whisper.load_model("base")
            result = model.transcribe(tmp.name)
            st.write("**النص المقروء:**")
            st.code(result["text"])

# نص تذييلي
st.markdown("---")
st.caption("MNB AI - © 2023 | يدعم جميع اللغات والوظائف المتقدمة")
