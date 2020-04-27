# Python-Scripting-v1.0
This only who want to love to do scripting from many several website to retrive data as like website

Motivation
On July 21, 2017, the New York Times updated an opinion article called Trump's Lies, detailing every public lie the President has told since taking office. Because this is a newspaper, the information was (of course) published as a block of text:

this is the some text of this website

JAN. 21 “I wasn't a fan of Iraq. I didn't want to go into Iraq.” (He was for an invasion before he was against it.)  JAN. 21 “A reporter for Time magazine — and I have been on their cover 14 or 15 times. I think we have the all-time record in the history of Time magazine.” (Trump was on the cover 11 times and Nixon appeared 55 times.)  JAN. 23 “Between 3 million and 5 million illegal votes caused me to lose the popular vote.” (There's no evidence of illegal voting.)  JAN. 25 “Now, the audience was the biggest ever. But this crowd was massive. Look how far back it goes. This crowd was massive.” (Official aerial photos show Obama's 2009 inauguration was much more heavily attended.)  JAN. 25 “Take a look at the Pew reports (which show voter fraud.)” (The report never mentioned voter fraud.)  JAN. 25 “You had millions of people that now aren't insured anymore.” (The real number is less than 1 million, according to the Urban Institute.)  JAN. 25 “So, look, when President Obama was there two weeks ago making a speech, very nice speech. Two people were shot and killed during his speech. You can't have that.” (There were no gun homicide victims in Chicago that day.)  JAN. 26 “We've taken in tens of thousands of people. We know nothing about them. They can say they vet them. They didn't vet them. They have no papers. How can you vet somebody when you don't know anything about them and you have no papers? How do you vet them? You can't.” (Vetting lasts up to two years.)  JAN. 26 “I cut off hundreds of millions of dollars off one particular plane, hundreds of millions of dollars in a short period of time. It wasn't like I spent, like, weeks, hours, less than hours, and many, many hundreds of millions of dollars. And the plane's going to be better.” (Most of the cuts were already planned.)  JAN. 28 “The coverage about me in the @nytimes and the @washingtonpost has been so false and angry that the Times actually apologized to its dwindling subscribers and readers.” (It never apologized.)  JAN. 29 “The Cuban-Americans, I got 84 percent of that vote.” (There is no support for this.)  JAN. 30 “Only 109 people out of 325,000 were detained and held for questioning. Big problems at airports were caused by Delta computer outage.” (At least 746 people were detained and processed, and the Delta outage happened two days later.)  FEB. 3 “Professional anarchists, thugs and paid protesters are proving the point of the millions of people who voted to MAKE AMERICA GREAT AGAIN!” (There is no evidence of paid protesters.)  FEB. 4 “After being forced to apologize for its bad and inaccurate coverage of me after winning the election, the FAKE NEWS @nytimes is still lost!” (It never apologized.)  FEB. 5 “We had 109 people out of hundreds of thousands of travelers and all we did was vet those people very, very carefully.” (About 60,000 people were affected.)  FEB. 6 “I have already saved more than $700 million when I got involved in the negotiation on the F-35.” (Much of the price drop was projected before Trump took office.)  FEB. 6 “It's gotten to a point where it is not even being reported. And in many cases, the very, very dishonest press doesn't want to report it.” (Terrorism has been reported on, often in detail.)  FEB. 6 “The failing @nytimes was forced to apologize to its subscribers for the poor reporting it did on my election win. Now they are worse!” (It didn't apologize.)  FEB. 6 “And the previous administration allowed it to happen because we shouldn't have been in Iraq, but we shouldn't have gotten out the way we got out. It created a vacuum, ISIS was formed.” (The group’s origins date to 2004.)  FEB. 7 “And yet the murder rate in our country is the highest it’s been in 47 years, right? Did you know that? Forty-seven years.” (It was higher in the 1980s and '90s.)  FEB. 7 “I saved more than $600 million. I got involved in negotiation on a fighter jet, the F-35.” (The Defense Department projected this price drop before Trump took office.)


File name of this Scriping in
# TrumpLiesScriptingWebSite.py

# 16-17 lines of code Here

import requests
import pandas as pd
from bs4 import BeautifulSoup

link = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
soup = BeautifulSoup(link.text, 'html.parser')
results = soup.find_all('span', attrs={'class': 'short-desc'})

records = []
for result in results:
    date = result.find('strong').text[0:-1] + ', 2017'
    lie = result.contents[1][1:-2]
    explanation = result.find('a').text[1:-1]
    url = result.find('a')['href']
    records.append((date, lie, explanation, url))

df = pd.DataFrame(records, columns=['Date', 'Lie', 'Explanation', 'URL'])
print(df)
#df['date'] = pd.to_datetime(df['date'])
df.to_csv('Result.csv', index=True, encoding='utf-8')

