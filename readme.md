# DataflowAnalysis
In this repository we are trying to find out if its possible to predict the pageviews of a Wikipediapage just by analysing all the pageviews of incoming and outgoing links from other wikipedia pages.
## Fundamental questions
- Can you predict pageviews with Page Flow Analysis?
- Which influence does categories have on the analysis?
- Is this technique better at predicting trending pages or better at predicting pages with constant pageviews?
- Which links are more helpful at prediction? The incoming or the outgoing links?
## Basic information about Wikipages
- 60% of all visitors are leaving the page after the first visit (means 40% percent pageflow)
- The average duration of a visit is approx. 4 minutes
- On average, 3 Wikipedia pages are viewed per visit
>Source: https://www.similarweb.com/top-websites/
## Which data do we collect?
- Daily data for a full year
- Trending categories
    - Celebrities who died last year
    - Political events
    - New Films and Series
- Constant categories
    - Animals
    - Historical events and wars
    - Cities
- 100 articles for each category
- Every article will be reduced to the top 30 links
- Collect data off all incoming and outgoing links in the top 30 of a page

![Analysis Overview](/readmeFiles/AnalysisOverview.png "Analysis Overview")