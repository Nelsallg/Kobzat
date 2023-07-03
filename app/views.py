"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Acceuil',
            'year': datetime.now().year,
        }
    )


def ai(request):
    """Renders the ai page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/ai.html',
        {
            'title': 'Intéliggence Artificielle',
            'year': datetime.now().year,
        }
    )


def video_game(request):
    """Renders the videoGame page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/video_game.html',
        {
            'title': 'Jeux video',
            'year': datetime.now().year,
        }
    )


def subscriptions(request):
    """Renders the subscriptions page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/subscriptions.html',
        {
            'title': 'Abonnements',
            'year': datetime.now().year,
        }
    )


def support(request):
    """Renders the support page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/support.html',
        {
            'title': 'Abonnements',
            'year': datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Contact',
            'message': 'Nos contacts.',
            'year': datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'A propos',
            'message': 'LivreLeur est une entreprise de livraisons créée le 16 juin 2023.',
            'year': datetime.now().year,
        }
    )