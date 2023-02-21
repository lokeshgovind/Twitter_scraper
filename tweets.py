# -*- coding: utf-8 -*-
import streamlit as st
import snscrape.modules.twitter as sntwitter
import pandas as pd
import pymongo as pm
import json as js
import time
from datetime import datetime
from datetime import timedelta
from streamlit_lottie import st_lottie
import requests

now=datetime.now()
current_date=now.strftime("%d/%m/%Y")
client=pm.MongoClient("mongodb://localhost:27017")
#giving name to our webpage
st.set_page_config(page_title="Twitter_scraper",layout="wide")

#To include animation in our webpage
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coding=load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_hdy0htc2.json")

#Title and header to display in streamlit
st.title(' Data Science Project')
st.write("##") 
st.header('Scraping Of  :blue[ Twitter_Data]')
with st.expander("About App"):
    st.write("This web application helps you to Search-Display-Download the twitter_data ")
left_column,right_column=st.columns(2)    
 
#dividing the page into two columns for including animation
with left_column:    
    username=st.text_input('Enter the username/hashtag needs to be searched:')
    start_date=st.date_input("Enter the start date here:")
    end_date=st.date_input("Enter the End date here:")


    #To get the datas exactly upto the start_date 
    previous_date=start_date-timedelta(days=1)

    query="{} since:{} until:{}".format(username,previous_date,end_date)

    #Number of tweets the user want
    number_of_tweets=st.number_input('Enter the number of tweets:',min_value=1,max_value=1000,step=1)

    tweets=[]

    if st.button("submit"): 
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
            if i>(number_of_tweets-1):
                break
            tweets.append([tweet.date,tweet.id,tweet.url,tweet.content,tweet.user.username,tweet.replyCount,tweet.retweetCount,tweet.lang,tweet.source,tweet.likeCount])
        df=pd.DataFrame(tweets,columns=['Date','Id','Url','Text','Username','Reply_count','Retweet_count','Language','Source','Likecount'])
       
        st.dataframe(df)
    #The displayed table could be downloaded by the user as 'csv' and 'json' file:   
        st.download_button('DOWNDLOAD_as_CSV',data=df.to_csv(),file_name="{}.csv".format(username),mime='csv')
        st.download_button("DOWNLOAD_as_JSON",data=df.to_json(),file_name="{}.json".format(username))

    #To load the searched data into mongodb as a document:
      
        if st.button('Upload File') is not None:
            my_db=client["twitter_data"]
            my_collection=my_db["scrapped_twitter_data"]
            
            data_dictionary=df.to_dict("records")
            about_tweet={
                "Scraped Word": username,
                "Scraped Date":current_date,
                "Scraped Data":data_dictionary
                }        
            my_collection.insert_one(about_tweet)
            progress_bar=st.progress(0)
            for perc_completed in range(100):
                time.sleep(0.05)
                progress_bar.progress(perc_completed+1,"Click 'upload File' to upload.....")

#right column we place the animation      
with right_column:
    st_lottie(lottie_coding,height=300,key="twitter")
     

