# linkingBBPOS
Conversion from BBPOS to Deep Linking (Concept):

------------------------------------------------

BBPOS allows users to trigger a transaction via http, so most integrations were built on the web. 

The goal of this project is to convert requests made in the BBPOS-like format to a deep link. This would hopefully allow people to simply alter the endpoint that the request goes to, and have the transaction open in the app.

So far, it only works when the http request is made with the expectation of an html page in the response.

Being that most BBPOS integrations use an AJAX call to trigger a transaction, I decided to return the link in json whenever the request is sent in a post (not a get).
