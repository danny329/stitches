from django.shortcuts import render,redirect, reverse, HttpResponse
from .models import Color,Pattern,ClothType, ClothMenu, Design , Collar, Cuff, ButtonHole,Button, Back,Front, Pocket, ShirtFit, Measurement,StandardSize
from customer.forms import MeasurementForm
import sweetify
from django.core.serializers import serialize
from django.core import serializers
from django.forms import modelformset_factory
from django.http import JsonResponse
# Create your views here.
design_summary = Design()
context = {}
measurement = MeasurementForm()
def selectionpage(request):
    return render(request, 'selectionpage.html')




def select(request, part=0):
    #to view list of already existing datas
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

    global design_summary
    global context
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
            print(rest, 'rest init')
            print(design_summary, 'design summary init')
            global measurement
        except:
            print('error get')
        context = {'color': color, 'pattern': pattern, 'clothtype': clothtype, 'pocket': pocket, 'collar': collar, 'back': back, 'front': front, 'cuff': cuff, 'button': button, 'buttonhole': buttonhole, 'standardsize': standardsize, 'shirtfit': shirtfit, 'clothmenu': clothmenu, 'count': count, 'rest': rest, 'summary': design_summary, 'measurement': measurement}
        context['scriptf'] = 'show active'
        context['scriptdco'] = 'show active'
        context['scriptdeb'] = 'show active'
        return render(request, 'new_selection.html', context)


    if request.method == 'POST':
        try:
            measurement = MeasurementForm(request.POST)
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
                    # design_summary.user = request.user
                elif MeasurementForm(request.POST):
                    measurement = MeasurementForm(request.POST)
                    if measurement.is_valid():
                        if design_summary.standard_size:
                            design_summary.standard_size = None
                        if design_summary.shirtfit:
                            design_summary.shirtfit = None
                        measure = measurement.save(commit=False)
                        design_summary.size = measure
                        measure.save()
            except Exception as e:
                print(e)
            print(design_summary, 'inside post')
            context = {'color': color, 'pattern': pattern, 'clothtype': clothtype, 'pocket': pocket, 'collar': collar,'back': back, 'front': front, 'cuff': cuff, 'button': button, 'buttonhole': buttonhole,'standardsize': standardsize, 'shirtfit': shirtfit, 'clothmenu': clothmenu, 'count': count,'rest': rest, 'summary': design_summary, 'measurement': measurement}
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


        # return redirect('/selection/select/')
        return render(request, 'new_selection.html', context)

def addtocart(request):
    global design_summary
    global context
    if design_summary.size is None and (design_summary.shirtfit is None and design_summary.standard_size is None):
        sweetify.sweetalert(request, 'Westworld is awesome', text='Really... if you have the chance - watch it!', persistent = 'I agree!')
        print('hello here')
        print(context)
        return redirect('/selection/select', context)
    if request.user.is_authenticated:
        try:
            if not design_summary.collar:
                design_summary.collar = Collar.objects.get(
                    collar_style=ClothMenu.objects.get(name=design_summary.cloth_menu.name).collar.collar_style)
                context['defaultcollar'] = '(default)'
            if not design_summary.cuff:
                design_summary.cuff = Cuff.objects.get(
                    cuff_style=ClothMenu.objects.get(name=design_summary.cloth_menu.name).cuff.cuff_style)
                context['defaultcuff'] = '(default)'
            if not design_summary.back:
                design_summary.back = Back.objects.get(
                    back_style=ClothMenu.objects.get(name=design_summary.cloth_menu.name).back.back_style)
                context['defaultback'] = '(default)'
            if not design_summary.front:
                design_summary.front = Front.objects.get(
                    front_style=ClothMenu.objects.get(name=design_summary.cloth_menu.name).front.front_style)
                context['defaultfront'] = '(default)'
            if not design_summary.pocket:
                design_summary.pocket = Pocket.objects.get(
                    pocket_style=ClothMenu.objects.get(name=design_summary.cloth_menu.name).pocket.pocket_style)
                context['defaultpocket'] = '(default)'
            if not design_summary.button_hole:
                design_summary.button_hole = ButtonHole.objects.get(button_hole_style=ClothMenu.objects.get(
                    name=design_summary.cloth_menu.name).button_hole.button_hole_style)
                context['defaultbutton_hole'] = '(default)'
            if not design_summary.button:
                design_summary.button = Button.objects.get(
                    button_style=ClothMenu.objects.get(name=design_summary.cloth_menu.name).button.button_style)
                context['defaultbutton'] = '(default)'
        except Exception as e:
            print(e)
        design_summary.user = request.user
        design_summary.save()
        return render(request, 'cart.html', context)
    else:
        print('hello to login page')
        print(context)
        return render(request, 'login_page.html',context)