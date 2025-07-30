#!/usr/bin/env python
# coding: utf-8

# ##  Reputation monitoring system
  

# **Code cell 1:** Set up programming environment to use code to send prompts to OpenAI's cloud-hosted service. 

# In[1]:


import openai
import os 

openai.api_key = os.getenv("OPENAI_API_KEY")

def llm_response(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role':'user','content':prompt}],
        temperature=0
    )
    return response.choices[0].message['content']


# **Code cell 2:** Create a list of reviews. 

# In[2]:


all_reviews = [
    'The mochi is excellent!',
    'Best soup dumplings I have ever eaten.',
    'Not worth the 3 month wait for a reservation.',
    'The colorful tablecloths made me smile!',
    'The pasta was cold.'
]

all_reviews


# **Code cell 3:** Classify the reviews as positive or negative. 

# In[3]:


all_sentiments = []
for review in all_reviews:
    prompt = f'''
        Classify the following review 
        as having either a positive or
        negative sentiment. State your answer
        as a single word, either "positive" or
        "negative":

        {review}
        '''
    response = llm_response(prompt)
    all_sentiments.append(response)

all_sentiments


# **Code cell 4**: Count the number of positive and negative reviews 

# In[4]:


num_positive = 0
num_negative = 0
for sentiment in all_sentiments:
    if sentiment == 'positive':
        num_positive += 1
    elif sentiment == 'negative':
        num_negative += 1
print(f"There are {num_positive} positive and {num_negative} negative reviews.")

