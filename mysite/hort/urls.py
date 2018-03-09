# File       :  urls.py
# Description:  Django MVC control urlpatterns for "hort" application
# Author     :  Ken Carbaugh
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^cust_list/$', views.cust_list, name='cust_list'),
    url(r'^cust_detail/(?P<customer_id>[0-9]+)/$', views.cust_detail, name='cust_detail'),
    url(r'^cust_detail/(?P<customer_id>[0-9]+)/cust_update/.*$', views.cust_detail, name='cust_detail_update'),
    url(r'^gs_list/$', views.gs_list, name='gs_list'),
    url(r'^gs_detail/(?P<gs_id>[0-9]+)/$', views.gs_detail, name='gs_detail'),
    url(r'^gs_detail/(?P<gs_id>[0-9]+)/gs_update/.*$', views.gs_detail, name='gs_detail_update'),
    url(r'^ledger/$', views.ledger, name='ledger'),
    url(r'^ledger_detail/(?P<ledger_acct_id>[0-9]+)/$', views.ledger_detail, name='ledger_detail'),
    url(r'^invoice/$', views.invoice, name='invoice_list'),
    url(r'^invoice_detail/(?P<invoice_id>[0-9]+)/$', views.invoice_detail, name='invoice_detail'),
    url(r'^invoice_detail/(?P<invoice_id>[0-9]+)/inv_update/.*$', views.invoice_detail, name='invoice_detail_update'),
    url(r'^invoice_item/(?P<invoice_id>[0-9]+)/(?P<detail_id>[0-9]+)/$', views.invoice_item, name='invoice_item'),
    url(r'^invoice_item_list/(?P<invoice_id>[0-9]+)/$', views.invoice_item_list, name='invoice_item_list'),
    url(r'^invoice_item/(?P<invoice_id>[0-9]+)/(?P<detail_id>[0-9]+)/.*$', views.invoice_item, name='invoice_item_update'),
    url(r'^tender/(?P<invoice_id>[0-9]+)/(?P<inout_multiplier>-?[0-9]+)/(?P<invoice_total>\d+\.\d{2})/$', views.tender, name='tender'),
    url(r'^tender/(?P<invoice_id>[0-9]+)/(?P<inout_multiplier>-?[0-9]+)/(?P<invoice_total>\d+\.\d{2})/final_entry/$', views.tender, name='tender_insert'),
    url(r'^ff_invoice/$', views.ff_invoice, name='ff_invoice_list'),
    #url(r'^trial_balance/$', views.trial_balance, name='trial_balance'),
    url(r'^order_audit/$', views.order_audit, name='order_audit'),
    url(r'^psx12/$', views.psx12, name='psx12'),
    url(r'^open_order_sched/$', views.open_order_sched, name='open_order_sched'),
    url(r'^my_service/(?P<cust_id>[0-9]+)/$', views.my_service, name='my_service'),
    url(r'^journal_rpt/$', views.journal_rpt, name='journal_rpt'),
]