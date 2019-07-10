from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .wikiapi import WikiApi
from io import BytesIO
from xhtml2pdf import pisa
import json

#Initialize API object
wiki = WikiApi()

def render_to_pdf(template, context={}):
    """
    method: render_to_pdf(template, context)

    This method is based on xhtml2pdf package.
    This method returns a pdf from a supplied html document.

    :Input params:
    template -> The html template that has to be rendered as PDF.
    context -> Dictionary that contains the elements that has to be
               rendered inside the template. Default is empty dictionary
    :return:
    HttpResonse of the converted pdf
    """
    template = get_template(template)
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(html, result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def homepage(request):
    """
    This method renders and returns the homepage html document.

    :param request:
    :return: render template method with the request,
            target template as parameters
    """
    return render(request, 'app/index.html')

def load_suggestion(request):
    """
    Loads suggestions based on the search term provided by the
    user

    :param request:
    :return: HttpResponse as jsonified object containing the suggestions
             from the wikipedia opensearch api.
    """
    search_term = request.GET['searchTerm']
    try:
        suggestions = wiki.load_suggestions(search_term)
        return HttpResponse(json.dumps({"suggestions":suggestions}))
    except ConnectionError:
        return HttpResponse('Unable to query API, please check your connectivity')

def get_article(request):
    """
    Gets the article from the wiki api and pushes as a pdf file.
    Used wikipedia python package to retreive data from wiki api.

    :param request:
    :return: HttpResponse object containing the pdf file.
    """
    article = request.GET['article']
    try:
        page = wiki.get_article(article)
        if page is not None:
            context = {
                'title': article,
                'content': page.content
            }
            pdf = render_to_pdf('app/content.html', context)
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = '{}-wiki.pdf'.format(article)
            content = "attachment; filename={}".format(filename)
            response['Content-Disposition'] = content
            return response
        else:
            return HttpResponse('Please provide an valid name get wiki data')
    except ConnectionError:
        return HttpResponse('Please check the connectivity')

