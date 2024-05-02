from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from app_v1.models import FizzBuzz, Fizz, Buzz
from django.core.exceptions import ObjectDoesNotExist
from subprocess import run


def check_fizz_buzz(model, number, lst):
    try:
        fb = model.objects.get(number=number)
    except ObjectDoesNotExist as e:
        fb = model.objects.create(number=number)
    finally:
        lst.append(fb.data)


def index(request: HttpRequest):
    return HttpResponse('Hello world! This is fizz_buzz app.')


def make_fizz_buzz(request: HttpRequest, number: int):
    fizzbuzz_list = []
    for _ in range(1, number + 1):
        if not (_ % 3) and not(_ % 5):
            check_fizz_buzz(FizzBuzz, _, fizzbuzz_list)
        elif not (_ % 3):
            check_fizz_buzz(Fizz, _, fizzbuzz_list)
        elif not (_ % 5):
            check_fizz_buzz(Buzz, _, fizzbuzz_list)
        else:
            fizzbuzz_list.append(_)
    fizzbuzz_list.append(f'Hostname: {run(["hostname"], capture_output=True, text=True, check=True).stdout}')
    return render(request, 'app_v1/fizz_buzz.html', {'fizzbuzz_list': fizzbuzz_list, 'number': number})
