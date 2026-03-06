import streamlit as st
import requests
from user_agent import generate_user_agent as zzz

st.set_page_config(page_title="AI Image Generator", page_icon="🎨")

st.title("AI Image Generator")
st.write("اكتب وصف الصورة وسيتم توليدها")

prompt = st.text_input("Prompt")

if st.button("Generate Image"):

    c = requests.Session()
    c.headers.update({
        'User-Agent': zzz(),
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Origin': 'https://aifreeforever.com',
        'Referer': 'https://aifreeforever.com/image-generators'
    })

    url = "https://aifreeforever.com/api/generate-image"

    data = {
        "prompt": prompt,
        "resolution": "1024 × 1024 (Square)",
        "speed_mode": "Unsqueezed 🍋 (highest quality)",
        "output_format": "webp",
        "output_quality": 100,
        "seed": -1,
        "model_type": "fast"
    }

    try:
        r = c.post(url, json=data)
        result = r.json()

        if "images" in result:
            img = result["images"][0]
            st.image(img)

        elif "imageUrl" in result:
            st.image(result["imageUrl"])

        else:
            st.error("Error generating image")

    except Exception as e:
        st.error(e)
