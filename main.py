import  streamlit as st
from utils import generate_xiaohongshu

st.header("爆款小红书AI写作助手 🖋️")
with st.sidebar:
    api_key = st.text_input("请输入DeepSeek密钥： ",type="password")
    st.markdown("[获取DeepSeek密钥](https://platform.deepseek.com/api_keys)")

theme = st.text_input("主题")
submit = st.button("开始写作")

if submit and not api_key:
    st.info("请输入你的DeepSeek密钥 🔑")
    st.stop()
if submit and not theme:
    st.info("请你输入内容的主题 ^(*￣(oo)￣)^")
    st.stop()

if submit:
    with st.spinner("AI正在努力创作中，请稍等..."):
        result = generate_xiaohongshu(theme, api_key)
    st.divider()
    l_c,r_c =  st.columns(2)
    with l_c:
        for i in range(5):
            a=str(i+1)
            st.markdown(f"##### 小红书标题{a}")
            st.write(result.titles[i])

    with r_c:
        st.markdown("##### 小红书正文")
        st.write(result.content)
