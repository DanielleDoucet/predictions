import datetime as dt
import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
#from PIL import Image
#from wordcloud import STOPWORDS, ImageColorGenerator, WordCloud

st.set_page_config(layout="wide")

#read the ece
df1=pd.read_excel('Predictions.xlsx', index_col=0,
              dtype={'name': str, 'relationship': str,'date': str, 'Delivery Time':str, 'time': str, 'weight':float, 'length':float, 'hair':str,'eye':str,'sex':str,'eye_color2':str})  

# convert the 'Date' column to datetime format
df1['date']= pd.to_datetime(df1['date'])


st.title ('Baby Prediction')
st.write ('When I had my baby shower I asked friends, family, and co-workers to give their predictions on when my baby would be born, how much it would weigh, how long it would be and other features. I have taken their predictions and graphed the results. Once baby arrives we can compare the results to see how close the guesses were to the real deal!')
st.write('To participate enter your predictions for the baby on the form below. Your predictions are combined with the previous guesses on the second tab. On the third tab see the breakdown of all the guesses and compare yours to the total on the scatter plot!')
st.write ('Below is some preliminary information on Mom and Dad for guesses pertaining to hair and eye color. Happy guessing!')
st.subheader ('Parent Information')
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("danielle.jpg")
with col2:
    st.header("Mom")
    st.write ("Hair: Brown")
    st.write("Eyes: Hazel")
    st.write("Height: 5ft 4in")
with col3:
    st.image("joe.jpg")
with col4:
    st.header("Dad")
    st.write ("Hair: Black")
    st.write("Eyes: Hazel")
    st.write("Height: 5ft 9in")

#form
form = st.form("My Prediction")
name=form.text_input(label='Your Name')
with form:
    relationship=st.selectbox('How do you know the parents?',['','Friend','Family','Other'])
    date=st.date_input('When do you think the baby will be born? Due date is 12/26/2022', dt.date(2022,12,26))
    time=st.selectbox('What time will baby be born?',('','AM','PM'))
    weight=st.slider('How much will baby weigh in ounces? Avg birthweight is 112 oz',80,160,120,1)
    length=st.slider('How long will baby be in inches? Avg length at birth is 19.5 in',10.0,30.0,20.0,0.25)
    hair=st.selectbox('What color hair do you think baby will have?',('','Blonde','Brown','Red','Black','Bald'))
    eye=st.selectbox('What color eyes will baby have?',('','Blue','Brown','Hazel','Green','Gray'))
    sex=st.selectbox('What do you think the baby will be?', ['','Female', 'Male'])
    #submitted1 = st.form_submit_button('Submit')
    st.form_submit_button('Submit')


data2={'name':[name],'relationship':[relationship],'date':[date],'time':[time],'weight':[weight],'length':[length],'hair':[hair],'eye':[eye],'sex':[sex]}
df2=pd.DataFrame(data2)
df2['date']= pd.to_datetime(df2['date'])


dfcombo=df1.append(df2, ignore_index = True)
dfcombo['relationship_count']=dfcombo.groupby('relationship')['relationship'].transform('count')
dfcombo['hair_count']=dfcombo.groupby('hair')['hair'].transform('count')
dfcombo['eye_count']=dfcombo.groupby('eye')['eye'].transform('count')
dfcombo['sex_count']=dfcombo.groupby('sex')['sex'].transform('count')
dfcombo['time_count']=dfcombo.groupby('time')['time'].transform('count')

#make tabs
tab1, tab2, tab3= st.tabs(['Your Guess','All Guesses','Analysis'])

with tab1:
    st.subheader("I predict that baby will be:")
    #st.markdown("""
#<style>
#.big-font {
#    font-size:20px !important;
#}
#</style>
#""", unsafe_allow_html=True)

#st.markdown('<p class="big-font">born on {delivery_Date}</p>', unsafe_allow_html=True)
    st.write(sex,', born on', date, "in the ",time, "with", hair,"hair and ",eye,"eyes, weighing", weight,"oz and be ",length,"inches long when born.")
  

  
with tab2:
    st.subheader('All Guesses')
    st.caption('CLICK on a column header to sort by that column.')
    st.caption('resize columns by DRAGGING and DROPPING column header borders.')
    st.caption('SEARCH through data by CLICKING a table, using hotkeys (⌘ Cmd + F or Ctrl + F) to bring up the SEARCH bar, and using the search bar to filter data.')
    #dfcombo
    st.dataframe(dfcombo)
with tab3:
    st.subheader('Relationship')
    df_friend = dfcombo[dfcombo['relationship'] == 'Friend']
    df_family = dfcombo[dfcombo['relationship'] == 'Family']
    df_other = dfcombo[dfcombo['relationship'] == 'Other']

    fig, ax = plt.subplots()
    ax.bar(df_friend.relationship,df_friend.relationship_count, color='teal')
    ax.bar(df_family.relationship,df_family.relationship_count, color='midnightblue')
    ax.bar(df_other.relationship,df_other.relationship_count, color='gold')


    ax.set_title('Count of Relationship')
    ax.set_xlabel('Relationship of Guesser', fontsize=12)
    ax.set_ylabel('Counts', fontsize=12)
    st.pyplot(plt)
    plt.clf()

#eye color
    st.subheader('Eye Color')
    df_hazel = dfcombo[dfcombo['eye'] == 'Hazel']
    df_blue = dfcombo[dfcombo['eye'] == 'Blue']
    df_brown = dfcombo[dfcombo['eye'] == 'Brown']
    df_green = dfcombo[dfcombo['eye'] == 'Green']
    df_gray = dfcombo[dfcombo['eye'] == 'Gray']

    fig, ax = plt.subplots()
    ax.bar(df_hazel.eye,df_hazel.eye_count, color='olive')
    ax.bar(df_brown.eye,df_brown.eye_count, color='saddlebrown')
    ax.bar(df_blue.eye,df_blue.eye_count, color='dodgerblue')
    ax.bar(df_green.eye,df_green.eye_count, color='seagreen')
    ax.bar(df_gray.eye,df_gray.eye_count, color='slategray')

    ax.set_title('Count of Eye Guesses')
    ax.set_xlabel('Eye Color', fontsize=12)
    ax.set_ylabel('Counts', fontsize=12)
    st.pyplot(plt)
    plt.clf()
   
    #hair color
    st.subheader('Hair Color')
    df_blonde = dfcombo[dfcombo['hair'] == 'Blonde']
    df_brown = dfcombo[dfcombo['hair'] == 'Brown']
    df_black = dfcombo[dfcombo['hair'] == 'Black']
    df_red = dfcombo[dfcombo['hair'] == 'Red']
    df_bald = dfcombo[dfcombo['hair'] == 'Bald']

    fig, ax = plt.subplots()
    ax.bar(df_blonde.hair,df_blonde.hair_count, color='gold')
    ax.bar(df_brown.hair,df_brown.hair_count, color='saddlebrown')
    ax.bar(df_red.hair,df_red.hair_count, color='orangered')
    ax.bar(df_black.hair,df_black.hair_count, color='black')
    ax.bar(df_bald.hair,df_bald.hair_count, color='sandybrown')

    #plt.bar(dfcombo.hair, dfcombo.hair_count, color=['midnightblue','gray','teal'])
    ax.set_title('Count of Hair Guesses')
    ax.set_xlabel('Hair', fontsize=12)
    ax.set_ylabel('Counts', fontsize=12)
    st.pyplot(plt)
    plt.clf()

#sex guesses
    st.subheader('He or She, what will it be?')
    st.write('There are tons of old wives tales that are sure to tell the sex of the baby before they are born, but DNA testing and ultrasounds are really the only way to know for sure before the big day.')
    df_fem = dfcombo[dfcombo['sex'] == 'Female']
    df_male = dfcombo[dfcombo['sex'] == 'Male']

    fig, ax = plt.subplots()
    ax.bar(df_fem.sex,df_fem.sex_count, color='salmon')
    ax.bar(df_male.sex,df_male.sex_count, color='midnightblue')

    #ax.bar(dfcombo.sex,dfcombo.sex_count, marker='*',c='red', s=df2.length)
    #plt.bar(dfcombo.sex, dfcombo.sex_count, color=['midnightblue','gray','teal'])
    ax.set_title('Count of Sex Guesses')
    ax.set_xlabel('Time', fontsize=12)
    ax.set_ylabel('Counts', fontsize=12)
    #plt.figure(figsize=(20,20)) 
    st.pyplot(plt)
    plt.clf()

    #time of day
    st.subheader('Time of Day')
    st.write('It really is a toss up as to what time of day a baby will be born. In 2013 the CDC examined birth certificate data and found that the highest percentage of births occured during the morning (between 8 AM and noon) and < 3% of babies were born during each hour from midnight to 6:59 a.m. This data however includes data from c-sections (which are more likely to occur during the day, especially if scheduled)')
    df_am = dfcombo[dfcombo['time'] == 'AM']
    df_pm = dfcombo[dfcombo['time'] == 'PM']

    fig, ax = plt.subplots()
    #plt.xticks(fontsize = 1)
    #plt.yticks(fontsize = 1)
    #fig, ax = plt.subplots(2,2, figsize=(3,5))
    ax.bar(df_am.time,df_am.time_count, color='orange')
    ax.bar(df_pm.time,df_pm.time_count, color='navy')
    #ax.set_ylim([0,200])
    ax.set_title('Count of Time of Day Guesses', fontsize=12)
    ax.set_xlabel('Time of Day', fontsize=12)
    ax.set_ylabel('Counts', fontsize=12)
    st.pyplot(plt)
    plt.clf()

    
   #weight and date
    st.subheader('Are Birthweight and Birthdate connected?')
    st.write("According to the CDC, based on 3.8 million births in the US in 2017: about 10% were born <37 weeks (preterm). 26% born between 37 to 38 weeks; 57% between 39 to 40 weeks; 6% in week 41; and <1% at 42 weeks or more")
    st.write('The lack of any kind of correlation in the scatterplot below demonstrates that individuals are not taking into account that increased gestational length (later due dates) equal heavier babies.')
    # create subsets of dataframes for each relationship (e.g. friend, family, other)
    df_friend = df1[df1['relationship'] == 'Friend']
    df_fam = df1[df1['relationship'] == 'Family']
    df_other = df1[df1['relationship'] == 'Other']

    # color map for each category
    fig, ax = plt.subplots()
    #plt.figure(figsize=(25),(15))
    labels = ['Friend', 'Family', 'Other','You']
    relationship=[x for x in dfcombo.relationship]
    #colors = {'Friend':'teal', 'Family':'midnightblue','Other':'gold'}
    #color_ls = [colors[i] for i in relationship]
    ax.scatter(df_friend.date,df_friend.weight, marker='*', c='teal', s=df_friend.length)
    ax.scatter(df_fam.date,df_fam.weight, marker='*', c='midnightblue', s=df_fam.length)
    ax.scatter(df_other.date,df_other.weight, marker='*', c='gold', s=df_other.length)
    ax.scatter(df2.date,df2.weight, marker='*',c='red', s=df2.length)

    plt.xticks(fontsize=5)
    ax.set_title('Date Estimate and Weight by Relationship')
    ax.set_xlabel('Date Estimate', fontsize=12)
    ax.set_ylabel('Weight Estimate in Oz', fontsize=12)
    #tooltip_name = 'name'
    #x = dfcombo[date]
    #y = df[weight]
    #tt = df[tooltip_name].values
    #plt.legend(dfcombo.relationship, loc="best")
    #plt.legend(labels,loc='best', fontsize=10)
    #ax.legend([friend, family, other], ['friend', 'family', 'other'])
    #patches = ax.get_legend_handles_labels()
    #ax.legend(patches, labels, loc="best")
    ax.legend(labels, loc="best")
    #plt.subplots_adjust(bottom=0.15)
    #plt.subplots_adjust(left=0.15)
    #plt.figure(figsize=(5,5))
    st.pyplot(plt)
    plt.clf()

    #weight and length

    #calculate the correlation
#    corr=round((dfcombo[length]).corr(dfcombo[weight]),2)
#    st.write(f"The correlation between length and weight is {corr}")
    st.subheader('Relationship of Length and Weight')
    #st.write('While the gestational age may not be taken into account when guessing weight and length there ')
    # create subsets of dataframes for each relationship (e.g. friend, family, other)
    df_friend = df1[df1['relationship'] == 'Friend']
    df_fam = df1[df1['relationship'] == 'Family']
    df_other = df1[df1['relationship'] == 'Other']

    # color map for each category
    fig, ax = plt.subplots()
    #plt.figure(figsize=(25),(15))
    labels = ['Friend', 'Family', 'Other','You']
    relationship=[x for x in dfcombo.relationship]
    #colors = {'Friend':'teal', 'Family':'midnightblue','Other':'gold'}
    #color_ls = [colors[i] for i in relationship]
    ax.scatter(df_friend.length,df_friend.weight, marker='*', c='teal', s=df_friend.length)
    ax.scatter(df_fam.length,df_fam.weight, marker='*', c='midnightblue', s=df_fam.length)
    ax.scatter(df_other.length,df_other.weight, marker='*', c='gold', s=df_other.length)
    ax.scatter(df2.length,df2.weight, marker='*',c='red', s=df2.length)

    plt.xticks(fontsize=5)
    ax.set_title('Weight and Length guesses by Relationship')
    ax.set_xlabel('Length Estimate in In', fontsize=12)
    ax.set_ylabel('Weight Estimate in Oz', fontsize=12)
    ax.legend(labels, loc="upper right")
    #ax.legend(bbox_to_anchor=(1,1), loc="upper left")
    #plt.subplots_adjust(bottom=0.15)
    #plt.subplots_adjust(left=0.15)
    #plt.figure(figsize=(5,5))
    st.pyplot(plt)
    plt.clf()
#with tab4:
    #st.metric(label="Height", value=df2.height, delta="17.5")

    



    