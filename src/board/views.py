from django.shortcuts import render,get_object_or_404,redirect,get_list_or_404
from .models import Board,Slide_Advertising,Topic,Topic_Advertising,Up_img
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone
from .forms import Creat_form
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin


# # عرض صفحة المواضيع
# def base(request,id):
#     topic = get_object_or_404(Topic, pk=id)
#     # boards = Board.objects.all()
#     Topic_Advs = Topic_Advertising.objects.all()
#     topics_list = Topic.objects.filter(created_by=topic.created_by.id)
#
#     context = {
#         # 'title':'قرية المصممين | الرئيسية',
#         # 'a_boards':boards,
#         'Topic_Advs':Topic_Advs,
#         'topics_list': topics_list
#     }
#     return render(request,'base.html',context)



# # عرض صفحة المواضيع
def boards_topic(request, id):
    Slide_Advs = Slide_Advertising.objects.all()
    Topic_Advs = Topic_Advertising.objects.all()

    a_boards = Board.objects.filter(active=True)
    board = get_object_or_404(Board, pk=id)
    board_list = board.topics.filter(active=True)

    query = request.GET.get('q')
    if query:
        board_list = board_list.filter(
            Q(title__icontains=query) |
            Q(board__name__icontains=query) |
            Q(created_by__first_name__icontains=query) |
            Q(created_by__last_name__icontains=query)
        ).distinct()

    paginator = Paginator(board_list, 10)
    page = request.GET.get('page')
    try:
        board_list = paginator.page(page)
    except PageNotAnInteger:
        board_list = paginator.page(1)

    except EmptyPage:
        board_list = paginator.page(Paginator.num_page)

    context = {

        'board':board,
        'board_list': board_list,
        'page': page,


        'a_boards': a_boards,
        'Slide_Advs':Slide_Advs,
        'Topic_Advs':Topic_Advs,
    }

    return render(request, 'topics.html',context)



# def Board_list(request):
#     board= Board.objects.order_by('id')
#     topics = Topic.objects.filter('board')
#
#     paginator = Paginator(topics, 3)
#     page = request.GET.get('page')
#
#     page = paginator.get_page(page)
#     try:
#         topics = paginator.page(page)
#     except PageNotAnInteger:
#         topics = paginator.page(1)
#
#     except EmptyPage:
#         topics = paginator.page(Paginator.num_pages)
#
#     context = {
#         'board': board,
#         'topics': topics,
#         'page': page,
#     }
#
#     return render(request, 'board_list.html', context)













#صفحة جميع الاعمال
def top_list(request):
    Slide_Advs = Slide_Advertising.objects.all()
    Topic_Advs = Topic_Advertising.objects.all()

    a_boards=Board.objects.filter(active=True)
    topics = Topic.objects.filter(active=True)

    query=request.GET.get('q')
    if query :
        topics=topics.filter(
            Q(title__icontains=query)|
            Q(board__name__icontains=query)|
            Q(created_by__first_name__icontains=query)|
            Q(created_by__last_name__icontains=query)
             ).distinct()
    paginator = Paginator(topics, 12)
    page = request.GET.get('page')
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)

    except EmptyPage:
        topics = paginator.page(Paginator.num_page)
    context = {
        'page': page,
        'topics':topics,
        'a_boards':a_boards,
        'Slide_Advs': Slide_Advs,
        'Topic_Advs': Topic_Advs,
    }
    return render(request, 'index.html',context)





# لصفحة مواقع الرفع
def Up_imge(request):
    Slide_Advs = Slide_Advertising.objects.all()
    Topic_Advs = Topic_Advertising.objects.all()
    a_boards = Board.objects.filter(active=True)
    up_images=Up_img.objects.all()
    context={
        'Slide_Advs': Slide_Advs,
        'a_boards': a_boards,
        'Topic_Advs': Topic_Advs,
        'up_images': up_images,
    }

    return render(request, 'up_imge.html',context)


# لاظهار تفاصيل العمل
def topic_detail(request, id,**kwargs):
    topic = get_object_or_404(Topic, pk=id)
    topics = Topic.objects.filter(created_by=topic.created_by.id)
    topics_list = Topic.objects.filter(created_by=topic.created_by.id)
    a_boards = Board.objects.filter(active=True)

    paginator = Paginator(topics_list, 12)
    page = request.GET.get('page')
    try:
        topics_list = paginator.page(page)
    except PageNotAnInteger:
        topics_list = paginator.page(1)

    except EmptyPage:
        topics_list = paginator.page(Paginator.num_page)

    context = {
        'title': topic,
        'topic':topic,
        'a_boards': a_boards,
        'topics': topics,
        'topics_list':topics_list,
        'page': page,
     }

    return render(request, 'detail.html', context)



#لعرض جميع أعمال المصمم
def designer_works(request, id,**kwargs):
    topic = get_object_or_404(Topic, pk=id)
    topics = Topic.objects.filter(created_by=topic.created_by.id)
    topics_list = Topic.objects.filter(created_by=topic.created_by.id)
    a_boards = Board.objects.filter(active=True)
    title1=topic.created_by

    paginator = Paginator(topics_list, 8)
    page = request.GET.get('page')
    try:
        topics_list = paginator.page(page)
    except PageNotAnInteger:
        topics_list = paginator.page(1)

    except EmptyPage:
        topics_list = paginator.page(Paginator.num_page)
    context = {
        'title': title1,
        'a_boards': a_boards,
        'posts': topics,
        'topics_list': topics_list,
        'page': page,

     }

    return render(request, 'user_topics.html', context)







#--------------------------------------------------------------------------------------------------


# لانشاء موضوع جديد


class TopicCreate(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Topic
    template_name = 'topic_form.html'
    fields = ['title','img_url','board']
    success_message=( 'تم انشاء الموضوع بنجاح')
    # success_url = '/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    # لتحديث الموضوع
class TopicUpdate(UserPassesTestMixin, LoginRequiredMixin,SuccessMessageMixin, UpdateView):

    model = Topic
    template_name = 'update.html'
    success_message=('تم تحديث الموضوع بنجاح')

    fields = ['title', 'img_url', 'board']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        topic = self.get_object()
        if self.request.user == topic.created_by:
            return True
        else:
            return False


# لحذف الموضوع
class TopicDelete(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Topic
    template_name = 'topic_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        topic = self.get_object()
        if self.request.user == topic.created_by:
            return True
        else:
            return False

