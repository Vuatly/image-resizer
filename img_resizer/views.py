from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import FormMixin

from .forms import ImageCreateForm, ImageEditForm
from .models import Image
from .utils import resize_image, get_image_from_link


class ImageListView(ListView):
    """Сервис, возвращающий список загруженных изображений"""
    model = Image
    template_name = 'img_resizer/img_list.html'


class ImageCreateView(CreateView):
    """Сервис, позволяющий загружать изображение"""
    model = Image
    form_class = ImageCreateForm
    template_name = 'img_resizer/img_create.html'

    def form_valid(self, form):
        img_obj = form.save(commit=False)
        if form.cleaned_data['link']:
            try:
                img_obj.file = get_image_from_link(form.cleaned_data['link'])
            except Exception as e:
                return render(self.request, self.template_name, {'form': form,
                                                                 'error': str(e)})
        img_obj.save()
        return HttpResponseRedirect(reverse_lazy('img_resizer:img_detail',
                                                 kwargs={'pk': img_obj.pk}))


class ImageDetailView(FormMixin, DetailView):
    model = Image
    template_name = 'img_resizer/img_detail.html'
    form_class = ImageEditForm

    def get_context_data(self, **kwargs):
        context = super(ImageDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            try:
                resize_image(self.object.pk, form.cleaned_data['width'],
                             form.cleaned_data['height'])
                return HttpResponseRedirect(self.request.path_info)
            except Exception as e:
                return render(request, self.template_name, {'error': str(e)})
        return self.form_invalid(form)
