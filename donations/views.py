from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _

from django.urls import reverse

from aideafricaine import settings
# from .models import Donation
# from .forms import DonationForm
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

# Home page function
# from .text import Donation_text


def home_view(request):
    context = {
        'title': _('Home')
    }
    return render(request, 'donations/home.html', context)


def about(request):
    template_name = 'donations/about.html'
    return render(request, template_name, {})

def donation(request):
    template_name = 'donations/donation.html'
    return render(request, template_name, {})


# def new_donation(request):
#
#     if request.method == "POST":
#
#         form = DonationForm(request.POST)
#
#         if form.is_valid():
#             donation = Donation()
#             donation.name = form.cleaned_data['name']
#             donation.amount = form.cleaned_data['amount']
#             donation.email = form.cleaned_data['email']
#             donation.message = form.cleaned_data['message']
#             donation.payment_method = 'paypal'
#             donation.payment_status = 'pending'
#             donation.save()
#
#             paypal_dict = {
#                 "bn": "Aide Africaine",
#                 "business": settings.PAYPAL_ACCOUNT,
#                 "amount": donation.amount,
#                 "currency_code": "USD",
#                 "item_name": "Donation",
#                 "invoice": "AIDE_AFRICAIN" + str(donation.id),
#                 "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
#                 "return": request.build_absolute_uri(reverse('home')),
#                 "cancel_return": request.build_absolute_uri(reverse('donation')),
#                 "custom": donation.id,
#             }
#
#             template_name = 'donations/paypal.html'
#
#             # create the instance
#             form = PayPalPaymentsForm(
#                 initial=paypal_dict, button_type="donate")
#
#             context = {
#                 "form": form,
#                 'donation': donation,
#             }
#
#             messages.add_message(
#                 request,
#                 messages.SUCCESS,
#                 Donation_text.thank_you
#             )
#
#             return render(request, template_name, context)
#
#     else:
#
#         form = DonationForm()
#
#     template = "donations/donation.html"
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, template, context)

