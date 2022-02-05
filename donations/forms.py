# from django import forms
# from django.utils import timezone
#
#
# class DonationForm(forms.Form):
#     """ Form for a new Donation, which can be tied to a specific fundraiser """
#
#     name = forms.CharField()
#     amount = forms.CharField()
#     other_amount = forms.CharField(required=False)
#     email = forms.EmailField()
#     date = timezone.now()
#
#     message = forms.CharField(
#         widget=forms.Textarea(
#             attrs={'required': False, 'rows': 3}
#         ),
#         required=False
#     )
#
#     def clean(self):
#         # if the user chooses "other amount", make that the amount
#
#         cleaned_data = super().clean()
#
#         try:
#             amount = cleaned_data.get("amount")
#         except KeyError:
#             amount = ""
#
#         try:
#             other_amount = cleaned_data.get("other_amount")
#         except KeyError:
#             other_amount = ""
#
#         if amount == 'other' or amount == '':
#             # TODO pull out just the number, in case they added a $
#             try:
#                 cleaned_data['amount'] = float(other_amount)
#             except ValueError:
#                 raise forms.ValidationError("Amount is not a number")
#
#         return cleaned_data
