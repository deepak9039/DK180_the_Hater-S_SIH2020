from django.shortcuts import render,HttpResponse,redirect

# # Create your views here.
from django.db.models import Q
from django.shortcuts import get_object_or_404
# # from rest_framework import generics, permissions, status
# # from rest_framework.response import Response
from quiz.models import Answer, Question, Quiz, QuizTaker, UsersAnswer
from django.views import generic
# # from quiz.serializers import MyQuizListSerializer, QuizDetailSerializer, QuizListSerializer, QuizResultSerializer, UsersAnswerSerializer
from account.views import is_company


class MyQuizList(generic.ListView):
    model = Quiz
    queryset = Quiz.objects.all()
    context_object_name = 'quiz_list'   
    template_name = "quiz.html"  
    
    def get_queryset(self, *args, **kwargs):
        queryset = Quiz.objects.filter(quiztaker__user=self.request.user)
        user = self.request.user
        if is_company(user):
            return HttpResponse("Invalid User !!")
        else:
            query = user.profile.skill
            intrest = user.profile.intrest
            queryset = queryset.filter(
				Q(name__icontains=query) |
				Q(description__icontains=query) |
				Q(name__icontains=intrest) |
				Q(description__icontains=intrest) 
			).distinct()
            return queryset
class QuizDetail(generic.DetailView):
    model = Quiz
    template_name = "quiz_detail.html"
    slug_url_kwarg = 'slug'
    context_object_name = 'quiz' 
    
    def get_context_data(self, **kwargs):
        slug = self.kwargs["slug"]
        quiz = get_object_or_404(Quiz, slug=slug)
        last_question = None
        obj, created = QuizTaker.objects.get_or_create(user=self.request.user, quiz=quiz)
        # print(quiz,"adsjiofsjgifodgjioj")
        if created:
            # print("YES!!!")
            for question in Question.objects.filter(quiz=quiz):
                UsersAnswer.objects.create(quiz_taker=obj, question=question)
        
        kwargs["quiztaker"] = obj
        # print(kwargs)
        return super().get_context_data(**kwargs)
 

def saveUserAnswer(request):
    if request.method == "POST":
        data = request.POST.get("allData",None)
        quiztaker_id = request.POST.get("quizTaker",None)
        data = eval(data)

        if data != {} and quiztaker_id is not None:
            quiztaker = get_object_or_404(QuizTaker, id=quiztaker_id)
            
            if quiztaker.completed:
                return HttpResponse("This quiz is already complete. you can't answer any more questions")

            for question_id,answer_id in data.items():
                question = get_object_or_404(Question, id=question_id)
                answer = get_object_or_404(Answer, id=answer_id)
                
                obj = get_object_or_404(UsersAnswer, quiz_taker=quiztaker, question=question)
                obj.answer = answer
                obj.save()
                # print(obj,question,answer,"models") #done
            quiztaker.completed = True
            correct_answers = 0
            
            for users_answer in UsersAnswer.objects.filter(quiz_taker=quiztaker):
                answer = Answer.objects.get(question=users_answer.question, is_correct=True)
                print("Right_ans",answer)
                print("Your ANS",users_answer.answer)
                if users_answer.answer == answer:
                    correct_answers += 1
                    
            quiztaker.score = int(correct_answers / quiztaker.quiz.question_set.count() * 100)
            print(quiztaker.score)
            quiztaker.save()

            return redirect("result",quiztaker.quiz.slug)

        else:
            return render(request,"result.html")

    else:
        return HttpResponse("Plese select Options")

def  show_result(request,slug):
    quiz = get_object_or_404(Quiz, slug=slug)
    obj, created = QuizTaker.objects.get_or_create(user=request.user, quiz=quiz)
    # if created:
    print(obj.score)
    mark = obj.score
    if mark >= 50 :
        is_pass = True
    else : 
        is_pass = False
    return render(request,"result.html",{
            "quiz_taker" : obj,
            "is_pass" : is_pass
        })
def instruction(request):
    slug = request.GET.get("quiz",None)
    if slug:
        return render(request,"instruction.html",{"slug":slug})
    return HttpResponse("Invalid Exam Selection <b>Go Back</b>!! ")
# class SubmitQuizAPI(generics.GenericAPIView):
# 	serializer_class = QuizResultSerializer
# 	permission_classes = [
# 		permissions.IsAuthenticated
# 	]

# 	def post(self, request, *args, **kwargs):
# 		quiztaker_id = request.data['quiztaker']
# 		question_id = request.data['question']
# 		answer_id = request.data['answer']

# 		quiztaker = get_object_or_404(QuizTaker, id=quiztaker_id)
# 		question = get_object_or_404(Question, id=question_id)

# 		quiz = Quiz.objects.get(slug=self.kwargs['slug'])

# 		if quiztaker.completed:
# 			return Response({
# 				"message": "This quiz is already complete. You can't submit again"},
# 				status=status.HTTP_412_PRECONDITION_FAILED
# 			)

# 		if answer_id is not None:
# 			answer = get_object_or_404(Answer, id=answer_id)
# 			obj = get_object_or_404(UsersAnswer, quiz_taker=quiztaker, question=question)
# 			obj.answer = answer
# 			obj.save()

# 		quiztaker.completed = True
# 		correct_answers = 0

# 		for users_answer in UsersAnswer.objects.filter(quiz_taker=quiztaker):
# 			answer = Answer.objects.get(question=users_answer.question, is_correct=True)
# 			print(answer)
# 			print(users_answer.answer)
# 			if users_answer.answer == answer:
# 				correct_answers += 1

# 		quiztaker.score = int(correct_answers / quiztaker.quiz.question_set.count() * 100)
# 		print(quiztaker.score)
# 		quiztaker.save()

# 		return Response(self.get_serializer(quiz).data)



