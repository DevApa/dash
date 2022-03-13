from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from documents.models import Document
from documents.forms import DocumentForm
from django.http import JsonResponse


class DocumentListView(ListView):
    model = Document
    template_name = 'documento/list.html'
    success_url = reverse_lazy('docs:list-doc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Documento'
        context['pageview'] = 'Documento'
        context['object_list'] = Document.objects.filter(state=True)
        context['action'] = 'add'
        context['create_url'] = reverse_lazy('docs:create-doc')
        context['url_list'] = reverse_lazy('docs:list-doc')
        return context


class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentForm
    template_name = "documento/create.html"
    success_url = reverse_lazy('docs:list-doc')

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
        context['title'] = 'Creación de Documento'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('docs:list-doc')
        return context


class DocumentUpdateView(UpdateView):
    model = Document
    form_class = DocumentForm
    template_name = "documento/update.html"
    success_url = reverse_lazy('docs:list-doc')

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
        context['title'] = 'Actualizar Documento'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('docs:list-doc')
        return context


class DocumentDeleteView(DeleteView):
    model = Document
    success_url = reverse_lazy('docs:list-doc')

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
            return redirect('docs:list-doc')
