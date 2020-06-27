from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UMForm, ProductoForm

from baseapp.views import SinPrivilegios

# vista basada en clases
class CategoriaView(SinPrivilegios, generic.ListView):
    permission_required = "invapp.view_categoria"
    model = Categoria
    template_name = "invapp/categoria_list.html"
    context_object_name = "obj"


class CategoriaNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    permission_required = "invapp.add_categoria"
    model = Categoria
    template_name = "invapp/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    success_message = "Categoria Creada Satistactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class CategoriaEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "invapp.change_categoria"
    model = Categoria
    template_name = "invapp/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    success_message = "Categoria Actualizada Satistactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class CategoriaDel(SuccessMessageMixin, SinPrivilegios, generic.DeleteView):
    permission_required = "invapp.delete_categoria"
    model = Categoria
    template_name = "invapp/categoria_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:categoria_list")
    success_message = "Categoria Eliminada Satistactoriamente"
   

class SubCategoriaView(SinPrivilegios, generic.ListView):
    permission_required = "invapp.view_subcategoria"
    model = SubCategoria
    template_name = "invapp/subcategoria_list.html"
    context_object_name = "obj"
    

class SubCategoriaNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = SubCategoria
    template_name = "invapp/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    success_message = "Sub categoria Creada Satistactoriamente"
    permission_required = "invapp.add_subcategoria"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class SubCategoriaEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = SubCategoria
    template_name = "invapp/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    success_message = "Sub categoria Actualizada Satistactoriamente"
    permission_required = "invapp.change_subcategoria"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class SubCategoriaDel(SuccessMessageMixin, SinPrivilegios, generic.DeleteView):
    model = SubCategoria
    template_name = "invapp/categoria_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:subcategoria_list")
    success_message = "Sub Categoria Eliminada Satistactoriamente"
    permission_required = "invapp.delete_subcategoria"


class MarcaView(SinPrivilegios, generic.ListView):
    permission_required = "invapp.view_marca"
    model = Marca
    template_name = "invapp/marca_list.html"
    context_object_name = "obj"


class MarcaNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = Marca
    template_name = "invapp/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    success_message = "Marca Creada Satistactoriamente"
    permission_required = "invapp.add_marca"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class MarcaEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Marca
    template_name = "invapp/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    success_message = "Marca Modificada Satistactoriamente"
    permission_required = "invapp.change_marca"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('invapp.change_marca', login_url='base:sin_privilegios')
# vista basada en funcion
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto ={}
    template_name ="invapp/categoria_del.html"

    if not marca:
        return redirect("inv:marca_list")

    if request.method=='GET':
        contexto={'obj':marca}

    if request.method == 'POST':
        marca.estado = False
        marca.save()
        messages.success(request, 'Marca Inactivada')
        return redirect("inv:marca_list")

    return render(request, template_name, contexto)


class UMView(SinPrivilegios, generic.ListView):
    permission_required = "invapp.view_unidadmedida"
    model = UnidadMedida
    template_name = "invapp/um_list.html"
    context_object_name = "obj"
    

class UMNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = UnidadMedida
    template_name = "invapp/um_form.html"
    context_object_name = "obj"
    form_class = UMForm
    success_url = reverse_lazy("inv:um_list")
    success_message = "Unidad de Medida Creada Satistactoriamente"
    permission_required = "invapp.add_unidadmedida"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class UMEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = UnidadMedida
    template_name = "invapp/um_form.html"
    context_object_name = "obj"
    form_class = UMForm
    success_url = reverse_lazy("inv:um_list")
    success_message = "Unidad de Medida Modificada Satistactoriamente"
    permission_required = "invapp.change_unidadmedida"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)


@login_required(login_url="/login/")
@permission_required("invapp.change_unidadmedida", login_url="/login/")
# vista basada en funcion
def um_inactivar(request, id):
    um = UnidadMedida.objects.filter(pk=id).first()
    contexto = {}
    template_name = "invapp/categoria_del.html"

    if not um:
        return redirect("inv:um_list")

    if request.method == 'GET':
        contexto = {'obj': um}

    if request.method == 'POST':
        um.estado = False
        um.save()
        return redirect("inv:um_list")

    return render(request, template_name, contexto)


class ProductoView(SinPrivilegios, generic.ListView):
    model = Producto
    template_name = "invapp/producto_list.html"
    context_object_name = "obj"
    permission_required = "invapp.view_producto"


class ProductoNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = Producto
    template_name = "invapp/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    success_message = "Producto Creada Satistactoriamente"
    permission_required = "invapp.add_producto"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductoNew, self).get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["subcategorias"] = SubCategoria.objects.all()
        return context
    


class ProductoEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Producto
    template_name = "invapp/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    success_message = "Producto Modificado Satistactoriamente"
    permission_required = "invapp.change_producto"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super(ProductoEdit, self).get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["subcategorias"] = SubCategoria.objects.all()
        context["obj"] = Producto.objects.filter(pk=pk).first()
        return context


@login_required(login_url="/login/")
@permission_required("invapp.change_producto", login_url="/login/")
def producto_inactivar(request, id):
    prod = Producto.objects.filter(pk=id).first()
    contexto = {}
    template_name = "invapp/categoria_del.html"

    if not prod:
        return redirect("inv:producto_list")

    if request.method == 'GET':
        contexto = {'obj': prod}

    if request.method == 'POST':
        prod.estado = False
        prod.save()
        return redirect("inv:producto_list")

    return render(request, template_name, contexto)
    


