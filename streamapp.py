import streamlit as st
import pandas as pd

url1="https://drive.google.com/file/d/1M8C8-nsECj5DB5m3cRc10ahNm3faQ-FO/view?usp=sharing"
url1='https://drive.google.com/uc?id=' + url1.split('/')[-2]
af = pd.read_csv(url1)

url2="https://drive.google.com/file/d/1_Sramq2IYxVk9sE_vzdm3iAeMvkL4g0j/view?usp=sharing"
url2='https://drive.google.com/uc?id=' + url2.split('/')[-2]
bf = pd.read_csv(url2)

url3="https://drive.google.com/file/d/1cvFhrlTl7TZyX1nH_mD2FP_Tq-b3m6UO/view?usp=sharing"
url3='https://drive.google.com/uc?id=' + url3.split('/')[-2]
cf = pd.read_csv(url3)

st.title('Listings')
st.write(af)
st.title('Calendar')
st.write(bf)
st.title('Reviews')
st.write(cf)