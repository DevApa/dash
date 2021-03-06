from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from documents.models import DocumentType
from documents.forms import DocumentTypeForm
from django.http import JsonResponse


class DocumentTypeListView(ListView):
    model = DocumentType
    template_name = 'tipo_documento/list.html'
    success_url = reverse_lazy('docs:list-t-doc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Tipo de Documento'
        context['pageview'] = 'Tipo de Documento'
        context['object_list'] = DocumentType.objects.filter(state=True)
        context['action'] = 'add'
        context['create_url'] = reverse_lazy('docs:list-t-doc')
        context['url_list'] = reverse_lazy('docs:list-t-doc')
        return context


class DocumentTypeCreateView(CreateView):
    model = DocumentType
    form_class = DocumentTypeForm
    template_name = "tipo_documento/create.html"
    success_url = reverse_lazy('docs:list-t-doc')

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
        context['title'] = 'Creaci??n de Tipo de Documento'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('docs:list-t-doc')
        return context


class DocumentTypeUpdateView(UpdateView):
    model = DocumentType
    form_class = DocumentTypeForm
    template_name = "tipo_documento/update.html"
    success_url = reverse_lazy('docs:list-t-doc')

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
        context['title'] = 'Actualizar Tipo de Documento'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('docs:list-t-doc')
        return context


class DocumentTypeDeleteView(DeleteView):
    model = DocumentType
    success_url = reverse_lazy('docs:list-t-doc')

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
            return redirect('docs:list-t-doc')
