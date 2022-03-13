from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventory.models import Brand
from inventory.forms import BrandForm
from django.http import JsonResponse


class BrandListView(ListView):
    model = Brand
    template_name = 'marca/list.html'
    success_url = reverse_lazy('inventory:list-brand')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Marca'
        context['pageview'] = 'Marca'
        context['object_list'] = Brand.objects.filter(state=True)
        context['create_url'] = reverse_lazy('inventory:create-brand')
        context['url_list'] = reverse_lazy('inventory:list-brand')
        return context


class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = "marca/create.html"
    success_url = reverse_lazy('inventory:list-brand')
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'{self.model.__name__} registrado correctamente'
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
        context['title'] = 'Creación de Marca'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('inventory:list-brand')
        return context
    

class BrandUpdateView(UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = "marca/update.html"
    success_url = reverse_lazy('inventory:list-brand')

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
        context['title'] = 'Actualizar Marca'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('inventory:list-brand')
        return context


class BrandDeleteView(DeleteView):
    model = Brand
    success_url = reverse_lazy('inventory:list-brand')

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            cycle = self.get_object()
            cycle.delete()
            # university.save()
            message = f'{self.model.__name__} eliminada correctamente!'
            errors = 'No se encontraron errores'
            response = JsonResponse({'message': message, 'error': errors})
            response.status_code = 201
            return response
        else:
            return redirect('inventory:list-brand')
