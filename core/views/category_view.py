from django.utils.decorators import method_decoratorfrom django.contrib.auth.decorators import login_requiredfrom django.contrib.messages.views import SuccessMessageMixinfrom django.core.paginator import Paginator, EmptyPage, PageNotAnIntegerfrom django.views.generic import CreateView, ListView, UpdateView, DeleteViewfrom core.models.category import Categoryfrom core.forms.category_form import CategoryForm@method_decorator(login_required(login_url='/login/'), name='dispatch')class CategoryCreateListView(SuccessMessageMixin, CreateView, ListView):    paginate_by = 6    model = Category    success_url = '/category/'    form_class = CategoryForm    context_object_name = 'category'    template_name = 'category/category.html'    success_message = "Category successfully created!"    def get_context_data(self, **kwargs):        context = super(CategoryCreateListView, self).get_context_data(**kwargs)        category = self.get_queryset()        page = self.request.GET.get('page')        paginator = Paginator(category, self.paginate_by)        try:            category = paginator.page(page)        except PageNotAnInteger:            category = paginator.page(1)        except EmptyPage:            category = paginator.page(paginator.num_pages)        context['category'] = category        return context        # return dict(        #     super(CreateCategory, self).get_context_data(**kwargs),        #     category=self.model.objects.all().order_by('-id')        # )@method_decorator(login_required(login_url='/login/'), name='dispatch')class CategoryUpdate(SuccessMessageMixin, UpdateView):    model = Category    form_class = CategoryForm    success_url = '/category/'    template_name = 'category/update_category.html'    success_message = "Category successfully updated!"@method_decorator(login_required(login_url='/login/'), name='dispatch')class CategoryDelete(DeleteView):    model = Category    success_url = '/category/'    template_name = 'category/category_confirm_delete.html'