from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, ArchiveIndexView, CreateView, UpdateView, DeleteView

from .forms import ReservedRoomForm
from .models import ReservedRoom


class ReservedRoomCreateView(LoginRequiredMixin, CreateView):
    model = ReservedRoom
    form_class = ReservedRoomForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        messages.success(self.request, '예약을 저장했습니다.')
        return super().form_valid(form)


reserve_new = ReservedRoomCreateView.as_view()


class ReservedRoomListView(ListView):
    model = ReservedRoom
    paginate_by = 10


reservedroom_list = ReservedRoomListView.as_view()


class ReservedRoomDetailView(DetailView):
    model = ReservedRoom
    # queryset = Post.objects.filter(is_public=True)

    def get_queryset(self):  # 오버라이딩: request는 앞단에서 받음
        qs = super().get_queryset()  # 부모 호출로 쿼리셋 먼저 얻기(model.object.all())
        # if not self.request.user.is_authenticated:  # 로그인 안되어 있으면 공개 항목만 봐
        #     qs = qs.filter(is_public=True)
        return qs


reservedroom_detail = ReservedRoomDetailView.as_view()


class ReservedRoomUpdateView(LoginRequiredMixin, UpdateView):
    model = ReservedRoom
    form_class = ReservedRoomForm

    def dispatch(self, request, *args, **kwargs):
        reservedroom = self.get_object()
        if reservedroom.user != request.user:
            messages.error(request, '작성자만 수정할 수 있습니다.')
            return redirect(reservedroom)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, '예약을 수정했습니다.')
        return super().form_valid(form)


reservedroom_edit = ReservedRoomUpdateView.as_view()


class ReservedRoomDeleteView(LoginRequiredMixin, DeleteView):
    model = ReservedRoom
    success_url = reverse_lazy('reserveapp:reservedroom_list')

    def dispatch(self, request, *args, **kwargs):
        reservedroom = self.get_object()
        if reservedroom.user != request.user:
            messages.error(request, '작성자만 삭제할 수 있습니다.')
            return redirect(reservedroom)
        return super().dispatch(request, *args, **kwargs)


reservedroom_delete = ReservedRoomDeleteView.as_view()
