from django.forms import ModelForm, Textarea
from django import forms
from datetimewidget.widgets import DateTimeWidget, DateWidget

from .models import Customer, LedgerAcct, Details, GoodAndServices, Orders

# Create your forms here.

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        #['id', 'CustID', 'FirstName', 'LastName', 'ExtraLine', 'StreetAddress', 'PostOffice', 'ZipCode']
        
class InvoiceForm(ModelForm):
    class Meta:
        model = Orders
        #fields = '__all__'
        fields = ['Type','EnteredBy','OrdersCustID','PONumber',
                  'Status','StatusBy','AccountingDate','InOrOut','OrderNotes',
        ]
        widgets = {
            #Use localization and bootstrap 3
            'StatusDT': DateTimeWidget(attrs={'id':"id_StatusDT"}, usel10n = True, bootstrap_version=3),
            'AccountingDate': DateWidget(attrs={'id':"id_AccountingDate"}, usel10n = True, bootstrap_version=3),
            #'DataEntryCompleteDT': DateTimeWidget(attrs={'id':"id_DataEntryCompleteDT"}, usel10n = True, bootstrap_version=3),
            #'CheckedOutToFillDT': DateTimeWidget(attrs={'id':"id_CheckedOutToFillDT"}, usel10n = True, bootstrap_version=3),
            #'QueuedForPSX12DT': DateTimeWidget(attrs={'id':"id_QueuedForPSX12DT"}, usel10n = True, bootstrap_version=3),
            #'SentViaPXS12DT': DateTimeWidget(attrs={'id':"id_SentViaPXS12DT"}, usel10n = True, bootstrap_version=3),
            'OrderNotes': Textarea(attrs={'rows': 4, 'cols': 40,}),
        }
        
class InvoiceItemsForm(ModelForm):
    class Meta:
        model = Details
        #fields = '__all__'
        fields = ['OrderID','GSID','QtyOrdered','AcctEntry',
                  'CPEach','QtyInOrOut','ExtPrice','Ledger',
                  'ScheduledStartDT','ScheduledCompleteDT',
        ]
        #fields[0].widget.attrs['readonly'] = True
        widgets = {
            #Use localization and bootstrap 3
            'ScheduledStartDT': DateTimeWidget(attrs={'id':"id_ScheduledStartDT"}, usel10n = True, bootstrap_version=3),
            'ScheduledCompleteDT': DateTimeWidget(attrs={'id':"id_ScheduledCompleteDT"}, usel10n = True, bootstrap_version=3),
            #'ActualStartDT': DateTimeWidget(attrs={'id':"id_ActualStartDT"}, usel10n = True, bootstrap_version=3),
            #'ActualCompleteDT': DateTimeWidget(attrs={'id':"id_ActualCompleteDT"}, usel10n = True, bootstrap_version=3),
            #'FrontNotes': Textarea(attrs={'rows': 4, 'cols': 40,}),
            #'BackNotes': Textarea(attrs={'rows': 4, 'cols': 40,}),
        }
        #def __init__(self, *args, **kwargs):
        #    self.fields['OrderID'].widget.attrs['readonly'] = 'readonly'

class GSForm(ModelForm):
    class Meta:
        model = GoodAndServices
        fields = '__all__'
        
class AcctDateForm(forms.Form):
    acct_dt = forms.ChoiceField(choices=[], required=False)
    def __init__(self, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)
        self.fields['acct_dt'].choices = Event.objects.all().values_list("AccountingDate","AccountingDate").distinct()



