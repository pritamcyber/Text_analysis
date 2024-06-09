from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
import string
import re
import  os

import nltk 
import math
print(nltk.download('stopwords'))
# nltk.download('punkt')
# print(len(set(stopwords.words('english'))))

main_working_dir =str( os.getcwd())




def word_count(text):
    
    """
    We count the total cleaned words present in the text by 
           1. removing the stop words (using stopwords class of nltk package).
           2. removing any punctuations like ? ! , . from the word before counting.


    Returns:
        int: total numer of words after remove puncuatoin and stopwords 
    """
    stop_words = list(set(stopwords.words('english')))

    words = word_tokenize(text)
    
    
    cleaned_word = []
    for word in words:
        word  = word.translate(str.maketrans('','',string.punctuation))
        '''2. removing any punctuations like ? ! , . from the word before counting.'''
        
        
        word = word.lower()
        
        if word  and word not in stop_words :
            '''1. removing the stop words (using stopwords class of nltk package).'''
            cleaned_word.append(word)
        
    
    return len(cleaned_word)
            

# def Average_word_length(text):

#     sents = sent_tokenize(text)
#     words = word_tokenize(text)
#     sents_len = len(sents)
#     words_len =  len(words)

#     if sents_len == 0:
#         return 0
#     Average = int(words_len/sents_len)

#     return Average
    
    



def Average_word_length(text) ->int:
    '''
    This funtion gives you total number of  character
    Average Word Length is calculated by the formula:
    Sum of the total number of characters in each word/Total number of words
    '''
    # cleaning 
    text  =     re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()

    

    words= word_tokenize(text)
    
    if len(words)<= 0:
        return 0
        
    
    ch_len = sum( len(word) for word in words)
    

    av_length = math.floor(ch_len / len(words))

    return av_length
  
  
  
  
def count_syllables(word):
    
    word = word.lower().strip()
    vowels = "aeiou"
    syllable_count = 0

    if word.endswith("es") or word.endswith("ed"):
        
        word = word[:-2]

    if len(word) == 0:
        return 1

    if word[0] in vowels:
        syllable_count += 1

    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            syllable_count += 1

    if syllable_count == 0:
        syllable_count = 1

    return syllable_count  
def Complex_word_count(word:str)-> int:
    # this is main funciton to get syllable count  of a word 

    vowels = "aeiou"
    syllabls = 0 
    word  = word.lower()
    
    if  word   ==  '':
        return syllabls

    if word and  word[0] in vowels:
        syllabls += 1
    
    for i in range(1,len(word)):
        if  word[i] in vowels and word[i-1] not in vowels :
            syllabls +=1
            
            
    
    if word.endswith('ed') or  word.endswith('es')   :

        syllabls -=1
    
        
    if syllabls == 0:
        syllabls +=1

    
    return syllabls
  
def count_complex_word(text):
    
    
    '''This  function count to total complex word
        Complex words are words in the text that contain more than two syllables.
    '''
    
    words = word_tokenize(text)
    word = sum([1 for  word in  words if Complex_word_count(word) >2])
    return word 

def total_syllable_count(text):
    # This function gives you total number  of  syllable in text  
    words  =  word_tokenize(text)
    

    total_syllable_count = sum(Complex_word_count(word) for word in words if word.isalpha())
    
    return total_syllable_count

# This function conunt  the syllable in text and gives the sum of all syllable
def syllable_count_per_word(text):
    
    
    words = word_tokenize(text)
    
   
    syllable_counts = sum(Complex_word_count(word) for word in words)
    
    return syllable_counts
 
 
 




def personal_pernoun(text):

    words= word_tokenize(text)
    if len(words) == 0:
        return 0
    

    
    pr_pattern = r'(?!\.)\b(?:I|we|my|ours|us)\b(?!\.)'
    
    # Initialize a dictionary to store the counts of each pronoun
    pr_counts = {'i': 0, 'we': 0, 'my': 0, 'ours': 0, 'us': 0,"our":0,'total':0}

    for  word in words:
        if word =="US":
            continue
        if re.match(pr_pattern,word,re.I):
            
            
            if word == 'i.e':
                
                continue
            
            pr_counts[str(word.lower())] += 1
    total = 0
    for i in pr_counts.keys():
        if i  == 'total':
            continue
        else:
            
            pr_counts['total'] +=int(pr_counts.get(i))
            
    return pr_counts

 
 
def clean_text(text):
    """
    Perform basic cleaning of the text.
    """
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    # Normalize punctuation spacing
    text = re.sub(r'\s([?.!"](?:\s|$))', r'\1', text)
    return text
   
def Average_Number_of_Words_Per_Sentence(text= 0, word=  0 ,sent = 0):

    '''This calculates the average number of  word per sentence 
        avg_word  = total number of words / total number of sentences '''
    
    if  word  ==  0 and  sent  ==  0:
        sents = sent_tokenize(text)
        
        texts = clean_text(text)

        texts = re.sub(r'[,.]', '', text)
        
        words = word_tokenize(texts)

        # print(words) 
    else:
        words,sents =  word,sent
    
    
    avg_sent_len = math.floor(len(words)/len(sents) if  len(sents) >0 else 0)
    return avg_sent_len
    

    
    
    
def readability_score(text) ->set:
    complex_word  =  count_complex_word(text)
    
    sents = sent_tokenize(text)
    
    words  = word_tokenize(clean_text(text))
    pt_cpx_word = round( int(complex_word)/ len(words) , 2 ) * 100 if len(words) > 0 else 0
    
    


    fog_index = 0.4 * (float(Average_Number_of_Words_Per_Sentence(sent = sents , word = words)) + pt_cpx_word)
    return (fog_index,pt_cpx_word)
  



#  Sentimental Analysis

def positive_and_negative_word_from_folder_word_list(filtered_words,folder_name = '../Files/MasterDictionary'):
    negative_words = []
    positive_words = []
    os.chdir(folder_name)
    # os.chdir(folder_name)
    
    pos_neg_list = os.listdir()
    
    for i  in range(2):
        if 'negative' in str(pos_neg_list[i]).lower():
            with open(pos_neg_list[i],'r') as p_n_file:
                for i  in p_n_file.read().splitlines():
                    negative_words.append(str(i.lower()))
                    
        else:
             with open(pos_neg_list[i],'r') as p_n_file:
                for i  in p_n_file.read().splitlines():
                    
                    positive_words.append(str(i.lower()))
    pure_positive_list = [ word for  word in filtered_words if word in positive_words]
        
    
    pure_negative_word  = [word for word in filtered_words if  word in negative_words]

    os.chdir(main_working_dir)
    return (pure_positive_list,pure_negative_word)

def filtered_word_from_stopword_folder(text,folder_name = '../Files/StopWords'):
    
    
    os.chdir(folder_name)
    files_names = os.listdir(os.getcwd())
    st_word = set(stopwords.words('english'))

    
    stop_words_to_remove = list()
    for f_name  in files_names:
        with open(f_name,'r') as file:
            for i in file.read().splitlines():
                
                
                stop_words_to_remove.append(i.lower())
  
    
    st_word.update(set(stop_words_to_remove))
    
    
    texts = text
  
    texts = clean_text(re.sub(r'[,.]', '', texts))
    words = word_tokenize(texts.lower())
    
    
    filtered_words = [word.lower()  for word in words if word.isalpha() and word.lower()  not  in st_word]

    os.chdir(main_working_dir)
    return filtered_words 

    
        
    
        
        
        

        
      
def sentiment_analyze(filtered_words,postive_words,negaitve_words):
    polarity_score = 0
    positive_score = len(postive_words)
    negative_score = len(negaitve_words)

    if positive_score + negative_score == 0:
        polarity_score = 0
    else:
        polarity_score =  (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    
    if  len(filtered_words) == 0:
        
        Subjectivity_Score = 0
    else:
        Subjectivity_Score = (positive_score + negative_score) / ((len(filtered_words)) + 0.000001)
    
    return {"postive_score":int(positive_score),'negative_score':int(negative_score),'poloarity_score':float(polarity_score),'subjectivity_score':float(Subjectivity_Score)}
    

 
 
def all_scores(text):
    filtered_list = filtered_word_from_stopword_folder(text=text)
    pos_list,neg_list = positive_and_negative_word_from_folder_word_list(filtered_words=filtered_list)
    
    score =  sentiment_analyze(filtered_list,pos_list,neg_list)
    return {"Count_complex_word":count_complex_word(text),"average_word_length":Average_word_length(text),
            'Syllable_count':total_syllable_count(text),'personal_pernoun':personal_pernoun(text),"word_count":word_count(text),'average_sent_length':Average_Number_of_Words_Per_Sentence(text)
            ,'readability_test':readability_score(text),'sentimental_scores':score}
 
  

    



   

