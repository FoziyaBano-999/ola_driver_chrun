import streamlit as st
import pandas as pd
import joblib

begg = joblib.load("beging.joblib")
gbdtt = joblib.load("gbdt.joblib")
xgbt = joblib.load("xgbost.joblib")
stt = joblib.load("stack.joblib")

df = pd.read_csv("new_data.csv")

#  this is user info for model 

st.title("Ola Driver Churn Prediction System")
st.divider()

dateofjoining = st.date_input("Select your joining date:")
joining = pd.to_datetime(dateofjoining , format="mixed")

reportingdate = st.date_input("Select your reporting date:")

Reporting = pd.to_datetime(reportingdate , format="mixed")

Reporting_year = Reporting.year
Reporting_moth = Reporting.month
Reporting_day = Reporting.day

Dofj_year = joining.year
Dofj_moth = joining.month
Dofj_day = joining.day




Age = st.number_input("Enter your age :" , min_value=18 , max_value=100)
t_b_v = st.number_input("Enter your total business value")
income = st.number_input("Enter your monthly income:" , min_value=1000 , max_value=500000)


City1 = st.selectbox("Enter your city name:" ,[
    "Delhi",
    "Mumbai",
    "Kolkata",
    "Chennai",
    "Bengaluru",
    "Hyderabad",
    "Pune",
    "Jaipur",
    "Ahmedabad",
    "Lucknow",
    "Chandigarh",
    "Bhopal",
    "Indore",
    "Patna",
    "Surat",
    "Nagpur",
    "Coimbatore",
    "Visakhapatnam",
    "Vadodara",
    "Noida",
    "Gurugram",
    "Kanpur",
    "Ludhiana",
    "Agra",
    "Varanasi",
    "Ranchi",
    "Raipur",
    "Guwahati",
    "Mysuru"
]
)
def city_(c):
    if c == "Delhi":
        return 1
    elif c == "Mumbai":
        return 2
    elif c == "Kolkata":
        return 3
    elif c == "Chennai":
        return 4
    elif c == "Bengaluru":
        return 5
    elif c == "Hyderabad":
        return 6
    elif c == "Pune":
        return 7
    elif c == "Jaipur":
        return 8
    elif c == "Ahmedabad":
        return 9
    elif c == "Lucknow":
        return 10
    elif c == "Chandigarh":
        return 11
    elif c == "Bhopal":
        return 12
    elif c == "Indore":
        return 13
    elif c == "Patna":
        return 14
    elif c == "Surat":
        return 15
    elif c == "Nagpur":
        return 16
    elif c == "Coimbatore":
        return 17
    elif c == "Visakhapatnam":
        return 18
    elif c == "Vadodara":
        return 19
    elif c == "Noida":
        return 20
    elif c == "Gurugram":
        return 21
    elif c == "Kanpur":
        return 22
    elif c == "Ludhiana":
        return 23
    elif c == "Agra":
        return 24
    elif c == "Varanasi":
        return 25
    elif c == "Ranchi":
        return 26
    elif c == "Raipur":
        return 27
    elif c == "Guwahati":
        return 28
    elif c == "Mysuru":
        return 29
    else:
        return 0  # Unknown

    
City = city_(City1)


Grade = st.selectbox("Select your grade:" , df['Grade'].unique())
Education_Level1 = st.selectbox("Select your education level:" ,  ["10th pass" , "12th pass" , "Graduate" , "Post Graduate" ,"Engineer"])
def el(e):
    if e =="10th pass" :
        return 1
    elif e == "12th pass":
        return 2
    elif e == "Graduate":
        return 3
    elif e == "Post Graduate":
        return 4
    elif e == "Engineer":
        return 5

Education_Level = el(Education_Level1)


j_ds1 = st.selectbox("Select your joining designation:" , ["Taxi driver", "Auto-rickshaw driver", "Private car chauffeur", "Delivery driver", "Tourist cab driver"])
def jd(e):
    if e =="Taxi driver" :
        return 1
    elif e == "Auto-rickshaw driver":
        return 2
    elif e == "Private car chauffeur":
        return 3
    elif e == "Delivery driver":
        return 4
    elif e == "Tourist cab driver":
        return 5
J_ds = jd(j_ds1)

Gender1 = st.radio("Select your gender" , ["Male" , "Female"])
Gender = 0 if Gender1 == "Male" else 1

Increase_rating1 = st.radio("Has your rating increased recently?", ["Yes" , "No"])
inc_rating = 1 if Increase_rating1 == "Yes" else 0

Increase_income1 = st.radio("Has your income increased recently?", ["Yes" , "No"])
income_increase = 1 if Increase_income1 == "Yes" else 0


user_data = {
    "Age": Age,
    "Gender": Gender,
    "City": City,
    "Education_Level": Education_Level,
    "Income": income,
    "J_ds": J_ds,
    "Grade": Grade,
    "inc_rating": inc_rating,
    "t_b_v": t_b_v,
    "income_increase": income_increase,
    "Reporting_year": Reporting_year,
    "Reporting_moth": Reporting_moth,
    "Reporting_day": Reporting_day,
    "Dofj_year": Dofj_year,
    "Dofj_moth": Dofj_moth,
    "Dofj_day": Dofj_day
}


input_df = pd.DataFrame([user_data])


# ------------------ MODEL PREDICTION ------------------

st.title("Choose a model for prediction 🤖 ")
st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Bagging" , use_container_width=True):
        pred = begg.predict(input_df)
        if pred == 1:
            st.success(f"Driver has churned from the company")
        else:
            st.success("Driver has not churned from the company")
with col2:
    if st.button("GBDT" , use_container_width=True):
        pred = gbdtt.predict(input_df)
        if pred == 1:
            st.success(f"Driver has churned from the company")
        else:
            st.success("Driver has not churned from the company")

with col3:
    if st.button("XGBoost" , use_container_width=True):
        pred = xgbt.predict(input_df)
        if pred == 1:
            st.success(f"Driver has churned from the company")
        else:
            st.success("Driver has not churned from the company")

with col4:
    if st.button("Stacking" , use_container_width=True):
        pred = stt.predict(input_df)
        if pred == 1:
            st.success(f"Driver has churned from the company")
        else:
            st.success("Driver has not churned from the company")

