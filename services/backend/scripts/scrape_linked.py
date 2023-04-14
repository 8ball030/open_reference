import pickle
import os
from linkedin_api import Linkedin
import click




# Authenticate using any Linkedin account credentials
api = Linkedin(os.environ["LINKEDIN_UN"], os.environ["LINKEDIN_PW"])
# GET a profile
profile = api.get_profile('tom-r-89723755')
print(profile)

file = open("object", "wb")
pickle.dump(profile, file)
