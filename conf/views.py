from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from conf.forms import *
from conf.models import *


class MenuContentView(View):

    # Carga los datos iniciales del HTML
    def get(self, request):
        menusview = Menu.objects.order_by('orden')
        modulos = Modulo.objects.order_by('descripcion')
        menusItem = Menu.objects.exclude(url__isnull=False).exclude(modulo_id__isnull=True).order_by('descripcion')
        greeting = {'heading': "Menu", 'pageview': "Administración", "menusview": menusview}
        return render(request, 'conf/menu.html', greeting)

    # Metodo para guardar un nuevo menu
    def newMenu(request):
        if request.method == 'POST':
            print("if")
            menuForm = MenuForm(request.POST)
            if menuForm.is_valid():
                menuForm.save()
                messages.success(request, "Se registro correctamente", "success")
            else:
                messages.error(request, "No se puedo registrar", "error")
            return redirect('menu')
        else:
            print("else")
            menuFormView = MenuForm()
            menu = Menu()
            view = False
            context = {'menuFormView': menuFormView, 'menu': menu, 'view': view}
        return render(request, 'conf/menuForm.html', context)

    # Consulta el registro de un menu por su pk
    def viewMenu(request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        menuFormView = MenuForm(instance=menu)
        view = True
        context = {'menuFormView': menuFormView, 'menu': menu, 'view': view}
        return render(request, 'conf/menuForm.html', context)

    # Editar los datos de un menu por su pk
    def editMenu(request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        if request.method == 'POST':
            ##editarField
            request.POST._mutable = True
            request.POST['descripcion'] = request.POST['descripcion'].capitalize()
            request.POST['key'] = request.POST['descripcion'].replace(" ", "_").lower() + "_" + request.POST['orden']
            if request.POST['modulo_id'] and request.POST['parent_id']:
                request.POST['modulo_id'] = ''
            request.POST._mutable = False
            # endEditarField
            form = MenuForm(request.POST, instance=menu)
            if form.is_valid():
                form.save()
                messages.success(request, "Se edito correctamente", "success")
                return redirect('menu')
        else:
            menuFormView = MenuForm(instance=menu)
            view = False
            context = {'menuFormView': menuFormView, 'menu': menu, 'view': view}
        return render(request, 'conf/menuForm.html', context)

    # Elimina un registro del menu
    def deleteMenu(request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        if menu:
            menu.delete()
            messages.success(request, "Se ha eliminado correctamente", "success")
        return redirect('menu')

    # AJAX
    def loadMenus(request):
        modulo_id = request.GET.get('modulo_id')
        menus = Menu.objects.filter(Q(modulo_id=modulo_id) & Q(href__isnull=True)).order_by('descripcion')
        return render(request, 'conf/menuList.html', {'menus': menus})


class ModuloContentView(View):

    # Carga los datos iniciales del HTML
    def get(self, request):
        modulos = Modulo.objects.order_by('orden')
        greeting = {'heading': "Modulo", 'pageview': "Administración", 'modulosview': modulos}
        return render(request, 'conf/modulo.html', greeting)

    # Metodo para guardar un nuevo modulo
    def newModulo(request):
        if request.method == 'POST':
            ##editarField
            request.POST._mutable = True
            request.POST['descripcion'] = request.POST['descripcion'].capitalize()
            request.POST['key'] = request.POST['descripcion'].replace(" ", "_").lower() + "_" + request.POST['orden']
            request.POST._mutable = False
            # endEditarField
            modForm = ModuloForm(request.POST)
            if modForm.is_valid():
                modForm.save()
                messages.success(request, "Se registro correctamente", "success")
            else:
                messages.error(request, "No se puedo registrar", "error")
            return redirect('modulo')
        else:
            moduloFormView = ModuloForm();
            modulo = Modulo()
            view = False
            context = {'moduloFormView': moduloFormView, 'modulo': modulo, 'view': view}
        return render(request, 'conf/moduloForm.html', context)

    # Consulta el registro de un modulo por su pk
    def viewModulo(request, pk):
        modulo = get_object_or_404(Modulo, pk=pk)
        moduloFormView = ModuloForm(instance=modulo)
        view = True
        context = {'moduloFormView': moduloFormView, 'modulo': modulo, 'view': view}
        return render(request, 'conf/moduloForm.html', context)

    # Editar los datos de un modulo por su pk
    def editModulo(request, pk):
        modulo = get_object_or_404(Modulo, pk=pk)
        if request.method == 'POST':
            ##editarField
            request.POST._mutable = True
            request.POST['descripcion'] = request.POST['descripcion'].capitalize()
            request.POST['key'] = request.POST['descripcion'].replace(" ", "_").lower() + "_" + request.POST['orden']
            request.POST._mutable = False
            # endEditarField
            form = ModuloForm(request.POST, instance=modulo)
            if form.is_valid():
                form.save()
                messages.success(request, "Se edito correctamente", "success")
                return redirect('modulo')
        else:
            moduloFormView = ModuloForm(instance=modulo)
            view = False
            context = {'moduloFormView': moduloFormView, 'modulo': modulo, 'view': view}
        return render(request, 'conf/moduloForm.html', context)

    # Elimina un registro del modulo
    def deleteModulo(request, pk):
        modulo = get_object_or_404(Modulo, pk=pk)
        if modulo:
            modulo.delete()
            messages.success(request, "Se ha eliminado correctamente", "success")
        return redirect('modulo')


class RolContentView(View):
    # Carga los datos iniciales del HTML
    def get(self, request):
        rol = Rol.objects.order_by('descripcion')
        greeting = {'heading': "Roles del SECOED", 'pageview': "Administración", 'rolview': rol}
        return render(request, 'conf/roles.html', greeting)

    # Metodo para guardar un nuevo rol
    def newRol(request):
        if request.method == 'POST':
            rolForm = RolForm(request.POST)
            if rolForm.is_valid():
                rolForm.save()
                messages.success(request, "Se registro correctamente", "success")
            else:
                messages.error(request, "No se puedo registrar", "error")
            return redirect('roles')
        else:
            rolFormView = RolForm();
            rol = Rol()
            view = False
            context = {'rolFormView': rolFormView, 'rol': rol, 'view': view}
        return render(request, 'conf/rolesForm.html', context)

    # Consulta el registro de un rol por su pk
    def viewRol(request, pk):
        rol = get_object_or_404(Rol, pk=pk)
        rolFormView = RolForm(instance=rol)
        view = True
        context = {'rolFormView': rolFormView, 'rol': rol, 'view': view}
        return render(request, 'conf/rolesForm.html', context)

    # Editar los datos de un rol por su pk
    def editRol(request, pk):
        rol = get_object_or_404(Rol, pk=pk)
        if request.method == 'POST':
            form = RolForm(request.POST, instance=rol)
            if form.is_valid():
                form.save()
                messages.success(request, "Se edito correctamente", "success")
                return redirect('roles')
        else:
            rolFormView = RolForm(instance=rol)
            view = False
            context = {'rolFormView': rolFormView, 'rol': rol, 'view': view}
        return render(request, 'conf/rolesForm.html', context)

    # Elimina un registro del rol
    def deleteRol(request, pk):
        rol = get_object_or_404(Rol, pk=pk)
        if rol:
            rol.delete()
            messages.success(request, "Se ha eliminado correctamente", "success")
        return redirect('roles')


class RolMenuContentView(View):
    # Carga los datos iniciales del HTML
    def get(self, request):
        rolesMenu = RolMenu.objects.order_by('descripcion')
        greeting = {'heading': "Roles de menú del SECOED", 'pageview': "Administración", 'rolesMenuView': rolesMenu}
        return render(request, 'conf/rolMenu.html', greeting)

    # Elimina un registro del rol-usuario
    def deleteRolMenu(request, pk):
        rol = get_object_or_404(RolMenu, pk=pk)
        if rol:
            rol.delete()
            messages.success(request, "Se ha eliminado correctamente", "success")
        return redirect('roles-menu')


class RolUsuarioContentView(View):
    # Carga los datos iniciales del HTML
    def get(self, request):
        rolesUsuario = Rol.objects.order_by('descripcion')
        greeting = {'heading': "Roles de usuario del SECOED", 'pageview': "Administración", 'rolesUsuarioView': rolesUsuario}
        return render(request, 'conf/rolUsuarios.html', greeting)

    # Elimina un registro del rol-usuario
    def deleteRolUsuario(request, pk):
        rol = get_object_or_404(Rol, pk=pk)
        if rol:
            rol.delete()
            messages.success(request, "Se ha eliminado correctamente", "success")
        return redirect('roles-usuario')