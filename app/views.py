from django.shortcuts import render
from django.http import HttpResponse
from .wikiapi import WikiApi
import json

#Initialize API object
wiki = WikiApi()

def homepage(request):
    return render(request, 'app/index.html')

def load_suggestion(request):
    search_term = request.GET['searchTerm']
    suggestions = wiki.load_suggestions(search_term)
    keys = []
    for i in suggestions:
        keys.append(i)
    return HttpResponse(json.dumps({"keys":keys}))

def get_article(request, article):
    page = wiki.get_article(article)
    context = {
        'content': page.content
    }
    return render(request, 'app/content.html', context)

