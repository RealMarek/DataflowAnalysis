# DataflowAnalysis
In this repository we are trying to find out if its possible to predict the pageviews of a Wikipediapage just by analysing all the pageviews of incoming and outgoing links from other wikipedia pages.
## Fundamental questions
- Can you predict pageviews with Page Flow Analysis?
- Does it make a difference if you predict values of one page or of a category?
- Which model is better at predicting?
## Basic information about Wikipages
- 60% of all visitors are leaving the page after the first visit (means 40% percent pageflow)
- The average duration of a visit is approx. 4 minutes
- On average, 3 Wikipedia pages are viewed per visit
>Source: https://www.similarweb.com/top-websites/
## Which data do we collect?
- We select 100 random articles of the Wikipedia Category "New York"
- For each article we select the views of 3 months and the views over 3 months of the 30 top links on the page
- For some other articles we collect daily data for a full year

## Which Models do we train?
- Decision Tree
- Random Forest
- Multiple Linear Regression