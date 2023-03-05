# Preparation
[wirfuervielfalt.de](https://www.wirfuervielfalt.de/) uses [Matomo](https://matomo.org/) which is the most common free and open source web analytics application to track online visits to a website and display reports on these visits for analysis.

* [How do I make the Matomo Analytics RAW data available to my data warehouse?](https://matomo.org/faq/how-to/faq_24536/)
* [How do I export the Raw data from Matomo (users, actions, clicks)?](https://matomo.org/faq/how-to/faq_24574/)
* [What data does Matomo track?](https://matomo.org/faq/general/faq_18254/)
* [Configure Privacy Settings in Matomo](https://matomo.org/faq/general/configure-privacy-settings-in-matomo/)
* [Anonymize previously tracked raw data](https://matomo.org/faq/how-to/faq_35661/)

## About the wirfuervielfalt.de Website

* more than 100 projects
* more than 2 years

## Matomo Demo
https://demo.matomo.cloud/

### Matomo Demo Data
https://github.com/dssg-berlin/web-tracking-analytics/releases/tag/preparation

Note that Matomo encodes csv files using utf-16le encoding. https://github.com/matomo-org/matomo/issues/5729

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
* Where are the visitors referred from: direct/search engine/email(i.e. newsletter)/social media? How do visitors find the website? Which sources are underrepresented and could attract additional visitors?
* What are the search engine keywords that lead visitors to the website? https://matomo.org/faq/search-engine-keywords-performance/faq_23862/

### Content
* What are the top landing pages? What are the keywords of the top landing pages? 
* What are the top keywords by location? Are there other locations with similar interest as indicated by keywords?
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
* Suggested conversion: click on betterplace donation link, "projekt anbieten", referring to a listed project, 

## Data Scheme
* https://developer.matomo.org/guides/database-schema

## Analytics Tools
* https://github.com/retentioneering/retentioneering-tools

## Terms
* Landing Page, Exit Page
* Funnel
* BounceRate
* Event
* 1st vs 3rd Party Cookies
* Pages per Session, Average Session Duration
* A/B Testing
* Metric, Dimension, Goals/Conversion
* CTR click-through rate
* Fingerprinting
* GDPR CCPA LGPD
* Segmentation

Metrics are measurable, numerical data like time spent on site or pages viewed. Conversions are data on how many users have completed a desired action on your site, for example buying a product or signing up for a newsletter. Dimensions are groups of user data that can be used to generate a report, such as their device type or location.

https://learndigital.withgoogle.com/digitalunlocked/course/digital-marketing

https://learndigital.withgoogle.com/assets/media/pdf/10-web-analytics-glossary.pdf

## Web Tracking Solutions
* Matomo
* Google Analytics
* Adobe Analytics
* Plausible
* Fathom
* Hotjar
* WP-Statistics
* Microsoft Clarity

## Education

* https://analytics.google.com/analytics/academy/
* https://experienceleague.adobe.com/

## Recommendations

* Include Project Counter
* Correct typos:

'''<img alt="twitter" title="twitter" src="/img/linkedin.svg" class="twitter">
<a href="https://www.linkedin.com/company/54338698/" title="linkedin" class="xsbbLabel"><img alt="twitter" title="twitter" src="/img/linkedinhell.svg" class="icons"></a>
<a href="https://www.betterplace.org/de/projects/91900?utm_campaign=user_share&amp;utm_medium=ppp_sticky&amp;utm_source=Link" title="spenden" class="xsbbLabel"><img alt="youtube" title="spenden" src="/img/SpendenButtonDesktop.svg" class="spendeicon"></a>
<div data-v-7f0f8cef="" data-v-44845210="" class="vel-img-title">Vorstellung einer Präsenatation vom Diplom-Pädagogen Ants Kiel</div>'''