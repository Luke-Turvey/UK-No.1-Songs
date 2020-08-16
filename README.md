# UK-No.1-Songs

This repository includes all the code needed to create the visualisation in the png file which shows the song duration of No. 1 songs throughout time.

# Data collection
First I needed to scrape the data off https://www.officialcharts.com/chart-news/all-the-number-1-singles__7931/ in order to get time series data for every number 1 song.
I did this using BeautifulSoup and UrllibReq and exported to numberones.csv. Then I used the spotify playlist linked in the article to get the song durations for each song in my data (I did this by hand) and then used a python program to convert my written durations into seconds (e.g. 1.50 -> 110).

# Data Visualisation
I used the ggplot2, and ggthemes packages in R to create the visualisation. The code visualisation.r loads in the csv file as a datframe, mutates the date column DATE into a date type and then plots date against song duration to create the visualisation.
