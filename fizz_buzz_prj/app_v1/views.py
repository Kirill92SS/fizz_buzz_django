from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest):
    return HttpResponse('Hello world! This is fizz_buzz app.')


def make_fizz_buzz(request: HttpRequest, number: int):
    fizzbuzz_list = []
    for _ in range(1, number + 1):
        if not (_ % 3) and not(_ % 5):
            fizzbuzz_list.append("FizzBuzz")
        elif not (_ % 3):
            fizzbuzz_list.append("Fizz")
        elif not (_ % 5):
            fizzbuzz_list.append("Buzz")
        else:
            fizzbuzz_list.append(str(_))
    return render(request, 'app_v1/fizz_buzz.html', {'fizzbuzz_list': fizzbuzz_list, 'number': number})
