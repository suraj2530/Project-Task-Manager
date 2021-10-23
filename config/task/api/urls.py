from django.urls import path

from .views import ( ProjectDetail, ProjectList, TaskList, TaskDetail,
                    CommentList, CommentDetail, ReminderDetail, ReminderList) 

urlpatterns = [
  path('project/', ProjectList.as_view() ), 
  path('project/<int:pk>/', ProjectDetail.as_view()),
  
  path('task/', TaskList.as_view()), 
  path('task/<int:pk>/', TaskDetail.as_view()),

  path('comment/', CommentList.as_view()),
  path('comment/<int:pk>/', CommentDetail.as_view),
  

  path('reminder', ReminderList.as_view()),
  path('reminder/<int:pk>/', ReminderDetail.as_view()),




]
