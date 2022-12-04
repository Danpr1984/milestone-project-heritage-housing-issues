import streamlit as st

def page_hypothesis_and_validation_body():

    st.write("### Project Hypothesis and Validation")
	
    st.info(
    f"**1.** We suspect houses with better overall quality will have "
    f"a higher `sales price`: **Correct**. \n "
    f"- `Overal Quality` is the feature with the highest correlation "
    f"with the target variable `Sale Price`. \n\n"

    f"**2.** We suspect houses with larger living area will have a higher sales price."
    f"**Correct**. \n "
    f"`Ground Living Area` is the feature with the second highest"
    f"correlation with the target variable `Sale Price`.\n\n"

    f"**3.**We suspect that houses with more recent remodelations"
    f"`will have a higher sales price.  "
    f"**Correct**.\n"
    f"- Eventhough the  `Remodelation Year` has a low correlation with `Sale Price`,"
    f"there is a strong correlation between `Remodelation Year` and `Overal Quality`"
    f"which is the feature with strongest correlation with `Sale Price`. n\n"
    )