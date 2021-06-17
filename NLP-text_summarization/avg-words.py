import sys
import pandas as pd


#path with predictions
path_predictions=sys.argv[1]

#we load the csv file
df=pd.read_csv(path_predictions, usecols=["input_text","gold_summary","predicted_summary"], engine="python", encoding='utf-8',error_bad_lines=False, delimiter='|')
predicted_summaries=df['predicted_summary'].tolist() #list with the generated summaries
total_words = 0
num_summaries = 0
num_sentences = 1

# Calculate the number of total_words
for summary in predicted_summaries:
    if type(summary) is str:
        words = summary.split()

        # Calculate num of sentences
        for word in words:
            if ("." in word):
                num_sentences +=1

        partial_avg = len(words)/num_sentences
        total_words += partial_avg

        num_sentences = 1
        num_summaries += 1

#avg of words
avg_words = total_words / num_summaries

#Writte results on a .txt
with open("avg.txt", "a") as f: 
    f.write(str(path_predictions)+": "+str(avg_words)+"\n") 