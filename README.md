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
      * `code`
        using System.IO.Compression;

#pragma warning disable 414, 3021

namespace MyApplication
{
    [Obsolete("...")]
    class Program : IInterface
    {
        public static List<int> JustDoIt(int count)
        {
            Console.WriteLine($"Hello {Name}!");
            return new List<int>(new int[] { 1, 2, 3 })
        }
    }
}
4. use **steamlit** to create a *webpage
5. add the option for users to download the file as
     * csv
     - json
6. #### **Inserting the data into database**
     + first we have to conver the table into dictionary format
     + Sub-lists are made by indenting 2 spaces:
