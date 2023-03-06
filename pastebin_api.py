from urllib import response
import requests 

API_POST_URL = 'https://pastebin.com/api/api_post.php'
def main():
    new_paste('Jayrajsinh paste', 'A bunch of paste', expiration='10M',listed=True)
    """Creates a new paste on PasteBin using the PasteBin API.

    Parameters:
    title (str): title of paste.
    body (str): content of paste.
    expiration (str):expiration date of. values which are possible 'N', '10M', '1H', '1D', '1W', '2W', '1M'.
    public (bool): Whether the paste should be visible or not.

    Returns:
    str: URL of the paste newly created, if successful
    None: If the paste was not created successfully.
"""
    

def new_paste(title, body, expiration, public):
    #create dictionary  of parameter values

    data = { 
        'api_dev_key': '4TTsT4TNUymV0f9oSdxS6sk-yTTgj52q',
        'api_option': 'Paste',
        'api_paste_code': body,
        'api_paste_name':title,
        'api_paste_expire_date':expiration,
        'api_paste_private': '0' if public else '1',
        'api_paste_code': body
    }
    #POST request to Pastebin API
    print("Added something new to the pastebin.", end='')
    response = requests.post(API_POST_URL, data=data)

#Testing if request POST was success 
if response.status_code == requests.codes.ok:
    response.text.strip()
    print(f'URL of new paste: {response}')

          
        
else:
        print("FAILED")
         

        

if __name__ == "__main__":
    main()


    