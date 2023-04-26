import streamlit as st
import pickle

st.sidebar.title("Loan Eligibility Prediction")
text = '''
Loan Eligibility Prediction based on gradient boosting classifier.

'''
st.sidebar.write(text)
x = False

gen=["Male","Female"]
edu = ["Graduate", "Not Graduate"]
m=["Yes", "No"]
sel=["Yes", "No"]
credit=["Yes", "No"]
pro=["Urban","Semiurban","Rural"]
dep=["0","1","2","3+"]
 
def predict(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):
    model = pickle.load(open('model.pkl', 'rb'))
    if Credit_History=='Yes':
        Credit_History=1
    else:
        Credit_History=0
    data = [ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History]

    Gender_array = [0]*len(gen)
    Married_array = [0]*len(m)
    Dependents_array = [0]*len(dep)
    Education_array = [0]*len(edu)
    Self_Employed_array = [0]*len(sel)
    Property_Area_array = [0]*len(pro)
    

    Gender_array[gen.index(Gender)] = 1
    Married_array[m.index(Married)] = 1
    Dependents_array[dep.index(Dependents)] = 1
    Education_array[edu.index(Education)] = 1
    Self_Employed_array[sel.index(Self_Employed)] = 1
    Property_Area_array[pro.index(Property_Area)] = 1
    

    data.extend(Gender_array)
    data.extend(Married_array)
    data.extend(Dependents_array)
    data.extend(Education_array)
    data.extend(Self_Employed_array)
    data.extend(Property_Area_array)
    

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
    Gender = col2.selectbox("Gender",gen, key="Gender")
    Married = col1.selectbox("Marriage Status",m, key="Married")
    Education = col2.selectbox("Education",edu,key="Education")
    Self_Employed = col1.selectbox("Self Employeed",sel,key="Self_Employed")
    ApplicantIncome = col2.number_input("Applicant Income (in ₹)", value=0, step=1, key="ApplicantIncome", min_value=0)
    CoapplicantIncome = col1.number_input("Co-Applicant Income (in ₹)", value=0, step=1, key="CoapplicantIncome", min_value=0)
    Dependents = col2.selectbox("Dependents",dep, key="Dependents",)
    LoanAmount = col1.number_input("Loan Amount (in ₹)", value=0, step=1, key="LoanAmount", min_value=0)
    Loan_Amount_Term = col2.number_input("Loan Amount Term (in months)", value=0, step=1, key="Loan_Amount_Term", min_value=0)
    Credit_History = col1.selectbox("Credit History",credit,key="Credit_History")
    Property_Area = col2.selectbox("Collateral Property Area",pro,key="Property_Area")



    _,cent,_ = st.columns([3,1,3])
    submitted = cent.form_submit_button("Submit")

    if submitted:
        prediction = predict(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)
        x = True

