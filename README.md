# synthetic-material-and-performance-generator
![alt text](https://github.com/mantek-singh/synthetic-material-and-performance-generator/blob/main/assets/brembo_logo.png?raw=true)

We participated in the [Brembo hackathon](https://brembo-hackathon.bemyapp.com/), where the task was to use Generative AI to create new compounds, forecast testing results and create the framework for predicting the effectiveness and characteristics of a new Brembo brake product using historical friction test data. 


<h2>Problem Statement</h2>

Using friction test data provided by Brembo, use Generative AI to create new compounds, forecast testing results
and create the framework for predicting the effectiveness and characteristics of a new Brembo brake product.
The data provided will include a list of compounds previously used and tested by Brembo, as well as their outcomes.
Solutions must be based on Generative AI, applied to provide a model able to propose new recipes that increase the
number of candidate compounds, ensuring feasibility and good performances.

<h2>Design Overview</h2>

The design for our solution is representated by the image below.

![alt text](https://github.com/mantek-singh/synthetic-material-and-performance-generator/blob/main/assets/brembo_design.png?raw=true)

Essentially, we had 3 basic components
* Material Selection Module: Responsible for generating new recipes. This outputs a bunch of new friction materials and their material compositions.
* Data Generator Module: Given a synthetic material and past historical performance data of various compounds, generate synthetic performance data for this material.
* Data Validator: Identify how good/bad the output of the data generator is. This module uses trends seen in the provided historical data (for example: Pressure and mu
  are inversely related to each other over time, deceleration seems to follow a linear pattern while temperature increase curve seems more exponential in nature) to rate how
  good or bad the synthetic performance data is. This can be used to give human feedback to the model to improve the system performance.

<h2>Code Walkthrough</h2>

The code has been added in the [notebooks](https://github.com/mantek-singh/synthetic-material-and-performance-generator/blob/main/Brembo-C1-Presentation.pdf) folder.

The files are:
* Brembo_Start.ipynb: Initial EDA
* Brembo_C1_DataGenerator.ipynb: Logic for finetuning and prompt tuning the data generator
* Brembo_C1_UseDataGenerator.ipynb: Logic for making api calls to the fine tuned model
* Brembo_C1_Merge_CSVs.ipynb: Utility to merge the generated performance data files.


<h2>Conclusion</h2>

We WON!! 🥳 🍺 
![image](https://github.com/user-attachments/assets/c8a9db20-e999-43be-a76b-0b0aa22a3248)

