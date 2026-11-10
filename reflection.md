# REST API Public Fetch Reflection

For this project, I created a Python program to perform an asynchronous HTTP GET request on NHTSA's publicly available API. The program displays a loading message and sends the request. Upon receiving the response, the program checks for errors and then transforms the data into JSON. After getting the data in JSON format, I accessed the Results field, filtered for records where the GroupName is Active Safety System and printed out the relevant information.

The convenience and accessibility of external APIs made me realize the amount of data one can access with a couple of lines of code. Along the process, I was able to implement my code with greater detail to accommodate errors, and apply filters for greater specificity. Asynchronous HTTP requests, JSON parsing, and data filtering are clearer for me than before. I hope to expand on these learnings by researching APIs that expose more data, and visualizing the data in an elegant GUI.
