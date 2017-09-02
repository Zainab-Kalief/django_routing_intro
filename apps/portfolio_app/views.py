from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'real_portfolio/index.html')

def testimonial(request):
    return render(request, 'real_portfolio/testimonials.html')

def projects(request):
    return render(request, 'real_portfolio/projects.html')

def about(request):
    return render(request, 'real_portfolio/about.html')
