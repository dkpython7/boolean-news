# boolean-news
QHACKS 2025

**Inspiration

When brainstorming a creative AI project to address a common issue, we were struck by the prevalence of misinformation in today’s world. From sensationalized news on platforms like TikTok to misleading articles circulating online, fake news is produced and shared at an alarming rate. Recognizing how easily people can fall for and spread such information, we were inspired to develop a simple yet powerful tool. Our goal was to empower users to evaluate the credibility of articles quickly and effectively, equipping them with the means to combat fake news and promote informed decision-making.

**What it does

Boolean-News is a simple yet powerful tool designed to help users analyze the credibility of news articles. Users can paste any article into the platform and instantly receive a classification of whether the news is True or False, alongside a confidence score represented as a percentage. This confidence score allows users to gauge how certain the AI is in its prediction, with higher percentages reflecting greater certainty. To provide further insights, Boolean-News also analyzes the article for bias using polarity and subjectivity scores. Polarity measures the sentiment of the text, ranging from -1 (negative) to 1 (positive), helping users understand the tone of the article. Subjectivity evaluates how opinion-based the article is, ranging from 0 (completely objective) to 1 (highly subjective), enabling users to distinguish between factual reporting and personal opinions. Together, these metrics empower users to critically assess the tone and bias of the content they’re consuming. If a user disagrees with the AI’s classification, they can submit feedback directly within the platform. This feedback is stored in a database, helping refine and improve the system over time.

**How we built it

To create Boolean-News, we began by sourcing and preprocessing a large dataset of fake and real news articles. Using TF-IDF Vectorization, we analyzed word frequencies and patterns, enabling our AI model to identify common traits in fake news, such as sensational language or repetitive phrases. We trained and evaluated three machine learning models—Logistic Regression, Random Forest, and XGBoost—selecting the most accurate model with a 96% success rate. The backend was developed using Flask and also process bias analysis, and feedback collection. For additional insights, we implemented TextBlob, which provides polarity and subjectivity scores to detect tone and bias in articles. Feedback from users is stored in a SQLite database, creating a system that can learn and improve over time. To ensure a user-friendly experience, we designed the interface in Figma, which is now being developed using HTML and CSS. This combination of technologies provides a seamless way for users to analyze articles and gain valuable insights into their credibility.

**Challenges we ran into

There were a lot of new frameworks we learned about when tackling this project allowing us to gain valuable experience. Although it was time consuming, learning scikit-learn and learning to train machine learning models including logistic regression, random forest, and XG boost was exciting because we learned to train AI models from scratch. Our AI model was initially very inaccurate with only 50% accuracy rate and coming up with ways to increase its accuracy was a very tedious and frustrating process as we had to research different techniques to manipulate the data and train the AI to make it as accurate as possible but it payed off in the end when it reached a 96 percent accuracy. Additionally, no one had experience with SQLite or any other database engines for that matter so learning from zero knowledge how SQLite works and how it can be used in our program to store user feedback was challenging.

**Accomplishments that we're proud of

We’re proud of successfully training a machine learning model to achieve 96% accuracy in detecting fake news, a significant improvement from our initial 50% accuracy. Another major accomplishment was integrating multiple features, such as bias detection and feedback storage, into a cohesive system. For many of us, this was our first time working with SQLite, and building a fully functional feedback loop was a rewarding challenge.

**What we learned

This project taught us how to train machine learning models using tools like scikit-learn, explore text processing with TF-IDF Vectorization, and implement sentiment analysis. We gained valuable experience integrating a database using SQLite. We also gained more hands-on experience working with html/css to create a user-friendly interface.

**What’s Next for Boolean-News

The next steps for Boolean-News includes integrating the ability to process images, allowing users to upload screenshots of articles or social media posts for analysis. Additionally, we aim to introduce PDF scanning, enabling users to upload entire documents for misinformation detection. For users who encounter fake news, the system will suggest other credible articles covering the same topic to promote informed decision-making.
