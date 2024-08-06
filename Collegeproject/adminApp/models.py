from django.db import models

# Create your models here.
class NoticeModel (models.Model):
    notice = models.CharField(max_length=200)

class VideoModel (models.Model):
    hvideo = models.FileField(upload_to="static/uploads/")

class DepartmentModel(models.Model):
    dname = models.CharField(max_length=100)
    dimg = models.FileField(upload_to="static/uploads/")
    ddis = models.TextField()

class StulifeModel(models.Model):
    stulimg = models.FileField(upload_to="static/uploads/")
    stultitle = models.CharField(max_length=100)
    stuldis = models.TextField()

class FacilityModel(models.Model):
    faciimg = models.FileField(upload_to="static/uploads/")
    facidis = models.TextField()

class AboutusModel(models.Model):
    aboutus_dis = models.TextField()
    aboutus_img = models.FileField(upload_to="static/uploads/") 
    
class HistoryModel(models.Model):
    history = models.TextField()

class MsgDirectorModel(models.Model):
    msgdis = models.TextField()
    msgdimg = models.FileField(upload_to="static/uploads/") 

class LeadershipModel(models.Model):
    lname = models.CharField(max_length=100)
    lposition = models.CharField(max_length=100)
    limg = models.FileField(upload_to="static/uploads/")

class AdminiModel(models.Model):
    admininame = models.CharField(max_length=100)
    adminiposition = models.CharField(max_length=100)
    adminiimg = models.FileField(upload_to="static/uploads/")

class FacultyModel(models.Model):
    fname = models.CharField(max_length=100)
    fspeci = models.CharField(max_length=100)
    fdepart = models.CharField(max_length=100)
    fimg = models.FileField(upload_to="static/uploads/")

class StaffModel(models.Model):
    stafname = models.CharField(max_length=100)
    stafdep = models.CharField(max_length=100)
    stafimg = models.FileField(upload_to="static/uploads/")

class WhystdModel(models.Model):
    whytitle = models.CharField(max_length=100)
    whydis = models.CharField(max_length=400)



class GrcelldisModel(models.Model):
    grdis = models.TextField()

class GrcellobjModel(models.Model):
    grobj = models.TextField()

class GrcellfunModel(models.Model):
    grfun = models.TextField()


class AntirModel(models.Model):
    antirdis = models.TextField()


class WocelldisModel(models.Model):
    wodis = models.TextField()

class WocellobjModel(models.Model):
    woobj = models.TextField()

class WocellfunModel(models.Model):
    wofun = models.TextField()




class EqopobjModel(models.Model):
    eqopobj = models.TextField()

class EqoprolModel(models.Model):
    eqoprol = models.TextField()


class EleobjModel(models.Model):
    eleobj = models.TextField()
    
class ElerolModel(models.Model):
    elerol = models.TextField()


class SexhModel(models.Model):
    sexhdis = models.TextField()


# BCS ===============================================

class BcsModel(models.Model):
    bcsdis = models.TextField()
    bcsimg = models.FileField(upload_to="static/uploads/")

class BcsCdMOdel(models.Model):
    bcscd = models.TextField()

class BcsIsMOdel(models.Model):
    bcsis = models.TextField()

class BcsNriMOdel(models.Model):
    bcsnri = models.TextField()

class BcsAdqMOdel(models.Model):
    bcsadq = models.TextField()

class BcsElgMOdel(models.Model):
    bcselg = models.TextField()

class BcsAdpMOdel(models.Model):
    bcsadp = models.TextField()


# BA =====================================================

class BAModel(models.Model):
    badis = models.TextField()
    baimg = models.FileField(upload_to="static/uploads/")

class BaCdMOdel(models.Model):
    bacd = models.TextField()

class BaIsMOdel(models.Model):
    bais = models.TextField()

class BaNriMOdel(models.Model):
    banri = models.TextField()

class BaAdqMOdel(models.Model):
    baadq = models.TextField()

class BaElgMOdel(models.Model):
    baelg = models.TextField()

class BaAdpMOdel(models.Model):
    baadp = models.TextField()


#MCS ===================================================================================

class McsModel(models.Model):
    mcsdis = models.TextField()
    mcsimg = models.FileField(upload_to="static/uploads/")

class McsCdMOdel(models.Model):
    mcscd = models.TextField()

class McsIsMOdel(models.Model):
    mcsis = models.TextField()

class McsNriMOdel(models.Model):
    mcsnri = models.TextField()

class McsAdqMOdel(models.Model):
    mcsadq = models.TextField()

class McsElgMOdel(models.Model):
    mcselg = models.TextField()

class McsAdpMOdel(models.Model):
    mcsadp = models.TextField()

# =====================================================================================

class IsobjModel(models.Model):
    isobj =  models.TextField()


class NriobjModel(models.Model):
    nriobj =  models.TextField()


class AslideModel(models.Model):
    aslide = models.FileField(upload_to="static/uploads/")

class JobopModel(models.Model):
    jobtitle = models.CharField(max_length=100)
    jobdis = models.CharField(max_length=200)
    jobdate = models.CharField(max_length=50)


class ContactModel(models.Model):
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    ofcontact = models.CharField(max_length=15)

class NewsandstoryModel(models.Model):
    nsimg = models.FileField(upload_to="static/uploads/")
    nsdate = models.CharField(max_length=100)
    nstitle = models.CharField(max_length=100)
    nsdis = models.TextField()
    nors = models.CharField(max_length=10)

class EventModel(models.Model):
    eventimg = models.FileField(upload_to="static/uploads/")
    eventdate = models.CharField(max_length=100)
    eventtitle = models.CharField(max_length=100)
    eventdis = models.TextField()
    puevent = models.CharField(max_length=10)

class GalleryModel(models.Model):
    galleryimg = models.FileField(upload_to="static/uploads/")
    imgdis = models.CharField(max_length=100)

class AaboutModel (models.Model):
    aboutdis = models.TextField()

class AobjectiveModel(models.Model):
    aobjective = models.CharField(max_length=300)
    