from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import *
from council.models import *
from public import settings
from .models import members, Complaints, WardMember
from .models import Complaints
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Complaints
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.files.base import ContentFile
import base64




def index(request):
    if request.method == 'POST':
        _state_name = request.POST.get('state')
        _district = request.POST.get('district')
        _taluk = request.POST.get('taluk')
        _city = request.POST.get('city')
        _ward_no = request.POST.get('wardno')
        _colony = request.POST.get('wardname')
        _number = request.POST.get('phone')
        _date = request.POST.get('date')


        state_name = state.objects.get(id=_state_name)
        distric = district.objects.get(id=_district)
        my_user1 = taluk.objects.get(id=_taluk)
        my_user2 = City.objects.get(id=_city)
        my_user3 = ward_noo.objects.get(id=_ward_no)

        my_user4 = colony.objects.create(colony_name=_colony)
        a = colony.objects.all().last()

        my_user9 = number.objects.create(phone_no=_number)
        b = number.objects.all().last()

        my_user10 = date.objects.create(date=_date)
        c = date.objects.all().last()

        complaints = Complaints.objects.create(
            state_id=state_name.id,
            dist_id=distric.id,
            taluk_id=my_user1.id,
            city_id=my_user2.id,
            colony_id=a.id,
            ward_noo_id=my_user3.id,
            phone_id=b.id,
            date_id=c.id
        )
        complaints.save()

        return redirect('index2')
    else:
        states = state.objects.all()
        districts = district.objects.all()
        taluks = taluk.objects.all()
        cities = City.objects.all()
        ward_nos = ward_noo.objects.all()

        context = {
            'state': states,
            'district': districts,
            'taluk': taluks,
            'city': cities,
            'ward_noo': ward_nos,
        }

        return render(request, 'council/base.html', context)




def sign(request):
    if request.method == 'POST':
        _water_dept=request.POST['pure']
        _garbage_dept=request.POST['clean']
        _electric_dept=request.POST['electric']
        # print(_electric_dept)
        # print(_garbage_dept)
        # print(_water_dept)
        # my_user5=water.objects.create(water_name=_water_dept)
        # print(my_user5)
        a=Complaints.objects.all().last()
        a.water = _water_dept
        a.save()
        b=Complaints.objects.all().last()
        b.garbage=_garbage_dept
        b.save()
        c=Complaints.objects.all().last()
        c.electric=_electric_dept
        c.save()

    # if request.method == 'POST':
    #  _ garbage_dept=request.post['']
        
        # my_user5.save()
        return redirect('index3')

    return render(request,'council/index2.html')


def index3(request):
    # if request.method == 'POST':
    #     _location = request.POST['location']
    #     print( _location)
    #     z=Complaints.objects.all().last()
    #     z.save()
    
    return render(request,'council/index3.html')

def comp(request, pk):
    print(pk)
    
    cmp = get_object_or_404(Complaints, pk=pk)
    print(cmp)
    
    return render(request, 'council/index4.html', {'complaint': cmp})


@login_required
def compa(request):
    a = Complaints.objects.all()
    disp={
        'show':a     
    }
    return render(request,"council/index4.html",disp)

def main(request):
    return render(request,"council/main.html")


def error(request):
    return render(request,"index5.html")



@login_required
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        
        try:
            user = members.objects.get(user_name=username)

            if user.password == password:
                ward_member = WardMember.objects.get(user=user)
                assigned_wards = ward_member.assigned_wards.all()
                
                assigned_complaints = Complaints.objects.filter(ward_noo__in=assigned_wards)
                
                disp = {
                    'show': assigned_complaints,
                    'user': user  
                }
                
                return render(request, 'council/index4.html', disp)
            else:
                return redirect('error')
        
        except members.DoesNotExist:
            return redirect('error')

    return render(request, "council/login.html")


# def save_photo(request):
#     sub = "Requesting for a check the complaint"

#     if request.method == 'POST':
#         photo = request.FILES.get('photo')
#         text_area = request.POST.get('text_area')

#         try:
#             p = Complaints.objects.all().last()
#             p.photo = photo
#             p.save()

#             t = Complaints.objects.all().last()
#             t.text_area = text_area
#             t.save()
            # import pdb
            # pdb.set_trace()
    #         to = ['daneshganagimla@gmail.com']
    #         txt = "Please solve our ward problem"
    #         from_mail = settings.EMAIL_HOST_USER
    #         email = EmailMultiAlternatives(sub,txt,from_mail,to)
    #         email.send()

    #         return JsonResponse({'message': 'Complaint raised successfully!'})
            
    #     except Exception as e:
    #         return JsonResponse({'error': str(e)})

    # return JsonResponse({'error': 'Invalid request method'})



def save_photo(request):
    sub = "Requesting for a check of the complaint"

    if request.method == 'POST':
        photo_data = request.POST.get('photo')
        text_area = request.POST.get('text_area')
        location = request.POST.get('location')


        try:
            l = Complaints.objects.all().last()
            l.  location = location
            l.save()
            t = Complaints.objects.all().last()
            t.text_area = text_area
            t.save()
            # to = ['daneshganagimla@gmail.com']
            txt = "Please solve our ward problem"
            from_mail = settings.EMAIL_HOST_USER
            email = EmailMultiAlternatives(sub,txt,from_mail,)
            email.send()

            p = Complaints.objects.all().last()
            format, imgstr = photo_data.split(';base64,') 
            ext = format.split('/')[-1]  
            data = ContentFile(base64.b64decode(imgstr), name=f'complaint_photo.{ext}')
            p.photo.save(f'complaint_photo.{ext}', data, save=True)


            return JsonResponse({'message': 'Complaint raised successfully!'})
            
        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Invalid request method'})










def home(request):
    return render(request,"council/home.html")



def boot(request):
 return render(request,"council/index6.html")











