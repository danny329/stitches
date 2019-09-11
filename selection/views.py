from django.shortcuts import render,redirect, reverse, HttpResponse
from .models import Color,Pattern,ClothType, ClothMenu, Orders , Collar, Cuff, ButtonHole,Button, Back,Front, Pocket, ShirtFit, Measurement,StandardSize,OrderStatusCode
from customer.forms import MeasurementForm
from django.contrib.auth.models import User
# Create your views here.
design_summary = Orders()
context = {}
def selectionpage(request):
    return render(request, 'selectionpage.html')




def select(request, part=0):
    #to view list of already existing datas
    try:

        color = Color.objects.all()
        pattern = Pattern.objects.all()
        clothtype = ClothType.objects.all()
        clothmenu = ClothMenu.objects.all()
        collar = Collar.objects.all()
        cuff = Cuff.objects.all()
        back = Back.objects.all()
        front = Front.objects.all()
        pocket = Pocket.objects.all()
        button = Button.objects.all()
        buttonhole = ButtonHole.objects.all()
        standardsize = StandardSize.objects.all()
        shirtfit = ShirtFit.objects.all()
        measurement = MeasurementForm()
        list_of_measure = None
    except Exception as e:
        print(e)
    global design_summary
    global context
    if request.user.is_authenticated:
        list_of_measure = Measurement.objects.filter(user__username=request.user)

    rest = []
    if request.method == 'GET':
        try:
            count = 0
            # initial loading of the page
            count = clothmenu.count()
            try:
                if count > 7:
                    count = count % 7
            except ZeroDivisionError:
                count = 2

            # fill of div col
            rest.clear()
            for i in range(1, 6 - (count % 6)):
                rest.append(i)

        except:
            print('error get')


        context = {'color': color, 'pattern': pattern, 'clothtype': clothtype, 'pocket': pocket, 'collar': collar, 'back': back, 'front': front, 'cuff': cuff,
                   'button': button, 'buttonhole': buttonhole, 'standardsize': standardsize, 'shirtfit': shirtfit, 'clothmenu': clothmenu, 'count': count,
                   'rest': rest, 'summary': design_summary, 'measurement': measurement, 'list_of_measure':list_of_measure}
        # if request.user.is_authenticated and Measurement.objects.get(user__username=request.user):
        #     instance = Measurement.objects.get(user__username=request.user)
        #     existing_measurement = MeasurementForm(instance=instance)
        #     context['existing_measurement']: existing_measurement
        context['scriptf'] = 'show active'
        context['scriptdco'] = 'show active'
        context['scriptdeb'] = 'show active'
        return render(request, 'new_selection.html', context)


    if request.method == 'POST':
        try:
            # for selection search submit begin -->
            if 'pattern' in request.POST:
                patterns = request.POST['pattern']
            if 'color_select' in request.POST:
                colors = request.POST['color_select']
            if 'type' in request.POST:
                clothtypes = request.POST['type']
            if 'pattern' in request.POST and 'color_select' in request.POST and 'type' in request.POST:
                clothmenu = ClothMenu.objects.filter(color__color_style=colors, pattern__pattern_style=patterns, cloth_type__cloth_type_style = clothtypes)
            elif 'pattern' in request.POST and 'color_select' in request.POST:
                clothmenu = ClothMenu.objects.filter(color__color_style=colors, pattern__pattern_style=patterns)
            elif 'color_select' in request.POST and 'type' in request.POST:
                clothmenu = ClothMenu.objects.filter(color__color_style=colors, cloth_type__cloth_type_style=clothtypes)
            elif 'pattern' in request.POST and 'type' in request.POST:
                clothmenu = ClothMenu.objects.filter(pattern__pattern_style=patterns, cloth_type__cloth_type_style=clothtypes)
            elif 'pattern' in request.POST:
                clothmenu = ClothMenu.objects.filter(pattern__pattern_style=patterns)
            elif 'color_select' in request.POST:
                clothmenu = ClothMenu.objects.filter(color__color_style=colors)
            elif 'type' in request.POST:
                clothmenu = ClothMenu.objects.filter(cloth_type__cloth_type_style=clothtypes)
            # selection search ends here--!
            # for div alignment
            count = clothmenu.count()
            try:
                if count > 7:
                    count = count % 7
            except ZeroDivisionError:
                count = 2
            rest.clear()
            for i in range(1, 6 - (count % 6)):
                rest.append(i)
            # summary on selection
            try:
                if 'clothmenu_select' in request.POST:
                    design_summary.cloth_menu = ClothMenu.objects.get(name=request.POST['clothmenu_select'])
                elif 'collar_select' in request.POST:
                    design_summary.collar = Collar.objects.get(collar_style=request.POST['collar_select'])
                elif 'cuff_select' in request.POST:
                    design_summary.cuff = Cuff.objects.get(cuff_style=request.POST['cuff_select'])
                elif 'back_select' in request.POST:
                    design_summary.back = Back.objects.get(back_style=request.POST['back_select'])
                elif 'front_select' in request.POST:
                    design_summary.front = Front.objects.get(front_style=request.POST['front_select'])
                elif 'pocket_select' in request.POST:
                    design_summary.pocket = Pocket.objects.get(pocket_style=request.POST['pocket_select'])
                elif 'button_select' in request.POST:
                    design_summary.button = Button.objects.get(button_style=request.POST['button_select'])
                elif 'button_hole_select' in request.POST:
                    design_summary.button_hole = ButtonHole.objects.get(button_hole_style=request.POST['button_hole_select'])
                elif 'shirt_fit' in request.POST:
                    if design_summary.size is not None:
                        design_summary.size = None
                    design_summary.shirtfit = ShirtFit.objects.get(shirt_fit_style=request.POST['shirt_fit'])
                    print(design_summary.shirtfit)
                elif 'Standard_size' in request.POST:
                    if design_summary.size is not None:
                        design_summary.size = None
                    design_summary.standard_size = StandardSize.objects.get(standard_size_style=request.POST['Standard_size'])
                    print(design_summary.standard_size)
                elif 'profile_select' in request.POST:
                    design_summary.size = Measurement.objects.get(pk=request.POST['profile_select'])
                    if design_summary.standard_size is not None:
                        design_summary.standard_size = None
                    if design_summary.shirtfit is not None:
                        design_summary.shirtfit = None
            except Exception as e:
                print(e)
            measurement = MeasurementForm(request.POST)
            if measurement.is_valid():
                measure = measurement.save(commit=False)
                if request.user.is_authenticated:
                    measure.user = User.objects.get(username=request.user)
                if design_summary.standard_size is not None:
                    design_summary.standard_size = None
                if design_summary.shirtfit is not None:
                    design_summary.shirtfit = None
                design_summary.size = measure
                measure.save()
                print(design_summary.size)

            context = {'color': color, 'pattern': pattern, 'clothtype': clothtype, 'pocket': pocket, 'collar': collar,'back': back, 'front': front, 'cuff': cuff,
                       'button': button, 'buttonhole': buttonhole,'standardsize': standardsize, 'shirtfit': shirtfit, 'clothmenu': clothmenu, 'count': count,
                       'rest': rest, 'summary': design_summary, 'measurement': measurement, 'list_of_measure':list_of_measure }

            # end  selection summary
        except Exception as e:
            print(e)


        if part == 'FABRIC':
            context['scriptf'] = 'show active'
            context['scriptdco'] = 'show active'
            context['scriptdeb'] = 'show active'
        elif part == 'COLLAR':
            context['scriptdco'] = 'show active'
            context['scriptd'] = 'show active'
            context['scriptdeb'] = 'show active'
        elif part == 'CUFF':
            context['scriptdcu'] = 'show active'
            context['scriptd'] = 'show active'
            context['scriptdeb'] = 'show active'
        elif part == 'BACK':
            context['scriptdb'] = 'show active'
            context['scriptd'] = 'show active'
            context['scriptdeb'] = 'show active'
        elif part == 'FRONT':
            context['scriptdf'] = 'show active'
            context['scriptd'] = 'show active'
            context['scriptdeb'] = 'show active'
        elif part == 'POCKET':
            context['scriptdp'] = 'show active'
            context['scriptd'] = 'show active'
            context['scriptdeb'] = 'show active'
        elif part == 'BUTTONHOLE':
            context['scriptdebu'] = 'show active'
            context['scriptde'] = 'show active'
            context['scriptdco'] = 'show active'
        elif part == 'BUTTON':
            context['scriptdeb'] = 'show active'
            context['scriptde'] = 'show active'
            context['scriptdco'] = 'show active'
        elif part == 'SIZE':
            context['scripts'] = 'show active'
            context['scriptdeb'] = 'show active'
            context['scriptdco'] = 'show active'

        return render(request, 'new_selection.html', context)

def addtocart(request):
    global design_summary
    global context
    if design_summary.size is None and design_summary.shirtfit is not None and design_summary.standard_size is None:
        return redirect('/selection/select', context)
    if design_summary.size is None and design_summary.shirtfit is None and design_summary.standard_size is not None:
        return redirect('/selection/select', context)
    if design_summary.size is None and design_summary.shirtfit is None and design_summary.standard_size is None:
        return redirect('/selection/select', context)
    if request.user.is_authenticated:
        design_summary.user = request.user
        design_summary.quantity = 1
        design_summary.subtotal = design_summary.quantity * design_summary.cloth_menu.price
        design_summary.status = OrderStatusCode.objects.get(status='INCART')
        design_summary.save()
        design_summary = Orders()
        return redirect('/cart/')
    else:
        print('hello to login page')
        print(context)
        return render(request, 'login_page.html', context)
def mes(request):
    measurement = MeasurementForm()
    if request.method == 'POST':
        measurement = MeasurementForm(request.POST)
        measure = measurement.save(commit=False)
        if request.user.is_authenticated:
            measure.user = User.objects.get(username=request.user)
        measure.save()
    context={'measurement': measurement}
    return render(request,'measurement.html',context)