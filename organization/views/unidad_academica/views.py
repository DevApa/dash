from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from organization.models import AcademicUnit
from organization.forms import AcademicUnitForm
from django.http import JsonResponse


class AcademicUnitListView(ListView):
    model = AcademicUnit
    template_name = 'uacademica/list.html'
    success_url = reverse_lazy('org:uac-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Unidad Académica'
        context['create_url'] = reverse_lazy('org:uac-create')
        context['url_list'] = reverse_lazy('org:uac-list')
        return context


class AcademicUnitCreateView(CreateView):
    model = AcademicUnit
    form_class = AcademicUnitForm
    template_name = 'uacademica/create.html'
    success_url = reverse_lazy('org:uac-list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
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
        context['title'] = 'Creación de Unidad Académica'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('org:uac-list')
        return context


class AcademicUnitUpdateView(UpdateView):
    model = AcademicUnit
    form_class = AcademicUnitForm
    template_name = 'uacademica/update.html'
    success_url = reverse_lazy('org:uac-list')

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
        context['title'] = 'Actualizar Unidad Académica'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('org:uac-list')
        return context


class AcademicUnitDeleteView(DeleteView):
    model = AcademicUnit
    success_url = reverse_lazy('org:uac-list')

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
            return redirect('org:uac-list')
