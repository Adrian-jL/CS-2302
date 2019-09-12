#Adrian Lopez, 09/01/19
#CS2302 - Data Structures
#Lab 1 option A (Reddit Comments)

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw


reddit = praw.Reddit(client_id='7XQb-7zTZKZNUQ',
                     client_secret='JaMx3kiCR8Ufu_MD_dN0pZoMhAw',
                     user_agent='AdrianCS21'
                     )


nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()


def get_text_negative_proba(text): 
   return sid.polarity_scores(text)['neg']


def get_text_neutral_proba(text):
   return sid.polarity_scores(text)['neu']


def get_text_positive_proba(text):
   return sid.polarity_scores(text)['pos']


def get_submission_comments(url):
    submission = reddit.submission(url=url)
    submission.comments.replace_more()

    return submission.comments

#Method takes in Comments, which holds the URL, and returns 3 lists, positive, negative, and neutral
def process_comments(comments, pos_list, neu_list, neg_list):

   #For loop to go through each comment in the list of comments and replies until end
   for comment in comments:
      text = comment.body

      pos_proba = get_text_positive_proba(text)
      neu_proba = get_text_neutral_proba(text)
      neg_proba = get_text_negative_proba(text)
      #positive comments
      if pos_proba != False:
         pos_list.append(pos_proba)
         #Removes the diplicates from list
         pos_list = list(dict.fromkeys(pos_list))

      #neutral comments
      if neu_proba != False:
         neu_list.append(neu_proba)
         neu_list = list(dict.fromkeys(neu_list))
      
      #negative comments
      if neg_proba != False:
         neg_list.append(neg_proba)
         neg_list = list(dict.fromkeys(neg_list))
      
      #Recursion returns the reply of the comment and reply of reply and so on
      process_comments(comment.replies, pos_list, neu_list, neg_list)
   return pos_list, neu_list, neg_list

def main():
   
   comments = get_submission_comments('https://www.reddit.com/r/washingtondc/comments/d2xdb5/love_the_improvements_wmata/')
   pos_list = []
   neu_list = []
   neg_list = []

   process_comments(comments, pos_list, neu_list, neg_list)

   pos_list, neu_list, neg_list = process_comments(comments, pos_list, neu_list, neg_list)
   print("//POS: ", pos_list, "//NEU: ", neu_list, "//NEG: ", neg_list)

main()
