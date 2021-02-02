from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Persona
from .forms import PersonaForm


class PersonaList(ListView):
    model = Persona
    template_name = 'index.html'


class PersonaCrear(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crearPersona.html'
    success_url = reverse_lazy('index')


class PersonaEditar(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'editarPersona.html'
    success_url = reverse_lazy('index')


class PersonaEliminar(DeleteView):
    model = Persona
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')
