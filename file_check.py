# Libraries

import pandas as pd
import requests
from bs4 import BeautifulSoup

# Data tickets
data_raw = [
        ('56079')
      , ('27300')
      , ('41190')
   ]


# df tickets
df = pd.DataFrame(data_raw, columns=['num'])


# Function check tickets
def check_lottery(df_tocheck: object):
    
    """ Function to check dataframe which contains tickets.

    """
    
    data_result = []
    
    for ticket in df_tocheck['num']:
        
        ticket_int = int(ticket)
        
        # requesting
        rr = requests.get(f'https://www.lavanguardia.com/loterias/loteria-navidad/comprobar-numeros/{ticket_int}.html')
        
        
        # Parse
        soup = BeautifulSoup(rr.text, 'html.parser')
        
        # Find values
        result = soup.find('span', class_='lt-ticket__result').text
        detail = soup.find('p', class_='lt-ticket__title').text
        
        # New row
        
        row = (ticket_int, result, detail)
        
        data_result.append(row)
    
    # df result
    
    return pd.DataFrame(data_result, columns=['ticket', 'result', 'detail'])

        
    
if __name__ == "__main__":
    
    
    checker = check_lottery(df_tocheck = df)
    print(checker)


