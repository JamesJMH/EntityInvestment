# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Investor, Company
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'entityinvestment/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Company.objects.order_by('-pub_date')[:5]


class CompanyDetailView(generic.DetailView):
    model = Company
    template_name = 'entityinvestment/detail.html'


class InvestorDetailView(generic.DetailView):
    model = Investor
    template_name = 'entityinvestment/results.html'