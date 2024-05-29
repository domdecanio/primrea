import pandas as pd

def df_funct():
    '''
    This function creates a test pd.DataFrame, and prints it.
    '''
    thing = {"a":[1, 2, 3, 4, 5], "b":['apple', 'banana', 'pear', 'orange', 'cherry'], "c":[True, False, False, False, True]}
    thing_df = pd.DataFrame(thing)

    return thing_df

def hello():
    '''
    This function says hello!
    '''
    print('Hello World!')

    return

