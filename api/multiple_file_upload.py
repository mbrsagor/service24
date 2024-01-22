from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def create_engine_view(request):
    template_name = 'engine/create_engine.html'

    # Engine main form
    if request.method == 'POST' and 'engine_form' in request.POST:
        form = engine_form.EngineGalleryModelForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        if form.is_valid():
            engine = form.save(commit=False)
            engine.save()
            if files:
                for f in files:
                    EngineGallery.objects.create(engine=engine, image=f)
                messages.add_message(request, messages.INFO, "The engine has been created.")
                return redirect('create_engine')
            else:
                messages.add_message(request, messages.ERROR, 'There was an error')
    else:
        form = engine_form.EngineGalleryModelForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)
