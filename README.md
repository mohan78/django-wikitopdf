# django-wikitopdf
A Django web application where you can search and download Wikipedia articles as PDFs. Uses Wikipedia API

Using this web application, one can download the wikipedia articles.

On accessing http://localhost:8000, you will be prompted with a homepage
asking for search. We have to enter the term that we are looking for.
Upon typing, we will get the matching results below.

Along with the matching search keyword, summary and a download button is
displayed in a table. Upon finding the correct record, we can click the
download button to download the wikipedia article in a PDF file.

I have used the mediawiki opensearch API to find suggestions. And wikipedia
python package to get the parsed content for a given article name.
For converting the html template to PDF, I have used xhtml2pdf library.
