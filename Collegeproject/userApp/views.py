from django.shortcuts import render

from adminApp.models import AaboutModel, AboutusModel, AdminiModel, AntirModel, AobjectiveModel, AslideModel, BAModel, BaAdpMOdel, BaAdqMOdel, BaCdMOdel, BaElgMOdel, BaIsMOdel, BaNriMOdel, BcsAdpMOdel, BcsAdqMOdel, BcsCdMOdel, BcsElgMOdel, BcsIsMOdel, BcsModel, BcsNriMOdel, ContactModel, DepartmentModel, EleobjModel, ElerolModel, EqopobjModel, EqoprolModel, EventModel, FacilityModel, FacultyModel, GalleryModel, GrcelldisModel, GrcellfunModel, GrcellobjModel, HistoryModel, IsobjModel, JobopModel, LeadershipModel, McsAdpMOdel, McsAdqMOdel, McsCdMOdel, McsElgMOdel, McsIsMOdel, McsModel, McsNriMOdel, MsgDirectorModel, NewsandstoryModel, NoticeModel, NriobjModel, SexhModel, StaffModel, StulifeModel, VideoModel, WhystdModel, WocelldisModel, WocellfunModel, WocellobjModel

# Create your views here.
def home(r):
    notices = NoticeModel.objects.all()
    videos = VideoModel.objects.get(id=1)
    departments = DepartmentModel.objects.all()
    stulifes = StulifeModel.objects.all()
    facilities = FacilityModel.objects.get(id=1)
    return render(r,"user/home.html",{"notices":notices,"videos":videos,"departments":departments, "stulifes":stulifes, "facilities":facilities})

def about_us(r):
    about_uss = AboutusModel.objects.all()
    return render(r,"user/about_us.html",{"about_uss":about_uss})

def history(r):
    histories = HistoryModel.objects.get(id=1)
    return render(r,"user/history.html",{"histories":histories})

def message(r):
    msgds = MsgDirectorModel.objects.get(id=1)
    return render(r,"user/message.html",{"msgds":msgds})

def leadership(r):
    leaders = LeadershipModel.objects.all()
    return render(r,"user/leadership.html",{"leaders":leaders})

def administration(r):
    adminis = AdminiModel.objects.all()
    return render(r,"user/administration.html",{"adminis":adminis})

def faculty(r):
    faculties = FacultyModel.objects.all()
    return render(r,"user/faculty.html",{"faculties":faculties})

def staff(r):
    staffs = StaffModel.objects.all()
    return render(r,"user/staff.html",{"staffs":staffs})

def why_study(r):
    whystds = WhystdModel.objects.all()
    return render(r,"user/why_study.html",{"whystds":whystds})

def grievance(r):
    grdiss = GrcelldisModel.objects.get(id=1)
    grobjs = GrcellobjModel.objects.all()
    grfuns = GrcellfunModel.objects.all()
    return render(r,"user/grievance.html",{"grdiss":grdiss,"grobjs":grobjs,"grfuns":grfuns})

def anti_ragging(r):
    antirdiss = AntirModel.objects.get(id=1)
    return render(r,"user/anti_ragging.html",{"antirdiss":antirdiss})

def women(r):
    wodiss = WocelldisModel.objects.get(id=1)
    woobjs = WocellobjModel.objects.all()
    wofuns = WocellfunModel.objects.all()
    return render(r,"user/women.html",{"wodiss":wodiss,"woobjs":woobjs,"wofuns":wofuns})

def opportunity(r):
    eqopobjs = EqopobjModel.objects.all()
    eqoprols = EqoprolModel.objects.all()
    return render(r,"user/opportunity.html",{"eqopobjs":eqopobjs,"eqoprols":eqoprols})

def electoral(r):
    eleobjs = EleobjModel.objects.all()
    elerols = ElerolModel.objects.all()
    return render(r,"user/electoral.html",{"eleobjs":eleobjs,"elerols":elerols})

def harassment(r):
    sexhdiss = SexhModel.objects.get(id=1)
    return render(r,"user/harassment.html",{"sexhdiss":sexhdiss})

def bcs(r):
    bcss = BcsModel.objects.get(id=1) 
    bcscds = BcsCdMOdel.objects.get(id=1) 
    bcsiss = BcsIsMOdel.objects.all() 
    bcsnris = BcsNriMOdel.objects.all() 
    bcsadqs = BcsAdqMOdel.objects.get(id=2) 
    bcselgs = BcsElgMOdel.objects.all() 
    bcsadps = BcsAdpMOdel.objects.all() 
    return render(r,"user/bcs.html",{"bcss":bcss,"bcscds":bcscds,"bcsiss":bcsiss,"bcsnris":bcsnris,"bcsadqs":bcsadqs,"bcselgs":bcselgs,"bcsadps":bcsadps,})

def ba(r):
    bas = BAModel.objects.get(id=1) 
    bacds = BaCdMOdel.objects.get(id=1) 
    baiss = BaIsMOdel.objects.all() 
    banris = BaNriMOdel.objects.all() 
    baadqs = BaAdqMOdel.objects.get(id=1) 
    baelgs = BaElgMOdel.objects.all() 
    baadps = BaAdpMOdel.objects.all()
    return render(r,"user/ba.html",{"bas":bas,"bacds":bacds,"baiss":baiss,"banris":banris,"baadqs":baadqs,"baelgs":baelgs,"baadps":baadps})

def bba(r):
    return render(r,"user/bba.html")

def bcom(r):
    return render(r,"user/bcom.html")

def mcs(r):
    mcss = McsModel.objects.get(id=1) 
    mcscds = McsCdMOdel.objects.get(id=1) 
    mcsiss = McsIsMOdel.objects.all() 
    mcsnris = McsNriMOdel.objects.all() 
    mcsadqs = McsAdqMOdel.objects.get(id=1) 
    mcselgs = McsElgMOdel.objects.all() 
    mcsadps = McsAdpMOdel.objects.all()
    return render(r,"user/mcs.html",{"mcss":mcss,"mcscds":mcscds,"mcsiss":mcsiss,"mcsnris":mcsnris,"mcsadqs":mcsadqs,"mcselgs":mcselgs,"mcsadps":mcsadps})

def mcom(r):
    return render(r,"user/mcom.html")

def stulog(r):
    return render(r,"user/stulog.html")

def faclog(r):
    return render(r,"user/faclog.html")

def interstu(r):
    isobjs = IsobjModel.objects.all()
    return render(r,"user/interstu.html",{"isobjs":isobjs})

def nristu(r):
    nriobjs = NriobjModel.objects.all()
    return render(r,"user/nristu.html",{"nriobjs":nriobjs})

def alumni(r):
    aslides = AslideModel.objects.all()
    jobop = JobopModel.objects.all()
    contactinfos = ContactModel.objects.get(id=1)
    gallerys = GalleryModel.objects.all()
    nss = NewsandstoryModel.objects.all()
    events = EventModel.objects.all()
    return render(r,"user/alumni.html",{"aslides":aslides, "jobop":jobop, "contactinfos":contactinfos,"gallerys":gallerys,"nss":nss,"events":events})

def new_sto(r):
    nss = NewsandstoryModel.objects.all()
    return render(r,"user/new_sto.html",{"nss":nss})

def event(r):
    events = EventModel.objects.all()
    return render(r,"user/event.html",{"events":events})

def gallery(r):
    gallerys = GalleryModel.objects.all()
    return render(r,"user/gallery.html",{"gallerys":gallerys})


def aabout_us(r):
    aabouts = AaboutModel.objects.get(id=1)
    aobjectives = AobjectiveModel.objects.all()
    return render(r,"user/aabout_us.html",{"aabouts":aabouts, "aobjectives":aobjectives})