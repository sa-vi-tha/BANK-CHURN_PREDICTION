import streamlit as st
import pickle
from PIL import Image
import webbrowser

# Set the page configuration (optional)
st.set_page_config(
    page_title="Welcome to the Customer Churn Dashboard",
    layout="centered",
    initial_sidebar_state="auto",
)



# Add a sidebar for navigation
st.sidebar.title("Pages")
page = st.sidebar.radio("Select a page", ["Welcome", "Predict Churn","Additional Insights"])

if page == "Welcome":

    page_element = """
        <style>
        [data-testid="stAppViewContainer"]{
          background-image: url("https://tse4.mm.bing.net/th?id=OIP.2qoj175C2JAxvPXXnti_ZQHaG9&pid=Api&P=0&h=180");
          background-size: cover;
        }
        </style>
        """

    st.markdown(page_element, unsafe_allow_html=True)



    # Add a welcome title and a subtitle
    st.title("Welcome to the Customer Churn Dashboard")
    st.subheader("**Analyze customer data and predict churn efficiently**")

    # Display an introductory image or logo
    image = Image.open("bank.jpeg")  # Ensure you have a relevant image file
    st.image(image, caption="Analyze your customer base with data-driven insights", use_column_width=True)
    st.write("**The primary objective is to predict whether a customer will continue their association with the bank or choose their account,commonly known as churn.**")
    # Add some introductory text
    st.write("""
    ### Overview:
    This dashboard is designed to provide insightful analysis on customer churn based on various attributes such as credit score, age, balance, and more. 
    You'll be able to interact with data visualizations, view key metrics, and understand the factors that affect churn rates.

    #### Key Features:
    - Data Visualization: Gain insights from interactive charts.
    - Predictive Analysis: Use models to forecast customer churn.
    - User-Friendly Interface: Navigate easily through sections like Data Overview, Analysis, and Reports.
    """)
    st.sidebar.success("select a page")


elif page == "Predict Churn":

    page_element = """
     <style>
     [data-testid="stAppViewContainer"]{
       background-image: url("https://tse2.mm.bing.net/th?id=OIP.f9FAz8bNP4ZTEIJf0WojbgAAAA&pid=Api&P=0&h=180");
       background-size: cover;
     }
     </style>
     """

    st.markdown(page_element, unsafe_allow_html=True)


    def main():
        st.title("BANK CHURN PREDICTION")
        st.write("**Enter customer details below to predict whether they will exit or stay.**")
        img = Image.open('blogWhat_s-a-good-Customer-Churn-Rate-scaled.jpeg')
        st.image(img, width=650)
        CreditScore = st.text_input("**Credit Score**", "")
        Age = st.text_input("**Age**", "")
        Tenure = st.text_input("**Tenure**", "")
        Balance = st.text_input("***Balance***", "")
        NumOfProducts = st.text_input("**Num Of Products**", "")
        HasCrCard = st.radio("**Has a credit card**", ["Yes", "No"])
        if HasCrCard == "Yes":
            HasCrCard = 1
        else:
            HasCrCard = 0
        IsActiveMember = st.radio("**Is Active Member**", ["Active", "Inactive"])
        if IsActiveMember == "Active":
            IsActiveMember = 1
        else:
            IsActiveMember = 0
        EstimatedSalary = st.text_input("**Estimated Salary**", "")
        Geography_Germany = st.radio("**From Germany**", ["Yes", "No"])
        if Geography_Germany == "Yes":
            Geography_Germany = 1
        else:
            Geography_Germany = 0
        Geography_Spain = st.radio("**From Spain**", ["Yes", "No"])
        if Geography_Spain == "Yes":
            Geography_Spain = 1
        else:
            Geography_Spain = 0
        Gender_Male = st.radio("**Gender**", ["Male", "Female"])
        if Gender_Male == "Male":
            Gender_Male = 1
        else:
            Gender_Male = 0
        features = [CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary,
                    Geography_Germany, Geography_Spain, Gender_Male]
        scaler = pickle.load(open('scaler.sav', 'rb'))
        model = pickle.load(open('model.sav', 'rb'))
        pred = st.button("**PREDICT**")
        if pred:
            result = model.predict(scaler.transform([features]))
            if result == 0:
                st.write("**Account Activating**")
                st.success("***✅ Good news: Low Risk of Churn!***", icon="🎉")
                st.write("**Thank you for using the churn prediction service!**")
            else:
                st.write("**Account will exited soon**")
                st.warning("**⚠️ Attention: High Risk of Churn!**", icon="⚠️")
                st.write("**Thank you for using the churn prediction service!**")

    main()





elif page == "Additional Insights":


    page_element = """
    <style>
    [data-testid="stAppViewContainer"]{
      background-image: url("https://tse2.mm.bing.net/th?id=OIP.ZDqXmWlbY7qzZ245UWz3ZQHaEL&pid=Api&P=0&h=180");
      background-size: cover;
    }
    </style>
    """

    st.markdown(page_element, unsafe_allow_html=True)





    # Thank you message
    st.write("**We appreciate your feedback!**")
    st.write("**If you have any questions or comments,mail:comment@gmail.com, feel free to reach out to us.**")
    st.write("**Open Google Colab**")

    # Display instructions
    st.write("**Click the button below to open the Google Colab project.**")

    # Add a button to open the Google Colab link
    if st.button('Open Google Colab'):
        colab_url = "https://colab.research.google.com/drive/1IQrkeU81rnKEhifsAtpdJruHYrNjuzO8#scrollTo=9xspnQ2gdZSc"  # Replace with your actual Colab URL
        webbrowser.open_new_tab('colab_url')
        st.write("**Opening Google Colab...**")




