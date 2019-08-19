from django.shortcuts import render,redirect, reverse, HttpResponse
from .models import Color,Pattern,ClothType, ClothMenu, Design , Collar, Cuff, ButtonHole,Button, Back,Front, Pocket, ShirtFit, Measurement,StandardSize
from django.http import JsonResponse
# Create your views here.
def selectionpage(request):
    return render(request, 'selectionpage.html')

design_summary = Design()
def select(request, part=0):
    rest = []
    count = 0
    print(design_summary , 'design summary')
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
            print(rest ,'rest')
            # summary on selection of fabric

            try:
                if 'clothmenu_select' in request.POST:
                    design_summary.cloth_menu = ClothMenu.objects.get(name=request.POST['clothmenu_select'])
                elif 'collar_select' in request.POST:
                    design_summary.collar = Collar.objects.get(collar_style=request.POST['collar_select'])
                elif 'cuff_select' in request.POST:
                    design_summary.cuff = Cuff.objects.get(cuff_style=request.POST['cuff_select'])
                elif 'back_select' in request.POST:
                    design_summary.back = Back.objects.get(back_style=request.POST['back_select'])
               # design_summary.user = request.user

            except:
                print("error summary")
            # end fabric selection summary
            print(design_summary, 'inside post')
            context = {'color': color, 'pattern': pattern, 'clothtype': clothtype, 'pocket':pocket,'collar': collar,'back': back, 'front': front, 'cuff':cuff, 'button':button, 'buttonhole':buttonhole,'standardsize':standardsize,'shirtfit':shirtfit, 'clothmenu': clothmenu, 'count': count, 'rest' : rest,'summary': design_summary}
            if part == 1:
                return render(request, 'new_selection.html', context)
            else:
                return redirect('select')
        except:
            print("error")

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

    context = {'color': color, 'pattern': pattern, 'clothtype': clothtype,'pocket':pocket,'collar': collar,'back': back, 'front': front, 'cuff':cuff, 'button':button, 'buttonhole':buttonhole,'standardsize':standardsize,'shirtfit':shirtfit, 'clothmenu': clothmenu,  'count': count, 'rest' : rest,'summary': design_summary}
    return render(request, 'new_selection.html', context)

