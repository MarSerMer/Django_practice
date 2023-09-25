from django.shortcuts import render
from django.http import HttpResponse
import logging
# Create your views here.

logger = logging.getLogger(__name__)

def main_page(request):
    text = '''<font color="orange"><center><h1>Main page</h1>
    <p>This is our welcome page, so welcome!!</p></center></font>'''
    logger.info('Main page visited')
    return HttpResponse(text)


def about_page(request):
    text = '''<font color="blue"><center><h1>About me</h1>
        <p>I am supposed to tell a few words about myself on this page.</p>
        <p>So, I live in Russia and I am learning to become a programmer. Hope I will be able to.</p>
        <p>Also I am learning to play table tennis. This is a wonderful sport and I really hope to succeed.</p></center></font>'''
    logger.info('About page visited')
    return HttpResponse(text)