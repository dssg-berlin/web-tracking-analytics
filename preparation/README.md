# Preparation
[wirfuervielfalt.de](https://www.wirfuervielfalt.de/) uses [Matomo](https://matomo.org/) which is the most common free and open source web analytics application to track online visits to a website and display reports on these visits for analysis.

* [How do I make the Matomo Analytics RAW data available to my data warehouse?](https://matomo.org/faq/how-to/faq_24536/)
* [How do I export the Raw data from Matomo (users, actions, clicks)?](https://matomo.org/faq/how-to/faq_24574/)

## Matomo Demo
https://demo.matomo.cloud/

### Matomo Heatmap Demo
![image](https://user-images.githubusercontent.com/8211411/222895767-1a8f8bb4-4037-4a78-bed6-e625fcbf3ac5.png)

## Data Challenges
https://teachtofishdigital.com/web-analytics-questions/

* What is the purpose of the website. The purpose defines the conversion event.
* Which message does the website send its visitors.

### Visitors
* What are the most common devices and browsers used that should be the focus for UI optimization and accessibility efforts?
* Are there patterns of visitor return/retention or duration of stay with page content or other features?
* Do sources or webpages correlate with visit duration?
* How many visits to the site? How many unique visitors?

### Sources
* Where are the visitors referred from: direct/search engine/email(i.e. newsletter)/social media? How do visitors find the website?
* What are the search engine keywords that lead visitors to the website? https://matomo.org/faq/search-engine-keywords-performance/faq_23862/

### Content
* What are the top landing pages? What are the keywords of the top landing pages?
* Is there a change of top landing pages over time? Does the interest shift?
* Which pages have a high exit rate?
* What pages are most visited?
* What pages trigger conversion action?
* What are the loading speeds?

### Actions/Conversions
* Is the recent tracking sufficient/fitting the purpose?
* What is the conversion rate (conversions/visitors)?
* What are the most common conversion paths?
* What is the average number of visits required before a visitor converts?

## Data Scheme
* https://developer.matomo.org/guides/database-schema

## Analytics Tools
* https://github.com/retentioneering/retentioneering-tools

## Terms
* Landing Page
* Funnel
* Event
* Conversion
* Cookies
* A/B Testing

## Web Tracking Solutions
* Matomo
* Google Analytics
* Adobe Analytics
* Plausible
* Fathom
* Hotjar
* WP-Statistics

### Matomo Demo Data
https://github.com/dssg-berlin/web-tracking-analytics/releases/tag/preparation

Note that Matomo encodes csv files using utf-16le encoding. https://github.com/matomo-org/matomo/issues/5729

