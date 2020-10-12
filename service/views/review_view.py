from django.views.generic import CreateView, ListViewfrom django.contrib.auth.decorators import login_requiredfrom django.utils.decorators import method_decoratorfrom django.contrib.messages.views import SuccessMessageMixinfrom service.forms.review_form import ReviewFormfrom service.models.review import Review@method_decorator(login_required(login_url='/login/'), name='dispatch')class ReviewCreate(SuccessMessageMixin, CreateView):    model = Review    form_class = ReviewForm    template_name = 'review/add_review.html'    success_url = '/dashboard/'    success_message = "Review has been successfully created!"