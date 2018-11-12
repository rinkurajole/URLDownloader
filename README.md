# URLDownloader(Python Django Rest App)
An api which when given a list of urls as a post request and email, downloads the urls as html, zips it and sends an email with zip file as attachment.

Example : 
{
    "urls": [
        "https://www.adnabu.com",
        "https://www.amazon.com"
    ],
    "email": "salil@adnabu.com"
}

- Expected response is an email to the email id with a zip file attached
- The api should return a result immediately and the downloading and sending email should work in the backend

