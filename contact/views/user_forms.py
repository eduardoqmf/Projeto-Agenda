from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from contact.forms import RegisterForm, RegisterUpdateForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('contact:user_login')
    return render(
        request,
        'contact/register.html',
        {
            'form': form,
        }
    )


def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form,
            }
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form,
            }
        )

    form.save()
    messages.success(request, 'Usuário atualizado com sucesso!')
    return redirect('contact:index')


def user_login(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('contact:index')
        else:
            messages.error(request, 'Usuário ou senha inválidos')

    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )


def user_logout(request):
    auth.logout(request)
    return redirect('contact:user_login')
