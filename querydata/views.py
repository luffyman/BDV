from django.shortcuts import render
import requests


def result_view(request):
    # Your view logic here to process the data and create a context
    return render(request, 'result_template.html', context)

def country_code_input(request):
    if request.method == 'POST':
        country_code = request.POST.get('country_code')
        # Assuming you have a function to retrieve bank data from the API
        bank_data = retrieve_bank_data(country_code)
        return render(request, 'result_template.html', {'bank_data': bank_data})
    else:
        return render(request, 'country_code_input.html')

def retrieve_bank_data(country_code):
    url = f"https://api.apilayer.com/bank_data/banks_by_country?country_code={country_code}"

    headers = {
        "apikey": "5b4vCbnrRGQbwD3iliLJicClMNi3d9o8"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get('data', [])
    else:
        return []


# from django.shortcuts import render

# def process_country_code(request):
#     if request.method == 'POST':
#         country_code = request.POST.get('country_code')
#         # Process the country_code here as needed
#         # You can also redirect to another page or return a response
#         return render(request, 'result_template.html', {'country_code': country_code})
#     else:
#         return render(request, 'country_code_input.html')
