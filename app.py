import streamlit as st
import pickle

st.sidebar.title("Loan Eligibility Prediction")
text = '''
Loan Eligibility Prediction uses Random Forest Classifier to predict whether a person is eligible for a loan or not.
It uses the principle of Responsible AI and keeps the predictions transparent to the user. Responsible AI is the practice of designing, developing, and deploying AI with good intention to empower employees and businesses, and fairly impact customers and society—allowing companies to engender trust and scale AI with confidence.
If the user is not eligible for a loan, the AI will tell you why.
Many banks have not been able to provide transparency into the process of their loan eligibility prediction systems, which can lead to some awkward conversations between clients and bank employees. Our app will help banks give a more appropriate answer to why an application was rejected, so that people are able to learn from mistakes and submit better applications next time.
'''
st.sidebar.write(text)
x = False
 
def predict(gender,married,dependents,education,SE,income,income2,LA,LAT,CH,PA):
    model = pickle.load(open('model.pkl', 'rb'))
    if married=='No':
        married=0
    else:
        married=1
    if education=='Not Graduate':
        education=0
    else:
        education=1
    if SE=='Yes':
        SE=1
    else:
        SE=0
    if CH=='Yes':
        CH=1
    else:
        CH=0
    data = [gender,married,dependents,education,SE,income,income2,LA,LAT,CH,PA]
    ans = model.predict([data])
    return ans[0]

def parsePrediction(prediction):
    if prediction==0:
        st.balloons()
        st.header("Congratulations! You are Eligible for the loan.")
    else:
        st.header("Sorry! You are not eligible for the loan.")

with st.form("input form"):
    col1, col2 = st.columns(2)
    name = col1.text_input("Enter Applicant's Name",key="name")
    gender = col2.selectbox("Gender", ["Male", "Female"], key="gender")
    married = col1.selectbox("Marriage Status", ["Yes", "No"], key="married")
    education = col2.selectbox("Education",["Graduate", "Not Graduate"],key="education")
    SE = col1.selectbox("Self Employeed",["Yes", "No"],key="SE")
    income = col2.number_input("Applicant Income (in ₹)", value=0, step=1, key="income", min_value=0)
    income2 = col1.number_input("Co-Applicant Income (in ₹)", value=0, step=1, key="income2", min_value=0)
    dependents = col2.number_input("Dependents", value=0, step=1, key="dependents", min_value=0)
    LA = col1.number_input("Loan Amount (in ₹)", value=0, step=1, key="LA", min_value=0)
    LAT = col2.number_input("Loan Amount Term (in months)", value=0, step=1, key="LAT", min_value=0)
    CH = col1.selectbox("Credit History",["Yes", "No"],key="CH")
    PA = col2.selectbox("Collateral Property Area",["Urban", "Semi-urban","Rural"],key="PA")



    _,cent,_ = st.columns([3,1,3])
    submitted = cent.form_submit_button("Submit")

    if submitted:
        prediction = predict(gender,married,dependents,education,SE,income,income2,LA,LAT,CH,PA)
        x = True

def getInsight():
    if age<=30:
        st.write("People with age less than 30 are 3% less likely to be eligible for the loan.")

    if exp<=4:
        st.write("People with less than 5 years of experience are 4% less likely to be eligible for the loan.")
    elif exp<16:
        st.write("People with less than 16 years of experience are 2% less likely to be eligible for the loan.")
    
    if mat=='Single':
        st.write("People who are married are 3% more likely to be eligible for the loan.")

    if house=='Rented':
        st.write("People who own a house are 3% more likely to be eligible for the loan.")

    if car=='No':
        st.write("People who own a car are 2% more likely to be eligible for the loan.")
    
    if cJY<=2:
        st.write("People who have less than 3 years of experience in current job are 4% less likely to be eligible for the loan.")
    if cJY<5:
        st.write("People who have less than 5 years of experience in current job are 2% less likely to be eligible for the loan.")

    if cHY<=11:
        st.write("People who have less than 12 years of time in current home are 2% less likely to be eligible for the loan.")

if x:
    parsePrediction(prediction)
    if prediction==1:
        with st.expander("Want to know more?"):
            getInsight()
    x = False
