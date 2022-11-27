from django.shortcuts import render
from django.views import View
# Create your views here.
from paint_app.forms import ColorPickerForm



class ColorPickerView(View):
    def get(self, request):
        color_form = ColorPickerForm(request.POST)
        
        red_value = int(request.POST['red_amount'])
        green_value = int(request.POST['green_amount'])
        blue_value = int(request.POST['blue_amount'])
        
        html_data = {
            'form': color_form,
            'red': red_value,
            'green': green_value,
            'blue': blue_value,
        }
        return render(
            request=request, 
            template_name='color_picker.html',
            context={}
        )
        
        def post(self, request):
            print(request.POST)
