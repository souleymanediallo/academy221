from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.signing import Signer
from django.core.mail import send_mail
from django.urls import reverse
from django.core.signing import Signer, BadSignature
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = user.first_name.capitalize()
            user.last_name = user.last_name.capitalize()
            user.save()

            signer = Signer()
            signed_user_id = signer.sign(user.id)

            confirm_url = request.build_absolute_uri(
                reverse('email_confirm', args=[signed_user_id])
            )
            send_mail(
                'Confirmez votre adresse email',
                f'Cliquez sur ce lien pour confirmer votre adresse email : {confirm_url}',
                'no-reply@academy221.com',
                [user.email],
                fail_silently=False,
            )

            messages.success(request, 'Votre compte a été créé avec succès. Vérifiez votre email pour confirmer votre adresse.')
            return redirect('home')
        else:
            messages.error(request, 'Erreur lors de la création de votre compte. Veuillez réessayer.')

    form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def confirm_email(request, signed_user_id):
    try:
        signer = Signer()
        user_id = signer.unsign(signed_user_id)
        user = CustomUser.objects.get(id=user_id)
        user.email_confirmed = True
        user.save()
        messages.success(request, 'Votre email a été confirmé avec succès.')
        return redirect('home')
    except (BadSignature, CustomUser.DoesNotExist):
        messages.error(request, 'Lien de confirmation invalide.')
        return redirect('home')


def login_user(request):
    if request.method == "POST":
        email = request.POST["email"].lower()
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.email_confirmed:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Veuillez confirmer votre adresse email.")
                return redirect("login")
        else:
            messages.error(request, "Erreur email ou mot de passe")
            return redirect("login")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile_update(request):
    if request.method == "POST":
        u_form = CustomUserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            first_name = u_form.cleaned_data.get("first_name")
            messages.success(request, f"{first_name}, votre compte a été mis à jour")
            return redirect('dashboard')
    else:
        u_form = CustomUserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "accounts/update.html", context)


@login_required
def delete_user(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        logout(request)
        messages.success(request, "Votre compte a été supprimé avec succès.")
        return redirect("home")

    return render(request, "accounts/delete.html")


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
