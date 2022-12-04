import streamlit as st
from app_pages.multipages import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_sale_price_study import page_sale_price_study_body
from app_pages.page_predict import page_predict_body
from app_pages.page_hypothesis_and_validation import page_hypothesis_and_validation_body
from app_pages.page_ml_predict import page_ml_predict_body

app = MultiPage(app_name= "Heritage Housing") # Create an instance of the app 

# Add your app pages here using .add_page()
app.app_page("Project Summary", page_summary_body)
app.app_page("House Sale Price Study", page_sale_price_study_body)
app.app_page("Predict House Value", page_predict_body)
app.app_page("Project Hypothesis and Validation", page_hypothesis_and_validation_body)
app.app_page("ML: Predict House Value", page_ml_predict_body)

app.run() # Run the  app