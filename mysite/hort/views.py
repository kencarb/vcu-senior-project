# File       :  views.py
# Description:  Django MVC view classes for "hort" application
# Author     :  Ken Carbaugh
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django import forms
from django.db.models import Sum
from django.contrib.auth import logout
import sqlite3
import http.client

from .models import Customer, LedgerAcct, Details, GoodAndServices, Orders 
from .forms import CustomerForm, InvoiceItemsForm, GSForm, InvoiceForm

#
# Login and initial pages
#
def login(request):
    context = {}
    return render(request, 'hort/login.html', context)
    
@login_required
def index(request):
    current_user = request.user
    print("current_user.id")
    print(current_user.id)
    try:
        #rel_menu = Customer.objects.filter(User_id=current_user.id).values_list('Relationship', flat=True)[0]
        rel_menu = Customer.objects.filter(User_id=current_user.id).values('Relationship')[0]
        cust_id = Customer.objects.filter(User_id=current_user.id).values('id')[0]
        name = Customer.objects.filter(User_id=current_user.id).values('FirstName','LastName')[0]
    except:
        logout(request)
        return HttpResponse("<h3>Sorry... cannot find your Customer user_id ... <a href='/account/login/?next=/hort/'>Try again</a></h3>")
    print(rel_menu)
    print(cust_id)
    print(name)
    context = {'rel_menu': rel_menu, 'cust_id': cust_id, 'name': name}
    return render(request, 'hort/index.html', context)

#
# Customer management
#
@login_required
def cust_list(request):
    customer_list = Customer.objects.order_by('LastName')
    context = {'customer_list': customer_list}
    return render(request, 'hort/cust_list.html', context)
    
@login_required
def cust_detail(request, customer_id):
    print("customer_id = " + customer_id)
    if int(customer_id) == 0 and request.method != 'POST':
        form = CustomerForm()
        return render(request, 'hort/cust_detail.html', {'form': form})
    if request.method == 'POST':
        if int(customer_id) == 0:
            form = CustomerForm(request.POST)
        else:
            form = CustomerForm(request.POST, instance=Customer.objects.get(id=customer_id))
        if form.is_valid():
            cid = request.POST.get('CustID')
            print(cid)
            a = Customer.objects.filter(CustID=cid).count()
            print(a)
            if (int(customer_id) == 0 and a > 0):
                print("Duplicate CustID: " + cid)
            else:
                form.save(commit=True)
            return cust_list(request)
        else:
            print(form.errors)
    else:
        form = CustomerForm(instance=Customer.objects.get(id=customer_id))
    return render(request, 'hort/cust_detail.html', {'form': form})

#
# GoodAndServices management
#
@login_required
def gs_list(request):
    gs_list = GoodAndServices.objects.order_by('Class')
    context = {'gs_list': gs_list}
    return render(request, 'hort/gs_list.html', context)
    
@login_required
def gs_detail(request, gs_id):
    print("gs_id = " + gs_id)
    if int(gs_id) == 0 and request.method != 'POST':
        form = GSForm()
        return render(request, 'hort/gs_detail.html', {'form': form})
    if request.method == 'POST':
        if int(gs_id) == 0:
            form = GSForm(request.POST)
        else:
            form = GSForm(request.POST, instance=GoodAndServices.objects.get(id=gs_id))
        if form.is_valid():
            desc = request.POST.get('Description')
            part = request.POST.get('PrimarySupplierPartNo')
            a = GoodAndServices.objects.filter(Description=desc).filter(PrimarySupplierPartNo=part).count()
            print(a)
            if int(gs_id) == 0 and a > 0:
                print("Duplicate GS id: " + desc + ' - ' + part)
            else:
                form.save(commit=True)
            return gs_list(request)
        else:
            print(form.errors)
    else:
        form = GSForm(instance=GoodAndServices.objects.get(id=gs_id))
    return render(request, 'hort/gs_detail.html', {'form': form})
    
#
# LedgerAcct management
#
@login_required
def ledger(request):
    ledger_acct_list = LedgerAcct.objects.order_by('LedgerAcctNum')
    context = {'ledger_acct_list': ledger_acct_list}
    return render(request, 'hort/ledger_list.html', context)
    
@login_required
def ledger_detail(request, ledger_acct_id):
    # response = "<h2>This is LedgerAcctNum %s."
    # return HttpResponse(response % ledger_acct_id)
    ledger_acct_items = Details.objects.filter(Ledger=ledger_acct_id)
    return render(request, 'hort/ledger_acct_items.html',{'ledger_acct_items': ledger_acct_items})
    
#
# Orders and Details transaction management
#
@login_required
def invoice(request):
    invoice_list = Orders.objects.filter(Status='OP').order_by('id')
    #invoice_list = Orders.objects.all().order_by('StatusDT')
    context = {'invoice_list': invoice_list}
    #print(context)
    return render(request, 'hort/invoice_list.html', context)
    
@login_required
def invoice_detail(request, invoice_id):
    print("invoice_id = " + invoice_id)
    if int(invoice_id) == 0 and request.method != 'POST':
        form = InvoiceForm(initial={'Status':'OP','EnteredBy':3,'StatusBy':3})
        return render(request, 'hort/invoice_detail.html', {'form': form})
    if request.method == 'POST':
        if int(invoice_id) == 0:
            form = InvoiceForm(request.POST)
        else:
            form = InvoiceForm(request.POST, instance=Orders.objects.get(id=invoice_id))
        if form.is_valid():
            invoice = form.save(commit=True)
            print("form.cleaned_data...")
            print(form.cleaned_data)
            print("invoice.id...")
            print(invoice.id)
            #return invoice(request)
            if request.POST.get('Status') == 'OP':
                return invoice_item_list(request, invoice.id)
            else:
                return ff_invoice(request)
        else:
            print(form.errors)
    else:
        form = InvoiceForm(instance=Orders.objects.get(id=invoice_id))
    return render(request, 'hort/invoice_detail.html', {'form': form})

@login_required
def invoice_item_list(request, invoice_id):
    order_info = Orders.objects.get(id=invoice_id)
    cust_str = str(order_info.OrdersCustID)
    cust_arr = cust_str.split(" - ")
    custid = cust_arr[0]
    cust_info = Customer.objects.get(CustID=custid)
    item_info = Details.objects.filter(OrderID=invoice_id)
    item_total = Details.objects.filter(OrderID=invoice_id).aggregate(item_sum=Sum('ExtPrice'))
    print(item_total)
    context = {'order_info':order_info,'cust_info':cust_info,'item_info':item_info,'item_total':item_total}
    return render(request, 'hort/invoice_item.html', context)
    
@login_required
def invoice_item(request, invoice_id, detail_id):
    print("detail_id = " + detail_id)
    print("invoice_id = " + invoice_id)
    if int(detail_id) == 0 and request.method != 'POST':
        form = InvoiceItemsForm(initial={'OrderID':invoice_id,'CPEach':0,'QtyOrdered':1,'QtyInOrOut':0,'ExtPrice':0,'Ledger':9999})
        #form.fields['OrderID'].widget.attrs['disabled'] = 'disabled'  #for FK fields
        form.fields['OrderID'].widget.attrs['readonly'] = 'readonly'  #for text fields
        #form.fields['CPEach'].widget = forms.HiddenInput()
        form.fields['AcctEntry'].widget.attrs['onChange'] = 'Hide()'
        form.fields['QtyInOrOut'].widget = forms.HiddenInput()
        form.fields['ExtPrice'].widget = forms.HiddenInput()
        form.fields['Ledger'].widget = forms.HiddenInput()
        return render(request, 'hort/invoice_item_detail.html', {'form': form})
    if request.method == 'POST':
        gsid = request.POST.get('GSID')
        print("GSID = " + gsid)
        qty = int(request.POST.get('QtyOrdered'))
        print("QtyOrdered = " + str(qty))
        inout = Orders.objects.filter(id=invoice_id).values_list('InOrOut', flat=True)[0]
        print("InOrOut = " + str(inout))
        type = Orders.objects.filter(id=invoice_id).values_list('Type', flat=True)[0]
        print("Type = " + type)
        acct_flg = request.POST.get('AcctEntry')
        print("AcctEntry = " + str(acct_flg))
        if acct_flg == '1':
            cpe_s = request.POST.get('CPEach')
            cpe = float(cpe_s)
        elif type == 'P':
            cpe = GoodAndServices.objects.filter(id=gsid).values_list('Cost')[0][0]
        else:
            cpe = GoodAndServices.objects.filter(id=gsid).values_list('Price')[0][0]
        if inout == 1:
            ldgr = GoodAndServices.objects.filter(id=gsid).values_list('LedgerIn', flat=True)[0]
        else:
            ldgr = GoodAndServices.objects.filter(id=gsid).values_list('LedgerOut', flat=True)[0]
        qtyio = qty*inout
        extpr = qty*cpe
        mutable = request.POST._mutable
        request.POST._mutable = True
        # populate the request hidden fields (hack?)...
        request.POST['CPEach'] = cpe
        request.POST['QtyInOrOut'] = qtyio
        request.POST['ExtPrice'] = extpr
        request.POST['Ledger'] = ldgr
        # ...done
        request.POST._mutable = mutable
        if int(detail_id) == 0:
            form = InvoiceItemsForm(request.POST)
        else:
            form = InvoiceItemsForm(request.POST, instance=Details.objects.get(id=detail_id))
        if form.is_valid():
            print("form.cleaned_data...")
            print(form.cleaned_data)
            form.save(commit=True)
            return invoice_item_list(request, invoice_id)
        else:
            print(form.errors)
    else:
        form = InvoiceItemsForm(instance=Details.objects.get(id=detail_id))
        #form.fields['OrderID'].widget.attrs['disabled'] = 'disabled'  #for FK fields
        form.fields['OrderID'].widget.attrs['readonly'] = 'readonly'  #for text fields
        #form.fields['CPEach'].widget = forms.HiddenInput() # ...handling this in template
        form.fields['AcctEntry'].widget.attrs['onChange'] = 'Hide()'
        form.fields['QtyInOrOut'].widget = forms.HiddenInput()
        form.fields['ExtPrice'].widget = forms.HiddenInput()
        form.fields['Ledger'].widget = forms.HiddenInput()
    return render(request, 'hort/invoice_item_detail.html', {'form': form})

#
# Fulfillment and Accounting counter entry
#
@login_required
def tender(request, invoice_id, inout_multiplier, invoice_total):
    print("invoice_id = " + invoice_id)
    print("inout_multiplier = " + inout_multiplier)
    print("invoice_total = " + invoice_total)
    if request.method == 'POST':
        #print('\n'.join(list(request.POST)))
        form = InvoiceItemsForm(request.POST)
        if form.is_valid():
            print("form.cleaned_data...")
            print(form.cleaned_data)
            form.save(commit=True)
            order_info = Orders.objects.get(id=invoice_id)
            order_info.Status = "FF"
            order_info.save(update_fields=["Status"])
            return invoice(request)
        else:
            print(form.errors)
    else:
        order_info = Orders.objects.get(id=invoice_id)
        inverse_qty = int(inout_multiplier)*(-1)
        form = InvoiceItemsForm(initial={'OrderID':invoice_id,'GSID':8,'CPEach':invoice_total,'AcctEntry':1,'QtyOrdered':1,'QtyInOrOut':inverse_qty,'ExtPrice':invoice_total,'Ledger':1000})
        form.fields['OrderID'].widget = forms.HiddenInput()
        form.fields['CPEach'].widget.attrs['readonly'] = 'readonly'
        form.fields['QtyInOrOut'].widget.attrs['readonly'] = 'readonly'
        form.fields['QtyOrdered'].widget.attrs['readonly'] = 'readonly'
        form.fields['AcctEntry'].widget = forms.HiddenInput()
        form.fields['QtyInOrOut'].widget = forms.HiddenInput()
        form.fields['ExtPrice'].widget = forms.HiddenInput()
        form.fields['Ledger'].widget = forms.HiddenInput()
        form.fields['ScheduledStartDT'].widget = forms.HiddenInput()
        form.fields['ScheduledCompleteDT'].widget = forms.HiddenInput()
        return render(request, 'hort/invoice_tender.html', {'order_info':order_info,'form': form})

#
# Fulfilled Orders and Trial Balance (PSX12)
#
@login_required
def ff_invoice(request):
    invoice_list = Orders.objects.filter(Status='FF').order_by('id')
    return render(request, 'hort/ff_invoice_list.html', {'invoice_list': invoice_list})

@login_required
def journal_rpt(request):
    conn = sqlite3.connect('KCspr16eve.sqlite3')
    c = conn.cursor()
    rows = c.execute('select * from hort_journal_rpt')
    q_list = rows.fetchall()
    #print(q_list)
    j_rpt = '"'
    for each_row in q_list:
        j_rpt = j_rpt + each_row[0]
    j_rpt = j_rpt + '"'
    print(j_rpt)
    journal_rpt = eval(j_rpt)
    print(journal_rpt)
    conn.close()
    return render(request, 'hort/journal_rpt.html', {'journal_rpt':journal_rpt})
    
@login_required
def psx12(request):    
    conn = sqlite3.connect('KCspr16eve.sqlite3')
    c = conn.cursor()
    rows = c.execute('select * from hort_psx12')
    list = rows.fetchall()
    cnt = 0
    raw_str = '"'
    for line in list:
        raw_str = raw_str + line[0] + '\\' + 'r' + '\\' + 'n'
        cnt += 1
    footer = 'EJV*' + str(cnt)
    raw_str = raw_str + footer + '"'
    print('raw_str=')
    print(raw_str)
    conn = http.client.HTTPConnection("info465.info")
    payload = eval(raw_str)
    print('payload=')
    print(payload)
    headers = {'cache-control': "no-cache"}
    conn.request("POST", "/ledgerengine/psX12InWebSvc.php", payload, headers)
    res = conn.getresponse()
    psx12_data = res.read()
    psx12_text = psx12_data.decode("utf-8")
    #print(psx12_text)
    #print(psx12_data)
    conn.close()
    return render(request, 'hort/psx12_resp.html', {'psx12_text':psx12_text})
    
#
# DB Utilities
#
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#
# Order Audit
#
@login_required
def order_audit(request):
    conn = sqlite3.connect('KCspr16eve.sqlite3')
    conn.row_factory = dict_factory
    curs = conn.cursor()
    curs.execute('select * from hort_order_audit')
    audit_info = curs.fetchall()
    #print(audt)
    conn.close()
    return render(request, 'hort/order_audit.html', {'audit_info':audit_info})

#
# Open Order Schedule
#
@login_required
def open_order_sched(request):
    conn = sqlite3.connect('KCspr16eve.sqlite3')
    c = conn.cursor()
    rows = c.execute('select * from hort_crew_orders')
    list = rows.fetchall()
    #print(list)
    sched = '"'
    for each_row in list:
        sched = sched + each_row[0]
    sched = sched + '"'
    print(sched)
    rpt_sched = eval(sched)
    print(rpt_sched)
    conn.close()
    return render(request, 'hort/crew_sched.html', {'rpt_sched':rpt_sched})

#
# Customer Order Schedule
#
@login_required
def my_service(request, cust_id):
    print('cust_id = ' + cust_id)
    order_ids = ",".join(map(str,Orders.objects.filter(OrdersCustID=cust_id).values_list('id', flat=True)))
    print("order_ids =")
    print(order_ids)
    conn = sqlite3.connect('KCspr16eve.sqlite3')
    c = conn.cursor()
    stmt = 'select ord_line from hort_cust_orders where OrderID in (' + order_ids + ')'
    rows = c.execute(stmt)
    list = rows.fetchall()
    #print(list)
    sched = '"'
    for each_row in list:
        sched = sched + each_row[0]
    sched = sched + '"'
    print(sched)
    cust_sched = eval(sched)
    print(cust_sched)
    conn.close()
    return render(request, 'hort/cust_sched.html', {'cust_sched':cust_sched})
    