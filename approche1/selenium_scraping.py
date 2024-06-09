import pandas as pd
# from pathlib import Path

from bs4_links_reader import bs4_file_creater
from  selenium_links_reader import file_creater_using_selenium
from cleaning import  all_scores
print("helo")


import os 

URL_ID = []
URL = []

POSITIVE_SCORE = []
NEGATIVE_SCORE = []  
POLARITY_SCORE = []
SUBJECTIVITY_SCORE = []
AVG_SENTENCE_LENGTH = []
PERCENTAGE_OF_COMPLEX_WORDS = []
FOG_INDEX = []
AVG_NUMBER_OF_WORDS_PER_SENTENCE = []
COMPLEX_WORD_COUNT = []
WORD_COUNT = []
SYLLABLE_PER_WORD = []
PERSONAL_PRONOUNS = []
AVG_WORD_LENGTH = []
# def connection():
if __name__ == "__main__":
    # blackCoffer_project\Files\Input.xlsx
    file_read = pd.read_excel("../Files/Input.xlsx",nrows=5)

    os.chdir('../Files/')
    print(os.getcwd())
   
    
    links_and_id  = file_read[['URL_ID','URL']]
    
    
    url = tuple(zip(links_and_id['URL_ID'],links_and_id['URL']))
    
    
    for i in url:
        text_value = bs4_file_creater(i)
        
        if text_value == 'skip':
            URL_ID.append(i[0])
            URL.append(i[1])
            POSITIVE_SCORE.append(None)
            SUBJECTIVITY_SCORE.append(None)
            NEGATIVE_SCORE.append(None)
            POLARITY_SCORE.append(None)
            AVG_SENTENCE_LENGTH.append(None)
            PERCENTAGE_OF_COMPLEX_WORDS.append(None)
            FOG_INDEX.append(None)
            AVG_NUMBER_OF_WORDS_PER_SENTENCE.append(None)
            COMPLEX_WORD_COUNT.append(None)
            WORD_COUNT.append(None)
            SYLLABLE_PER_WORD.append(None)
            PERSONAL_PRONOUNS.append(None)
            AVG_WORD_LENGTH.append(None)

            continue
        with open(f'../text_files/{i[0]}.txt',"+w" ,encoding="utf-8") as file:
            file.write(text_value)
        with open(f'../text_files/{i[0]}.txt','r',encoding="utf-8") as file:
            lines = list(file.readlines())
            text = ' '.join(lines)
            scores = all_scores(text)
            URL_ID.append(i[0])
            URL.append(i[1])
            POSITIVE_SCORE.append(scores['sentimental_scores']['postive_score'] )
            SUBJECTIVITY_SCORE.append(scores['sentimental_scores']['subjectivity_score'])
            NEGATIVE_SCORE.append(scores['sentimental_scores']['negative_score'])
            POLARITY_SCORE.append(scores['sentimental_scores']['poloarity_score'],)
            AVG_SENTENCE_LENGTH.append(scores['average_sent_length'])
            PERCENTAGE_OF_COMPLEX_WORDS.append(scores['readability_test'][1])
            FOG_INDEX.append(scores['readability_test'][0])
            AVG_NUMBER_OF_WORDS_PER_SENTENCE.append(scores['average_sent_length'])
            COMPLEX_WORD_COUNT.append(scores['Count_complex_word'])
            WORD_COUNT.append(scores['word_count'])
            SYLLABLE_PER_WORD.append(scores['Syllable_count'])
            PERSONAL_PRONOUNS.append(scores['personal_pernoun']['total'])
            AVG_WORD_LENGTH.append(scores['average_word_length'])

            
            

            
            
    
    data = {'URL ID':URL_ID,
            'URL':URL,
        'POSITIVE SCORE': POSITIVE_SCORE,
        'NEGATIVE SCORE': NEGATIVE_SCORE,
        'POLARITY SCORE': POLARITY_SCORE,
        'SUBJECTIVITY SCORE':SUBJECTIVITY_SCORE,
        'AVG SENTENCE LENGTH':AVG_SENTENCE_LENGTH,
        'PERCENTAGE OF COMPLEX WORDS':PERCENTAGE_OF_COMPLEX_WORDS,
        'FOG INDEX':FOG_INDEX,
        'AVG NUMBER OF WORDS PER SENTENCE':AVG_NUMBER_OF_WORDS_PER_SENTENCE,
        'COMPLEX WORD COUNT':COMPLEX_WORD_COUNT,
        
        'WORD COUNT':WORD_COUNT,
        'SYLLABLE PER WORD':SYLLABLE_PER_WORD,
        'PERSONAL PRONOUNS':PERSONAL_PRONOUNS,
        
        
        'AVG WORD LENGTH':AVG_WORD_LENGTH}

    df_new = pd.DataFrame(data)
    print(df_new)

    with pd.ExcelWriter('../files/Result_Data_Structures.xlsx', engine='openpyxl', mode='w') as writer:
    # Write the new DataFrame to a new sheet
        df_new.to_excel(writer, index=False)
            




    

