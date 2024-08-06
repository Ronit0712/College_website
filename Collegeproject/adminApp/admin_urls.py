from django.urls import  path
from adminApp import views

urlpatterns =[
    path('',views.home),
    path('save_notice/',views.save_notice),
    path('delete_notice/',views.delete_notice),
    path('save_video/',views.save_video),
    path('save_department/',views.save_department),
    path('delete_department/',views.delete_department),
    path('save_stulife/',views.save_stulife),
    path('save_facility/',views.save_facility),





    path('about_us/',views.about_us),
    path('save_about_us/',views.save_about_us),
    path('delete_about_us/',views.delete_about_us),





    path('history/',views.history),
    path('save_history/',views.save_history),




    path('msg_director/',views.msg_director),
    path('save_msgd/',views.save_msgd),



    path('leadership/',views.leadership),
    path('save_leadership/',views.save_leadership),
    path('delete_leadership/',views.delete_leadership),



    path('administration/',views.administration),
    path('save_admini/',views.save_admini),
    path('delete_admini/',views.delete_admini),



    path('faculty/',views.faculty),
    path('save_faculty/',views.save_faculty),
    path('delete_faculty/',views.delete_faculty),



    path('staff/',views.staff),
    path('save_staff/',views.save_staff),
    path('delete_staff/',views.delete_staff),



    path('why_std/',views.why_std),
    path('save_whystd/',views.save_whystd),
    path('delete_whystd/',views.delete_whystd),


    path('grcell/',views.grcell),
    path('save_grcell/',views.save_grcell),
    path('save_grobj/',views.save_grobj),
    path('delete_grobj/',views.delete_grobj),
    path('save_grfun/',views.save_grfun),
    path('delete_grfun/',views.delete_grfun),



    path('antircell/',views.antircell),
    path('save_antir/',views.save_antir),




    path('womencell/',views.womencell),
    path('save_wocell/',views.save_wocell),
    path('save_woobj/',views.save_woobj),
    path('delete_woobj/',views.delete_woobj),
    path('save_wofun/',views.save_wofun),
    path('delete_wofun/',views.delete_wofun),





    path('equopcell/',views.equopcell),
    path('save_eqopobj/',views.save_eqopobj),
    path('delete_eqopobj/',views.delete_eqopobj),
    path('save_eqoprol/',views.save_eqoprol),
    path('delete_eqoprol',views.delete_eqoprol),




    path('eleclub/',views.eleclub),
    path('save_eleobj/',views.save_eleobj),
    path('delete_eleobj/',views.delete_eleobj),
    path('save_elerol/',views.save_elerol),
    path('delete_elerol',views.delete_elerol),



    path('antisexcell/',views.antisexcell),
    path('save_sexh/',views.save_sexh),




    path('undergraduate/',views.undergraduate),
    path('save_bcs/',views.save_bcs),
    path('save_bcscd/',views.save_bcscd),
    path('save_bcsis/',views.save_bcsis),
    path('save_bcsnri/',views.save_bcsnri),
    path('save_bcsadq/',views.save_bcsadq),
    path('save_bcselg/',views.save_bcselg),
    path('save_bcsadp/',views.save_bcsadp),

    path('save_ba/',views.save_ba),
    path('save_bacd/',views.save_bacd),
    path('save_bais/',views.save_bais),
    path('save_banri/',views.save_banri),
    path('save_baadq/',views.save_baadq),
    path('save_baelg/',views.save_baelg),
    path('save_baadp/',views.save_baadp),

  




    path('postgraduate/',views.postgraduate),
    path('save_mcs/',views.save_mcs),
    path('save_mcscd/',views.save_mcscd),

    path('save_mcsis/',views.save_mcsis),
    path('delete_mcsis',views.delete_mcsis),

    path('save_mcsnri/',views.save_mcsnri),
    path('delete_mcsnri/',views.delete_mcsnri),

    path('save_mcsadq/',views.save_mcsadq),

    path('save_mcselg/',views.save_mcselg),
    path('delete_mcselg/',views.delete_mcselg),


    path('save_mcsadp/',views.save_mcsadp),
    path('delete_mcsadp/',views.delete_mcsadp),





    path('inter_stu/',views.inter_stu),
    path('save_isobj/',views.save_isobj),
    path('delete_isobj/',views.delete_isobj),

  


    path('nri_stu/',views.nri_stu),
    path('save_nriobj/',views.save_nriobj),
    path('delete_nriobj/',views.delete_nriobj),



    path('ahome/',views.ahome),
    path('save_aslide/',views.save_aslide),
    path('delete_aslide/',views.delete_aslide),

    path('save_jobop/',views.save_jobop),
    path('delete_jobop/',views.delete_jobop),
    path('save_contactinfo/',views.save_contactinfo),




    path('anew_sto/',views.anew_sto),
    path('save_ns/',views.save_ns),
    path('delete_ns/',views.delete_ns),


    path('aevents/',views.aevents),
    path('save_event/',views.save_event),
    path('delete_event/',views.delete_event),


    path('agallery/',views.agallery),
    path('save_agallery/',views.save_agallery),
    path('delete_img/',views.delete_img),
 
    path('aabout/',views.aabout),
    path('save_aabout/',views.save_aabout),
    path('save_aobjective/',views.save_aobjective),
    path('delete_aobjective/',views.delete_aobjective)


]