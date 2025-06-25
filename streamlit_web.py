import streamlit as st
import numpy as np
from datetime import datetime
import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import StandardScaler


st.set_page_config(
    page_title="Obezite Tahmin",
)


# st.markdown("## **Obezite Tahmin Modeli**")
# st.markdown("Bulunmakta olan sitemiz açık kaynaklı olmak üzeredir. sitemizdeki girdiğiniz veriler sitemizde kayıtlı bulunmamaktadır")

st.markdown("""# **Obezite Tahmin Modeli**

Bulunmakta olan sitemiz açık kaynaklı olmak üzeredir. sitemizdeki girdiğiniz veriler sitemizde kayıtlı bulunmamaktadır
            
### **Ne kullandık:**
- SQL: `PostgreSQL`
- Web: `streamlit`
- Veri Bilimi: `numpy`, `pandas`, `matplotlib` , `seaborn`
- Model Kütüphaneleri: `scikit-learn`, `XGBosst`
""")

st.markdown("---")
gender = st.radio(
    "## **Cinsiyetin Ne?**",
    ["Kız", "Erkek"])
if gender == "Kız":
    gender_numeric = 0
elif gender == "Erkek":
    gender_numeric = 1

st.markdown("---")
st.markdown("#### **Yaş**")
age = st.slider("Yaşınızı Seçiniz:", min_value=21, max_value=110, value=30)

st.markdown("---")
st.markdown("#### **Boy**")
height = st.slider("Boyunuzu Seçiniz:", min_value=120, max_value=200, value=165)

st.markdown("---")
st.markdown("#### **Kilo**")
weigh = st.slider("Kilonuzu Seçiniz:", min_value=30, max_value=150, value=70)




st.markdown("---")

family_history = st.radio(
    "## **Aile Geçmişinde Obez Biri Var Mı?**",
    ["Evet", "Hayır"]
)

if family_history == "Evet":
    family_history_numeric = 1
elif family_history == "Hayır":
    family_history_numeric = 0

st.markdown("---")
high_calorie_food = st.radio(
    "## **Yüksek Kalorili Yemekleri Yer Misin?**",
    ["Evet", "Hayır"])
if high_calorie_food == "Evet":
    high_calorie_food_numeric = 1
elif high_calorie_food == "Hayır":
    high_calorie_food_numeric = 0

st.markdown("---")

vegatable_food = st.radio(
    "## **Meyve Sebze Yeme Seviyen?**",
    ["Seviye 1", "Seviye 2", "Seviye 3"])
if vegatable_food == "Seviye 1":
    vegatable_food_numeric = 1.0
elif vegatable_food == "Seviye 2":
    vegatable_food_numeric = 2.0
elif vegatable_food == "Seviye 3":
    vegatable_food_numeric = 3.0

st.markdown("---")
st.markdown("**Günde Kaç Öğün Yemek Yersin**")
meals_per_day = st.number_input("", min_value=1, max_value=5, value=3, step=1)
st.markdown("---")

food_between_meals = st.selectbox(
    "## **Hangi Sıklıkla Öğün Arası Atıştırırsın?**",
    ["Hiçbir zaman", "Bazen", "Sık sık", "Her zaman"])
if food_between_meals == "Hiçbir zaman":
    food_between_meals_numeric = 3
elif food_between_meals == "Bazen":
    food_between_meals_numeric = 2
elif food_between_meals == "Sık sık":
    food_between_meals_numeric = 1
elif food_between_meals == "Her zaman":
    food_between_meals_numeric = 0

    
st.markdown("---")

smoking = st.radio(
    "## **Sigara İçer Misin?**",
    ["Evet", "Hayır"])
if smoking == "Evet":
    smoking_numeric = 1
elif smoking == "Hayır":
    smoking_numeric = 0
st.markdown("---")
water = st.radio(
    "## **Ne Kadar Su İçersin?**",
    ["Seviye 1", "Seviye 2", "Seviye 3"])
if water == "Seviye 1":
    water_numeric = 1.0
elif water == "Seviye 2":
    water_numeric = 2.0
elif water == "Seviye 3":
    water_numeric = 3.0
st.markdown("---")
calorie_tracking = st.radio(
    "## **Kalori Alımını Takip Eder Misin?**",
    ["Evet", "Hayır"])
if calorie_tracking == "Evet":
    calorie_tracking_numeric = 1
elif calorie_tracking == "Hayır":
    calorie_tracking_numeric = 0

#
st.markdown("---")
physical_activity = st.radio(
    "## **Hangi Sıklıkla Fiziksel Aktevite Yaparsın?**",
    ["Seviye 0", "Seviye 1", "Seviye 2", "Seviye 3"])
if physical_activity == "Seviye 0":
    physical_activity_numeric = 0.0
elif physical_activity == "Seviye 1":
    physical_activity_numeric = 1.0
elif physical_activity == "Seviye 2":
    physical_activity_numeric = 2.0
elif physical_activity == "Seviye 3":
    physical_activity_numeric = 3.0
st.markdown("---")

#
time_spent_on_tech = st.radio(
    "## **Zamanın Ne Kadarını Teknolojiye Ayırsın?**",
    ["Seviye 0", "Seviye 1", "Seviye 2", "Seviye 3"])
if time_spent_on_tech == "Seviye 0":
    time_spent_on_tech_numeric = 0.0
elif time_spent_on_tech == "Seviye 1":
    time_spent_on_tech_numeric = 1.0
elif time_spent_on_tech == "Seviye 2":
    time_spent_on_tech_numeric = 2.0
elif time_spent_on_tech == "Seviye 3":
    time_spent_on_tech_numeric = 3.0
st.markdown("---")
alcohol = st.selectbox(
    "## **Hangi Sıklıkla Alkol Tüketirsin?**",
    ["Hiçbir zaman", "Bazen", "Sık sık", "Her zaman"])

#
if alcohol == "Hiçbir zaman":
    alcohol_numeric = 3
elif alcohol == "Bazen":
    alcohol_numeric = 2
elif alcohol == "Sık sık":
    alcohol_numeric = 1
elif alcohol == "Her zaman":
    alcohol_numeric = 0

#
st.markdown("---")
transportation = st.selectbox(
    "## **Genellikle Ulaşımını Ne ile Yaparsın?**",
    ["Otomobil", "Bisiklet", "Motobisiklet", "Toplu Taşıma", "Yürüme"])

if transportation == "Otomobil":
    transportation_numeric = 0
elif transportation == "Bisiklet":
    transportation_numeric = 1
elif transportation == "Motobisiklet":
    transportation_numeric = 2
elif transportation == "Toplu Taşıma":
    transportation_numeric = 3
elif transportation == "Yürüme":
    transportation_numeric = 4


# Model

from joblib import load

model = load('xgboost_model.pkl')




#Xgboost Model Eğitim
input_df = pd.DataFrame({
    'Gender': [gender_numeric],
    'Age': [age],
    'Height': [height],
    'Weight': [weigh],
    'family_history_with_overweight': [family_history_numeric],
    'FAVC': [high_calorie_food_numeric],
    'FCVC': [vegatable_food_numeric],
    'NCP': [meals_per_day],
    'CAEC': [food_between_meals_numeric],
    'SMOKE': [smoking_numeric],
    'CH2O': [water_numeric],
    'SCC': [calorie_tracking_numeric],
    'FAF': [physical_activity_numeric],
    'TUE': [time_spent_on_tech_numeric],
    'CALC': [alcohol_numeric],
    'MTRANS': [transportation_numeric]

})
model = load('xgboost_model.pkl')
scaler = load('scaler.pkl')  # scaler'ın kaydedildiği dosyayı yükleyin

# Giriş verilerini ölçeklendirme
scaled_input = scaler.transform(input_df)

# Ölçeklendirilmiş veri ile tahmin yapma
prediction = model.predict(scaled_input)

#Yapılan Testin Sonucu
if prediction[0] == 1:
    prediction_text = "Normal Kilo"
elif prediction[0] == 5:
    prediction_text = "Obez Seviye 1"
elif prediction[0] == 6:
    prediction_text = "Obez Seviye 2"
elif prediction[0] == 2:
    prediction_text = "Obezize Tip 1"
elif prediction[0] == 0:
    prediction_text = "Yetersiz Kilo"
elif prediction[0] == 3:
    prediction_text = "Obezize Tip 2"
elif prediction[0] == 4:
    prediction_text = "Obezize Tip 3"

if st.button("**Tahmin Yap**"):
    with st.expander("# **Tahmin Sonucu**"):
        st.success(f"Tahmin Sonucu: {prediction_text}")




#Kenar Çubuğu Github Repostory Yönlendirme
with st.sidebar:
    st.markdown("## **Repository'miz**:")
    st.markdown("Kaynak kodu ve daha fazla bilgi için Repositroy'mize bakabilirsiniz")
    st.link_button("GitHub", "https://github.com/YazoTECHClone/obezite-tahmin--stdsa-1")
    st.markdown("## **Biz Kimiz**")
    st.markdown("Ben Yağız Gülbe. Bu Projenin Yapılma Sebebi İstanbul Data Seince Academy 3. projesi.")