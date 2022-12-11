# predictions

## When are you due?
This is the question you hear over and over and over again as soon as you tell people you're pregnant. The due date is a very valuable tool during pregnancy but how accurate is it?
Almost as soon as you find out your pregnant you are given a "due date". This date is calculated by adding 280 days to the last menstural period, or with a dating ultrasound in the three months of pregnancy. 
This due date is then used to determine when you receive vaccinations, pre natal tests, and track your pregnancy moving forward. It's also used to help potential parents determine when they should expect to take leave from work and plan for baby's arrival.
However, this due "date" is more of a prediction and is often joked as "the least likely day the baby will be born". 
Along with when will baby be born everyone you talk to friends, family, neighbors (strangers on the street, or the cashier at the grocery store) has some sort of method for "predicting" different features for when the baby is born.
From [Chinese gender calendars](https://www.whattoexpect.com/pregnancy/preparing-for-baby/chinese-gender-predictor-chart/), to the way you carry pregnancy weight, whether or not you have heartburn or acne etc. 
While there is scientific evidence to back any of these guessing tactics or [old wives tales](https://www.pampers.com/en-us/pregnancy/pregnancy-announcement/article/old-wives-tales-gender-prediction) it is fun to speculate.

## Data Collection
Being a data person I decided to put everyone's "predictions" to the test. Throughout my pregnancy whenever someone made a "guess" as to some feature or aspect of the birth I wrote it down and stored it in an excel document.
At my baby shower I passed out prediction pages for guests to enter their guesses on and stored the data in the excel sheet. 
For this project I wanted to do descriptive statistics on the prediction data I gathered to see what trends existied. 

## Steps and Approaches
### Preprocessing/clean the dataset: 
- Check for missing values
- Consistency- Initially there were some issues with data consistancy because of the gradual and informal collection process of the data itself. These were corrected in the final cleaning stages of this project.
### Identify variables to be used. 
 -I struggled a bit with which values to use, I wanted to use specific time but cleaning the time data was difficult so I defaulted to AM or PM instead. 
### Formating Visulizations
 -I wanted to ensure that different categories of data, such as hair and eye color had correctly corresponding colors to go with the categories. 
### Analysis
-I used descriptive statistics to observe the data
-The scatter plots use color defrienation to observce differences in guesses based on relationship as well as isolating the user input guess from others.


### Create Streamlit App
Streamlit app was created in order to share results with friends, fmaily, coworkers easily and from one space.
I also wanted to allow others to enter their guesses, without altering the original dateset. This required that I create a form to accept new user input and add it to the existing data.
I also created a brief section on my husband and myself to include physical feature attributes to make guessing of those parameters a bit easier.

### Create Visulizations in Python
I used Jupiter Notebook to test out my python before adding it to the python file for the streamlit app. I worked with a small dataset to begin with and then layered in the data later.
I created a new data frame within python to append the orignial data and the new user input to make it more interactive.
I used matplotlib to create the visulizations. 
