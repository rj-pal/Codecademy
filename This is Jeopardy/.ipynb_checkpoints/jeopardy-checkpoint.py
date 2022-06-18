# Two functions below default to column 'question' but can be used with any name for the question column in the jeopardy data base


def keyword_string_filter(data, words, col_name='question' ):
    """Returns a Pandas Series of boolean values for the word list filter regardless of letter case and any word string that matches"""
    words_filter = lambda question: all(word.lower() in question.lower() for word in words)
    
    filtered_series = data.question.apply(words_filter)

    return filtered_series


def keyword_filter(data, words, col_name='question'):
    """Returns Pandas Seris of word list filter regardless of letter case with exact matches only. Default col_name to question"""        
    question_words = lambda question: (q_word.lower() for q_word in question.split())
    
    words_filter = lambda function: lambda question: all(word.lower() in function(question) for word in words)
    
    filtered_series = data[col_name].apply(words_filter(question_words))
    
    return filtered_series

# Function defaults to the exact match keyword filter function, but function containing any string match can be used

def filtered_df(data, word_filter, filter_function=keyword_filter):
    """Returns new data frame filtered by the keyword filter list"""
    
    return data.loc[filter_function(data, word_filter)]
    
    
def split_df(data):
    """Splits the data frame into Jeopardy and Double Jeopardy rounds, and Final Jeopardy and Tiebreaker rounds"""
    regular_jeopardy_data = data.copy()[~(data.value == 'None')]
    final_jeopardy_data = data.copy()[(data.value == 'None')]
    
    return regular_jeopardy_data, final_jeopardy_data

def float_value_column_df(data, col_name='value', new_col_name='new_value'):
    """Returns the data frame with a new column of the Jeopardy dollar value column as type Float"""
    data_copy = data.copy()
    col_filter = lambda value: 0 if value == 'None' else float(value.lstrip('$').replace(',', ''))
    new_col = data[col_name].apply(col_filter)
    data_copy[new_col_name] = new_col
    
    return data_copy

def answer_frequency(data, col_name='answer'):
    """Return a Pandas Series of the frequency of answers for any Jeopardy Data Frame"""
    
    return data[col_name].value_counts()
