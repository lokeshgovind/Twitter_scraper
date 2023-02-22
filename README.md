# Twitter_scraper
## Scraping the User-chosen Data from Twitter
----
### ABOUT:
   The code is used to scrape the data on a range of date using python and displayed using streamlit
***
#### Task List:
Import some needed modules
- [x] sreamlit
- [x] snscrape
- [x] pandas
- [x] json

 ---
### **How it works** ?
1. To scrape data use **snscrape**. [reference](https://medium.com/dataseries/how-to-scrape-millions-of-tweets-using-snscrape-195ee3594721)
2. create a empty list to add the data 
3. get the data and convert it into a table using **pandas**
      * it has a class called _DataFrame_
      * `code`.
```
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
            if i>(number_of_tweets-1):
                break
            tweets.append([tweet.date,tweet.id,tweet.url,tweet.content,tweet.user.username,tweet.replyCount,tweet.retweetCount,tweet.lang,tweet.source,tweet.likeCount])
df=pd.DataFrame(tweets,columns=['Date','Id','Url','Text','Username','Reply_count','Retweet_count','Language','Source','Likecount'])

```
4. use **streamlit** to create a *webpage*
5. add the option for users to download the file as
     * csv
     - json
6. #### **Inserting the data into database**
     + first we have to conver the table into dictionary format
     + and add the dictionry file as a document into the collection **scrapped_twitter_data** of the database **twitter_data**
     * `code`
     ```
      my_db=client["twitter_data"]
            my_collection=my_db["scrapped_twitter_data"]                        
            now=datetime.now()
            current_date=now.strftime("%d/%m/%Y")
            data_dictionary=df.to_dict("records")
            about_tweet={
                "Scraped Word": username,
                "Scraped Date":current_date,
                "Scraped Data":data_dictionary
                }        
            my_collection.insert_one(about_tweet)
```
