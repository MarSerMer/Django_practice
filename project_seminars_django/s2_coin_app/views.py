import random
from django.http import HttpResponse
import logging

from django.utils import timezone

from .models import HeadsTails
# Create your views here.

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,filename='logs/seminar2_coins.log',filemode='a')
def seminar2(request):
    logger.info(f'{request} request received')
    return HttpResponse("Seminar 2 page")


def heads_tails(request):
    logger.info(f'{request} request received')
    n = request.GET.get('n','10') #  в данном случае 5 - это значение по умолчанию
    res = random.choice(['Орёл', 'Решка'])
    res_w = HeadsTails(res=res)
    HeadsTails.save(res_w)
    data = HeadsTails.statistic(n)
    return HttpResponse(f'{data} ------------> Last result: {res}')