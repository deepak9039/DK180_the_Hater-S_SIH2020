from django.urls import path, re_path
# from views import MyQuizListAPI, QuizListAPI, QuizDetailAPI, SaveUsersAnswer, SubmitQuizAPI
from . import views

urlpatterns = [
	path("", views.MyQuizList.as_view(),name="myQuizList"),
	path("quize/<slug>/", views.QuizDetail.as_view(),name="quizDetail"),
	path("save-answer/", views.saveUserAnswer,name= "saveUserAnswer"),
	path("result/<slug>/", views.show_result,name="result"),
	path("instruction/", views.instruction,name= "instruction"),
	# re_path(r"quizzes/(?P<slug>[\w\-]+)/$", QuizDetailAPI.as_view()),
	# re_path(r"quizzes/(?P<slug>[\w\-]+)/submit/$", SubmitQuizAPI.as_view()),
]