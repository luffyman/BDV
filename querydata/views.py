from django.shortcuts import render

def process_country_code(request):
    if request.method == 'POST':
        country_code = request.POST.get('country_code')
        # Process the country_code here as needed
        # You can also redirect to another page or return a response
        return render(request, 'result_template.html', {'country_code': country_code})
    else:
        return render(request, 'country_code_input.html')
