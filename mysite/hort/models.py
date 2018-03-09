# File       :  models.py
# Description:  Django MVC model classes for "hort" application
# Author     :  Ken Carbaugh
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.conf.urls import patterns, url, include

class UserProfile(models.Model):
    User = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    Url = models.URLField("Website", blank=True)
    Company = models.CharField(max_length=50, blank=True)
    PrimaryRelationship = models.CharField(max_length=12, blank=True)
    PassQuestion = models.CharField(max_length=60, blank=True)
    PassAnswer = models.CharField(max_length=60, blank=True)
    PSX12EnterpriseID = models.CharField(max_length=6, blank=True)
    MailingAddress = models.CharField(max_length=60, blank=True)
    MailingExtraLine = models.CharField(max_length=60, blank=True)
    MailingPostOffice = models.CharField(max_length=60, blank=True)
    MailingZip = models.CharField(max_length=60, blank=True)
    PhoneNumbers = models.CharField(max_length=60, blank=True)
    Notes = models.CharField(max_length=1000, blank=True)
    SourceOfThisRecord = models.CharField(max_length=60, blank=True)
    SourceID = models.CharField(max_length=60, blank=True)
    TakenOnDT = models.DateTimeField(auto_now_add=True)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
    
class Customer(models.Model):
    SUPPLIER = 'SUP'
    CUSTOMER = 'CUS'
    INVESTOR = 'INV'
    OWNER = 'OWN'
    EMPLOYEE = 'EMP'
    RELATIONSHIP_CHOICES = ((SUPPLIER, 'Supplier'), (CUSTOMER, 'Customer'), (INVESTOR, 'Investor'),(OWNER, 'Owner'),(EMPLOYEE, 'Employee'),)
    CustID = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=50, blank=True)
    LastName = models.CharField(max_length=50)
    ExtraLine = models.CharField(max_length=75, blank=True)
    StreetAddress = models.CharField(max_length=75)
    PostOffice = models.CharField(max_length=50)
    ZipCode = models.CharField(max_length=10)
    Relationship = models.CharField(max_length=3, choices=RELATIONSHIP_CHOICES, default=CUSTOMER)
    User_id = models.IntegerField(default=0)
    def __str__(self):
        return self.CustID + ' - ' + self.LastName
        
class LedgerAcct(models.Model):
    LedgerAcctNum = models.IntegerField(primary_key=True)
    LedgerAcctTxt = models.CharField(max_length=50)
    def __str__(self):
        return self.LedgerAcctTxt
        
class GoodAndServices(models.Model):
    GOOD = 'Good'
    SERVICES = 'Svcs'
    ACCOUNTING = 'Acct'
    CLASS_CHOICES = ((GOOD, 'Good'), (SERVICES, 'Svcs'),(ACCOUNTING, 'Acct'),)
    #L_IN = LedgerAcct.objects.filter(LedgerAcctNum__lt=2000).values_list('LedgerAcctNum', 'LedgerAcctTxt')
    #L_OUT = LedgerAcct.objects.filter(LedgerAcctNum__gte=2000).values_list('LedgerAcctNum', 'LedgerAcctTxt')
    #L_IN = LedgerAcct.objects.values_list('LedgerAcctNum', 'LedgerAcctNum')
    L_ITER = [ ( p[0], '{0} - {1}'.format( p[0], p[1] ),) for p in LedgerAcct.objects.values_list('LedgerAcctNum', 'LedgerAcctTxt') ]
    SUPPLIERS = Customer.objects.filter(Q(Relationship='SUP') | Q(Relationship='OWN')).values_list('CustID', 'LastName')
    Description = models.CharField(max_length=50)
    Class = models.CharField(max_length=12, choices=CLASS_CHOICES)
    LedgerIn = models.IntegerField(default=0, choices=L_ITER)   #FK to LedgerAcct?
    Cost = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    LedgerOut = models.IntegerField(default=0, choices=L_ITER)   #FK to LedgerAcct?
    Price = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    PrimarySupplier = models.CharField(max_length=50, choices=SUPPLIERS)
    PrimarySupplierPartNo = models.CharField(max_length=20, blank=True)
    #ImageName = models.CharField(max_length=60, blank=True)
    #QOH = models.DecimalField(max_digits=14, decimal_places=4, default=0.0000)
    #SafetyLevel = models.DecimalField(max_digits=14, decimal_places=4, default=0.0000)
    #EOQ = models.DecimalField(max_digits=14, decimal_places=4, default=0.0000)
    def __str__(self):
        return '[' + self.Class + '] ' +self.Description

class Orders(models.Model):
    IN = 1
    OUT = -1
    IN_OR_OUT_CHOICES = ((IN, 'In [1]'), (OUT, 'Out [-1]'),)
    OPEN = 'OP'
    FULLFILLED = 'FF'
    #CANCELLED = 'CA'
    #SHIPPED = 'SH'
    STATUS_CHOICES = ((OPEN, 'Open'), (FULLFILLED, 'Fullfilled'),) # (CANCELLED, 'Cancelled'), (SHIPPED, 'Shipped'),)
    PURCH = 'P'
    SALE = 'S'
    TYPE_CHOICES = ((PURCH, 'Purchase'), (SALE, 'Sale'),)
    USER_CHOICES = User.objects.all().values_list('id', 'username')
    Type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    #InitialStatus = models.CharField(max_length=10, choices=STATUS_CHOICES)
    Status = models.CharField(max_length=10, choices=STATUS_CHOICES, blank=True)
    StatusDT = models.DateTimeField(auto_now=True)
    StatusBy = models.IntegerField(choices=USER_CHOICES, blank=True)  #ref to auth_user.id field?
    OrderNotes = models.TextField(max_length=1000, blank=True)
    AccountingDate = models.DateField(null=True, blank=True)
    EnteredDT = models.DateTimeField(auto_now_add=True)
    EnteredBy = models.IntegerField(choices=USER_CHOICES)  #ref to auth_user.id field?
    #DataEntryCompleteDT = models.DateTimeField(null=True, blank=True)
    #DataEntryCompleteBy = models.IntegerField(choices=USER_CHOICES, blank=True)  #ref to auth_user.id field?
    #CheckedOutToFillDT = models.DateTimeField(null=True, blank=True)
    #CheckedOutToFillBy = models.IntegerField(choices=USER_CHOICES, blank=True)  #ref to auth_user.id field?
    OrdersCustID = models.ForeignKey('Customer', on_delete=models.CASCADE)   #ref to hort_customer.id field?
    InOrOut = models.IntegerField(choices=IN_OR_OUT_CHOICES, blank=True)
    #QueuedForPSX12DT = models.DateTimeField(null=True, blank=True)
    #SentViaPXS12DT = models.DateTimeField(null=True, blank=True)
    PONumber = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return str(self.id)

class Details(models.Model):
    USER_CHOICES = User.objects.all().values_list('id', 'username')
    L_ITER = [ ( p[0], '{0} - {1}'.format( p[0], p[1] ),) for p in LedgerAcct.objects.values_list('LedgerAcctNum', 'LedgerAcctTxt') ]
    NO = 0
    YES = 1
    ACCT_ENTRY_CHOICES = ((NO, 'No'), (YES, 'Yes'),)
    AcctEntry = models.IntegerField(choices=ACCT_ENTRY_CHOICES, default=0)
    #OrderID = models.ForeignKey('Orders', on_delete=models.CASCADE)
    OrderID = models.IntegerField(null=False)
    #DetailDT = models.DateTimeField(auto_now=True)
    #DetailBy = models.IntegerField(choices=USER_CHOICES)  #ref to auth_user.id field?
    #OrigDetailID = models.IntegerField(null=True, blank=True)
    #BackOrderDetailID = models.IntegerField(null=True, blank=True)
    GSID = models.ForeignKey('GoodAndServices', on_delete=models.CASCADE)
    QtyOrdered = models.IntegerField(null=True)
    QtyInOrOut = models.IntegerField(null=True)
    #QtyDelivered = models.DecimalField(max_digits=14, decimal_places=4, blank=True)
    CPEach = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    ExtPrice = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    #Ledger = models.IntegerField(default=0, choices=L_ITER)   #FK to LedgerAcct
    Ledger = models.IntegerField(null=True)
    #ShipToCustID = models.ForeignKey('Customer', on_delete=models.CASCADE)   #ref to hort_customer.id field?
    ScheduledStartDT = models.DateTimeField(null=True, blank=True)
    ScheduledCompleteDT = models.DateTimeField(null=True, blank=True)
    #ActualStartDT = models.DateTimeField(null=True, blank=True)
    #ActualCompleteDT = models.DateTimeField(null=True, blank=True)
    #FrontNotes = models.TextField(max_length=1000, blank=True)
    #BackNotes = models.TextField(max_length=1000, blank=True)
    def __str__(self):
        return str(self.id)