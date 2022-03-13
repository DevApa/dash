from django.contrib.auth.decorators import login_required
from django.urls import path
from conf import views

urlpatterns = [
    # menu
    path(r'menu', login_required(views.MenuContentView.as_view()), name='menu'),
    path(r'newMenu', login_required(views.MenuContentView.newMenu), name='newMenu'),
    path(r'editMenu/<int:pk>', login_required(views.MenuContentView.editMenu), name='editMenu'),
    path(r'viewMenu/<int:pk>', login_required(views.MenuContentView.viewMenu), name='viewMenu'),
    path(r'deleteMenu/<int:pk>', login_required(views.MenuContentView.deleteMenu), name='deleteMenu'),
    path(r'ajax/loadMenus', login_required(views.MenuContentView.loadMenus), name='loadMenus'),

    # modulo
    path(r'modulo', login_required(views.ModuloContentView.as_view()), name='modulo'),
    path(r'newModulo', login_required(views.ModuloContentView.newModulo), name='newModulo'),
    path(r'editModulo/<int:pk>', login_required(views.ModuloContentView.editModulo), name='editModulo'),
    path(r'viewModulo/<int:pk>', login_required(views.ModuloContentView.viewModulo), name='viewModulo'),
    path(r'deleteModulo/<int:pk>', login_required(views.ModuloContentView.deleteModulo), name='deleteModulo'),

    # roles
    path(r'roles', login_required(views.RolContentView.as_view()), name='roles'),
    path(r'newRol', login_required(views.RolContentView.newRol), name='newRol'),
    path(r'editRol/<int:pk>', login_required(views.RolContentView.editRol), name='editRol'),
    path(r'viewRol/<int:pk>', login_required(views.RolContentView.viewRol), name='viewRol'),
    path(r'deleteRol/<int:pk>', login_required(views.RolContentView.deleteRol), name='deleteRol'),

    path(r'roles-menu', login_required(views.RolMenuContentView.as_view()), name='roles-menu'),
    path(r'roles-usuario', login_required(views.RolUsuarioContentView.as_view()), name='roles-usuario'),
    path(r'deleteRolMenu/<int:pk>', login_required(views.RolMenuContentView.deleteRolMenu), name='deleteRolMenu'),
    path(r'deleteRolUsuario/<int:pk>', login_required(views.RolUsuarioContentView.deleteRolUsuario),
         name='deleteRolUsuario'),

]
