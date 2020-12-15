from .models import *
from django.utils import timezone


def get_material():
    materials = Material.objects.all()
    return materials


def get_services():
    services = Service.objects.all()
    return services


def get_review():
    reviews = Review.objects.all()
    return reviews


def autoriz(login, passw):
    users = Employee.objects.filter(login=login, password=passw)
    return users


def order_master(master_id):
    o_master = Order.objects.filter(master_id=master_id).prefetch_related("service_id")
    return o_master


def order_today():
    date_today = timezone.now()
    o_today = Order.objects.filter(time=date_today)
    return o_today


def get_masters():
    masters = Employee.objects.filter(privilegies=False)
    return masters


def add_review(name, email, descript):
    a_review = Review(customer_name=name, customer_email=email, description=descript)
    a_review.save()


def add_order(customer_name, customer_number, master, status, date, services, description, cost):
    a_order = Order(customer_name=customer_name, customer_number=customer_number, description=description, time=date, price=cost, status=status,
                    master_id=Employee.objects.get(id=master))
    a_order.save()
    for service in services:
        a_order.service_id.add(Service.objects.get(id=service))


def update_order(id, customer_name, customer_number, master, status, date, services, description, cost):
    u_order = Order.objects.get(id=id)
    u_order.customer_name=customer_name
    u_order.customer_number=customer_number
    u_order.description=description
    u_order.time=date
    u_order.price=cost
    u_order.status=status
    u_order.master_id=Employee.objects.get(id=master)
    u_order.save()
    for service in services:
        u_order.service_id.add(Service.objects.get(id=service))


def get_order_id(id):
    i_order = Order.objects.get(id=id)
    return i_order
