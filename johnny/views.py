from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Home, About, Portfolio, Category, Skills, Profile, Contact


def index(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = {
            'name': name,
            'subject': subject,
            'email': email,
            'message': message,
        }
        email_body = f'''
        New Messaage: {data['message']}

        From: {data['email']}
        '''.format(data['message'], data['email'])

        send_mail(data['subject'], email_body, '',
                  ['km.monzurul.islam@gmail.com'])
        return HttpResponse('Thanks for contacting me. I will be in touch soon.')
    # Home Record
    home = Home.objects.latest('updated')
    # About Record
    about = About.objects.latest('updated')
    # Portfolio
    profiles = Profile.objects.filter(about=about)
    facebook_link = profiles[0]
    linkedin_link = profiles[1]
    github_link = profiles[2]
    # Skills
    catagories = Category.objects.all()
    # Portfolios
    portfolios = Portfolio.objects.all()
    # My Contact
    contact = Contact.objects.latest('updated')

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'catagories': catagories,
        'portfolios': portfolios,
        'facebook_link': facebook_link,
        'linkedin_link': linkedin_link,
        'github_link': github_link,
        'contact': contact,
    }
    return render(request, 'html/index.html', context)
