from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    def get(self, request, params=None):
        print(request)
        return render(request, 'index.html')
