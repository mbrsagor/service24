from django.shortcuts import render, redirect, get_object_or_404from django.contrib import messagesfrom django.http import JsonResponse# from django.contrib.auth.mixins import PermissionRequiredMixinfrom django.contrib.auth.decorators import login_required, permission_required, user_passes_test# paginationfrom django.core.paginator import EmptyPage, PageNotAnInteger, Paginatorfrom core.forms.category_form import CategoryFormfrom core.models.category import Categorydef category(request):    category_obj = Category.objects.all().order_by('-id')    # pagination    paginator = Paginator(category_obj, 4)    page = request.GET.get('page')    category_obj = paginator.get_page(page)    form = CategoryForm()    # Search query    search_query = request.GET.get('category_obj')    if search_query:        category_obj = category_obj.filter(name__icontains=search_query)    context = {        'category_obj': category_obj,        'form': form    }    template_name = 'category/category.html'    return render(request, template_name)