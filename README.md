## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace. 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa; indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|





## Business Requirements
A good friend, John, has received an inheritance from his deceased mother. John has requested me to help him analyze the value of his properties to make business decisions. The properties are in Ames, Iowa. 

Although my friend has an excellent understanding of property prices in his own state and residential area, he fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. He also wants to spot what attributes are more important to possibly remodel them and get a better price for the house.  What makes a house desirable and valuable where he comes from might not be the same in Ames, Iowa. He found a public dataset with house prices for Ames, Iowa, and will provide me with that information. 

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that. This will help him identify potential improvements in order to increase the price. 
* 2 - The client is interested in predicting the house sale price from her 4 inherited houses, and any other house in Ames, Iowa.



## Hypothesis and how to validate?

* 1 - We suspect houses with better overall quality will have a higher sales price.
    * A Correlation study can help in this using PPS, Pearson and Spearman methods would help the investigation.
* 2 - We suspect houses with larger living area will have a higher sales price.
    * * A Correlation study can help in this using PPS, Pearson and Spearman methods would help the investigation.
* 3 - We suspect that houses with more recent remodelations will have a higher sales price. 
    * A Correlation study can help in this using PPS, Pearson and Spearman methods would help the investigation.



## The rationale to map the business requirements to the Data Visualisations and ML tasks
* **Business Requirement 1:** Data Visualization and Correlation study
	* We will inspect the data related to the customer base.
	* We will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to Churn.
	* We will plot the main variables against Churn to visualize insights.

* **Business Requirement 2:** Regression, Data Analysis
	* We want to predict the value of a house. We want to build a regression model to predict the target variable SalePrice.
	* We want to make plots to visualize the train and test sets predictions vs the actual.
	* We want to run regression evaluation to demonstrate the R2 Score and Mean Absolute Error.



## ML Business Case
### Predict Sale Price
#### Regression Model 
* We want an ML model to predict the sale price of a house. A target variable is a serial number. We consider a **regression model**, which is supervised and uni-dimensional.
* Our ideal outcome is to provide John with reliable insight into what sale price he should expect for his inherited houses or identify what improvements he could implement to increase the price. 
* The model success metrics are
  - At least 0.8 for R2 score, on train and test set
* The ML model is considered a failure if:
   - After 6 months of usage, the model's predictions are 30% off more than 25% of the time. 
* The model output should be a constant value for the **`sale price`**.


## Dashboard Design (Streamlit App User Interface)

### Page 1 
### Quick project summary
* Quick project summary
	* Project Terms & Jargon
	* Describe Project Dataset
	* State Business Requirements
### Page 2
### Sale Price Study
* Before the analysis, we knew we wanted this page to answer business requirement 1, but we couldn't know in advance which plots would need to be displayed.


* After data analysis, we agreed with stakeholders that the page will: 
	* State business requirement 1
	* Checkbox: data inspection on house attributes (display the number of rows and columns in the data, and display the first ten rows of the data)
  
	* Display the most correlated variables to Sale Price and the conclusions
  
	* Checkbox: Individual plots showing the Sale Price levels for each correlated variable 
  
	* Checkbox: Parallel plot using Sale Price and correlated variables
  

  

### Page 3
### House Price Predictor
* State business requirement 2
* Set of widgets inputs, which relates to the prospect profile. Each set of inputs is related to a given ML task to predict prospect Sale Price.
* Run predictive analysis" button that serves the prospect data to our ML pipelines, and predicts if the prospect will increase Sale Price or not, if so, when. For the Sale Price predictions, the page will inform the associated probability for Sale Price level.




### Page 4
### Project Hypothesis and Validation
* Before the analysis, we knew we wanted this page to describe each project hypothesis, the conclusions, and how we validated each. After the data analysis, we can report that:

* 1 - We suspect houses with better overall quality will have a higher sales price.
    * Correct. `Overal Quality` is the feature with the highest correlation with the target variable `Sale Price`.

* 2 - We suspect houses with larger living area will have a higher sales price.
    * Correct. `Ground Living Area` is the feature with the second highest correlation with the target variable `Sale Price`.
    
* 3 - We suspect that houses with more recent remodelations will have a higher sales price. 
    * Correct. Eventhough the  `Remodelation Year` has a low correlation with `Sale Price`, there is a strong correlation between `Remodelation Year` and `Overal Quality` which is the feature with strongest correlation with `Sale Price`


### Page 5
### Predict Sale Price
* Considerations and conclusions after the pipeline is trained
* Present ML pipeline steps
* Feature importance
* Pipeline performance



---


## Unfixed Bugs
* I struggled when running the Jupyter Notebooks since a lot of cells would come back with the older version and this took plenty of time.
* I had a few dependency issues so I had to uninstall and install again a few applications. 
* I got a 503 server error when trying to open the app in Heroku. 

## Deployment
### Heroku

* The App live link is: https://housing-predictions-app.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* In case you would like to thank the people that provided support through this project.

