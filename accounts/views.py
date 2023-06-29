from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView, CreateView, DetailView
from .forms import ProfileForm, CustomUserCreationForm
from .models import Profile

User = get_user_model()


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


profile = ProfileView.as_view()


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile_detail.html'
    # queryset = Post.objects.filter(is_public=True)

    def get_queryset(self):  # 오버라이딩: request는 앞단에서 받음
        qs = super().get_queryset()  # 부모 호출로 쿼리셋 먼저 얻기(model.object.all())
        # if not self.request.user.is_authenticated:  # 로그인 안되어 있으면 공개 항목만 봐
        #     qs = qs.filter(is_public=True)
        return qs


profile_detail = ProfileDetailView.as_view()


@login_required
def profile_edit(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_form.html', {
        'form': form,
    })


# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = profile
#     form_class = ProfileForm
#
#
# profile_edit = ProfileUpdateView.as_view()


class SignupView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = settings.LOGIN_REDIRECT_URL
    template_name = 'accounts/signup_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return response


signup = SignupView.as_view()
