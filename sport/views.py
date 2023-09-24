from django.shortcuts import render

# Create your views here.


def index(req):
    return render(req, 'index.html')


def foot(req):
    return render(req, 'football.html')


def basket(req):
    return render(req, 'basketball.html')


def volley(req):
    return render(req, 'volleyball.html')


def sportsmen(req, sport, id):
    footballs = [
        {'name': 'Sergio Rames', 'pic':'img/f1.jpg', 'picsport':'img/fball.jpg',
         'desc':'Играет за Спартак, забил 10 голов'},
        {'name': 'Helio Servantes', 'pic': 'img/f1.jpg', 'picsport': 'img/fball.jpg',
         'desc': 'Играет за Спартак, забил 20 голов'},
        {'name': 'Ivan Ivanov', 'pic': 'img/f1.jpg', 'picsport': 'img/fball.jpg',
         'desc': 'Играет за Спартак, забил 20 голов'},
    ]
    data = {}

    if sport == 'football':
        data = {'name': footballs[id]['name'],
                'pic': footballs[id]['pic'],
                'picsport': footballs[id]['picsport'],
                'desc': footballs[id]['desc']}

    return render(req, 'sportsmen.html', data)

