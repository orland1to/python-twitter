import  twitter
import os
from decouple import config
api_client=twitter.Api(
    consumer_key=config('CONSUMER_KEY'),
	consumer_secret=config('CONSUMER_SECRET'),
	access_token_key=config('ACCESS_TOKEN_KEY'),
	access_token_secret=config('ACCESS_TOKEN_SECRET'))
#print(api_client.VerifyCredentials())

#result =   api_client.GetFollowers()
#first_ten= result[:10]
#print(result[0])
#image_path= os.path.abspath('meteorito.jpg')
result=api_client.PostUpdate("@orland1to1  is  #learning #python at #huajuapan and using  #decouple")
print(result)