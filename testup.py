import streamlit as st

# Title of the app
st.title("Data Science for Chemical Engineering Test 2")

# Instructor and Date Information
st.write(f"**Instructor: Prof. Okolie**")
st.write(f"**Date: {st.date_input('Select Today\'s Date')}**")

# Exam Question Instructions
st.write("""
### Instructions:
- This is an open-book exam.
- You are required to download the dataset and perform exploratory data analysis (EDA) using Python.
- Your analysis should include data cleaning, visualization, and preparing the dataset for machine learning tasks in the future.
- Ensure you comment on your code.
- The test will last for 60 minutes.
- Once completed, submit a link to your GitHub repository with your code and findings on Moodle.

### Question:
You are provided with a dataset on **Dry Reforming of Methane**. Dry reforming of methane (DRM) is an important process used to convert methane (CH₄) and carbon dioxide (CO₂) into synthesis gas (syngas), which is a mixture of hydrogen (H₂) and carbon monoxide (CO).


This process is particularly important because it utilizes two greenhouse gases, methane and carbon dioxide, and converts them into valuable chemical products.

### Dataset:
Download the dataset provided below, which includes various parameters affecting the DRM process, such as catalyst type, methane conversion, and syngas ratio. Use this dataset to answer the following:

1. Perform data inspection and identify any missing or inconsistent values.
2. Handle any missing data using appropriate techniques (e.g., fill missing values or remove incomplete rows).
3. Apply data transformation techniques, such as normalization or encoding categorical variables, to prepare the data for machine learning tasks.
4. Generate summary statistics (mean, median, standard deviation, etc.) for the dataset.
5. Create visualizations (scatter plots, histograms, box plots) to identify trends and relationships between variables.
6. Analyze the correlations between features and target variables (CH₄ Conversion, CO₂ Conversion, and Syngas Ratio).

### Dataset Column Descriptions:
1. **Catalyst**: The catalyst material used to accelerate the reaction. Different catalysts can have varying effects on conversion efficiency.
   
2. **Ratio of CH₄ in Feed**: The proportion of methane in the feedstock, affecting the conversion efficiency.
   
3. **Reaction Temperature**: The temperature at which the reaction takes place. High temperatures are needed for the DRM reaction to proceed effectively.
   
4. **Ni Loading**: The nickel content in the catalyst. Nickel is often used in DRM because of its catalytic properties.

5. **Reaction Time**: The time for which the reaction is allowed to occur. Longer reaction times can enhance the conversion of CH₄ and CO₂.
   
6. **Pore Size**: The size of the pores in the catalyst, which influences the accessibility of reactants to active sites.
   
7. **Pore Volume**: The total pore volume of the catalyst, influencing the surface area available for the reaction.

8. **Surface Area**: The surface area of the catalyst. A larger surface area provides more active sites for the reaction to occur.
   
9. **H₂-TPR Peak Temperature**: The temperature at which the maximum reduction of the catalyst occurs. This indicates the reducibility of the catalyst.

10. **Ni Particle Size**: The size of the nickel particles in the catalyst. Smaller particles generally result in higher surface area.

11. **Ni Dispersion**: The extent to which nickel is dispersed across the catalyst surface. Higher dispersion typically correlates with better catalytic activity.

12. **Modifier Electronegativity**: Electronegativity of modifying agents added to the catalyst. Modifiers can impact catalytic activity and selectivity.

13. **GHSV (Gas Hourly Space Velocity)**: The volumetric flow rate of gas through the reactor relative to the volume of the catalyst. Higher GHSV means a faster flow rate, which can affect the reaction kinetics.

14. **CH₄ Conversion (Target)**: The percentage of methane converted into products.

15. **CO₂ Conversion (Target)**: The percentage of carbon dioxide converted during the reaction.

16. **Syngas Ratio (Target)**: The ratio of hydrogen to carbon monoxide in the syngas produced. This is important for syngas applications such as fuel synthesis.

Once completed, submit your Python code and a report with your findings to your GitHub repository and share the link on Moodle.
""")

# Load the Excel file
file_path = 'Test2 dataset.xlsx'  # Ensure this file is in the same directory as your Python script

with open(file_path, "rb") as file:
    btn = st.download_button(
        label="Download Dataset (Test2 dataset)",
        data=file,
        file_name="Test2_dataset.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# Footer
st.write("""
Compiled by Jude Okolie PhD
""")
