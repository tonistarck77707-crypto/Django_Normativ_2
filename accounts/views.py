from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import RegisterForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()


            group, created = Group.objects.get_or_create(name="User")
            user.groups.add(group)

            return redirect("login")

    else:
        form = RegisterForm()

    context = {
        "form": form
    }

    return render(request, "accounts/register.html", context)