from datetime import datetime
from random import randint
from pandas import merge

# Two functions below default to column 'question' but can be used with any name for the question column in the jeopardy data base

def keyword_string_filter(data, words):
    """Returns a Pandas Series of boolean values for the word list filter regardless of letter case and any word string that matches"""
    words_filter = lambda question: all(word.lower() in question.lower() for word in words)
    
    filtered_series = data.iloc[:, 5].apply(words_filter)

    return filtered_series


def keyword_filter(data, words):
    """Returns Pandas Seris of word list filter regardless of letter case with exact matches only. Default col_name to question"""        
    question_words = lambda question: (q_word.lower() for q_word in question.split())
    
    words_filter = lambda function: lambda question: all(word.lower() in function(question) for word in words)
    
    filtered_series = data.iloc[:, 5].apply(words_filter(question_words))
    
    return filtered_series


# Function defaults to the exact match keyword filter function, but function containing any string match can be used

def filtered_df(data, word_filter, filter_function=keyword_filter):
    """Returns new data frame filtered by the keyword filter list"""
    
    return data.loc[filter_function(data, word_filter)]
    
    
def split_df(data):
    """Splits the data frame into Jeopardy and Double Jeopardy rounds, and Final Jeopardy and Tiebreaker rounds, and returns new data frames"""
    regular_jeopardy_data = data.copy()[~(data.value == 'None')]
    final_jeopardy_data = data.copy()[(data.value == 'None')]
    
    return regular_jeopardy_data, final_jeopardy_data


def add_float_value_column(data, new_col_name='new_value'):
    """Returns a new data frame with a new column of the Jeopardy dollar value column as type Float"""
    col_filter = lambda value: 0 if value == 'None' else float(value.lstrip('$').replace(',', ''))
    new_col = data.iloc[:, 4].apply(col_filter)
    data[new_col_name] = new_col    
    

def add_datetime_decades_columns(data, new_col_name='decade'):
    """Modifies the original data frame with column 'Air Date' converted to datatime object and a integer column for the decade."""
    
    dt_converter = lambda time: datetime.strptime(time, '%Y-%m-%d')
    dt_air_date = data.iloc[:, 1].apply(dt_converter)
    data.iloc[:, 1] = dt_air_date
    decade_filter = lambda year: int(year//10 * 10)
    decade = data.air_date.dt.year.apply(decade_filter)
    data[new_col_name] = decade
    

def show_number_filtered_data(data, word_filter, col_name='decade'):
    """Returns a summary statistics data frame of the number of shows aggregated by any column or field and filtered by keywords."""
    if type(word_filter) is str:
        word_filter = word_filter.split()
        
    filtered_data = filtered_df(data, word_filter)
    full_col_counts = data.groupby(col_name).count().iloc[:,0]

    
    col_counts = filtered_data.groupby(col_name).count().iloc[:,0].rename('number_of_shows')
    col_sum = col_counts.sum()
    col_percentage = col_counts.apply(lambda count: round(count/col_sum, 3)).rename('proportion_of_total')
    new_data = merge(col_counts, col_percentage, on=col_name).reset_index()


    
    percentage = lambda row: round(row['number_of_shows']/full_col_counts[row[col_name]]*100, 3)
    new_col_name = 'as_percentage_of_' + col_name
    new_data[new_col_name] = new_data.apply(percentage, axis=1)
    
    
    return new_data


# Can be used to obtain on the show number counts and percentage of decade only- original summary function   
def column_data(data, word_filter):
    """Returns a new data frame aggregated by decade with summary stats for the number of shows"""
    filtered_data = filtered_df(data, word_filter)
    
    col_counts = data.groupby('decade').show_number.count()

    
    new_data = filtered_data.groupby('decade')['show_number'].count().reset_index()
    percentage = lambda row: row['show_number']/col_counts[row[col_name]]*100
    new_data['as_percentage_of_decade'] = new_data.apply(percentage, axis=1)
    
    return new_data


def answer_frequency(data, col_name='answer'):
    """Return a Pandas Series of the frequency of answers for any Jeopardy Data Frame"""
    
    return data[col_name].value_counts()


# the following three functions work together to run a quiz program for the user
def play_jeopardy(data, rounds=5):
    """Starts an interactive quiz set to the number of rounds. Shows randomly selected questions and takes user input for the answers."""
    add_float_value_column(data)
    total_score = 0
    number = 0
    correct = 0
    while number < rounds :
        score = quiz(data)
        total_score += score
        if score != 0:
            correct +=1
        print()
        print("Round Earnings:", score,)
        print("Total winnings:", total_score)
        print()
        number +=1
    print("Correct:", str(correct) + "/" +str(rounds))
    print("Winnings:", total_score)

          
def random_question(data):
    """Returns a random question with the relevant information for the quiz function."""
    first = 0
    last = data.shape[0] - 1
    number = randint(a=first, b=last)
    
    return data.iloc[number, 2:8]


def quiz(data):
    """Provides a random question and takes an answer from the user and checks if the answer is correct. Returns the dollar value of the question."""
    j_round, cat, val, quest, ans, score = random_question(data)
    print("Round:", j_round)
    print("Category:", cat)
    print("Value:", val)
    print("Question:", quest)
    print()
    answer = input("Answer: ")
    answer_words = answer.lower().split()
    print()
    response = False

    if answer_words: # check if there was some input and not just 'enter' was pressed
        
        if '(or' in ans: # check for multiple posible answers to one question 
            ans_list = ans.split()
            new_ans_list = []
            new_ans_list.append(ans_list[0].lower())
            new_ans_list.append(ans_list[-1][:-1].lower())
            for word in answer_words: 
                if word in new_ans_list:
                    reponse = True
                    break
        elif '&' in ans: # check for answers that require more than one response
            ans_list = ans.split()
            new_ans_list = []
            for a in ans_list:
                if a != '&':
                    new_ans_list.append(a.lower().replace(',', ''))
            
            response = all(word in new_ans_list for word in answer_words)
                    
        else:
            for word in answer_words:
                if word in ans.lower():
                    response = True
                    break
        
    if response:   
        print("Correct. The answer is", ans)
        
        return score
    else:
        print("Incorrect. The answer is", ans)
        
        return 0
        
if __name__ == "__main__":
    from pandas import read_csv
    
    data = read_csv('jeopardy.csv')
    play_jeopardy(data)