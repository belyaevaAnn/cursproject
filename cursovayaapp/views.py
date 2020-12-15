from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .basa import *


class MainPage(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context=context)


class AdminPage(View):
    def get(self, request):
        o_today = order_today()
        masters = get_masters()
        context = {
            'o_today': o_today,
            'masters': masters
        }
        return render(request, 'admin.html', context=context)


class AdminMasterPage(View):
    def get(self, request, id):
        o_master = order_master(id)
        masters = get_masters()
        context = {
            "o_today": o_master,
            'masters': masters
        }
        return render(request, 'admin.html', context=context)


class EnterPage(View):
    def get(self, request):
        context = {}
        return render(request, 'enter.html', context=context)

    def post(self, request):
        entered_login = request.POST.get("enter_login")
        entered_passw = request.POST.get("enter_pass")
        users = autoriz(entered_login, entered_passw)
        if not users:
            context = {
                "message": "Введен неверный логин или пароль"
            }
            return render(request, 'enter.html', context=context)
        elif users[0].privilegies == 0:
            request.session["id_user"]=users[0].id
            request.session["priv_user"]=users[0].privilegies

            return HttpResponseRedirect('master.html')
        else:
            request.session["id_user"] = users[0].id
            request.session["priv_user"] = users[0].privilegies
            return HttpResponseRedirect('admin.html')


class FormReviewPage(View):
    def get(self, request):
        context = {}
        return render(request, 'form_review.html', context=context)

    def post(self, request):
        context = {}
        customer_name = request.POST.get("review_name")
        customer_email = request.POST.get("review_email")
        description = request.POST.get("review_text")
        if not customer_name:
            context["message_name"] = "Введите имя"
        if not customer_email:
            context["message_email"] = "Введите email"
        if not description:
            context["message_desc"] = "Введите текст отзыва"

        if context:
            return render(request, "form_review.html", context=context)
        else:
            add_review(customer_name, customer_email, description)
            return HttpResponseRedirect('review.html')


class MasterPage(View):
    def get(self, request):
        o_master = order_master(request.session['id_user'])
        context = {
            "o_master": o_master
        }
        return render(request, 'master.html', context=context)


class MaterialPage(View):
    def get(self, request):
        materials = get_material()
        context = {
            'materials': materials
        }
        return render(request, 'material.html', context=context)


class OrderPage(View):
    def get(self, request):
        masters = get_masters()
        services = get_services()
        materials = get_material()
        status = ['Принят', 'В работе', 'Ожидает примерки', 'Завершен', 'Отдан']
        context = {
            'masters': masters,
            'services': services,
            'materials': materials,
            'status': status
        }
        return render(request, 'order.html', context=context)

    def post(self, request):
        context = {}
        order_name = request.POST.get("order_name")
        order_status = request.POST.get("order_status")
        order_telephone = request.POST.get("order_telephone")
        order_date = request.POST.get("order_date")
        order_master = request.POST.get("order_master")
        order_services = request.POST.getlist("order_services")
        order_masterials = request.POST.getlist("order_masterials")
        order_text = request.POST.get("order_text")
        order_cost = request.POST.get("order_cost")
        if not order_name:
            context["message_name"] = "Введите имя"

        if context:
            return render(request, "order.html", context=context)
        else:
            add_order(order_name, order_telephone, order_master, order_status, order_date,  order_services, order_text, order_cost)
            if not request.session["priv_user"]:
                return HttpResponseRedirect('master.html')
            else:
                return HttpResponseRedirect('admin.html')


class ReviewPage(View):
    def get(self, request):
        reviews = get_review()
        context = {
            "reviews": reviews
        }
        return render(request, 'review.html', context=context)


class ServicePage(View):
    def get(self, request):
        services = get_services()
        context = {
            "services": services
        }
        return render(request, 'service.html', context=context)


class SessionCheck(View):
    def get(self, request):
        if not request.session["priv_user"]:
            return HttpResponseRedirect('master.html')
        else:
            return HttpResponseRedirect('admin.html')


class EditOrderPage(View):
    def get(self, request, id):
        masters = get_masters()
        services = get_services()
        materials = get_material()
        order = get_order_id(id)
        status = ['Принят', 'В работе', 'Ожидает примерки', 'Завершен', 'Отдан']
        context = {
            'masters': masters,
            'services': services,
            'materials': materials,
            'order': order,
            'status': status
        }
        return render(request, 'edit_order.html', context=context)

    def post(self, request, id):
        context = {}
        order_name = request.POST.get("order_name")
        order_status = request.POST.get("order_status")
        order_telephone = request.POST.get("order_telephone")
        order_date = request.POST.get("order_date")
        order_master = request.POST.get("order_master")
        order_services = request.POST.getlist("order_services")
        order_text = request.POST.get("order_text")
        order_cost = request.POST.get("order_cost")
        if not order_name:
            context["message_name"] = "Введите имя"

        if context:
            return render(request, "order.html", context=context)
        else:
            update_order(id, order_name, order_telephone, order_master, order_status, order_date,  order_services, order_text, order_cost)

            if not request.session["priv_user"]:
                return HttpResponseRedirect('../master.html')
            else:
                return HttpResponseRedirect('../admin.html')
