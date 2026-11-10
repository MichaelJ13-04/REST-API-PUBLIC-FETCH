# REST API Public Fetch Reflection

For this assignment, I created a Python program that makes an asynchronous GET request to the NHTSA public vehicle data API. The program starts by displaying a loading message, sends the request to the provided URI, checks for HTTP or network errors, and converts the response into JSON. I then accessed the `Results` list and filtered the records so that only items with a `GroupName` of `Active Safety System` are displayed.

One thing that stood out to me was how much useful information an API can provide without having to build or maintain the original database. My code evolved from simply retrieving data to handling possible errors and narrowing the results with a condition. I understand asynchronous requests, JSON responses, and filtering data better now. I would like to learn more about how APIs organize large datasets and how to display the results in a graphical interface.
