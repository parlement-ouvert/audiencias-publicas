from django.conf.urls import url
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.routers import DefaultRouter
from apps.core.views import (VideoDetail, RoomQuestionList, ClosedVideos,
                             QuestionDetail, index, redirect_to_room,
                             RoomReportView, set_answer_time, set_answered,
                             set_priotity, WidgetVideoDetail)
from apps.core import api


urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^pergunta/(?P<pk>\d+)/?$', QuestionDetail.as_view(),
        name='question_detail'),
    url(r'^pergunta/(?P<question_id>\d+)/definir_resposta/?$', set_answer_time,
        name='set_question_answer_time'),
    url(r'^pergunta/(?P<question_id>\d+)/respondida/?$', set_answered,
        name='set_question_answered'),
    url(r'^pergunta/(?P<question_id>\d+)/prioritaria/?$', set_priotity,
        name='set_question_priotity'),
    url(r'^sala/(?P<pk>\d+)/?$', VideoDetail.as_view(), name='video_room'),
    url(r'^sala/(?P<pk>\d+)/relatorio/?$', RoomReportView.as_view(),
        name='room_report'),
    url(r'^sala/reuniao/(?P<cod_reunion>\d+)/?$', redirect_to_room,
        name='video_reunion_room'),
    url(r'^sala/(?P<pk>\d+)/perguntas/?$', RoomQuestionList.as_view(),
        name='questions_list'),
    url(r'^fechadas/?$', ClosedVideos.as_view(), name='video_list'),
    url(r'^widget/(?P<pk>\d+)/?$',
        ensure_csrf_cookie(WidgetVideoDetail.as_view()),
        name='widget_index'),
]

router = DefaultRouter()
router.register(r'api/user', api.UserViewSet)
router.register(r'api/message', api.MessageViewSet)
router.register(r'api/question', api.QuestionViewSet)
router.register(r'api/room', api.RoomViewSet)
router.register(r'api/vote', api.VoteViewSet)

urlpatterns += router.urls
urlpatterns += [
    url(r'^api/$', api.api_root),
]
