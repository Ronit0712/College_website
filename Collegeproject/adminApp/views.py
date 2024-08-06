from django.http import HttpResponse
from django.shortcuts import redirect, render

from adminApp.models import AaboutModel, AboutusModel, AdminiModel, AntirModel, AobjectiveModel, AslideModel, BAModel, BaAdpMOdel, BaAdqMOdel, BaCdMOdel, BaElgMOdel, BaIsMOdel, BaNriMOdel, BcsAdpMOdel, BcsAdqMOdel, BcsCdMOdel, BcsElgMOdel, BcsIsMOdel, BcsModel, BcsNriMOdel, ContactModel, DepartmentModel, EleobjModel, ElerolModel, EqopobjModel, EqoprolModel, EventModel, FacilityModel, FacultyModel, GalleryModel, GrcelldisModel, GrcellfunModel, GrcellobjModel, HistoryModel, IsobjModel, JobopModel, LeadershipModel, McsAdpMOdel, McsAdqMOdel, McsCdMOdel, McsElgMOdel, McsIsMOdel, McsModel, McsNriMOdel, MsgDirectorModel, NewsandstoryModel, NoticeModel, NriobjModel, SexhModel, StaffModel, StulifeModel, VideoModel, WhystdModel, WocelldisModel, WocellfunModel, WocellobjModel

# Create your views here.
def home(r):
    notices = NoticeModel.objects.all()
    videos = VideoModel.objects.get(id=1)
    departments = DepartmentModel.objects.all()
    stulifes = StulifeModel.objects.all()
    facilities = FacilityModel.objects.get(id=1)
    return render(r,"admin/home.html",{"notices":notices,"videos":videos,"departments":departments, "stulifes":stulifes, "facilities":facilities })

def save_notice(r):
    newnotice = NoticeModel(
        notice = r.POST['notice']
    )
    newnotice.save()
    return redirect("/admin")

def delete_notice(r):
    NoticeModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin")


def save_video(r):
    # newvideo = VideoModel(
    #     hvideo = r.FILES['hvideo']
    # )
    # newvideo.save()

    uvideo = VideoModel.objects.get(id=1)
    if "hvideo" in r.FILES :
        uvideo.hvideo = r.FILES['hvideo']
    uvideo.save()

    return redirect("/admin")

def save_department(r):
    newdepartment = DepartmentModel(
        dname = r.POST['dname'],
        dimg = r.FILES['dimg'],
        ddis = r.POST['ddis'],
    )
    newdepartment.save()
    return redirect("/admin")

def delete_department(r):
    DepartmentModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin")


def save_stulife(r):
    newstulife = StulifeModel(
        stulimg = r.FILES['stulimg'],
        stultitle = r.POST['stultitle'],
        stuldis = r.POST['stuldis']
    )
    newstulife.save()
    return redirect("/admin")

def save_facility(r):
    # newfacility = FacilityModel(
    #     faciimg = r.FILES['faciimg'],
    #     facidis = r.POST['facidis'],
    # )
    # newfacility.save()

    ufacility = FacilityModel.objects.get(id=1)
    if "faciimg" in r.FILES:
        ufacility.faciimg = r.FILES['faciimg']
        ufacility.facidis = r.POST['facidis']
    ufacility.save()
    return redirect("/admin")




# --------------------------------------------------------------------------------

def about_us(r):
    about_uss = AboutusModel.objects.all()
    return render(r,"admin/about_us.html", {"about_uss":about_uss})

def save_about_us(r):
    newaboutus = AboutusModel(
        aboutus_dis = r.POST['aboutus_dis'],
        aboutus_img = r.FILES['aboutus_img']
    )
    newaboutus.save()
    return redirect("/admin/about_us")

def delete_about_us (r):

    AboutusModel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/about_us")

    


# ---------------------------------------------------------------------------------

def history(r):
    histories = HistoryModel.objects.get(id=1)
    return render(r,"admin/history.html", {"histories":histories})

def save_history(r):
    # newhistory = HistoryModel(
    #     history = r.POST['history']
    # )
    # newhistory.save()

    uhistory = HistoryModel.objects.get(id=1)
    uhistory.history = r.POST['history']
    uhistory.save()
    return redirect("/admin/history")



# =====================================================================================

def msg_director(r):
    msgds = MsgDirectorModel.objects.get(id=1)
    return render(r,"admin/msg_director.html", {"msgds":msgds})

def save_msgd(r):
    # newmsgd = MsgDirectorModel(
    #     msgdis = r.POST['msgdis'],
    #     msgdimg = r.FILES['msgdimg']
    # )
    # newmsgd.save()

    umsgd = MsgDirectorModel.objects.get(id=1)
    if "msgdimg" in r.FILES:
        umsgd.msgdis = r.POST['msgdis']
        umsgd.msgdimg = r.FILES['msgdimg']
    umsgd.save()   
    return redirect("/admin/msg_director")


# ====================================================================================

def leadership(r):
    leaders = LeadershipModel.objects.all()
    return render(r,"admin/leadership.html",{"leaders":leaders})

def save_leadership(r):
    newleader = LeadershipModel(
       lname = r.POST['lname'],
       lposition = r.POST['lposition'],
       limg = r.FILES['limg']
    )
    newleader.save()
    return redirect("/admin/leadership")

def delete_leadership(r):
    LeadershipModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/leadership")



# ====================================================================================

def administration(r):
    adminis = AdminiModel.objects.all()
    return render(r,"admin/administration.html",{"adminis":adminis})

def save_admini(r):
    newadmini = AdminiModel(
        admininame = r.POST['admininame'],
        adminiposition = r.POST['adminiposition'],
        adminiimg = r.FILES['adminiimg']
    )
    newadmini.save()
    return redirect("/admin/administration")

def delete_admini(r):
    AdminiModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/administration")

# ====================================================================================

def faculty(r):
    faculties = FacultyModel.objects.all()
    return render(r,"admin/faculty.html",{"faculties":faculties})

def save_faculty(r):
    newfaculty = FacultyModel(
        fname = r.POST['fname'], 
        fspeci = r.POST['fspeci'],
        fdepart = r.POST['fdepart'],
        fimg = r.FILES['fimg']
    )
    newfaculty.save()
    return redirect("/admin/faculty")

def delete_faculty(r):
    FacultyModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/faculty")


# ====================================================================================


def staff(r):
    staffs = StaffModel.objects.all()
    return render(r,"admin/staff.html",{"staffs":staffs})

def save_staff(r):
    newstaff = StaffModel(
        stafname = r.POST['stafname'],
        stafdep = r.POST['stafdep'],
        stafimg = r.FILES['stafimg']
    )
    newstaff.save()
    return redirect("/admin/staff")

def delete_staff(r):
    StaffModel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/staff")




# =====================================================================================
def why_std(r):
    whystds = WhystdModel.objects.all()
    return render(r,"admin/why_std.html",{"whystds":whystds})

def save_whystd(r):
    newwhystd = WhystdModel(
        whytitle = r.POST['whytitle'],
        whydis = r.POST['whydis']
    )
    newwhystd.save()
    return redirect("/admin/why_std")

def delete_whystd(r):
    WhystdModel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/why_std")

# =====================================================================================

def grcell(r):
    grdiss = GrcelldisModel.objects.get(id=1)
    grobjs = GrcellobjModel.objects.all()
    grfuns = GrcellfunModel.objects.all()
    return render(r,"admin/grcell.html",{"grdiss":grdiss,"grobjs":grobjs,"grfuns":grfuns})

def save_grcell(r):
    # newgrdis = GrcelldisModel(
    #     grdis = r.POST['grdis']
    # )
    # newgrdis.save()

    ugrdis = GrcelldisModel.objects.get(id=1)
    ugrdis.grdis = r.POST['grdis']
    ugrdis.save()
    return redirect("/admin/grcell")

def save_grobj(r):
    newgrobj = GrcellobjModel(
        grobj = r.POST['grobj']
    )
    newgrobj.save()
    return redirect("/admin/grcell")
def delete_grobj(r):
    GrcellobjModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/grcell")


def save_grfun(r):
    newgrfun = GrcellfunModel(
        grfun = r.POST['grfun'] 
    )
    newgrfun.save()
    return redirect("/admin/grcell")
def delete_grfun(r):
    GrcellfunModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/grcell")



# ===================================================================================


def antircell(r):
    antirdiss = AntirModel.objects.get(id=1)
    return render(r,"admin/antircell.html",{"antirdiss":antirdiss})
def save_antir(r):
    # newantirdis = AntirModel(
    #     antirdis = r.POST['antirdis']
    # )
    # newantirdis.save()

    uantir=AntirModel.objects.get(id=1)
    uantir.antirdis = r.POST['antirdis']
    uantir.save()
    return redirect("/admin/antircell")

# =======================================================================================

def womencell(r):
    wodiss = WocelldisModel.objects.get(id=1)
    woobjs = WocellobjModel.objects.all()
    wofuns = WocellfunModel.objects.all()
    
    return render(r,"admin/womencell.html",{"wodiss":wodiss,"woobjs":woobjs,"wofuns":wofuns})

def save_wocell(r):
    # newwodis = WocelldisModel(
    #     wodis = r.POST['wodis']
    # )
    # newwodis.save()

    uwodis = WocelldisModel.objects.get(id=1)
    uwodis.wodis = r.POST['wodis']
    uwodis.save()
    return redirect("/admin/womencell")

def save_woobj(r):
    newwoobj = WocellobjModel(
        woobj = r.POST['woobj']
    )
    newwoobj.save()
    return redirect("/admin/womencell")
def delete_woobj(r):
    WocellobjModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/womencell")


def save_wofun(r):
    newwofun = WocellfunModel(
        wofun = r.POST['wofun'] 
    )
    newwofun.save()
    return redirect("/admin/womencell")
def delete_wofun(r):
    WocellfunModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/womencell")




# =======================================================================================
def equopcell(r):
    eqopobjs = EqopobjModel.objects.all()
    eqoprols = EqoprolModel.objects.all()
    return render(r,"admin/equopcell.html",{"eqopobjs":eqopobjs,"eqoprols":eqoprols})

def save_eqopobj(r):
    neweqopobj = EqopobjModel(
        eqopobj = r.POST['eqopobj']
    )
    neweqopobj.save()
    return redirect("/admin/equopcell")

def delete_eqopobj(r):
    EqopobjModel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/equopcell")

def save_eqoprol(r):
    neweqoprol = EqoprolModel(
        eqoprol= r.POST['eqoprol']
    )
    neweqoprol.save()
    return redirect("/admin/equopcell")

def delete_eqoprol(r):
    EqoprolModel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/equopcell")

# =======================================================================================

def eleclub(r):
    eleobjs = EleobjModel.objects.all()
    elerols = ElerolModel.objects.all()
    return render(r,"admin/eleclub.html",{"eleobjs":eleobjs,"elerols":elerols})

def save_eleobj(r):
    neweleobj = EleobjModel(
        eleobj = r.POST['eleobj']
    )
    neweleobj.save()
    return redirect("/admin/eleclub")

def delete_eleobj(r):
    EleobjModel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/eleclub")

def save_elerol(r):
    newelerol = ElerolModel(
        elerol= r.POST['elerol']
    )
    newelerol.save()
    return redirect("/admin/eleclub")

def delete_elerol(r):
    ElerolModel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/eleclub")


# =======================================================================================

def antisexcell(r):
    sexhdiss = SexhModel.objects.get(id=1)
    return render(r,"admin/antisexcell.html",{"sexhdiss":sexhdiss})

def save_sexh(r):
    # newsexhdis = SexhModel(
    #     sexhdis = r.POST['sexhdis']
    # )
    # newsexhdis.save()

    usexhdis = SexhModel.objects.get(id=1)
    usexhdis.sexhdis = r.POST['sexhdis']
    usexhdis.save
    return redirect("/admin/antisexcell")



# =================================================================================

def undergraduate(r):
    bcss = BcsModel.objects.get(id=1) 
    bcscds = BcsCdMOdel.objects.get(id=1) 
    bcsiss = BcsIsMOdel.objects.all() 
    bcsnris = BcsNriMOdel.objects.all() 
    bcsadqs = BcsAdqMOdel.objects.get(id=2) 
    bcselgs = BcsElgMOdel.objects.all() 
    bcsadps = BcsAdpMOdel.objects.all() 

    bas = BAModel.objects.get(id=1) 
    bacds = BaCdMOdel.objects.get(id=1) 
    baiss = BaIsMOdel.objects.all() 
    banris = BaNriMOdel.objects.all() 
    baadqs = BaAdqMOdel.objects.get(id=1) 
    baelgs = BaElgMOdel.objects.all() 
    baadps = BaAdpMOdel.objects.all() 

    return render(r,"admin/undergraduate.html",{"bcss":bcss,"bcscds":bcscds,"bcsiss":bcsiss,"bcsnris":bcsnris,"bcsadqs":bcsadqs,"bcselgs":bcselgs,"bcsadps":bcsadps, "bas":bas,"bacds":bacds,"baiss":baiss,"banris":banris,"baadqs":baadqs,"baelgs":baelgs,"baadps":baadps})

# BCS==============================================

def save_bcs(r):
    # newbcs = BcsModel(
    #     bcsdis = r.POST['bcsdis'],
    #     bcsimg = r.FILES['bcsimg']
    # )
    # newbcs.save()
    ubcs= BcsModel.objects.get(id=1)
    if"bcsimg" in r.FILES:
        ubcs.bcsdis = r.POST['bcsdis']
        ubcs.bcsimg = r.FILES['bcsimg']
    ubcs.save()
    return redirect("/admin/undergraduate")

def save_bcscd(r):
    # newbcscds = BcsCdMOdel(
    #     bcscd = r.POST['bcscd']
    # )
    # newbcscds.save()
    ubcscd = BcsCdMOdel.objects.get(id=1)
    ubcscd.bcscd = r.POST['bcscd']
    ubcscd.save()

    return redirect("/admin/undergraduate")

def save_bcsis(r):
    newbcsis = BcsIsMOdel(
        bcsis = r.POST['bcsis']
    )
    newbcsis.save() 
    return redirect("/admin/undergraduate")

def save_bcsnri(r):
    newbcsnri = BcsNriMOdel(
        bcsnri = r.POST['bcsnri']
    )
    newbcsnri.save()
    return redirect("/admin/undergraduate")

def save_bcsadq(r):
    # newbcsadq = BcsAdqMOdel(
    #     bcsadq = r.POST['bcsadq']
    # )
    # newbcsadq.save()
    ubcsadq= BcsAdqMOdel.objects.get(id=2)
    ubcsadq.bcsadq = r.POST['bcsadq']
    ubcsadq.save()
    return redirect("/admin/undergraduate")

def save_bcselg(r):
    newbcselg = BcsElgMOdel(
        bcselg = r.POST['bcselg']
    )
    newbcselg.save()
    return redirect("/admin/undergraduate")

def save_bcsadp(r):
    newbcsadp = BcsAdpMOdel(
        bcsadp = r.POST['bcsadp']
    )
    newbcsadp.save()
    return redirect("/admin/undergraduate")


# BA ==================================================================================

def save_ba(r):
    # newba = BAModel(
    #     badis = r.POST['badis'],
    #     baimg = r.FILES['baimg']
    # )
    # newba.save()
    uba= BAModel.objects.get(id=1)
    if"baimg" in r.FILES:
        uba.badis = r.POST['badis']
        uba.baimg = r.FILES['baimg']
    uba.save()
    return redirect("/admin/undergraduate")

def save_bacd(r):
    # newbacds = BaCdMOdel(
    #     bacd = r.POST['bacd']
    # )
    # newbacds.save()
    ubacd = BaCdMOdel.objects.get(id=1)
    ubacd.bacd = r.POST['bacd']
    ubacd.save()

    return redirect("/admin/undergraduate")

def save_bais(r):
    newbais = BaIsMOdel(
        bais = r.POST['bais']
    )
    newbais.save() 
    return redirect("/admin/undergraduate")

def save_banri(r):
    newbanri = BaNriMOdel(
        banri = r.POST['banri']
    )
    newbanri.save()
    return redirect("/admin/undergraduate")

def save_baadq(r):
    # newbaadq = BaAdqMOdel(
    #     baadq = r.POST['baadq']
    # )
    # newbaadq.save()
    ubaadq= BaAdqMOdel.objects.get(id=1)
    ubaadq.baadq = r.POST['baadq']
    ubaadq.save()
    return redirect("/admin/undergraduate")

def save_baelg(r):
    newbaelg = BaElgMOdel(
        baelg = r.POST['baelg']
    )
    newbaelg.save()
    return redirect("/admin/undergraduate")

def save_baadp(r):
    newbaadp = BaAdpMOdel(
        baadp = r.POST['baadp']
    )
    newbaadp.save()
    return redirect("/admin/undergraduate")







# ======================================================================================


def postgraduate(r):
    mcss = McsModel.objects.get(id=1) 
    mcscds = McsCdMOdel.objects.get(id=1) 
    mcsiss = McsIsMOdel.objects.all() 
    mcsnris = McsNriMOdel.objects.all() 
    mcsadqs = McsAdqMOdel.objects.get(id=1) 
    mcselgs = McsElgMOdel.objects.all() 
    mcsadps = McsAdpMOdel.objects.all() 
    return render(r,"admin/postgraduate.html",{"mcss":mcss,"mcscds":mcscds,"mcsiss":mcsiss,"mcsnris":mcsnris,"mcsadqs":mcsadqs,"mcselgs":mcselgs,"mcsadps":mcsadps})

# MCS==============================================

def save_mcs(r):
    # newmcs = McsModel(
    #     mcsdis = r.POST['mcsdis'],
    #     mcsimg = r.FILES['mcsimg']
    # )
    # newmcs.save()
    umcs= McsModel.objects.get(id=1)
    if"mcsimg" in r.FILES:
        umcs.mcsdis = r.POST['mcsdis']
        umcs.mcsimg = r.FILES['mcsimg']
    umcs.save()
    return redirect("/admin/postgraduate")

def save_mcscd(r):
    # newmcscds = McsCdMOdel(
    #     mcscd = r.POST['mcscd']
    # )
    # newmcscds.save()
    umcscd = McsCdMOdel.objects.get(id=1)
    umcscd.mcscd = r.POST['mcscd']
    umcscd.save()

    return redirect("/admin/postgraduate")

def save_mcsis(r):
    newmcsis = McsIsMOdel(
        mcsis = r.POST['mcsis']
    )
    newmcsis.save() 
    return redirect("/admin/postgraduate")

def delete_mcsis(r):
    McsIsMOdel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/postgraduate")



def save_mcsnri(r):
    newmcsnri = McsNriMOdel(
        mcsnri = r.POST['mcsnri']
    )
    newmcsnri.save()
    return redirect("/admin/postgraduate")

def delete_mcsnri(r): 
    McsNriMOdel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/postgraduate")

def save_mcsadq(r):
    # newmcsadq = McsAdqMOdel(
    #     mcsadq = r.POST['mcsadq']
    # )
    # newmcsadq.save()
    umcsadq= McsAdqMOdel.objects.get(id=2)
    umcsadq.mcsadq = r.POST['mcsadq']
    umcsadq.save()
    return redirect("/admin/postgraduate")

def save_mcselg(r):
    newmcselg = McsElgMOdel(
        mcselg = r.POST['mcselg']
    )
    newmcselg.save()
    return redirect("/admin/postgraduate")

def delete_mcselg(r):
    McsElgMOdel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/postgraduate")

def save_mcsadp(r):
    newmcsadp = McsAdpMOdel(
        mcsadp = r.POST['mcsadp']
    )
    newmcsadp.save()
    return redirect("/admin/postgraduate")

def delete_mcsadp(r):
    McsAdpMOdel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/postgraduate")




# =======================================================================================

def inter_stu(r):
    isobjs = IsobjModel.objects.all()
   
    return render(r,"admin/inter_stu.html",{"isobjs":isobjs})

def save_isobj(r):
    newisobj = IsobjModel(
        isobj = r.POST['isobj']
    )
    newisobj.save()
    return redirect("/admin/inter_stu")

def delete_isobj(r):
    IsobjModel.objects.get(id=r.GET['id']).delete()






def nri_stu(r):
    nriobjs = NriobjModel.objects.all()
    return render(r,"admin/nri_stu.html",{"nriobjs":nriobjs})

def save_nriobj(r):
    newnriobj = NriobjModel(
        nriobj = r.POST['nriobj']
    )
    newnriobj.save()
    return redirect("/admin/inter_stu")

def delete_nriobj(r):
    NriobjModel.objects.get(id=r.GET['id']).delete()


# =====================================================================================


def ahome(r):
    aslides = AslideModel.objects.all()
    jobop = JobopModel.objects.all()
    contactinfos = ContactModel.objects.get(id=1)
    return render(r,"admin/ahome.html",{"aslides":aslides, "jobop":jobop, "contactinfos":contactinfos})

def save_aslide(r):
    newaslide = AslideModel(
        aslide = r.FILES['aslide']
    )
    newaslide.save()
    return redirect("/admin/ahome")

def delete_aslide(r):
    AslideModel.objects.get(id=r.GET['id']).delete()

def save_jobop(r):
    newjobop = JobopModel(
        jobtitle = r.POST['jobtitle'],
        jobdis = r.POST['jobdis'],
        jobdate = r.POST['jobdate']
    )
    newjobop.save()
    return redirect("/admin/ahome")

def delete_jobop(r):
    JobopModel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/ahome")

def save_contactinfo(r):
    # newcontactinfo = ContactModel(
    #     address = r.POST['address'],
    #     contact = r.POST['contact'],
    #     ofcontact = r.POST['ofcontact']
    # )
    # newcontactinfo.save()

    ucontactinfo = ContactModel.objects.get(id=1)
    ucontactinfo.address = r.POST['address']
    ucontactinfo.contact = r.POST['contact']
    ucontactinfo.ofcontact = r.POST['ofcontact']
    ucontactinfo.save()
    return redirect("/admin/ahome")




# ====================================================================================

def anew_sto(r):
    nss = NewsandstoryModel.objects.all()
    return render(r,"admin/anew_sto.html",{"nss":nss})

def save_ns(r):
    newns = NewsandstoryModel(
        nsimg = r.FILES['nsimg'],
        nsdate = r.POST['nsdate'],
        nstitle = r.POST['nstitle'],
        nsdis = r.POST['nsdis'],
        nors = r.POST['nors'],
    )
    newns.save()
    return redirect("/admin/anew_sto")

def delete_ns(r):
    NewsandstoryModel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/anew_sto")


# =================================================================================

def aevents(r):
    events = EventModel.objects.all()
    return render(r,"admin/aevents.html",{"events":events})

def save_event(r):
    newevent = EventModel(
        eventimg = r.FILES['eventimg'],
        eventdate = r.POST['eventdate'],
        eventtitle = r.POST['eventtitle'],
        eventdis = r.POST['eventdis'],
        puevent = r.POST['puevent'],
    )
    newevent.save()
    return redirect("/admin/aevents")

def delete_event(r):
    EventModel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/aevents")


# =======================================================================================

def agallery(r):
    gallerys = GalleryModel.objects.all()
    return render(r,"admin/agallery.html",{"gallerys":gallerys})

def save_agallery(r):
    newgallery = GalleryModel(
        galleryimg = r.FILES['galleryimg'],
        imgdis = r.POST['imgdis']
    )
    newgallery.save()
    return redirect("/admin/agallery")

def delete_img(r):
    GalleryModel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/agallery")
# =======================================================================================

def aabout(r):
    aabouts = AaboutModel.objects.get(id=1)
    aobjectives = AobjectiveModel.objects.all()
    return render(r,"admin/aabout.html",{"aabouts":aabouts, "aobjectives":aobjectives})

def save_aabout(r):
    # newabout = AaboutModel(
    #     aboutdis = r.POST['aboutdis']
    # )
    # newabout.save()
    
    uaabout = AaboutModel.objects.get(id=1)
    uaabout.aboutdis = r.POST['aboutdis']
    uaabout.save()
    return redirect("/admin/aabout")

def save_aobjective(r):
   newaobjective = AobjectiveModel(
       aobjective = r.POST['aobjective']
   ) 
   newaobjective.save()
   return redirect("/admin/aabout") 

def delete_aobjective(r):
    AobjectiveModel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/aabout")


