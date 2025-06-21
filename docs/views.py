from summarizer import Summarizer
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from PIL import Image
import pytesseract
from .models import Document
from .forms import DocumentForm
import os
from keybert import KeyBERT
import spacy
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

custom_stop_words = set(ENGLISH_STOP_WORDS)
custom_stop_words.add('using')
custom_stop_words.add('use')
custom_stop_words.add('make')
custom_stop_words.add('does')
custom_stop_words.add('especially')
custom_stop_words.add('specially')
custom_stop_words.add('type')
custom_stop_words.add('perfectly')
custom_stop_words.add('uses')
custom_stop_words.add('made')
custom_stop_words.add('just')
custom_stop_words.add('examples')
custom_stop_words.add('usage')
custom_stop_words.add('example')
custom_stop_words.add('ss')

model = KeyBERT()
nlp = spacy.load("en_core_web_sm")


def extract_keywords(text):
    keywords = model.extract_keywords(text, keyphrase_ngram_range=(1, 1), stop_words=list(custom_stop_words), top_n=29)
    list_pos = {"NOUN","PROPN"}
    raw_keywords = []
    for kw, _ in keywords:
        docs = nlp(" ".join(kw))
        if any(token.pos_ in list_pos for token in docs):
            raw_keywords.append(kw)
    return raw_keywords


def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            uploaded_file = form.cleaned_data['image']
            image = Image.open(uploaded_file)
            text = pytesseract.image_to_string(image)
            tags = extract_keywords(text)
            doc.tags = ','.join(tags)
            model = Summarizer()
            summary = model(text, min_length=3)
            doc.subject = summary.strip()
            doc.save()
            return redirect('table_doc')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})


def table_data(request):
    query = request.GET.get('q', '')
    data = Document.objects.all()
    if query:
        data = data.filter(tags__icontains=query)
    paginator = Paginator(data, 5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'table.html', {'page_obj': page_obj, 'query': query})
