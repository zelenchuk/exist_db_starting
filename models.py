# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tbltestcodes(models.Model):
    id = models.IntegerField()
    labcode = models.CharField(db_column='LabCode', max_length=20)  # Field name made lowercase.
    testcode = models.CharField(db_column='TestCode', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500)  # Field name made lowercase.
    aka = models.CharField(db_column='AKA', max_length=500, blank=True, null=True)  # Field name made lowercase.
    subtests = models.CharField(db_column='SubTests', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder', blank=True, null=True)  # Field name made lowercase.
    spec_req = models.CharField(db_column='Spec_Req', max_length=500, blank=True, null=True)  # Field name made lowercase.
    spec_vol = models.CharField(db_column='Spec_Vol', max_length=500, blank=True, null=True)  # Field name made lowercase.
    spec_cont = models.CharField(db_column='Spec_Cont', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '___tblTestCodes'


class Cpt2Diagnoses(models.Model):
    cptcode = models.CharField(db_column='cptCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cptdescription = models.CharField(db_column='cptDescription', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    diagnosiscode = models.CharField(db_column='diagnosisCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    diagnosisdescription = models.CharField(db_column='diagnosisDescription', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__cpt2diagnoses'


class Cpt2DiagnosesCopy(models.Model):
    cptcode = models.CharField(db_column='cptCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cptdescription = models.CharField(db_column='cptDescription', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    diagnosiscode = models.CharField(db_column='diagnosisCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    diagnosisdescription = models.CharField(db_column='diagnosisDescription', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__cpt2diagnoses_copy'


class Antigen(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstname = models.CharField(db_column='firstName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255)  # Field name made lowercase.
    dob = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=45)
    sex = models.CharField(max_length=1)
    phone = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    clientid = models.BigIntegerField(db_column='clientID', blank=True, null=True)  # Field name made lowercase.
    result = models.CharField(max_length=13, blank=True, null=True)
    status = models.CharField(max_length=11)
    zip = models.CharField(max_length=45)
    collectiondate = models.DateTimeField(db_column='collectionDate', blank=True, null=True)  # Field name made lowercase.
    resultdate = models.DateTimeField(db_column='resultDate', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField()
    ordernumber = models.CharField(db_column='orderNumber', max_length=45)  # Field name made lowercase.
    accessionid = models.CharField(db_column='accessionID', max_length=45)  # Field name made lowercase.
    insurancename = models.CharField(db_column='insuranceName', max_length=255)  # Field name made lowercase.
    insuranceid = models.IntegerField(db_column='insuranceID', blank=True, null=True)  # Field name made lowercase.
    policy = models.CharField(max_length=255)
    ispcr = models.IntegerField(db_column='isPCR')  # Field name made lowercase.
    requisitionid = models.CharField(db_column='requisitionID', max_length=45)  # Field name made lowercase.
    day = models.DateField(blank=True, null=True)
    base64 = models.CharField(max_length=255)
    test = models.CharField(max_length=45)
    question1 = models.CharField(max_length=45)
    question2 = models.CharField(max_length=45)
    question3 = models.CharField(max_length=45)
    question4 = models.CharField(max_length=45)
    question5 = models.CharField(max_length=45)
    question6 = models.CharField(max_length=45)
    question7 = models.CharField(max_length=45)
    question8 = models.CharField(max_length=45)
    passport = models.CharField(max_length=45)
    pcrdate = models.DateTimeField(db_column='pcrDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'antigen'
        unique_together = (('lastname', 'firstname', 'dob', 'clientid', 'day'),)


class Auditfavorites(models.Model):
    physicianid = models.IntegerField(db_column='physicianID')  # Field name made lowercase.
    favorites = models.CharField(max_length=9)
    action = models.CharField(max_length=7)
    before = models.TextField(blank=True, null=True)
    after = models.TextField(blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auditFavorites'


class Auditgeneral(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    action = models.CharField(max_length=8)
    description = models.CharField(max_length=255, blank=True, null=True)
    table = models.CharField(max_length=45)
    tableid = models.IntegerField(db_column='tableID', blank=True, null=True)  # Field name made lowercase.
    oldvalues = models.JSONField(db_column='oldValues', blank=True, null=True)  # Field name made lowercase.
    newvalues = models.JSONField(db_column='newValues', blank=True, null=True)  # Field name made lowercase.
    insertedvalues = models.JSONField(db_column='insertedValues', blank=True, null=True)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auditGeneral'


class Audithistology(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    table = models.CharField(max_length=255)
    tableid = models.IntegerField(db_column='tableID')  # Field name made lowercase.
    field = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    before = models.TextField(blank=True, null=True)
    after = models.TextField(blank=True, null=True)
    misc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auditHistology'


class Auditsigninandout(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    date = models.DateTimeField()
    host = models.CharField(max_length=100, blank=True, null=True)
    action = models.CharField(max_length=10)
    ip = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auditSignInAndOut'


class Billingcomments(models.Model):
    id = models.SmallAutoField(primary_key=True)
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    who = models.CharField(max_length=45)
    comment = models.CharField(max_length=10)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'billingComments'


class Billingpermissions(models.Model):
    userid = models.IntegerField(db_column='userID', unique=True)  # Field name made lowercase.
    viewaudits = models.IntegerField(db_column='viewAudits')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'billingPermissions'


class Bookings(models.Model):
    id = models.BigAutoField(primary_key=True)
    ordernumber = models.CharField(db_column='orderNumber', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=255)  # Field name made lowercase.
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=45)
    zip = models.CharField(max_length=45)
    isinsured = models.CharField(db_column='isInsured', max_length=45)  # Field name made lowercase.
    insurancename = models.CharField(db_column='insuranceName', max_length=255)  # Field name made lowercase.
    policy = models.CharField(max_length=45)
    relationtoinsured = models.CharField(db_column='relationToInsured', max_length=45)  # Field name made lowercase.
    policyholder = models.CharField(db_column='policyHolder', max_length=255)  # Field name made lowercase.
    race = models.CharField(max_length=45)
    ethnicity = models.CharField(max_length=45)
    symptoms = models.JSONField(blank=True, null=True)
    exposure = models.JSONField(blank=True, null=True)
    risk = models.JSONField(blank=True, null=True)
    psccode = models.CharField(db_column='pscCode', max_length=45)  # Field name made lowercase.
    scheduledate = models.DateField(db_column='scheduleDate', blank=True, null=True)  # Field name made lowercase.
    scheduletime = models.TimeField(db_column='scheduleTime', blank=True, null=True)  # Field name made lowercase.
    senttoudotest = models.IntegerField(db_column='sentToUdotest')  # Field name made lowercase.
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bookings'


class Callpickup(models.Model):
    clientid = models.IntegerField(db_column='clientID')  # Field name made lowercase.
    ordertype = models.CharField(db_column='orderType', max_length=7, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    dob = models.CharField(max_length=15)
    contactname = models.CharField(db_column='contactName', max_length=45)  # Field name made lowercase.
    contactphone = models.CharField(db_column='contactPhone', max_length=45)  # Field name made lowercase.
    resultsby = models.CharField(db_column='resultsBy', max_length=3, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(max_length=255)
    date = models.DateTimeField(blank=True, null=True)
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    confirmation = models.CharField(max_length=45)
    driverid = models.IntegerField(db_column='driverID', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=9)
    qntpickedup = models.CharField(db_column='qntPickedUp', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pickedupdate = models.DateTimeField(db_column='pickedUpDate', blank=True, null=True)  # Field name made lowercase.
    qntdelivered = models.CharField(db_column='qntDelivered', max_length=45, blank=True, null=True)  # Field name made lowercase.
    datedelivered = models.DateTimeField(db_column='dateDelivered', blank=True, null=True)  # Field name made lowercase.
    confirmeddate = models.DateTimeField(db_column='confirmedDate', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(max_length=255)
    cancelreason = models.CharField(db_column='cancelReason', max_length=255)  # Field name made lowercase.
    base64 = models.CharField(max_length=45, blank=True, null=True)
    confirmuser = models.CharField(db_column='confirmUser', max_length=255)  # Field name made lowercase.
    labcomment = models.CharField(db_column='labComment', max_length=255)  # Field name made lowercase.
    routeid = models.IntegerField(db_column='routeID', blank=True, null=True)  # Field name made lowercase.
    pickupdate = models.DateTimeField(db_column='pickupDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'callPickup'


class Callpickuptests(models.Model):
    id = models.BigAutoField(primary_key=True)
    callpickupid = models.BigIntegerField(db_column='callPickUpID')  # Field name made lowercase.
    code = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'callPickupTests'


class Casecalllist(models.Model):
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    department = models.CharField(max_length=45)
    filename = models.CharField(db_column='fileName', max_length=255)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    comments = models.CharField(max_length=2000)
    iscompleted = models.IntegerField(db_column='isCompleted')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    completedate = models.DateTimeField(db_column='completeDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'caseCallList'


class Changes(models.Model):
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    who = models.CharField(max_length=45)
    action = models.CharField(max_length=255)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'changes'


class Claims(models.Model):
    id = models.SmallAutoField(primary_key=True)
    file = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'claims'


class Client2Equipment(models.Model):
    clientid = models.IntegerField(db_column='clientID')  # Field name made lowercase.
    type = models.CharField(max_length=7, blank=True, null=True)
    model = models.CharField(max_length=455, blank=True, null=True)
    quantity = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client2equipment'


class Client2Orderset(models.Model):
    clientid = models.IntegerField(db_column='clientID')  # Field name made lowercase.
    ordersetid = models.CharField(db_column='orderSetID', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client2orderSet'
        unique_together = (('clientid', 'ordersetid'),)


class Clientellkayinsurances2Insurances(models.Model):
    clientid = models.IntegerField(db_column='clientID')  # Field name made lowercase.
    insuranceid = models.IntegerField(db_column='insuranceID')  # Field name made lowercase.
    ellkayinsuranceid = models.CharField(db_column='ellkayInsuranceID', max_length=45)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    addressline1 = models.CharField(db_column='addressLine1', max_length=255)  # Field name made lowercase.
    addressline2 = models.CharField(db_column='addressLine2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=45)
    country = models.CharField(max_length=45, blank=True, null=True)
    zip = models.CharField(max_length=45, blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientEllkayInsurances2Insurances'


class Clientschedule(models.Model):
    clientid = models.IntegerField(db_column='clientID')  # Field name made lowercase.
    day = models.CharField(max_length=45)
    open = models.CharField(max_length=45)
    close = models.CharField(max_length=45)
    notes = models.CharField(max_length=4000)
    contactperson = models.CharField(db_column='contactPerson', max_length=255)  # Field name made lowercase.
    contactphone = models.CharField(db_column='contactPhone', max_length=45)  # Field name made lowercase.
    boxinhouse = models.IntegerField(db_column='boxInHouse')  # Field name made lowercase.
    boxlocation = models.CharField(db_column='boxLocation', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientSchedule'
        unique_together = (('clientid', 'day'),)


class Clientservicespermissions(models.Model):
    userid = models.IntegerField(db_column='userID', unique=True)  # Field name made lowercase.
    modifyclientphysicians = models.IntegerField(db_column='modifyClientPhysicians')  # Field name made lowercase.
    it = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clientServicesPermissions'


class Clientsideerrors(models.Model):
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    app = models.CharField(max_length=45)
    user = models.IntegerField()
    message = models.TextField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    line = models.CharField(max_length=45, blank=True, null=True)
    column = models.CharField(max_length=45, blank=True, null=True)
    stack = models.TextField(blank=True, null=True)
    platform = models.JSONField(blank=True, null=True)
    errortime = models.DateTimeField(db_column='errorTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientSideErrors'


class Clients(models.Model):
    salesgroupid = models.IntegerField(db_column='salesGroupID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    login = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=5, blank=True, null=True)
    fax = models.CharField(max_length=12, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    phoneext = models.CharField(db_column='phoneExt', max_length=5, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField()
    isactive = models.IntegerField(db_column='isActive')  # Field name made lowercase.
    isigs = models.IntegerField(db_column='isIGS')  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    billinginsidecompany = models.IntegerField(db_column='billingInsideCompany')  # Field name made lowercase.
    sendoutpriority = models.IntegerField(db_column='sendoutPriority')  # Field name made lowercase.
    cuttime = models.TimeField(db_column='cutTime')  # Field name made lowercase.
    ellkay = models.CharField(db_column='ellKay', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isvip = models.IntegerField(db_column='isVIP')  # Field name made lowercase.
    ischartrequired = models.IntegerField(db_column='isChartRequired')  # Field name made lowercase.
    emr = models.CharField(max_length=45, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    issomos = models.IntegerField(db_column='isSomos')  # Field name made lowercase.
    fl = models.IntegerField()
    issomosschool = models.IntegerField(db_column='isSomosSchool')  # Field name made lowercase.
    barcode = models.CharField(max_length=45)
    udotest = models.IntegerField()
    ez = models.IntegerField()
    qcc = models.IntegerField()
    ezh = models.IntegerField()
    dma = models.IntegerField()
    qcco = models.IntegerField()
    qccw = models.IntegerField()
    qcco2 = models.IntegerField()
    dymo550 = models.IntegerField()
    qccf = models.IntegerField()
    clia = models.CharField(max_length=45)
    clianumber = models.CharField(db_column='cliaNumber', max_length=45)  # Field name made lowercase.
    cliaaddress = models.CharField(db_column='cliaAddress', max_length=255)  # Field name made lowercase.
    cliacity = models.CharField(db_column='cliaCity', max_length=255)  # Field name made lowercase.
    cliaphone = models.CharField(db_column='cliaPhone', max_length=45)  # Field name made lowercase.
    cliadirector = models.CharField(db_column='cliaDirector', max_length=255)  # Field name made lowercase.
    ishomeinsurance = models.IntegerField(db_column='isHomeInsurance')  # Field name made lowercase.
    isflorida = models.IntegerField(db_column='isFlorida')  # Field name made lowercase.
    activedate = models.DateField(db_column='activeDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clients'


class Clients2Physicians(models.Model):
    clientid = models.IntegerField(db_column='clientID')  # Field name made lowercase.
    physicianid = models.IntegerField(db_column='physicianID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clients2physicians'
        unique_together = (('clientid', 'physicianid'),)


class Commentdictionary(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=7)
    description = models.CharField(max_length=45)
    content = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commentDictionary'


class Commondiagnoses(models.Model):
    code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'commonDiagnoses'


class Covidsite(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstname = models.CharField(db_column='firstName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255)  # Field name made lowercase.
    dob = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=45)
    sex = models.CharField(max_length=1)
    phone = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    clientid = models.BigIntegerField(db_column='clientID', blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(max_length=45)
    collectiondate = models.DateTimeField(db_column='collectionDate', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField()
    ordernumber = models.CharField(db_column='orderNumber', max_length=45)  # Field name made lowercase.
    day = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'covidSite'
        unique_together = (('lastname', 'firstname', 'dob', 'clientid', 'day'),)


class Cpthistory(models.Model):
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    testhistoryid = models.IntegerField(db_column='testHistoryID')  # Field name made lowercase.
    payerclaimnumber = models.CharField(db_column='payerClaimNumber', max_length=40)  # Field name made lowercase.
    patientidentifier = models.CharField(db_column='patientIdentifier', max_length=20)  # Field name made lowercase.
    notes = models.CharField(max_length=60)
    status = models.CharField(max_length=11)
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    units = models.IntegerField()
    modifier = models.TextField()
    price = models.FloatField()
    billed = models.FloatField()
    allowed = models.FloatField()
    deductibles = models.FloatField()
    copay = models.FloatField()
    coinsurance = models.FloatField()
    paid = models.FloatField(blank=True, null=True)
    datesent = models.DateField(db_column='dateSent', blank=True, null=True)  # Field name made lowercase.
    datebilled = models.DateField(db_column='dateBilled', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cptHistory'
        unique_together = (('patientid', 'testhistoryid', 'code'),)


class Cpts(models.Model):
    id = models.SmallAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=6, blank=True, null=True)
    description = models.CharField(max_length=60, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cpts'


class Cpts2Diagnoses(models.Model):
    cptcode = models.CharField(db_column='cptCode', max_length=6)  # Field name made lowercase.
    diagnosiscode = models.CharField(db_column='diagnosisCode', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cpts2diagnoses'


class Cytocontestdetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    salesid = models.CharField(db_column='salesID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    clientid = models.CharField(db_column='clientID', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    patientsqnt = models.IntegerField(db_column='patientsQNT', blank=True, null=True)  # Field name made lowercase.
    salesqnt = models.CharField(db_column='salesQNT', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cytoContestDetails'


class Cytologycases(models.Model):
    accessionid = models.CharField(db_column='accessionID', max_length=45)  # Field name made lowercase.
    patientid = models.IntegerField(db_column='patientID', unique=True)  # Field name made lowercase.
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cytologyCases'


class Cytologycontest(models.Model):
    salesid = models.CharField(db_column='salesID', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    salesname = models.CharField(db_column='salesName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    testqnt = models.IntegerField(db_column='testQNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cytologyContest'


class Cytologycontrols(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    slidehybridizationdate = models.DateField(db_column='slideHybridizationDate')  # Field name made lowercase.
    totalslides = models.IntegerField(db_column='totalSlides')  # Field name made lowercase.
    slideposthybridizationdate = models.DateField(db_column='slidePostHybridizationDate')  # Field name made lowercase.
    controlnumber = models.CharField(db_column='controlNumber', max_length=45)  # Field name made lowercase.
    probelotnumber = models.CharField(db_column='probeLotNumber', max_length=45)  # Field name made lowercase.
    probeexpirationdate = models.DateField(db_column='probeExpirationDate')  # Field name made lowercase.
    reagentlotnumber = models.CharField(db_column='reagentLotNumber', max_length=45)  # Field name made lowercase.
    reagentexpirationdate = models.DateField(db_column='reagentExpirationDate')  # Field name made lowercase.
    controllotnumber = models.CharField(db_column='controlLotNumber', max_length=45)  # Field name made lowercase.
    controlexpirationdate = models.DateField(db_column='controlExpirationDate')  # Field name made lowercase.
    controls = models.CharField(max_length=4, blank=True, null=True)
    prepquality = models.CharField(db_column='prepQuality', max_length=10, blank=True, null=True)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cytologyControls'


class Cytologycontrols2Slides(models.Model):
    cytologycontrolid = models.IntegerField(db_column='cytologyControlID')  # Field name made lowercase.
    cytologyslideid = models.IntegerField(db_column='cytologySlideID')  # Field name made lowercase.
    result = models.CharField(max_length=14, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cytologyControls2slides'


class Cytologyformgyn(models.Model):
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    cytologyslideid = models.IntegerField(db_column='cytologySlideID')  # Field name made lowercase.
    patienthistory = models.CharField(db_column='patientHistory', max_length=40)  # Field name made lowercase.
    routinescreen = models.IntegerField(db_column='routineScreen')  # Field name made lowercase.
    abnormalbleeding = models.IntegerField(db_column='abnormalBleeding')  # Field name made lowercase.
    menopausal = models.CharField(max_length=3, blank=True, null=True)
    other = models.CharField(max_length=255, blank=True, null=True)
    hrt = models.IntegerField(blank=True, null=True)
    previousdysplasia = models.IntegerField(db_column='previousDysplasia', blank=True, null=True)  # Field name made lowercase.
    radiationtherapy = models.IntegerField(db_column='radiationTherapy', blank=True, null=True)  # Field name made lowercase.
    highrisk = models.IntegerField(db_column='highRisk', blank=True, null=True)  # Field name made lowercase.
    hysterectomy = models.IntegerField(blank=True, null=True)
    iudinplace = models.IntegerField(db_column='iudInPlace', blank=True, null=True)  # Field name made lowercase.
    discharge = models.IntegerField(blank=True, null=True)
    vaginitis = models.IntegerField(blank=True, null=True)
    previouspap = models.DateField(db_column='previousPAP', blank=True, null=True)  # Field name made lowercase.
    papclassification = models.CharField(db_column='PAPClassification', max_length=20, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(max_length=255, blank=True, null=True)
    specimenreceived = models.CharField(db_column='specimenReceived', max_length=40, blank=True, null=True)  # Field name made lowercase.
    specimensource = models.CharField(db_column='specimenSource', max_length=40, blank=True, null=True)  # Field name made lowercase.
    lastmenstrualperiod = models.DateField(db_column='lastMenstrualPeriod', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cytologyFormGYN'
        unique_together = (('patientid', 'cytologyslideid'),)


class Cytologyformngyn(models.Model):
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    cytologyslideid = models.IntegerField(db_column='cytologySlideID')  # Field name made lowercase.
    specimenreceived = models.CharField(db_column='specimenReceived', max_length=40, blank=True, null=True)  # Field name made lowercase.
    specimentype = models.CharField(db_column='specimenType', max_length=75, blank=True, null=True)  # Field name made lowercase.
    specimensource = models.CharField(db_column='specimenSource', max_length=75, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    preparedslidetype = models.CharField(db_column='preparedSlideType', max_length=75, blank=True, null=True)  # Field name made lowercase.
    fixative = models.CharField(max_length=40, blank=True, null=True)
    stain = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    turbidity = models.CharField(max_length=20, blank=True, null=True)
    preparedslidesreceived = models.JSONField(db_column='preparedSlidesReceived', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    other = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cytologyFormNGYN'
        unique_together = (('cytologyslideid', 'patientid'),)


class Cytologyinstruments2Slidecount(models.Model):
    instrumentid = models.IntegerField(db_column='instrumentID', unique=True)  # Field name made lowercase.
    processedslidecountgyn = models.IntegerField(db_column='processedSlideCountGYN')  # Field name made lowercase.
    processedslidecountngyn = models.IntegerField(db_column='processedSlideCountNGYN')  # Field name made lowercase.
    processedslidecountgyn40 = models.IntegerField(db_column='processedSlideCountGYN40')  # Field name made lowercase.
    processedslidecountngyn40 = models.IntegerField(db_column='processedSlideCountNGYN40')  # Field name made lowercase.
    processedslidecountgyn250 = models.IntegerField(db_column='processedSlideCountGYN250')  # Field name made lowercase.
    processedslidecountngyn250 = models.IntegerField(db_column='processedSlideCountNGYN250')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cytologyInstruments2SlideCount'


class Cytologypermissions(models.Model):
    userid = models.IntegerField(db_column='userID', unique=True)  # Field name made lowercase.
    editinstruments = models.IntegerField(db_column='editInstruments')  # Field name made lowercase.
    editbatchresults = models.IntegerField(db_column='editBatchResults')  # Field name made lowercase.
    viewaudits = models.IntegerField(db_column='viewAudits')  # Field name made lowercase.
    editpermissions = models.IntegerField(db_column='editPermissions')  # Field name made lowercase.
    editcomments = models.IntegerField(db_column='editComments')  # Field name made lowercase.
    iscytotech = models.IntegerField(db_column='isCytotech')  # Field name made lowercase.
    ispathologist = models.IntegerField(db_column='isPathologist')  # Field name made lowercase.
    isadmin = models.IntegerField(db_column='isAdmin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cytologyPermissions'


class Cytologyreports(models.Model):
    cytologyslideid = models.IntegerField(db_column='cytologySlideID')  # Field name made lowercase.
    filename = models.CharField(db_column='fileName', max_length=255)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cytologyReports'


class Cytologyresults(models.Model):
    accessionid = models.CharField(db_column='accessionID', max_length=45)  # Field name made lowercase.
    dx = models.CharField(max_length=45)
    date = models.DateTimeField()
    clientid = models.IntegerField(db_column='clientID')  # Field name made lowercase.
    isabnormal = models.IntegerField(db_column='isAbnormal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cytologyResults'
        unique_together = (('accessionid', 'dx'),)


class Cytologyslides(models.Model):
    accessionid = models.CharField(db_column='accessionID', max_length=14, blank=True, null=True)  # Field name made lowercase.
    testhistoryid = models.IntegerField(db_column='testHistoryID', unique=True, blank=True, null=True)  # Field name made lowercase.
    slidenumber = models.CharField(db_column='slideNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    numberofslides = models.IntegerField(db_column='numberOfSlides', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(max_length=255, blank=True, null=True)
    entrydate = models.DateTimeField(db_column='entryDate', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    traylocation = models.CharField(db_column='trayLocation', max_length=45)  # Field name made lowercase.
    instruments = models.JSONField(blank=True, null=True)
    screeningmethod = models.CharField(db_column='screeningMethod', max_length=9)  # Field name made lowercase.
    externalcomments = models.TextField(db_column='externalComments')  # Field name made lowercase.
    specimenadequacy = models.JSONField(db_column='specimenAdequacy', blank=True, null=True)  # Field name made lowercase.
    diagnoses = models.JSONField(blank=True, null=True)
    clinicalinformation = models.TextField(db_column='clinicalInformation')  # Field name made lowercase.
    uvfish = models.JSONField(db_column='uvFish', blank=True, null=True)  # Field name made lowercase.
    reportimages = models.JSONField(db_column='reportImages', blank=True, null=True)  # Field name made lowercase.
    finalizedate = models.DateTimeField(db_column='finalizeDate', blank=True, null=True)  # Field name made lowercase.
    assignedto = models.IntegerField(db_column='assignedTo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cytologySlides'


class Cytologyslidesassignto(models.Model):
    slideid = models.IntegerField(db_column='slideID', unique=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    assigneeid = models.IntegerField(db_column='assigneeID')  # Field name made lowercase.
    comment = models.TextField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cytologySlidesAssignTo'


class Cytologyslidesdailylog(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    gyn = models.FloatField(db_column='GYN')  # Field name made lowercase.
    ngyn = models.FloatField(db_column='NGYN')  # Field name made lowercase.
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'cytologySlidesDailyLog'
        unique_together = (('userid', 'date'),)


class Cytologystainmaintenance(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    instrumentid = models.IntegerField(db_column='instrumentID')  # Field name made lowercase.
    stain = models.CharField(max_length=45)
    basin = models.IntegerField()
    action = models.CharField(max_length=10)
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    processedslidecount = models.IntegerField(db_column='processedSlideCount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cytologyStainMaintenance'


class Cytologystainqc(models.Model):
    userid = models.IntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    cytologyslideid = models.IntegerField(db_column='cytologySlideID')  # Field name made lowercase.
    category = models.CharField(max_length=10, blank=True, null=True)
    instruments = models.JSONField(blank=True, null=True)
    entrydate = models.DateTimeField(db_column='entryDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cytologyStainQC'


class Cytologystainqcslides(models.Model):
    stainqcid = models.IntegerField(db_column='stainQCID')  # Field name made lowercase.
    slidenum = models.CharField(db_column='slideNum', max_length=45)  # Field name made lowercase.
    processorinstrumentid = models.IntegerField(db_column='processorInstrumentID')  # Field name made lowercase.
    coverslipperinstrumentid = models.IntegerField(db_column='coverSlipperInstrumentID', blank=True, null=True)  # Field name made lowercase.
    nuclearstain = models.CharField(db_column='nuclearStain', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cytoplasmicstain = models.CharField(db_column='cytoplasmicStain', max_length=45, blank=True, null=True)  # Field name made lowercase.
    slideprepquality = models.CharField(db_column='slidePrepQuality', max_length=45, blank=True, null=True)  # Field name made lowercase.
    qcresults = models.CharField(db_column='qcResults', max_length=45, blank=True, null=True)  # Field name made lowercase.
    crosscontamination = models.CharField(db_column='crossContamination', max_length=45, blank=True, null=True)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cytologyStainQCSlides'


class Cytologyusers2Qc(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    slideid = models.IntegerField(db_column='slideID')  # Field name made lowercase.
    isreviewed = models.IntegerField(db_column='isReviewed')  # Field name made lowercase.
    revieweddate = models.DateTimeField(db_column='reviewedDate', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cytologyUsers2QC'


class Cytologyusers2Slides(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    slideid = models.IntegerField(db_column='slideID')  # Field name made lowercase.
    actionbefore = models.CharField(db_column='actionBefore', max_length=10)  # Field name made lowercase.
    actionafter = models.CharField(db_column='actionAfter', max_length=10)  # Field name made lowercase.
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cytologyUsers2slides'


class Diagnoses(models.Model):
    code = models.CharField(unique=True, max_length=10)
    description = models.CharField(max_length=255)
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diagnoses'


class Diagnoses2(models.Model):
    code = models.CharField(unique=True, max_length=10)
    description = models.CharField(max_length=255)
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diagnoses2'


class Diagnosishistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    patientid = models.BigIntegerField(db_column='patientID')  # Field name made lowercase.
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    oldid = models.CharField(db_column='oldID', unique=True, max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diagnosisHistory'
        unique_together = (('patientid', 'code'),)


class Docs(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'docs'


class Dohcalifornia(models.Model):
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    testhistoryid = models.IntegerField(db_column='testHistoryID')  # Field name made lowercase.
    elementhistoryid = models.BigIntegerField(db_column='elementHistoryID')  # Field name made lowercase.
    senttodoh = models.IntegerField(db_column='sentToDOH')  # Field name made lowercase.
    acknowledgement = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dohCalifornia'


class Dohhistory(models.Model):
    testhistoryid = models.IntegerField(db_column='testHistoryID')  # Field name made lowercase.
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    testcode = models.CharField(db_column='testCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    testdescription = models.CharField(db_column='testDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    element = models.CharField(max_length=255, blank=True, null=True)
    elementresult = models.CharField(db_column='elementResult', max_length=255, blank=True, null=True)  # Field name made lowercase.
    datefinalized = models.DateTimeField(db_column='dateFinalized', blank=True, null=True)  # Field name made lowercase.
    isprocessed = models.IntegerField(db_column='isProcessed')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    dateprocessed = models.DateTimeField(db_column='dateProcessed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dohHistory'
        unique_together = (('testhistoryid', 'element'),)


class Drawstationpermissions(models.Model):
    userid = models.IntegerField(db_column='userID', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'drawStationPermissions'


class Drivers(models.Model):
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    phone = models.CharField(max_length=45)
    pickuptype = models.CharField(db_column='pickupType', max_length=7, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    code = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'drivers'


class Element2Comment(models.Model):
    elementdictionaryid = models.IntegerField(db_column='elementDictionaryID')  # Field name made lowercase.
    elementcommentdictionaryid = models.IntegerField(db_column='elementCommentDictionaryID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'element2comment'
        unique_together = (('elementdictionaryid', 'elementcommentdictionaryid'),)


class Elementcodes(models.Model):
    elementdictionaryid = models.IntegerField(db_column='elementDictionaryID')  # Field name made lowercase.
    code = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'elementCodes'
        unique_together = (('elementdictionaryid', 'code'),)


class Elementcommentdictionary(models.Model):
    code = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    result = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elementCommentDictionary'


class Elementdictionary(models.Model):
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    worksheet = models.CharField(max_length=45)
    internalname = models.CharField(db_column='internalName', max_length=100)  # Field name made lowercase.
    reportname = models.CharField(db_column='reportName', max_length=100)  # Field name made lowercase.
    units = models.CharField(max_length=30)
    interpretivenormals = models.CharField(db_column='interpretiveNormals', max_length=6000)  # Field name made lowercase.
    loinc = models.CharField(max_length=45)
    mailoutcode = models.CharField(db_column='mailoutCode', max_length=45)  # Field name made lowercase.
    liscode = models.CharField(db_column='lisCode', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elementDictionary'
        unique_together = (('code', 'worksheet'),)


class Elementhistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    testhistoryid = models.IntegerField(db_column='testHistoryID')  # Field name made lowercase.
    testcode = models.CharField(db_column='testCode', max_length=45)  # Field name made lowercase.
    elementcode = models.CharField(db_column='elementCode', max_length=45)  # Field name made lowercase.
    elementdescription = models.CharField(db_column='elementDescription', max_length=255)  # Field name made lowercase.
    elementresult = models.CharField(db_column='elementResult', max_length=45)  # Field name made lowercase.
    units = models.CharField(max_length=45)
    normalranges = models.CharField(db_column='normalRanges', max_length=45)  # Field name made lowercase.
    abnormalflag = models.CharField(db_column='abnormalFlag', max_length=45)  # Field name made lowercase.
    comment = models.CharField(max_length=2000)
    date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=45)
    testnotperformed = models.IntegerField(db_column='testNotPerformed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elementHistory'
        unique_together = (('patientid', 'testhistoryid', 'elementcode'),)


class Elementquestmapping(models.Model):
    accessionid = models.IntegerField(db_column='accessionID')  # Field name made lowercase.
    testcode = models.CharField(db_column='testCode', max_length=45)  # Field name made lowercase.
    elementdictionaryid = models.IntegerField(db_column='elementDictionaryID')  # Field name made lowercase.
    elementcode = models.CharField(db_column='elementCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    internalresult = models.IntegerField(db_column='internalResult', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elementQuestMapping'
        unique_together = (('accessionid', 'elementdictionaryid'),)


class Elementresults(models.Model):
    accessionid = models.CharField(db_column='accessionID', max_length=45)  # Field name made lowercase.
    testcode = models.CharField(db_column='testCode', max_length=45)  # Field name made lowercase.
    elementcode = models.CharField(db_column='elementCode', max_length=45)  # Field name made lowercase.
    mailoutelementcode = models.CharField(db_column='mailoutElementCode', max_length=45)  # Field name made lowercase.
    elementresult = models.CharField(db_column='elementResult', max_length=45)  # Field name made lowercase.
    units = models.CharField(max_length=45)
    normalranges = models.CharField(db_column='normalRanges', max_length=45)  # Field name made lowercase.
    abnormalflag = models.CharField(db_column='abnormalFlag', max_length=45)  # Field name made lowercase.
    comment = models.CharField(max_length=2000)
    datefinalized = models.DateTimeField(db_column='dateFinalized', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'elementResults'
        unique_together = (('accessionid', 'testcode', 'elementcode'),)


class Elementresultsmapping(models.Model):
    elementdictionaryid = models.IntegerField(db_column='elementDictionaryID', blank=True, null=True)  # Field name made lowercase.
    externalresult = models.CharField(db_column='externalResult', max_length=45)  # Field name made lowercase.
    internalresult = models.CharField(db_column='internalResult', max_length=45)  # Field name made lowercase.
    comment = models.CharField(max_length=3000)
    notes = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'elementResultsMapping'
        unique_together = (('elementdictionaryid', 'externalresult'),)


class ElementHistory(models.Model):
    accession_id = models.CharField(max_length=20, blank=True, null=True)
    test_code = models.CharField(max_length=20, blank=True, null=True)
    element_code = models.CharField(max_length=100, blank=True, null=True)
    element_description = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    normal_range = models.CharField(max_length=255, blank=True, null=True)
    results = models.CharField(max_length=255, blank=True, null=True)
    previous_results = models.CharField(max_length=255, blank=True, null=True)
    unit_of_measuare = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'element_history'
        unique_together = (('accession_id', 'test_code', 'element_code'),)


class Elements(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    element_code = models.CharField(max_length=100, blank=True, null=True)
    internalname = models.CharField(db_column='internalName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flagnormalranges = models.CharField(db_column='flagNormalRanges', max_length=20, blank=True, null=True)  # Field name made lowercase.
    maximumacceptableentrylength = models.CharField(db_column='maximumAcceptableEntryLength', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isnullentryvalidfinalresult = models.CharField(db_column='isNullEntryValidFinalResult', max_length=200, blank=True, null=True)  # Field name made lowercase.
    acceptablenumericentrylimits = models.CharField(db_column='acceptableNumericEntryLimits', max_length=10, blank=True, null=True)  # Field name made lowercase.
    numericentrylimitslow = models.CharField(db_column='numericEntryLimitsLow', max_length=200, blank=True, null=True)  # Field name made lowercase.
    numericentrylimitshigh = models.CharField(db_column='numericEntryLimitsHigh', max_length=200, blank=True, null=True)  # Field name made lowercase.
    holdcritiriaautoresultrangelow = models.CharField(db_column='holdCritiriaAutoResultRangeLow', max_length=200, blank=True, null=True)  # Field name made lowercase.
    holdcritiriaautoresultrangehigh = models.CharField(db_column='holdCritiriaAutoResultRangeHigh', max_length=200, blank=True, null=True)  # Field name made lowercase.
    impliednumberofdecimalplaces = models.CharField(db_column='impliedNumberofDecimalPlaces', max_length=200, blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(max_length=200, blank=True, null=True)
    alphanumericentrypermitted = models.CharField(db_column='alphaNumericEntryPermitted', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mustalphaentriesbepredefined = models.CharField(db_column='mustAlphaEntriesBePreDefined', max_length=11, blank=True, null=True)  # Field name made lowercase.
    flagcritical = models.CharField(db_column='flagCritical', max_length=200, blank=True, null=True)  # Field name made lowercase.
    interpretivenormals = models.TextField(db_column='InterpretiveNormals', blank=True, null=True)  # Field name made lowercase.
    entirecommentstoappearononeprintedpage = models.CharField(db_column='entireCommentsToAppearOnOnePrintedPage', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loinccode = models.CharField(db_column='loincCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dohloinccode = models.CharField(db_column='dohLoincCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dohcriteria = models.CharField(db_column='dohCriteria', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dohresult = models.CharField(db_column='dohResult', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elements'


class Elements2Tests(models.Model):
    id = models.CharField(primary_key=True, max_length=120)
    testcode = models.CharField(db_column='testCode', max_length=60, blank=True, null=True)  # Field name made lowercase.
    elementcode = models.CharField(db_column='elementCode', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elements2tests'
        unique_together = (('testcode', 'elementcode'),)


class Elementsalfanumericresults(models.Model):
    elementcode = models.CharField(db_column='elementCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(max_length=20, blank=True, null=True)
    result = models.CharField(max_length=20, blank=True, null=True)
    flag = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=1000, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    oldid = models.CharField(db_column='oldID', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elementsAlfaNumericResults'


class Elementscriticalranges(models.Model):
    elementcode = models.CharField(db_column='elementCode', max_length=100)  # Field name made lowercase.
    agefrom = models.IntegerField(db_column='ageFrom')  # Field name made lowercase.
    ageto = models.IntegerField(db_column='ageTo')  # Field name made lowercase.
    sex = models.CharField(max_length=1, blank=True, null=True)
    lowvalue = models.FloatField(db_column='lowValue', blank=True, null=True)  # Field name made lowercase.
    highvalue = models.FloatField(db_column='highValue', blank=True, null=True)  # Field name made lowercase.
    oldid = models.CharField(db_column='oldID', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elementsCriticalRanges'


class Elementsnormalranges(models.Model):
    elementcode = models.CharField(db_column='elementCode', max_length=100)  # Field name made lowercase.
    agefrom = models.IntegerField(db_column='ageFrom')  # Field name made lowercase.
    ageto = models.IntegerField(db_column='ageTo')  # Field name made lowercase.
    sex = models.CharField(max_length=1, blank=True, null=True)
    lowvalue = models.FloatField(db_column='lowValue', blank=True, null=True)  # Field name made lowercase.
    highvalue = models.FloatField(db_column='highValue', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    oldid = models.CharField(db_column='oldID', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elementsNormalRanges'


class Emailsessions(models.Model):
    sid = models.CharField(primary_key=True, max_length=255)
    session = models.TextField()
    expires = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emailSessions'


class Emrdiagnoses(models.Model):
    orderid = models.IntegerField(db_column='orderID')  # Field name made lowercase.
    code = models.CharField(max_length=15)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'emrDiagnoses'
        unique_together = (('orderid', 'code'),)


class Emrinsurances(models.Model):
    orderid = models.IntegerField(db_column='orderID')  # Field name made lowercase.
    policy = models.CharField(max_length=255)
    insurancecode = models.CharField(db_column='insuranceCode', max_length=45)  # Field name made lowercase.
    relationtoinsured = models.CharField(db_column='relationToInsured', max_length=45)  # Field name made lowercase.
    date = models.DateTimeField()
    isprimary = models.IntegerField(db_column='isPrimary')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emrInsurances'


class Emrordersets(models.Model):
    orderid = models.IntegerField(db_column='orderID')  # Field name made lowercase.
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emrOrderSets'


class Emrorders(models.Model):
    requisitionid = models.CharField(db_column='requisitionID', max_length=15)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    middlename = models.CharField(db_column='middleName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    dob = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    homeaddress = models.CharField(db_column='homeAddress', max_length=255)  # Field name made lowercase.
    homecity = models.CharField(db_column='homeCity', max_length=45)  # Field name made lowercase.
    homestate = models.CharField(db_column='homeState', max_length=2)  # Field name made lowercase.
    homezip = models.CharField(db_column='homeZip', max_length=5)  # Field name made lowercase.
    phone = models.CharField(max_length=20)
    clientid = models.IntegerField(db_column='clientID')  # Field name made lowercase.
    physicianid = models.IntegerField(db_column='physicianID')  # Field name made lowercase.
    date = models.DateTimeField()
    ssn = models.CharField(max_length=12)
    billto = models.CharField(db_column='billTo', max_length=11)  # Field name made lowercase.
    relationtoinsured = models.CharField(db_column='relationToInsured', max_length=7)  # Field name made lowercase.
    status = models.CharField(max_length=9)
    chartnumber = models.CharField(db_column='chartNumber', max_length=45)  # Field name made lowercase.
    hl7 = models.TextField(blank=True, null=True)
    insuranceinfo = models.TextField(db_column='insuranceInfo', blank=True, null=True)  # Field name made lowercase.
    clx = models.IntegerField()
    scheduledate = models.DateField(db_column='scheduleDate', blank=True, null=True)  # Field name made lowercase.
    scheduletime = models.TimeField(db_column='scheduleTime', blank=True, null=True)  # Field name made lowercase.
    psc = models.CharField(max_length=45)
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'emrOrders'


class Emrorderscontest(models.Model):
    salesid = models.CharField(db_column='salesID', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    salesname = models.CharField(db_column='salesName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    testqnt = models.IntegerField(db_column='testQNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emrOrdersContest'


class Emrorderscontestdetails(models.Model):
    salesid = models.CharField(db_column='salesID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    salename = models.CharField(db_column='saleName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    clientid = models.CharField(db_column='clientID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    patientsqnt = models.CharField(db_column='patientsQNT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    percentofel = models.CharField(db_column='percentOfEl', max_length=45, blank=True, null=True)  # Field name made lowercase.
    salesqnt = models.CharField(db_column='salesQNT', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emrOrdersContestDetails'
        unique_together = (('clientid', 'salesid'),)


class Favoritediagnoses(models.Model):
    physicianid = models.SmallIntegerField(db_column='physicianID')  # Field name made lowercase.
    diagnosisid = models.IntegerField(db_column='diagnosisID')  # Field name made lowercase.
    position = models.IntegerField(blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'favoriteDiagnoses'
        unique_together = (('physicianid', 'diagnosisid'),)


class Favoritetests(models.Model):
    physicianid = models.SmallIntegerField(db_column='physicianID')  # Field name made lowercase.
    testid = models.IntegerField(db_column='testID')  # Field name made lowercase.
    position = models.IntegerField()
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    isflorida = models.IntegerField(db_column='isFlorida')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'favoriteTests'
        unique_together = (('physicianid', 'testid'),)


class Favorites(models.Model):
    id = models.IntegerField(primary_key=True)
    physicianid = models.CharField(db_column='physicianID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    testid = models.CharField(db_column='testID', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'favorites'


class Floridasms(models.Model):
    accessionid = models.CharField(db_column='accessionID', max_length=45)  # Field name made lowercase.
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'floridaSMS'


class Formmaternal(models.Model):
    patientid = models.IntegerField(db_column='patientID', blank=True, null=True)  # Field name made lowercase.
    testcode = models.CharField(db_column='testCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    expecteddeliverydate = models.DateField(db_column='expectedDeliveryDate', blank=True, null=True)  # Field name made lowercase.
    datingmethod = models.CharField(db_column='datingMethod', max_length=13, blank=True, null=True)  # Field name made lowercase.
    maternalweight = models.IntegerField(db_column='maternalWeight', blank=True, null=True)  # Field name made lowercase.
    maternaldob = models.DateField(db_column='maternalDOB', blank=True, null=True)  # Field name made lowercase.
    race = models.CharField(max_length=16, blank=True, null=True)
    diabetic = models.CharField(max_length=3, blank=True, null=True)
    nuchaltranslucency = models.CharField(db_column='nuchalTranslucency', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    repeatforntd = models.CharField(db_column='repeatForNTD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    crownrumplength = models.CharField(db_column='crownRumpLength', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    numberoffetuses = models.IntegerField(db_column='numberOfFetuses', blank=True, null=True)  # Field name made lowercase.
    familyhistoryofntd = models.CharField(db_column='familyHistoryOfNTD', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formMaternal'
        unique_together = (('patientid', 'testcode'),)


class Formquestgyn(models.Model):
    patientid = models.IntegerField(db_column='patientID', blank=True, null=True)  # Field name made lowercase.
    testcode = models.CharField(db_column='testCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clinicalinformation = models.CharField(db_column='clinicalInformation', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    lmp = models.CharField(db_column='LMP', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    grossdescription = models.CharField(db_column='grossDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    specimensource = models.CharField(db_column='specimenSource', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prevpap = models.CharField(db_column='prevPap', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prevbx = models.CharField(db_column='prevBX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    numberofslides = models.IntegerField(db_column='numberOfSlides', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formQuestGYN'
        unique_together = (('patientid', 'testcode'),)


class Formquestngyn(models.Model):
    patientid = models.IntegerField(db_column='patientID', blank=True, null=True)  # Field name made lowercase.
    testcode = models.CharField(db_column='testCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    specimensource = models.CharField(db_column='specimenSource', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    clinicalhistory = models.CharField(db_column='clinicalHistory', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    numberofcontainers = models.IntegerField(db_column='numberOfContainers', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formQuestNGYN'
        unique_together = (('patientid', 'testcode'),)


class Formspecimensource(models.Model):
    patientid = models.IntegerField(db_column='patientID', blank=True, null=True)  # Field name made lowercase.
    testcode = models.CharField(db_column='testCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formSpecimenSource'
        unique_together = (('patientid', 'testcode'),)


class Histologycpts(models.Model):
    histologycaseid = models.IntegerField(db_column='histologyCaseID')  # Field name made lowercase.
    histologyspecimenid = models.IntegerField(db_column='histologySpecimenID')  # Field name made lowercase.
    cptcode = models.CharField(db_column='cptCode', max_length=6)  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'histologyCPTs'


class Histologycases(models.Model):
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    assigneduserid = models.IntegerField(db_column='assignedUserID', blank=True, null=True)  # Field name made lowercase.
    casenumber = models.CharField(db_column='caseNumber', unique=True, max_length=12)  # Field name made lowercase.
    type = models.CharField(max_length=45)
    clinicalinformation = models.TextField(db_column='clinicalInformation', blank=True, null=True)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='entryDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=18)
    finalizeby = models.IntegerField(db_column='finalizeBy', blank=True, null=True)  # Field name made lowercase.
    finalizedate = models.DateTimeField(db_column='finalizeDate', blank=True, null=True)  # Field name made lowercase.
    reportimages = models.JSONField(db_column='reportImages', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'histologyCases'


class Histologycassettes(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    histologycaseid = models.IntegerField(db_column='histologyCaseID')  # Field name made lowercase.
    histologyspecimenid = models.IntegerField(db_column='histologySpecimenID')  # Field name made lowercase.
    cassettenumber = models.IntegerField(db_column='cassetteNumber')  # Field name made lowercase.
    comments = models.CharField(max_length=2000)
    qc = models.CharField(db_column='QC', max_length=255)  # Field name made lowercase.
    status = models.CharField(max_length=9)
    embeddate = models.DateTimeField(db_column='embedDate', blank=True, null=True)  # Field name made lowercase.
    embedbyuserid = models.IntegerField(db_column='embedByUserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'histologyCassettes'
        unique_together = (('histologycaseid', 'histologyspecimenid', 'cassettenumber'),)


class Histologycontest(models.Model):
    salesid = models.CharField(db_column='salesID', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    salesname = models.CharField(db_column='salesName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    testqnt = models.IntegerField(db_column='testQNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'histologyContest'


class Histologycontestdetails(models.Model):
    salesid = models.CharField(db_column='salesID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    clientid = models.CharField(db_column='clientID', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    patientsqnt = models.CharField(db_column='patientsQNT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    salesqnt = models.CharField(db_column='salesQNT', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'histologyContestDetails'


class Histologyihc(models.Model):
    description = models.CharField(max_length=40)
    cptunits = models.IntegerField(db_column='cptUnits')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'histologyIHC'


class Histologypermissions(models.Model):
    userid = models.IntegerField(db_column='userID', unique=True)  # Field name made lowercase.
    isadmin = models.IntegerField(db_column='isAdmin')  # Field name made lowercase.
    isaide = models.IntegerField(db_column='isAide')  # Field name made lowercase.
    ishistotech = models.IntegerField(db_column='isHistotech')  # Field name made lowercase.
    issupervisor = models.IntegerField(db_column='isSupervisor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'histologyPermissions'


class Histologyqc(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    type = models.CharField(max_length=13, blank=True, null=True)
    comments = models.CharField(max_length=255)
    techqc = models.CharField(db_column='techQC', max_length=4, blank=True, null=True)  # Field name made lowercase.
    overallqc = models.CharField(db_column='overallQC', max_length=4)  # Field name made lowercase.
    pathologyid = models.IntegerField(db_column='pathologyID', blank=True, null=True)  # Field name made lowercase.
    qcdate = models.DateTimeField(db_column='QCdate', blank=True, null=True)  # Field name made lowercase.
    stain = models.CharField(max_length=40)
    background = models.CharField(max_length=10)
    nuclearstain = models.CharField(db_column='nuclearStain', max_length=10)  # Field name made lowercase.
    cytoplasmicstain = models.CharField(db_column='cytoplasmicStain', max_length=10)  # Field name made lowercase.
    positivestainelements = models.CharField(db_column='positiveStainElements', max_length=10)  # Field name made lowercase.
    negativestainelements = models.CharField(db_column='negativeStainElements', max_length=10)  # Field name made lowercase.
    counterstain = models.CharField(db_column='counterStain', max_length=10)  # Field name made lowercase.
    slides = models.JSONField()
    status = models.CharField(max_length=7)
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'histologyQC'


class Histologyreports(models.Model):
    histologycaseid = models.IntegerField(db_column='histologyCaseID')  # Field name made lowercase.
    filename = models.CharField(max_length=75)
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    reportedbyuserid = models.IntegerField(db_column='reportedByUserID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'histologyReports'


class Histologysendout(models.Model):
    histologycaseid = models.IntegerField(db_column='histologyCaseID')  # Field name made lowercase.
    specialstainid = models.IntegerField(db_column='specialStainID')  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)
    sent = models.IntegerField()
    mailoutlab = models.CharField(db_column='mailoutLab', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histologySendout'


class Histologyslides(models.Model):
    histologycaseid = models.IntegerField(db_column='histologyCaseID')  # Field name made lowercase.
    histologycassetteid = models.IntegerField(db_column='histologyCassetteID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    clearedby = models.IntegerField(db_column='clearedBy', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.IntegerField(db_column='deletedBy', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=20)
    comment = models.CharField(max_length=255)
    index = models.IntegerField()
    status = models.CharField(max_length=9)
    cutdate = models.DateTimeField(db_column='cutDate', blank=True, null=True)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    deletedate = models.DateTimeField(db_column='deleteDate', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    isother = models.IntegerField(db_column='isOther')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'histologySlides'
        unique_together = (('histologycassetteid', 'description', 'index'),)


class Histologyspecialstains(models.Model):
    description = models.CharField(max_length=30)
    cpts = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histologySpecialStains'


class Histologyspecimens(models.Model):
    histologycaseid = models.IntegerField(db_column='histologyCaseID')  # Field name made lowercase.
    specimen = models.CharField(max_length=45)
    samplesite = models.CharField(db_column='sampleSite', max_length=255)  # Field name made lowercase.
    fixative = models.CharField(max_length=45)
    grossqc = models.CharField(db_column='grossQC', max_length=45)  # Field name made lowercase.
    testtype = models.CharField(db_column='testType', max_length=45)  # Field name made lowercase.
    status = models.CharField(max_length=8)
    isdecalcified = models.IntegerField(db_column='isDecalcified')  # Field name made lowercase.
    duration = models.FloatField(blank=True, null=True)
    macro = models.CharField(max_length=10)
    jarlabel1 = models.CharField(db_column='jarLabel1', max_length=45)  # Field name made lowercase.
    jarlabel2 = models.CharField(db_column='jarLabel2', max_length=45)  # Field name made lowercase.
    inked = models.CharField(max_length=45)
    color = models.CharField(max_length=45)
    dimensions = models.JSONField()
    submittedas = models.CharField(db_column='submittedAs', max_length=40)  # Field name made lowercase.
    grosscut = models.CharField(db_column='grossCut', max_length=20)  # Field name made lowercase.
    cassettes = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    specialstains = models.JSONField(db_column='specialStains')  # Field name made lowercase.
    ihc = models.JSONField(db_column='IHC')  # Field name made lowercase.
    diagnosis = models.JSONField()
    bonemarrowresults = models.JSONField(db_column='boneMarrowResults')  # Field name made lowercase.
    microscopicdescription = models.TextField(db_column='microscopicDescription', blank=True, null=True)  # Field name made lowercase.
    reportcomments = models.TextField(db_column='reportComments', blank=True, null=True)  # Field name made lowercase.
    internalcomments = models.TextField(db_column='internalComments', blank=True, null=True)  # Field name made lowercase.
    specialstainsandihc = models.TextField(db_column='specialStainsAndIHC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'histologySpecimens'
        unique_together = (('histologycaseid', 'specimen'),)


class Hl7Errors(models.Model):
    accessionid = models.CharField(db_column='accessionID', max_length=45)  # Field name made lowercase.
    error = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'hl7Errors'
        unique_together = (('accessionid', 'error'),)


class Hl7Resulterrors(models.Model):
    accessionid = models.CharField(db_column='accessionID', max_length=45)  # Field name made lowercase.
    error = models.CharField(max_length=100)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hl7ResultErrors'
        unique_together = (('accessionid', 'error'),)


class Hometest(models.Model):
    ordernumber = models.CharField(db_column='orderNumber', unique=True, max_length=255)  # Field name made lowercase.
    shippingaddress = models.CharField(db_column='shippingAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shippingcity = models.CharField(db_column='shippingCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shippingstate = models.CharField(db_column='shippingState', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shippingzip = models.CharField(db_column='shippingZip', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    status = models.CharField(max_length=15)
    qnt = models.IntegerField(blank=True, null=True)
    dateinprogress = models.DateTimeField(db_column='dateInProgress', blank=True, null=True)  # Field name made lowercase.
    dateshipped = models.DateTimeField(db_column='dateShipped', blank=True, null=True)  # Field name made lowercase.
    printedby = models.CharField(db_column='printedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    submittedby = models.CharField(db_column='submittedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shipping = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    mywellcomid = models.BigIntegerField(db_column='mywellcomID', blank=True, null=True)  # Field name made lowercase.
    test = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=45)
    return_field = models.CharField(db_column='return', max_length=255)  # Field renamed because it was a Python reserved word.
    clientid = models.BigIntegerField(db_column='clientID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hometest'


class Hometestdetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    orderid = models.BigIntegerField(db_column='orderID')  # Field name made lowercase.
    test = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(db_column='lastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dob = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    insurance = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField()
    dateactivated = models.DateTimeField(db_column='dateActivated', blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(max_length=255, blank=True, null=True)
    physician = models.CharField(max_length=255, blank=True, null=True)
    npi = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    collectiondate = models.CharField(db_column='collectionDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    collectiontime = models.CharField(db_column='collectionTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    race = models.CharField(max_length=255, blank=True, null=True)
    ethnicity = models.CharField(max_length=255, blank=True, null=True)
    employment = models.CharField(max_length=255, blank=True, null=True)
    employer = models.CharField(max_length=255, blank=True, null=True)
    employeraddress = models.CharField(db_column='employerAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    employerphone = models.CharField(db_column='employerPhone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    school = models.CharField(max_length=255, blank=True, null=True)
    schooladdress = models.CharField(db_column='schoolAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    result = models.CharField(max_length=45, blank=True, null=True)
    mywellcomid = models.BigIntegerField(db_column='myWellcomID', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(max_length=4000, blank=True, null=True)
    insuranceid = models.CharField(db_column='insuranceID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    symptoms = models.CharField(max_length=45, blank=True, null=True)
    risk = models.CharField(max_length=45, blank=True, null=True)
    accessionid = models.CharField(db_column='accessionID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    return_field = models.CharField(db_column='return', max_length=45, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'hometestDetails'
        unique_together = (('orderid', 'barcode'),)


class Housecallupdates(models.Model):
    patient_id = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    requisitionid = models.TextField(db_column='requisitionID', blank=True, null=True)  # Field name made lowercase.
    isfollowup = models.IntegerField(db_column='isFollowUp', blank=True, null=True)  # Field name made lowercase.
    followupdate = models.DateTimeField(db_column='followUpDate', blank=True, null=True)  # Field name made lowercase.
    actionstatus = models.CharField(db_column='actionStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'houseCallUpdates'


class Housecallpermissions(models.Model):
    userid = models.IntegerField(db_column='userID', unique=True)  # Field name made lowercase.
    issupervisor = models.IntegerField(db_column='isSupervisor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'housecallPermissions'


class Igserrors(models.Model):
    accessionid = models.CharField(db_column='accessionID', max_length=45)  # Field name made lowercase.
    error = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'igsErrors'
        unique_together = (('accessionid', 'error'),)


class Igshistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    patientid = models.BigIntegerField(db_column='patientID')  # Field name made lowercase.
    testhistoryid = models.BigIntegerField(db_column='testHistoryID')  # Field name made lowercase.
    testcode = models.CharField(db_column='testCode', max_length=45)  # Field name made lowercase.
    elementcode = models.CharField(db_column='elementCode', max_length=45)  # Field name made lowercase.
    elementdescription = models.CharField(db_column='elementDescription', max_length=255)  # Field name made lowercase.
    elementresult = models.CharField(db_column='elementResult', max_length=45)  # Field name made lowercase.
    units = models.CharField(max_length=45)
    normalranges = models.CharField(db_column='normalRanges', max_length=45)  # Field name made lowercase.
    abnormalflag = models.CharField(db_column='abnormalFlag', max_length=45)  # Field name made lowercase.
    comment = models.CharField(max_length=3000)
    date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=45)
    originalaccession = models.CharField(db_column='originalAccession', max_length=45, blank=True, null=True)  # Field name made lowercase.
    testnotperformed = models.IntegerField(db_column='testNotPerformed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'igsHistory'
        unique_together = (('patientid', 'testhistoryid', 'elementcode'),)


class Igspush(models.Model):
    id = models.BigAutoField(primary_key=True)
    accessionid = models.CharField(db_column='accessionID', max_length=45)  # Field name made lowercase.
    processed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'igsPush'


class Instruments(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    shortname = models.CharField(db_column='shortName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(max_length=45)
    type = models.CharField(max_length=45, blank=True, null=True)
    modelnumber = models.CharField(db_column='modelNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='serialNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=11)
    entrydate = models.DateTimeField(db_column='entryDate', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    misc = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instruments'


class Insurancepayments(models.Model):
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    memo = models.CharField(max_length=255)
    amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'insurancePayments'


class Insuranceresults(models.Model):
    accessionid = models.CharField(db_column='accessionID', unique=True, max_length=45)  # Field name made lowercase.
    insurance = models.CharField(max_length=255)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'insuranceResults'


class Insurances(models.Model):
    id = models.SmallAutoField(primary_key=True)
    group = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    sendallteststoreflab = models.IntegerField(db_column='sendAllTestsToRefLab', blank=True, null=True)  # Field name made lowercase.
    isbillsendout = models.IntegerField(db_column='isBillSendout', blank=True, null=True)  # Field name made lowercase.
    isgcode = models.IntegerField(db_column='isGCode')  # Field name made lowercase.
    is80050 = models.IntegerField()
    isgroupforbilling = models.IntegerField(db_column='isGroupForBilling')  # Field name made lowercase.
    notes = models.CharField(max_length=255, blank=True, null=True)
    billschedule = models.IntegerField(db_column='billSchedule', blank=True, null=True)  # Field name made lowercase.
    questcarriercode = models.TextField(db_column='questCarrierCode', blank=True, null=True)  # Field name made lowercase.
    neicpay = models.CharField(db_column='neicPay', max_length=20, blank=True, null=True)  # Field name made lowercase.
    provider = models.CharField(max_length=20, blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    isoutofstate = models.IntegerField(db_column='isOutOfState')  # Field name made lowercase.
    category = models.CharField(max_length=1000, blank=True, null=True)
    labcorpcategory = models.CharField(db_column='labcorpCategory', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pf = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'insurances'


class Inventorypermissions(models.Model):
    userid = models.IntegerField(db_column='userID', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventoryPermissions'


class Itassets(models.Model):
    category = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    brand = models.CharField(max_length=45)
    serial = models.CharField(max_length=45)
    ip = models.CharField(max_length=45)
    number = models.CharField(max_length=45)
    department = models.CharField(max_length=45)
    floor = models.CharField(max_length=45)
    room = models.CharField(max_length=45)
    date = models.DateTimeField()
    userlastname = models.CharField(db_column='userLastName', max_length=45)  # Field name made lowercase.
    userfirstname = models.CharField(db_column='userFirstName', max_length=45)  # Field name made lowercase.
    clientid = models.CharField(db_column='clientID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    notassigned = models.IntegerField(db_column='notAssigned')  # Field name made lowercase.
    phoneext = models.CharField(db_column='phoneExt', max_length=45, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(max_length=4000)
    lisip = models.CharField(db_column='lisIP', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itAssets'


class Itorder(models.Model):
    id = models.BigAutoField(primary_key=True)
    ordernumber = models.CharField(db_column='orderNumber', max_length=45)  # Field name made lowercase.
    clientid = models.BigIntegerField(db_column='clientID')  # Field name made lowercase.
    ordertype = models.CharField(db_column='orderType', max_length=9)  # Field name made lowercase.
    notes = models.CharField(max_length=1000)
    date = models.DateTimeField()
    status = models.CharField(max_length=9)
    dateapproved = models.DateTimeField(db_column='dateApproved', blank=True, null=True)  # Field name made lowercase.
    datecompleted = models.DateTimeField(db_column='dateCompleted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itOrder'


class Itorderdetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    orderid = models.BigIntegerField(db_column='orderID')  # Field name made lowercase.
    type = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    serial = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'itOrderDetails'


class Itrequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    clientid = models.BigIntegerField(db_column='clientID')  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userID')  # Field name made lowercase.
    type = models.CharField(max_length=45)
    details = models.TextField()
    status = models.CharField(max_length=9)
    date = models.DateTimeField()
    ordernumber = models.CharField(db_column='orderNumber', max_length=45)  # Field name made lowercase.
    scheduledate = models.DateField(db_column='scheduleDate', blank=True, null=True)  # Field name made lowercase.
    declinereason = models.CharField(db_column='declineReason', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itRequest'


class Kits(models.Model):
    sales = models.CharField(max_length=255)
    salesgroup = models.IntegerField(db_column='salesGroup')  # Field name made lowercase.
    clientname = models.CharField(db_column='clientName', max_length=255)  # Field name made lowercase.
    clientemail = models.CharField(db_column='clientEmail', max_length=255)  # Field name made lowercase.
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=45)
    zip = models.IntegerField()
    ordernumber = models.CharField(db_column='orderNumber', unique=True, max_length=45)  # Field name made lowercase.
    qnt = models.IntegerField()
    price = models.CharField(max_length=45)
    status = models.CharField(max_length=9)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kits'


class Labelprinters(models.Model):
    name = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=45)
    area = models.CharField(max_length=45)
    type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'labelPrinters'


class Logisticspermissions(models.Model):
    userid = models.IntegerField(db_column='userID', unique=True)  # Field name made lowercase.
    isdriver = models.IntegerField(db_column='isDriver')  # Field name made lowercase.
    isadmin = models.IntegerField(db_column='isAdmin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logisticsPermissions'


class Mailoutaccount(models.Model):
    id = models.IntegerField(primary_key=True)
    mailoutlabname = models.CharField(db_column='mailoutLabName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(max_length=45, blank=True, null=True)
    labcode = models.CharField(db_column='labCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='fullName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mailoutAccount'


class Mailouthistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    testhistoryid = models.BigIntegerField(db_column='testHistoryID', unique=True)  # Field name made lowercase.
    mailoutlabname = models.CharField(db_column='mailoutLabName', max_length=45)  # Field name made lowercase.
    mailouttestcode = models.CharField(db_column='mailoutTestCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mailoutHistory'


class Mayoorders(models.Model):
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    testhistoryid = models.IntegerField(db_column='testHistoryID')  # Field name made lowercase.
    testcode = models.CharField(db_column='testCode', max_length=45)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    isprocessed = models.IntegerField(db_column='isProcessed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mayoOrders'
        unique_together = (('patientid', 'testhistoryid'),)


class Medagency(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstname = models.CharField(db_column='firstName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255)  # Field name made lowercase.
    dob = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    isinsurance = models.CharField(db_column='isInsurance', max_length=45)  # Field name made lowercase.
    insurancename = models.CharField(db_column='insuranceName', max_length=255)  # Field name made lowercase.
    policy = models.CharField(max_length=255)
    policyholder = models.CharField(db_column='policyHolder', max_length=255)  # Field name made lowercase.
    relationtoinsured = models.CharField(db_column='relationToInsured', max_length=45)  # Field name made lowercase.
    race = models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)
    gender = models.CharField(max_length=45)
    submissionid = models.CharField(db_column='submissionID', max_length=255)  # Field name made lowercase.
    date = models.DateTimeField()
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'medAgency'


class Microplates(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'microPlates'


class Microplates2Tests(models.Model):
    testid = models.IntegerField(db_column='testID')  # Field name made lowercase.
    plateid = models.IntegerField(db_column='plateID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'microPlates2tests'


class Mywellcom(models.Model):
    id = models.BigAutoField(primary_key=True)
    lastname = models.CharField(db_column='lastName', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=255)  # Field name made lowercase.
    dob = models.DateField()
    street = models.CharField(max_length=2000)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=45)
    zip = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    ssn = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    ishipaa = models.IntegerField(db_column='isHipaa')  # Field name made lowercase.
    validated = models.IntegerField()
    date = models.DateTimeField()
    sex = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mywellcom'


class New(models.Model):
    code = models.CharField(max_length=2000, blank=True, null=True)
    required = models.CharField(max_length=2000, blank=True, null=True)
    volume = models.CharField(max_length=2000, blank=True, null=True)
    room = models.CharField(max_length=2000, blank=True, null=True)
    refrig = models.CharField(max_length=2000, blank=True, null=True)
    frozen = models.CharField(max_length=2000, blank=True, null=True)
    transport = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new'


class Newdbordererror(models.Model):
    accessionid = models.CharField(db_column='accessionID', max_length=45)  # Field name made lowercase.
    error = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'newDBOrderError'
        unique_together = (('accessionid', 'error'),)


class Newdbresulterror(models.Model):
    accessionid = models.CharField(db_column='accessionID', max_length=45)  # Field name made lowercase.
    error = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'newDBResultError'
        unique_together = (('accessionid', 'error'),)


class NewTable(models.Model):
    collectiondate = models.CharField(db_column='collectionDate', max_length=45, blank=True, null=True)  # Field name made lowercase.
    questaccession = models.CharField(db_column='questAccession', max_length=45, blank=True, null=True)  # Field name made lowercase.
    patientname = models.CharField(db_column='patientName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    eclaccession = models.CharField(db_column='eclAccession', max_length=45, blank=True, null=True)  # Field name made lowercase.
    physician = models.CharField(max_length=45, blank=True, null=True)
    cpt = models.CharField(max_length=45, blank=True, null=True)
    testname = models.CharField(db_column='testName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    questtestcode = models.CharField(db_column='questTestCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    price = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_table'


class Notes(models.Model):
    clientid = models.IntegerField(db_column='clientID', blank=True, null=True)  # Field name made lowercase.
    physicianid = models.IntegerField(db_column='physicianID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    ordersetid = models.IntegerField(db_column='orderSetID', blank=True, null=True)  # Field name made lowercase.
    testid = models.IntegerField(db_column='testID', blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(max_length=45)
    note = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'notes'


class Orderset2Test(models.Model):
    ordersetid = models.IntegerField(db_column='orderSetID')  # Field name made lowercase.
    testid = models.IntegerField(db_column='testID')  # Field name made lowercase.
    isinactive = models.IntegerField(db_column='isInactive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderSet2test'
        unique_together = (('ordersetid', 'testid'),)


class Ordersetdictionary(models.Model):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    specimenrequired = models.CharField(db_column='specimenRequired', max_length=1000)  # Field name made lowercase.
    alternatespecimen = models.CharField(db_column='alternateSpecimen', max_length=1000)  # Field name made lowercase.
    specimencontainer = models.CharField(db_column='specimenContainer', max_length=1000)  # Field name made lowercase.
    specimenvolume = models.CharField(db_column='specimenVolume', max_length=1000)  # Field name made lowercase.
    specimenstability = models.CharField(db_column='specimenStability', max_length=1000)  # Field name made lowercase.
    turnarounddays = models.CharField(db_column='turnAroundDays', max_length=1000)  # Field name made lowercase.
    collectioninstructions = models.CharField(db_column='collectionInstructions', max_length=2000)  # Field name made lowercase.
    shippingtemperature = models.CharField(db_column='shippingTemperature', max_length=1000)  # Field name made lowercase.
    testlimitations = models.CharField(db_column='testLimitations', max_length=1000)  # Field name made lowercase.
    rejectioncriteria = models.CharField(db_column='rejectionCriteria', max_length=2000)  # Field name made lowercase.
    clinicalinformation = models.CharField(db_column='clinicalInformation', max_length=2000)  # Field name made lowercase.
    patientpreparation = models.CharField(db_column='patientPreparation', max_length=1000)  # Field name made lowercase.
    methodology = models.CharField(max_length=1000)
    isigs = models.IntegerField(db_column='isIGS')  # Field name made lowercase.
    isactive = models.IntegerField(db_column='isActive')  # Field name made lowercase.
    showclinicalinformation = models.IntegerField(db_column='showClinicalInformation')  # Field name made lowercase.
    showpatientpreparation = models.IntegerField(db_column='showPatientPreparation')  # Field name made lowercase.
    showcollectioninstructions = models.IntegerField(db_column='showCollectionInstructions')  # Field name made lowercase.
    showmethodology = models.IntegerField(db_column='showMethodology')  # Field name made lowercase.
    showspecimenrequired = models.IntegerField(db_column='showSpecimenRequired')  # Field name made lowercase.
    showspecimencontainer = models.IntegerField(db_column='showSpecimenContainer')  # Field name made lowercase.
    showalternatespecimen = models.IntegerField(db_column='showAlternateSpecimen')  # Field name made lowercase.
    showspecimenstability = models.IntegerField(db_column='showSpecimenStability')  # Field name made lowercase.
    showrejectioncriteria = models.IntegerField(db_column='showRejectionCriteria')  # Field name made lowercase.
    showshippingtemperature = models.IntegerField(db_column='showShippingTemperature')  # Field name made lowercase.
    showspecimenvolume = models.IntegerField(db_column='showSpecimenVolume')  # Field name made lowercase.
    showturnarounddays = models.IntegerField(db_column='showTurnAroundDays')  # Field name made lowercase.
    ispanel = models.IntegerField(db_column='isPanel')  # Field name made lowercase.
    comment = models.CharField(max_length=2000)
    hasadditional = models.IntegerField(db_column='hasAdditional')  # Field name made lowercase.
    isflorida = models.IntegerField(db_column='isFlorida')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderSetDictionary'
        unique_together = (('code', 'isflorida'),)


class Ordersethistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    patientid = models.BigIntegerField(db_column='patientID')  # Field name made lowercase.
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    isfinal = models.IntegerField(db_column='isFinal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderSetHistory'
        unique_together = (('patientid', 'code'),)


class Ordersetpermissions(models.Model):
    ordersetid = models.IntegerField(db_column='orderSetID', unique=True)  # Field name made lowercase.
    website = models.IntegerField()
    wellcom = models.IntegerField()
    emr = models.IntegerField()
    iscustom = models.IntegerField(db_column='isCustom')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderSetPermissions'


class Orders(models.Model):
    id = models.BigAutoField(primary_key=True)
    patientid = models.BigIntegerField(db_column='patientID')  # Field name made lowercase.
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    json = models.JSONField()

    class Meta:
        managed = False
        db_table = 'orders'
        unique_together = (('patientid', 'code'),)


class Orders2Insurances(models.Model):
    id = models.IntegerField(primary_key=True)
    orderid = models.IntegerField(db_column='orderID')  # Field name made lowercase.
    insurancecode = models.CharField(db_column='insuranceCode', max_length=45)  # Field name made lowercase.
    insurancename = models.CharField(db_column='insuranceName', max_length=255)  # Field name made lowercase.
    address = models.CharField(max_length=1000)
    address2 = models.CharField(max_length=1000)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=45)
    zip = models.CharField(max_length=15)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders2Insurances'


class Ordrs(models.Model):
    ordernumber = models.CharField(db_column='orderNumber', unique=True, max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=255)  # Field name made lowercase.
    npi = models.CharField(max_length=255)
    physicianid = models.IntegerField(db_column='physicianID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientID', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField()
    status = models.CharField(max_length=45)
    source = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'ordrs'


class Ordrsresults(models.Model):
    id = models.BigAutoField(primary_key=True)
    orderid = models.IntegerField(db_column='orderID')  # Field name made lowercase.
    element = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    date = models.DateTimeField()
    sent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ordrsResults'
        unique_together = (('orderid', 'element'),)


class Parsererrors(models.Model):
    orderset = models.CharField(max_length=200)
    test = models.CharField(max_length=200)
    element = models.CharField(max_length=200)
    error = models.CharField(max_length=2000)

    class Meta:
        managed = False
        db_table = 'parserErrors'


class Pathologypermissions(models.Model):
    userid = models.IntegerField(db_column='userID', unique=True)  # Field name made lowercase.
    isadmin = models.IntegerField(db_column='isAdmin')  # Field name made lowercase.
    ismedicaldirector = models.IntegerField(db_column='isMedicalDirector')  # Field name made lowercase.
    cytology = models.IntegerField()
    histology = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pathologyPermissions'


class Pathologypreferences(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    autosave = models.IntegerField()
    quickrelease = models.IntegerField(db_column='quickRelease')  # Field name made lowercase.
    autosavetime = models.IntegerField(db_column='autosaveTime', blank=True, null=True)  # Field name made lowercase.
    imagesrequired = models.IntegerField(db_column='imagesRequired')  # Field name made lowercase.
    license = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'pathologyPreferences'


class Patientdetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstname = models.CharField(db_column='firstName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    homeaddress = models.CharField(db_column='homeAddress', max_length=255)  # Field name made lowercase.
    homecity = models.CharField(db_column='homeCity', max_length=45)  # Field name made lowercase.
    homestate = models.CharField(db_column='homeState', max_length=2)  # Field name made lowercase.
    homezip = models.CharField(db_column='homeZip', max_length=5)  # Field name made lowercase.
    dob = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    clientid = models.CharField(db_column='clientID', max_length=11)  # Field name made lowercase.
    primaryinsurancecode = models.IntegerField(db_column='primaryInsuranceCode')  # Field name made lowercase.
    primaryinsurancepolicy = models.CharField(db_column='primaryInsurancePolicy', max_length=20)  # Field name made lowercase.
    relationtoinsured = models.CharField(db_column='relationToInsured', max_length=6)  # Field name made lowercase.
    chartnumber = models.CharField(db_column='chartNumber', max_length=45)  # Field name made lowercase.
    secondaryphone = models.CharField(db_column='secondaryPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    forcovid = models.IntegerField(db_column='forCovid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patientDetails'
        unique_together = (('firstname', 'lastname', 'dob', 'clientid'),)


class Patientpayments(models.Model):
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    memo = models.CharField(max_length=255)
    amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'patientPayments'


class Patientservicecenterdocs(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    file = models.CharField(max_length=45)
    description = models.CharField(max_length=5000)
    video = models.CharField(max_length=45)
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patientServiceCenterDocs'


class Patientservicecenterdocs2(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    file = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    video = models.CharField(max_length=45)
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patientServiceCenterDocs2'


class Patients(models.Model):
    id = models.BigAutoField(primary_key=True)
    requisitionid = models.CharField(db_column='requisitionID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accessionid = models.CharField(db_column='accessionID', max_length=14, blank=True, null=True)  # Field name made lowercase.
    originalaccession = models.CharField(db_column='originalAccession', max_length=14, blank=True, null=True)  # Field name made lowercase.
    patientid = models.CharField(db_column='patientID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    middlename = models.CharField(db_column='middleName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    dob = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    homeaddress = models.CharField(db_column='homeAddress', max_length=255)  # Field name made lowercase.
    homecity = models.CharField(db_column='homeCity', max_length=45)  # Field name made lowercase.
    homestate = models.CharField(db_column='homeState', max_length=2)  # Field name made lowercase.
    homezip = models.CharField(db_column='homeZip', max_length=5)  # Field name made lowercase.
    billingaddress = models.CharField(db_column='billingAddress', max_length=255)  # Field name made lowercase.
    billingcity = models.CharField(db_column='billingCity', max_length=45)  # Field name made lowercase.
    billingstate = models.CharField(db_column='billingState', max_length=2)  # Field name made lowercase.
    billingzip = models.CharField(db_column='billingZip', max_length=5)  # Field name made lowercase.
    phone = models.CharField(max_length=20)
    clientid = models.IntegerField(db_column='clientID')  # Field name made lowercase.
    physicianid = models.IntegerField(db_column='physicianID')  # Field name made lowercase.
    phlebotomistid = models.IntegerField(db_column='phlebotomistID')  # Field name made lowercase.
    patientservicecenterid = models.IntegerField(db_column='patientServiceCenterID')  # Field name made lowercase.
    collectiondate = models.DateTimeField(db_column='collectionDate', blank=True, null=True)  # Field name made lowercase.
    receiveddate = models.DateTimeField(db_column='receivedDate', blank=True, null=True)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    isfasting = models.IntegerField(db_column='isFasting', blank=True, null=True)  # Field name made lowercase.
    housecallrepeat = models.CharField(db_column='houseCallRepeat', max_length=50)  # Field name made lowercase.
    housecallrepeaton = models.IntegerField(db_column='houseCallRepeatOn', blank=True, null=True)  # Field name made lowercase.
    housecallrepeatperiod = models.CharField(db_column='houseCallRepeatPeriod', max_length=7, blank=True, null=True)  # Field name made lowercase.
    housecallrepeatfrom = models.DateField(db_column='houseCallRepeatFrom', blank=True, null=True)  # Field name made lowercase.
    housecallrepeatto = models.DateField(db_column='houseCallRepeatTo', blank=True, null=True)  # Field name made lowercase.
    housecalllabreferralrequestedby = models.CharField(db_column='houseCallLabReferralRequestedBy', max_length=50)  # Field name made lowercase.
    clinicalinformation = models.TextField(db_column='clinicalInformation')  # Field name made lowercase.
    miscellaneousdiagnosisinformation = models.TextField(db_column='miscellaneousDiagnosisInformation')  # Field name made lowercase.
    ssn = models.CharField(max_length=12)
    ordertype = models.CharField(db_column='orderType', max_length=19, blank=True, null=True)  # Field name made lowercase.
    billto = models.CharField(db_column='billTo', max_length=11)  # Field name made lowercase.
    relationtoinsured = models.CharField(db_column='relationToInsured', max_length=7)  # Field name made lowercase.
    status = models.CharField(max_length=11)
    islabfinder = models.IntegerField(db_column='isLabFinder')  # Field name made lowercase.
    iscritical = models.IntegerField(db_column='isCritical')  # Field name made lowercase.
    aretestsfinalized = models.IntegerField(db_column='areTestsFinalized')  # Field name made lowercase.
    isvalid = models.IntegerField(db_column='isValid')  # Field name made lowercase.
    toclaim = models.IntegerField(db_column='toClaim')  # Field name made lowercase.
    isreviewed = models.IntegerField(db_column='isReviewed')  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    additionalinformation = models.CharField(db_column='additionalInformation', max_length=1000)  # Field name made lowercase.
    isigs = models.IntegerField(db_column='isIGS')  # Field name made lowercase.
    ispriority = models.IntegerField(db_column='isPriority')  # Field name made lowercase.
    chartnumber = models.CharField(db_column='chartNumber', max_length=255)  # Field name made lowercase.
    ismaternal = models.IntegerField(db_column='isMaternal')  # Field name made lowercase.
    issubmitedforredraw = models.IntegerField(db_column='isSubmitedForRedraw')  # Field name made lowercase.
    wellcomfinal = models.IntegerField(db_column='wellcomFinal')  # Field name made lowercase.
    totalvolume = models.CharField(db_column='totalVolume', max_length=45)  # Field name made lowercase.
    isabnormal = models.IntegerField(db_column='isAbnormal')  # Field name made lowercase.
    istnp = models.IntegerField(db_column='isTNP')  # Field name made lowercase.
    igstype = models.CharField(db_column='igsType', max_length=45)  # Field name made lowercase.
    qc = models.IntegerField()
    signed = models.IntegerField()
    isflorida = models.IntegerField(db_column='isFlorida')  # Field name made lowercase.
    email = models.CharField(max_length=255)
    abnormalcytohisto = models.IntegerField(db_column='abnormalCytoHisto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patients'
        unique_together = (('accessionid', 'isflorida'),)


class Patients2Insurances(models.Model):
    id = models.BigAutoField(primary_key=True)
    patientid = models.BigIntegerField(db_column='patientID')  # Field name made lowercase.
    insuranceid = models.IntegerField(db_column='insuranceID')  # Field name made lowercase.
    policynumber = models.CharField(db_column='policyNumber', max_length=1000)  # Field name made lowercase.
    isprimary = models.IntegerField(db_column='isPrimary')  # Field name made lowercase.
    billable = models.IntegerField()
    otherinsuranceinfo = models.JSONField(db_column='otherInsuranceInfo', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='groupID', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patients2insurances'
        unique_together = (('patientid', 'insuranceid', 'policynumber'),)


class Patientsmissingdiagnosis(models.Model):
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    testcode = models.CharField(db_column='testCode', max_length=20)  # Field name made lowercase.
    cptcode = models.CharField(db_column='cptCode', max_length=6)  # Field name made lowercase.
    queueid = models.IntegerField(db_column='queueID', blank=True, null=True)  # Field name made lowercase.
    matcheddiagnoses = models.JSONField(db_column='matchedDiagnoses', blank=True, null=True)  # Field name made lowercase.
    assigneddiagnoses = models.JSONField(db_column='assignedDiagnoses', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField()
    isprinted = models.IntegerField(db_column='isPrinted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patientsMissingDiagnosis'
        unique_together = (('patientid', 'testcode', 'cptcode'),)


class Payments(models.Model):
    id = models.BigAutoField(primary_key=True)
    invoice = models.CharField(max_length=255)
    confirmation = models.CharField(max_length=255)
    date = models.DateTimeField()
    sentlis = models.IntegerField(db_column='sentLIS')  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=255)  # Field name made lowercase.
    dob = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'payments'
        unique_together = (('invoice', 'confirmation'),)


class Pfinsurance(models.Model):
    ecl = models.CharField(max_length=45)
    pf = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'pfinsurance'


class Phlebotomists(models.Model):
    lastname = models.CharField(db_column='lastName', max_length=20)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=20)  # Field name made lowercase.
    phone = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'phlebotomists'


class Physicians(models.Model):
    id = models.SmallAutoField(primary_key=True)
    clientid = models.IntegerField(db_column='clientID', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=50, blank=True, null=True)
    fullname = models.CharField(db_column='fullName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastinitial = models.CharField(db_column='lastInitial', max_length=1, blank=True, null=True)  # Field name made lowercase.
    firstinitial = models.CharField(db_column='firstInitial', max_length=1, blank=True, null=True)  # Field name made lowercase.
    npi = models.CharField(max_length=12, blank=True, null=True)
    notify = models.IntegerField()
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'physicians'


class Printedreports2Users(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    accessionid = models.CharField(db_column='accessionID', max_length=45)  # Field name made lowercase.
    filename = models.CharField(db_column='fileName', max_length=255)  # Field name made lowercase.
    comments = models.CharField(max_length=255)
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'printedReports2Users'


class Problembox(models.Model):
    accessionid = models.CharField(db_column='accessionID', unique=True, max_length=45)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    enteredby = models.IntegerField(db_column='enteredBy')  # Field name made lowercase.
    entrycomment = models.CharField(db_column='entryComment', max_length=2000)  # Field name made lowercase.
    generalnotes = models.CharField(db_column='generalNotes', max_length=2000)  # Field name made lowercase.
    finaldate = models.DateTimeField(db_column='finalDate', blank=True, null=True)  # Field name made lowercase.
    finalby = models.IntegerField(db_column='finalBy', blank=True, null=True)  # Field name made lowercase.
    iscompleted = models.IntegerField(db_column='isCompleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'problemBox'


class Problemboxfl(models.Model):
    id = models.BigAutoField(primary_key=True)
    accessionid = models.CharField(db_column='accessionID', unique=True, max_length=45)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    enteredby = models.IntegerField(db_column='enteredBy')  # Field name made lowercase.
    description = models.CharField(max_length=2000)
    generalnotes = models.CharField(db_column='generalNotes', max_length=2000)  # Field name made lowercase.
    finaldate = models.DateTimeField(db_column='finalDate', blank=True, null=True)  # Field name made lowercase.
    finalby = models.IntegerField(db_column='finalBy', blank=True, null=True)  # Field name made lowercase.
    iscompleted = models.IntegerField(db_column='isCompleted')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientID', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=255)  # Field name made lowercase.
    entrycomment = models.CharField(db_column='entryComment', max_length=2000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'problemBoxFL'


class Pushtoigs(models.Model):
    accessionid = models.CharField(db_column='accessionID', max_length=45)  # Field name made lowercase.
    user = models.CharField(max_length=255)
    date = models.DateTimeField()
    isprocessed = models.IntegerField(db_column='isProcessed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pushToIGS'


class Queue(models.Model):
    params = models.JSONField()
    worker = models.CharField(max_length=30)
    status = models.CharField(max_length=10)
    totalnumber = models.IntegerField(db_column='totalNumber')  # Field name made lowercase.
    currentnumber = models.IntegerField(db_column='currentNumber')  # Field name made lowercase.
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'queue'


class Reasonhistory(models.Model):
    cpthistoryid = models.IntegerField(db_column='cptHistoryID')  # Field name made lowercase.
    code = models.CharField(max_length=10)
    amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'reasonHistory'
        unique_together = (('cpthistoryid', 'code'),)


class Regularpickup(models.Model):
    id = models.BigAutoField(primary_key=True)
    clientid = models.IntegerField(db_column='clientID')  # Field name made lowercase.
    notes = models.CharField(max_length=255)
    driverid = models.IntegerField(db_column='driverID', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=9)
    qntpickedup = models.CharField(db_column='qntPickedUp', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pickedupdate = models.DateTimeField(db_column='pickedUpDate', blank=True, null=True)  # Field name made lowercase.
    qntdelivered = models.CharField(db_column='qntDelivered', max_length=45, blank=True, null=True)  # Field name made lowercase.
    datedelivered = models.DateTimeField(db_column='dateDelivered', blank=True, null=True)  # Field name made lowercase.
    confirmeddate = models.DateTimeField(db_column='confirmedDate', blank=True, null=True)  # Field name made lowercase.
    scheduleid = models.CharField(db_column='scheduleID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(max_length=255)
    date = models.DateTimeField()
    base64 = models.CharField(max_length=45, blank=True, null=True)
    confirmuser = models.CharField(db_column='confirmUser', max_length=255)  # Field name made lowercase.
    labcomment = models.CharField(db_column='labComment', max_length=255)  # Field name made lowercase.
    routeid = models.IntegerField(db_column='routeID', blank=True, null=True)  # Field name made lowercase.
    day = models.CharField(max_length=45)
    scheduletime = models.CharField(db_column='scheduleTime', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'regularPickup'


class Regularpickup2(models.Model):
    id = models.BigAutoField(primary_key=True)
    clientid = models.IntegerField(db_column='clientID')  # Field name made lowercase.
    notes = models.CharField(max_length=255)
    driverid = models.IntegerField(db_column='driverID', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=9)
    qntpickedup = models.CharField(db_column='qntPickedUp', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pickedupdate = models.DateTimeField(db_column='pickedUpDate', blank=True, null=True)  # Field name made lowercase.
    qntdelivered = models.CharField(db_column='qntDelivered', max_length=45, blank=True, null=True)  # Field name made lowercase.
    datedelivered = models.DateTimeField(db_column='dateDelivered', blank=True, null=True)  # Field name made lowercase.
    confirmeddate = models.DateTimeField(db_column='confirmedDate', blank=True, null=True)  # Field name made lowercase.
    scheduleid = models.CharField(db_column='scheduleID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(max_length=255)
    date = models.DateTimeField()
    base64 = models.CharField(max_length=45, blank=True, null=True)
    confirmuser = models.CharField(db_column='confirmUser', max_length=255)  # Field name made lowercase.
    labcomment = models.CharField(db_column='labComment', max_length=255)  # Field name made lowercase.
    routeid = models.IntegerField(db_column='routeID', blank=True, null=True)  # Field name made lowercase.
    day = models.CharField(max_length=45)
    scheduletime = models.CharField(db_column='scheduleTime', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'regularPickup2'
        unique_together = (('clientid', 'routeid', 'scheduletime', 'date'),)


class Remarkhistory(models.Model):
    cpthistoryid = models.IntegerField(db_column='cptHistoryID')  # Field name made lowercase.
    code = models.CharField(max_length=10)
    value = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'remarkHistory'
        unique_together = (('cpthistoryid', 'code'),)


class Reportcomments(models.Model):
    id = models.SmallAutoField(primary_key=True)
    department = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    section = models.CharField(max_length=60)
    key = models.CharField(max_length=40)
    value = models.TextField()
    action = models.CharField(max_length=9)
    color = models.CharField(max_length=10)
    isrequired = models.IntegerField(db_column='isRequired')  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    malignant = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reportComments'


class Route2Driver(models.Model):
    routeid = models.IntegerField(db_column='routeID')  # Field name made lowercase.
    driverid = models.IntegerField(db_column='driverID')  # Field name made lowercase.
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'route2driver'


class Routes(models.Model):
    code = models.CharField(unique=True, max_length=45)
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    date = models.DateTimeField()
    driverid = models.IntegerField(db_column='driverID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'routes'


class Sales(models.Model):
    salesid = models.CharField(db_column='salesID', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    phone = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    groupid = models.CharField(db_column='groupID', max_length=45)  # Field name made lowercase.
    percent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sales'
        unique_together = (('salesid', 'groupid'),)


class Salescontest(models.Model):
    salesid = models.CharField(db_column='salesID', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    salesname = models.CharField(db_column='salesName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    clientqnt = models.CharField(db_column='clientQNT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    testqnt = models.IntegerField(db_column='testQNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salesContest'


class Salescontestdetails(models.Model):
    salesid = models.CharField(db_column='salesID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    clientid = models.CharField(db_column='clientID', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    patientsqnt = models.CharField(db_column='patientsQNT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    salesqnt = models.CharField(db_column='salesQNT', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salesContestDetails'


class Salesgroups(models.Model):
    salesgroupid = models.IntegerField(db_column='salesGroupID')  # Field name made lowercase.
    salesrepid = models.CharField(db_column='salesRepID', max_length=5)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=20)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=20)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    individual = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salesGroups'


class Salespermissions(models.Model):
    userid = models.IntegerField(db_column='userID', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salesPermissions'


class Salesreps(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(db_column='firstName', max_length=20)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=20)  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    individual = models.CharField(max_length=10, blank=True, null=True)
    idold = models.CharField(db_column='idOld', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salesReps'


class Schedule2Driver(models.Model):
    id = models.BigAutoField(primary_key=True)
    scheduleid = models.IntegerField(db_column='scheduleID')  # Field name made lowercase.
    driverid = models.IntegerField(db_column='driverID')  # Field name made lowercase.
    time = models.CharField(max_length=45)
    notes = models.CharField(max_length=4000)
    routeid = models.IntegerField(db_column='routeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schedule2driver'
        unique_together = (('scheduleid', 'routeid', 'time'),)


class Sendoutorder2Test(models.Model):
    id = models.BigAutoField(primary_key=True)
    orderid = models.BigIntegerField(db_column='orderID')  # Field name made lowercase.
    testcode = models.CharField(db_column='testCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    isprocessed = models.IntegerField(db_column='isProcessed')  # Field name made lowercase.
    isqns = models.IntegerField(db_column='isQns')  # Field name made lowercase.
    isnss = models.IntegerField(db_column='isNss')  # Field name made lowercase.
    testhistoryid = models.BigIntegerField(db_column='testHistoryID')  # Field name made lowercase.
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sendOutOrder2test'


class Sendoutcomments(models.Model):
    testhistoryid = models.IntegerField(db_column='testHistoryID', unique=True)  # Field name made lowercase.
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    assignto = models.IntegerField(db_column='assignTo', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=45, blank=True, null=True)
    testcode = models.CharField(db_column='testCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    isprocessed = models.IntegerField(db_column='isProcessed')  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    iscancelledinquest = models.IntegerField(db_column='isCancelledInQuest')  # Field name made lowercase.
    isprinted = models.IntegerField(db_column='isPrinted')  # Field name made lowercase.
    printedon = models.DateTimeField(db_column='printedOn', blank=True, null=True)  # Field name made lowercase.
    printedby = models.CharField(db_column='printedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sendoutComments'


class Sendoutdictionary(models.Model):
    code = models.CharField(max_length=45)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sendoutDictionary'


class Sendouthistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    testhistoryid = models.BigIntegerField(db_column='testHistoryID')  # Field name made lowercase.
    patientid = models.BigIntegerField(db_column='patientID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    testcode = models.CharField(db_column='testCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    iscancelledinquest = models.IntegerField(db_column='isCancelledInQuest')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sendoutHistory'


class Sendoutorders(models.Model):
    id = models.BigAutoField(primary_key=True)
    ordernumber = models.CharField(db_column='orderNumber', max_length=100)  # Field name made lowercase.
    json = models.JSONField()
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    mailoutlab = models.CharField(db_column='mailoutLab', max_length=100)  # Field name made lowercase.
    source = models.CharField(max_length=45)
    userid = models.IntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    accessionid = models.CharField(db_column='accessionID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    isprocessed = models.IntegerField(db_column='isProcessed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sendoutOrders'


class Sendoutpanels(models.Model):
    code = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    mailoutcode = models.CharField(db_column='mailoutCode', max_length=45)  # Field name made lowercase.
    mailoutdescription = models.CharField(db_column='mailoutDescription', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sendoutPanels'


class Sendoutpermissions(models.Model):
    userid = models.IntegerField(db_column='userID', unique=True)  # Field name made lowercase.
    issupervisor = models.IntegerField(db_column='isSupervisor')  # Field name made lowercase.
    isadmin = models.IntegerField(db_column='isAdmin')  # Field name made lowercase.
    ispendout = models.IntegerField(db_column='isPendOut')  # Field name made lowercase.
    nightshift = models.IntegerField(db_column='nightShift')  # Field name made lowercase.
    isroutine = models.IntegerField(db_column='isRoutine')  # Field name made lowercase.
    quest = models.IntegerField()
    acls = models.IntegerField()
    cordant = models.IntegerField()
    genova = models.IntegerField()
    labcorp = models.IntegerField()
    mayo = models.IntegerField()
    prometheus = models.IntegerField()
    tenet = models.IntegerField()
    neo = models.IntegerField()
    isdoh = models.IntegerField(db_column='isDOH')  # Field name made lowercase.
    kashi = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sendoutPermissions'


class Sendoutrequisition(models.Model):
    testhistoryid = models.CharField(db_column='testHistoryID', max_length=11)  # Field name made lowercase.
    patientid = models.CharField(db_column='patientID', max_length=11)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    ordernumber = models.CharField(db_column='orderNumber', max_length=20)  # Field name made lowercase.
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sendoutRequisition'


class Sessions(models.Model):
    sid = models.CharField(primary_key=True, max_length=255)
    session = models.TextField()
    expires = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessions'


class Solv(models.Model):
    id = models.BigAutoField(primary_key=True)
    practicename = models.CharField(db_column='practiceName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clinicname = models.CharField(db_column='clinicName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField()
    firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=245, blank=True, null=True)  # Field name made lowercase.
    dob = models.CharField(max_length=45, blank=True, null=True)
    birthsex = models.CharField(db_column='birthSex', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=245, blank=True, null=True)
    address1 = models.CharField(max_length=300, blank=True, null=True)
    address2 = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    zip = models.CharField(max_length=15, blank=True, null=True)
    mobile = models.CharField(max_length=25, blank=True, null=True)
    bookedbyfirstname = models.CharField(db_column='bookedByFirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bookedbylastname = models.CharField(db_column='bookedByLastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bookinginsurancecarrier = models.CharField(db_column='bookingInsuranceCarrier', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bookingmemberid = models.CharField(db_column='bookingMemberID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bookinginsuranceinsurertype = models.CharField(db_column='bookingInsuranceInsurerType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    employer = models.CharField(max_length=45, blank=True, null=True)
    ethnicity = models.CharField(max_length=45, blank=True, null=True)
    race = models.CharField(max_length=45, blank=True, null=True)
    paywithinsurance = models.CharField(db_column='payWithInsurance', max_length=45, blank=True, null=True)  # Field name made lowercase.
    insureddob = models.CharField(db_column='insuredDob', max_length=45, blank=True, null=True)  # Field name made lowercase.
    insuredlastname = models.CharField(db_column='insuredLastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    insuredfirstname = models.CharField(db_column='insuredFirstName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    symptoms = models.CharField(max_length=45, blank=True, null=True)
    risk = models.CharField(max_length=45, blank=True, null=True)
    senttoudotest = models.IntegerField(db_column='sentToUdotest')  # Field name made lowercase.
    appdate = models.DateField(db_column='appDate', blank=True, null=True)  # Field name made lowercase.
    apptime = models.CharField(db_column='appTime', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ordernumber = models.CharField(db_column='orderNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'solv'


class Somos(models.Model):
    order = models.CharField(max_length=45, blank=True, null=True)
    last = models.CharField(max_length=45, blank=True, null=True)
    first = models.CharField(max_length=45, blank=True, null=True)
    label = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'somos'


class Somosfit(models.Model):
    id = models.BigAutoField(primary_key=True)
    clientid = models.IntegerField(db_column='clientID')  # Field name made lowercase.
    physicianid = models.IntegerField(db_column='physicianID')  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=255)  # Field name made lowercase.
    dob = models.DateField(blank=True, null=True)
    insuranceid = models.IntegerField(db_column='insuranceID', blank=True, null=True)  # Field name made lowercase.
    policy = models.CharField(max_length=45, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    zip = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateTimeField()
    testcode = models.CharField(db_column='testCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    isprinted = models.IntegerField(db_column='isPrinted')  # Field name made lowercase.
    requisitionid = models.CharField(db_column='requisitionID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    npi = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'somosFit'


class Somosorders(models.Model):
    barcode = models.CharField(max_length=45)
    accessionid = models.CharField(db_column='accessionID', max_length=45)  # Field name made lowercase.
    date = models.DateTimeField()
    dateaccessioned = models.DateTimeField(db_column='dateAccessioned', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'somosOrders'


class SomosProblem(models.Model):
    label = models.CharField(max_length=255, blank=True, null=True)
    order = models.CharField(max_length=255, blank=True, null=True)
    accession = models.CharField(max_length=255, blank=True, null=True)
    last = models.CharField(max_length=455, blank=True, null=True)
    first = models.CharField(max_length=455, blank=True, null=True)
    dob = models.CharField(max_length=455, blank=True, null=True)
    phone = models.CharField(max_length=455, blank=True, null=True)
    cell = models.CharField(max_length=455, blank=True, null=True)
    site = models.CharField(max_length=455, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'somos_problem'


class Specimenhistory(models.Model):
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    code = models.CharField(max_length=20)
    quantity = models.IntegerField()
    totalvolume = models.IntegerField(db_column='totalVolume')  # Field name made lowercase.
    idold = models.CharField(db_column='idOld', max_length=24)  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'specimenHistory'
        unique_together = (('patientid', 'code'),)


class Specimens(models.Model):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'specimens'


class Statentry(models.Model):
    id = models.BigAutoField(primary_key=True)
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    testhistoryid = models.BigIntegerField(db_column='testHistoryID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    department = models.CharField(max_length=45)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'statEntry'
        unique_together = (('patientid', 'testhistoryid'),)


class Statfollowup(models.Model):
    pickupid = models.BigIntegerField(db_column='pickupID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'statFollowup'


class Statnotifications(models.Model):
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    accessionid = models.CharField(db_column='accessionID', max_length=14)  # Field name made lowercase.
    testcode = models.CharField(db_column='testCode', max_length=20)  # Field name made lowercase.
    sentat = models.DateTimeField(db_column='sentAt', blank=True, null=True)  # Field name made lowercase.
    scannedat = models.DateTimeField(db_column='scannedAt', blank=True, null=True)  # Field name made lowercase.
    finalizedat = models.DateTimeField(db_column='finalizedAt', blank=True, null=True)  # Field name made lowercase.
    users = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'statNotifications'
        unique_together = (('patientid', 'testcode'),)


class Statpickup(models.Model):
    id = models.BigAutoField(primary_key=True)
    confirmation = models.CharField(unique=True, max_length=45)
    resultsby = models.CharField(db_column='resultsBy', max_length=45)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    driverid = models.BigIntegerField(db_column='driverID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.BigIntegerField(db_column='clientID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'statPickup'


class Statpickup2Patient(models.Model):
    id = models.BigAutoField(primary_key=True)
    patientid = models.BigIntegerField(db_column='patientID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.BigIntegerField(db_column='clientID', blank=True, null=True)  # Field name made lowercase.
    notes = models.JSONField(blank=True, null=True)
    isfinal = models.IntegerField(db_column='isFinal')  # Field name made lowercase.
    date = models.DateTimeField()
    confirmation = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'statPickup2patient'
        unique_together = (('patientid', 'confirmation'),)


class Statpickupnotes(models.Model):
    id = models.BigAutoField(primary_key=True)
    statpatientid = models.BigIntegerField(db_column='statPatientID')  # Field name made lowercase.
    note = models.CharField(max_length=1000)
    date = models.DateTimeField()
    user = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'statPickupNotes'


class Statstationpermissions(models.Model):
    userid = models.IntegerField(db_column='userID', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'statStationPermissions'


class Stats(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    department = models.CharField(max_length=20)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stats'


class Supplies(models.Model):
    name = models.CharField(max_length=255)
    section = models.CharField(max_length=255)
    type = models.CharField(max_length=9)
    link = models.CharField(max_length=4000, blank=True, null=True)
    approval = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'supplies'


class Supplyorder(models.Model):
    ordernumber = models.CharField(db_column='orderNumber', unique=True, max_length=255)  # Field name made lowercase.
    notes = models.CharField(max_length=5000)
    tracking = models.CharField(max_length=1000)
    status = models.CharField(max_length=10)
    email = models.CharField(max_length=255)
    date = models.DateTimeField()
    sales = models.CharField(max_length=255, blank=True, null=True)
    clientid = models.IntegerField(db_column='clientID', blank=True, null=True)  # Field name made lowercase.
    shippingdate = models.DateTimeField(db_column='shippingDate', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(max_length=255)
    inprocess = models.IntegerField(db_column='inProcess')  # Field name made lowercase.
    address = models.CharField(max_length=255)
    ispsc = models.IntegerField(db_column='isPSC')  # Field name made lowercase.
    isdriver = models.IntegerField(db_column='isDriver')  # Field name made lowercase.
    driverid = models.IntegerField(db_column='driverID', blank=True, null=True)  # Field name made lowercase.
    pushedtony = models.IntegerField(db_column='pushedToNY')  # Field name made lowercase.
    pushedtofl = models.IntegerField(db_column='pushedToFL')  # Field name made lowercase.
    printedon = models.DateTimeField(db_column='printedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplyOrder'


class Supplyorderhistory(models.Model):
    supplyorderid = models.IntegerField(db_column='supplyOrderID')  # Field name made lowercase.
    supplyid = models.IntegerField(db_column='supplyID')  # Field name made lowercase.
    name = models.CharField(max_length=255)
    qnt = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'supplyOrderHistory'
        unique_together = (('supplyorderid', 'supplyid'),)


class Test2Comment(models.Model):
    testdictionaryid = models.IntegerField(db_column='testDictionaryID')  # Field name made lowercase.
    testcommentdictionaryid = models.IntegerField(db_column='testCommentDictionaryID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test2comment'
        unique_together = (('testdictionaryid', 'testcommentdictionaryid'),)


class Test2Element(models.Model):
    testid = models.IntegerField(db_column='testID')  # Field name made lowercase.
    elementid = models.IntegerField(db_column='elementID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test2element'
        unique_together = (('testid', 'elementid'),)


class Testcode2Department(models.Model):
    testcode = models.CharField(db_column='testCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=45, blank=True, null=True)
    department = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testCode2Department'


class Testcode2Cptcode(models.Model):
    testid = models.CharField(db_column='testID', max_length=11)  # Field name made lowercase.
    cptcode = models.CharField(db_column='cptCode', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'testCode2cptCode'


class Testcommentsdictionary(models.Model):
    code = models.CharField(max_length=45)
    description = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'testCommentsDictionary'


class Testdictionary(models.Model):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    aoe = models.JSONField(db_column='AOE')  # Field name made lowercase.
    mailouttestcode = models.CharField(db_column='mailoutTestCode', max_length=20)  # Field name made lowercase.
    currentmailoutlab = models.CharField(db_column='currentMailoutLab', max_length=20)  # Field name made lowercase.
    ismailout = models.IntegerField(db_column='isMailout')  # Field name made lowercase.
    isbillsendout = models.IntegerField(db_column='isBillSendout')  # Field name made lowercase.
    isshortstability = models.IntegerField(db_column='isShortStability')  # Field name made lowercase.
    isstat = models.IntegerField(db_column='isStat')  # Field name made lowercase.
    ispriority = models.IntegerField(db_column='isPriority')  # Field name made lowercase.
    isbeacon = models.IntegerField(db_column='isBeacon')  # Field name made lowercase.
    isflorida = models.IntegerField(db_column='isFlorida')  # Field name made lowercase.
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testDictionary'
        unique_together = (('code', 'isflorida'),)


class Testhistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=9)
    ismailout = models.IntegerField(db_column='isMailout')  # Field name made lowercase.
    isbillsendout = models.IntegerField(db_column='isBillSendout')  # Field name made lowercase.
    comment = models.CharField(max_length=6000)
    datefinalized = models.DateTimeField(db_column='dateFinalized', blank=True, null=True)  # Field name made lowercase.
    json = models.JSONField()
    oldid = models.CharField(db_column='oldID', unique=True, max_length=25, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    isfinalizedwithcomment = models.IntegerField(db_column='isFinalizedWithComment')  # Field name made lowercase.
    date = models.DateTimeField()
    wellcomstatus = models.CharField(db_column='wellcomStatus', max_length=9)  # Field name made lowercase.
    isabnormal = models.IntegerField(db_column='isAbnormal')  # Field name made lowercase.
    isaddon = models.IntegerField(db_column='isAddon')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'testHistory'
        unique_together = (('patientid', 'code'),)


class Tests(models.Model):
    code = models.CharField(unique=True, max_length=20, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    billschedule = models.IntegerField(db_column='billSchedule', blank=True, null=True)  # Field name made lowercase.
    issearchable = models.IntegerField(db_column='isSearchable')  # Field name made lowercase.
    isbillable = models.IntegerField(db_column='isBillable')  # Field name made lowercase.
    mailoutlabname = models.CharField(db_column='mailoutLabName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mailoutlabcode = models.CharField(db_column='mailoutLabCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mailouttestcode = models.TextField(db_column='mailoutTestCode', blank=True, null=True)  # Field name made lowercase.
    ismailout = models.IntegerField(db_column='isMailout', blank=True, null=True)  # Field name made lowercase.
    isbillsendout = models.IntegerField(db_column='isBillSendout')  # Field name made lowercase.
    specimenrequired = models.TextField(db_column='specimenRequired', blank=True, null=True)  # Field name made lowercase.
    specimenvolume = models.TextField(db_column='specimenVolume', blank=True, null=True)  # Field name made lowercase.
    specimencontainer = models.TextField(db_column='specimenContainer', blank=True, null=True)  # Field name made lowercase.
    alternatespecimen = models.TextField(db_column='alternateSpecimen', blank=True, null=True)  # Field name made lowercase.
    specimenstability = models.TextField(db_column='specimenStability', blank=True, null=True)  # Field name made lowercase.
    turnarounddays = models.TextField(db_column='turnAroundDays', blank=True, null=True)  # Field name made lowercase.
    collectioninstructions = models.TextField(db_column='collectionInstructions', blank=True, null=True)  # Field name made lowercase.
    shippingtemperature = models.TextField(db_column='shippingTemperature', blank=True, null=True)  # Field name made lowercase.
    testlimitations = models.TextField(db_column='testLimitations', blank=True, null=True)  # Field name made lowercase.
    rejectioncriteria = models.TextField(db_column='rejectionCriteria', blank=True, null=True)  # Field name made lowercase.
    clinicalinformation = models.TextField(db_column='clinicalInformation', blank=True, null=True)  # Field name made lowercase.
    hasadditional = models.IntegerField(db_column='hasAdditional')  # Field name made lowercase.
    notes = models.CharField(max_length=255, blank=True, null=True)
    billingalways = models.IntegerField(db_column='billingAlways')  # Field name made lowercase.
    billingnever = models.IntegerField(db_column='billingNever')  # Field name made lowercase.
    ispanel = models.IntegerField(db_column='isPanel')  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    isgroupforbilling = models.IntegerField(db_column='isGroupForBilling')  # Field name made lowercase.
    isshortstability = models.IntegerField(db_column='isShortStability')  # Field name made lowercase.
    sendoutcustom = models.IntegerField(db_column='sendoutCustom')  # Field name made lowercase.
    sendoutlongtat = models.IntegerField(db_column='sendoutLongTAT')  # Field name made lowercase.
    categorya = models.IntegerField(db_column='categoryA')  # Field name made lowercase.
    categoryb = models.IntegerField(db_column='categoryB')  # Field name made lowercase.
    categoryc = models.IntegerField(db_column='categoryC')  # Field name made lowercase.
    categoryd = models.IntegerField(db_column='categoryD')  # Field name made lowercase.
    categorye = models.IntegerField(db_column='categoryE')  # Field name made lowercase.
    categoryf = models.IntegerField(db_column='categoryF')  # Field name made lowercase.
    categoryg = models.IntegerField(db_column='categoryG')  # Field name made lowercase.
    categoryh = models.IntegerField(db_column='categoryH')  # Field name made lowercase.
    categoryi = models.IntegerField(db_column='categoryI')  # Field name made lowercase.
    isbeacon = models.IntegerField(db_column='isBeacon')  # Field name made lowercase.
    categoryj = models.IntegerField(db_column='categoryJ')  # Field name made lowercase.
    labcorpa = models.IntegerField(db_column='labcorpA')  # Field name made lowercase.
    labcorpb = models.IntegerField(db_column='labcorpB')  # Field name made lowercase.
    labcorpc = models.IntegerField(db_column='labcorpC')  # Field name made lowercase.
    labcorpd = models.IntegerField(db_column='labcorpD')  # Field name made lowercase.
    labcorpe = models.IntegerField(db_column='labcorpE')  # Field name made lowercase.
    labcorpf = models.IntegerField(db_column='labcorpF')  # Field name made lowercase.
    labcorpg = models.IntegerField(db_column='labcorpG')  # Field name made lowercase.
    labcorph = models.IntegerField(db_column='labcorpH')  # Field name made lowercase.
    labcorpi = models.IntegerField(db_column='labcorpI')  # Field name made lowercase.
    labcorpj = models.IntegerField(db_column='labcorpJ')  # Field name made lowercase.
    labcorprequired = models.CharField(db_column='labcorpRequired', max_length=255)  # Field name made lowercase.
    labcorpalternative = models.CharField(db_column='labcorpAlternative', max_length=255)  # Field name made lowercase.
    labcorpvolume = models.CharField(db_column='labcorpVolume', max_length=45)  # Field name made lowercase.
    labcorptemp = models.CharField(db_column='labcorpTemp', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tests'


class Tests2Clients(models.Model):
    id = models.SmallAutoField(primary_key=True)
    clientid = models.SmallIntegerField(db_column='clientID')  # Field name made lowercase.
    code = models.TextField()
    price = models.FloatField()
    date = models.DateTimeField()
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tests2clients'


class Tests2Cpts(models.Model):
    testid = models.SmallIntegerField(db_column='testID')  # Field name made lowercase.
    cptid = models.SmallIntegerField(db_column='cptID')  # Field name made lowercase.
    units = models.IntegerField()
    modifier = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tests2cpts'


class Tests2Panels(models.Model):
    panelcode = models.CharField(db_column='panelCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    testcode = models.CharField(db_column='testCode', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tests2panels'
        unique_together = (('panelcode', 'testcode'),)


class Tray(models.Model):
    id = models.BigAutoField(primary_key=True)
    trayid = models.CharField(db_column='trayID', max_length=45)  # Field name made lowercase.
    row = models.IntegerField()
    column = models.IntegerField()
    patientid = models.IntegerField(db_column='patientID', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tray'
        unique_together = (('trayid', 'row', 'column'),)


class Traylocation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    patientid = models.BigIntegerField(db_column='patientID')  # Field name made lowercase.
    tray = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'trayLocation'


class Useraccess(models.Model):
    userid = models.IntegerField(db_column='userID', unique=True)  # Field name made lowercase.
    billing = models.IntegerField()
    cytology = models.IntegerField()
    inventory = models.IntegerField()
    sales = models.IntegerField()
    clientservices = models.IntegerField(db_column='clientServices')  # Field name made lowercase.
    housecall = models.IntegerField(db_column='houseCall')  # Field name made lowercase.
    histology = models.IntegerField()
    sendout = models.IntegerField()
    pathology = models.IntegerField()
    statstation = models.IntegerField(db_column='statStation')  # Field name made lowercase.
    drawstation = models.IntegerField(db_column='drawStation')  # Field name made lowercase.
    supplies = models.IntegerField()
    logistics = models.IntegerField()
    admin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'userAccess'


class Users(models.Model):
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    middleinitial = models.CharField(db_column='middleInitial', max_length=1)  # Field name made lowercase.
    title = models.CharField(max_length=45, blank=True, null=True)
    photo = models.CharField(max_length=45)
    barcode = models.CharField(max_length=20)
    login = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    role = models.CharField(max_length=45, blank=True, null=True)
    sessiontimeout = models.IntegerField(db_column='sessionTimeout')  # Field name made lowercase.
    misc = models.JSONField(blank=True, null=True)
    printer = models.IntegerField(blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    date = models.DateTimeField()
    email = models.CharField(max_length=255, blank=True, null=True)
    salesid = models.CharField(db_column='salesID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    printerip = models.CharField(db_column='printerIP', max_length=100)  # Field name made lowercase.
    driverid = models.IntegerField(db_column='driverID', blank=True, null=True)  # Field name made lowercase.
    psconly = models.IntegerField(db_column='pscOnly')  # Field name made lowercase.
    psccode = models.CharField(db_column='pscCode', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('firstname', 'lastname', 'login', 'password'),)


class Websitenewsletter(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=45)
    unsuscribe = models.IntegerField()
    sent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'websiteNewsletter'


class Wellcomdiagnosishistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    patientid = models.BigIntegerField(db_column='patientID')  # Field name made lowercase.
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wellcomDiagnosisHistory'
        unique_together = (('patientid', 'code'),)


class Wellcomdocuments(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wellcomDocuments'


class Wellcomorders(models.Model):
    id = models.BigAutoField(primary_key=True)
    patientid = models.BigIntegerField(db_column='patientID')  # Field name made lowercase.
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    json = models.JSONField()

    class Meta:
        managed = False
        db_table = 'wellcomOrders'
        unique_together = (('patientid', 'code'),)


class Wellcompatients(models.Model):
    id = models.BigAutoField(primary_key=True)
    requisitionid = models.CharField(db_column='requisitionID', unique=True, max_length=15, blank=True, null=True)  # Field name made lowercase.
    accessionid = models.CharField(db_column='accessionID', max_length=14, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    middlename = models.CharField(db_column='middleName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    dob = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    homeaddress = models.CharField(db_column='homeAddress', max_length=255)  # Field name made lowercase.
    homecity = models.CharField(db_column='homeCity', max_length=45)  # Field name made lowercase.
    homestate = models.CharField(db_column='homeState', max_length=2)  # Field name made lowercase.
    homezip = models.CharField(db_column='homeZip', max_length=5)  # Field name made lowercase.
    billingaddress = models.CharField(db_column='billingAddress', max_length=255)  # Field name made lowercase.
    billingcity = models.CharField(db_column='billingCity', max_length=45)  # Field name made lowercase.
    billingstate = models.CharField(db_column='billingState', max_length=2)  # Field name made lowercase.
    billingzip = models.CharField(db_column='billingZip', max_length=5)  # Field name made lowercase.
    phone = models.CharField(max_length=20)
    clientid = models.IntegerField(db_column='clientID')  # Field name made lowercase.
    physicianid = models.IntegerField(db_column='physicianID')  # Field name made lowercase.
    phlebotomistid = models.IntegerField(db_column='phlebotomistID')  # Field name made lowercase.
    patientservicecenterid = models.IntegerField(db_column='patientServiceCenterID')  # Field name made lowercase.
    collectiondate = models.DateTimeField(db_column='collectionDate', blank=True, null=True)  # Field name made lowercase.
    receiveddate = models.DateTimeField(db_column='receivedDate', blank=True, null=True)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='entryDate')  # Field name made lowercase.
    isfasting = models.IntegerField(db_column='isFasting', blank=True, null=True)  # Field name made lowercase.
    housecallrepeat = models.CharField(db_column='houseCallRepeat', max_length=50)  # Field name made lowercase.
    housecallrepeaton = models.IntegerField(db_column='houseCallRepeatOn', blank=True, null=True)  # Field name made lowercase.
    housecallrepeatperiod = models.CharField(db_column='houseCallRepeatPeriod', max_length=7, blank=True, null=True)  # Field name made lowercase.
    housecallrepeatfrom = models.DateField(db_column='houseCallRepeatFrom', blank=True, null=True)  # Field name made lowercase.
    housecallrepeatto = models.DateField(db_column='houseCallRepeatTo', blank=True, null=True)  # Field name made lowercase.
    housecalllabreferralrequestedby = models.CharField(db_column='houseCallLabReferralRequestedBy', max_length=50)  # Field name made lowercase.
    clinicalinformation = models.CharField(db_column='clinicalInformation', max_length=3000)  # Field name made lowercase.
    miscellaneousdiagnosisinformation = models.CharField(db_column='miscellaneousDiagnosisInformation', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ssn = models.CharField(max_length=12)
    ordertype = models.CharField(db_column='orderType', max_length=19, blank=True, null=True)  # Field name made lowercase.
    billto = models.CharField(db_column='billTo', max_length=11)  # Field name made lowercase.
    relationtoinsured = models.CharField(db_column='relationToInsured', max_length=7)  # Field name made lowercase.
    status = models.CharField(max_length=11)
    islabfinder = models.IntegerField(db_column='isLabFinder')  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    additionalinformation = models.CharField(db_column='additionalInformation', max_length=1000)  # Field name made lowercase.
    isigs = models.IntegerField(db_column='isIGS')  # Field name made lowercase.
    chartnumber = models.CharField(db_column='chartNumber', max_length=45)  # Field name made lowercase.
    hl7 = models.TextField(blank=True, null=True)
    beaconcase = models.CharField(db_column='beaconCase', max_length=255)  # Field name made lowercase.
    rushstatus = models.CharField(db_column='rushStatus', max_length=45)  # Field name made lowercase.
    email = models.CharField(max_length=255)
    isflorida = models.IntegerField(db_column='isFlorida')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wellcomPatients'


class Wellcompatients2Insurances(models.Model):
    patientid = models.IntegerField(db_column='patientID')  # Field name made lowercase.
    insuranceid = models.SmallIntegerField(db_column='insuranceID')  # Field name made lowercase.
    policynumber = models.CharField(db_column='policyNumber', max_length=20)  # Field name made lowercase.
    isprimary = models.IntegerField(db_column='isPrimary')  # Field name made lowercase.
    billable = models.IntegerField()
    otherinsuranceinfo = models.JSONField(db_column='otherInsuranceInfo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wellcomPatients2insurances'
        unique_together = (('patientid', 'insuranceid', 'policynumber'),)


class Wellcomuseraccess(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wellcomUserAccess'
        unique_together = (('userid', 'clientid'),)


class Wellcomusers(models.Model):
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    login = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    role = models.CharField(max_length=45, blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted')  # Field name made lowercase.
    date = models.DateTimeField()
    status = models.CharField(max_length=9)
    one = models.CharField(max_length=255)
    answer1 = models.CharField(max_length=255)
    two = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    clientid = models.IntegerField(db_column='clientID', blank=True, null=True)  # Field name made lowercase.
    covidsite = models.IntegerField(db_column='covidSite')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wellcomUsers'
