from django.shortcuts import render, get_object_or_404, redirect

from keyword_models.extract_keys import extract_keywords
from fivecart.models import Book
from fivecart.models import Report
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.exceptions import ValidationError
import json

from django.core.paginator import Paginator


# from keybert import KeyBERT
# import joblib
# from flair.embeddings import TransformerDocumentEmbeddings
# import os


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    report_list = Report.objects.filter(book_id=book_id)
    context = {'book': book, 'report_list': report_list}
    return render(request, 'fivecart/book_detail.html', context)


def execute_keyfunc(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            param1 = data.get('param1', '')#본문
            param2 = data.get('param2', '')#모델명
            param3 = data.get('param3', '')#다양화 체크
            param4 = data.get('param4', '')#ngram 개수 체크

            if (param2 == "default"):
                filepath = './keyword_models/kw_model_klue_roberta-small.pkl'
            elif (param2 == "roberta-base"):
                filepath = './keyword_models/kw_model_klue_roberta-base.pkl'
            elif (param2 == "roberta-large"):
                filepath = './keyword_models/kw_model_klue_roberta-large.pkl'
            elif (param2 == "bert-base"):
                filepath = './keyword_models/kw_model_klue_bert-base.pkl'
            elif (param2 == "all-mpnet-base-v2"):
                filepath = './keyword_models/kw_model_all-mpnet-base-v2.pkl'
            elif (param2 == "distiluse-base-multilingual-cased-v1"):
                filepath = './keyword_models/kw_model_distiluse-base-multilingual-cased-v1.pkl'
            elif (param2 == "keybert-base"):
                filepath = './keyword_models/kw_model_base.pkl'
            else:
                filepath = './keyword_models/kw_model_klue_roberta-small.pkl'

            max_sum = False
            mmr = False
            if "max-sum" in param3:
                max_sum = True
            if "mmr" in param3:
                mmr = True

            res = extract_keywords(filepath, param1, max_sum, mmr, int(param4))
            response_data = {'keywords': res}
            return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON 데이터 파싱 오류'})
        # param = request.POST.get('param', '')  # 'param' 값을 받아옵니다.
        # filepath = './keyword_models/kw_model_klue_roberta-small.pkl'
        # res = extract_keywords(filepath, param)

        # response_data = {'keywords': res}

        # JsonResponse를 사용하여 JSON 응답 반환
        # return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})
    else:
        # GET 요청에 대한 처리
        return JsonResponse({'error': 'POST 요청을 사용하여 파라미터를 전달해야 합니다.'})


def update_keys(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            param1 = data.get('param1', '')
            param2 = data.get('param2', '')
            param3 = data.get('param3', '') #report_id

            report = get_object_or_404(Report, pk=param3)
            report.keywords = param1
            report.keyword_type = param2
            report.save()
            return JsonResponse({'message': '데이터베이스가 업데이트되었습니다.'})
        except ValidationError as e:
            # 데이터 유효성 검사에서 오류가 발생한 경우
            errors = e.message_dict
            return JsonResponse({'error': errors}, status=400)
        except Exception as e:
            # 다른 예외 처리
            return JsonResponse({'error': str(e)}, status=500)


def report_detail(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    # filepath = './keyword_models/kw_model_klue_roberta-small.pkl'
    # res = extract_keywords(filepath, report.report_text)
    res = "word";
    context = {'report': report, 'keywords': res}

    return render(request, 'fivecart/report_detail.html', context)
