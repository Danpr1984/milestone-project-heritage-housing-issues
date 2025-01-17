import streamlit as st

def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargons**\n"
        f"* **SalePrice** is the price a house sold for and is our target variable.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset represents housing records from Ames, Iowa; "
        f"indicating house profile (`Floor Area, Basement, Garage, Kitchen, "
        f"Lot, Porch, Wood Deck, Year Built`) and its respective sale price for houses "
        f"built between 1872 and 2010.\n"
        f"* There are many abbreviated terms used to describe features of the houses in "
        f"the data set. You can find the dataset with all the information"
        f"if you click **[HERE](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)**.\n\n"
        )
    
    
     # copied from README file - "Business Requirements" section
    st.success(
        f"#### The project has two business requirements:\n\n"
        f"**1.**  The client is interested in discovering how house attributes correlate with "
        f"the house Sale Price. Therefore, the client expects data visualizations "
        f"of the correlated variables against Sale Price to show that.\n\n"
        f"**2.** The client is interested to predict the house sales price from their 4 "
        f"inherited houses, and any other house in Ames, Iowa. "
        )

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"For additional information, please visit and **read** the "
        f"**[Project's README file](https://github.com/Danpr1984/milestone-project-heritage-housing-issues)**.")