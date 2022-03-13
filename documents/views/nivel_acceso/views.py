from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from documents.models import LevelAccess
from documents.forms import LevelAccessForm
from django.http import JsonResponse


class LevelAccessListView(ListView):
    model = LevelAccess
    template_name = 'nivel_acceso/list.html'
    success_url = reverse_lazy('docs:list-level-a')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Nivel de Acceso'
        context['pageview'] = 'Nivel'
        context['object_list'] = LevelAccess.objects.filter(state=True)
        context['action'] = 'add'
        context['create_url'] = reverse_lazy('docs:create-level-a')
        context['url_list'] = reverse_lazy('docs:list-level-a')
        return context


class LevelAccessCreateView(CreateView):
    model = LevelAccess
    form_class = LevelAccessForm
    template_name = "nivel_acceso/create.html"
    success_url = reverse_lazy('docs:list-level-a')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                option = request.POST['action']
                form = self.get_form()
                if option == 'add':
                    form.save()
                    message = f'{self.model.__name__} registrada correctamente'
                    error = 'No han ocurrido errores'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'{self.model.__name__} no se pudo registrar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Nivel de Acceso'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('docs:list-level-a')
        return context


class LevelAccessUpdateView(UpdateView):
    model = LevelAccess
    form_class = LevelAccessForm
    template_name = "nivel_acceso/update.html"
    success_url = reverse_lazy('docs:list-level-a')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST, instance=self.get_object())
                if form.is_valid():
                    form.save()
                    message = f'{self.model.__name__} actualizado correctamente'
                    error = 'No hay error'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'{self.model.__name__} no se pudo actualizar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Nivel de Acceso'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('docs:list-level-a')
        return context


class LevelAccessDeleteView(DeleteView):
    model = LevelAccess
    success_url = reverse_lazy('docs:list-level-a')

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            obj = self.get_object()
            obj.state = False
            obj.save()
            message = f'{self.model.__name__} eliminada correctamente!'
            errors = 'No se encontraron errores'
            response = JsonResponse({'message': message, 'error': errors})
            response.status_code = 201
            return response
        else:
            return redirect('docs:list-level-a')
