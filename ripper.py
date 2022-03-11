import requests
import urllib.request
from bs4 import BeautifulSoup

# A list is used so that multiple images can be downloaded with a loop
Urls_img = ["https://images.unsplash.com/photo-1519060825752-c4832f2d400a?ixlib=rb-1.2.1\
&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
]

# A list to store all the faulty links
Urls_faulty = []

# A counter to help us in naming the file
count = 0

for image in Urls_img:
    
    count += 1
    
    #Naming the file using our counter variable
    name = f"Image #{count}.png"
    print(f"This is the image name: {name}")

    # Now let's send a request to the image URL:
    req = requests.get(image, stream=True)
    # We need to check that the status code is 200 before doing anything else
    if req.status_code == 200:
        # This command below will allow us to write the data to a file as binary
        with open(name, 'wb') as f:
            for data in req:
                f.write(data)
    else:
        # We will write all the faulty URLs back to the Urls_faulty list:
        Urls_faulty.append(image)