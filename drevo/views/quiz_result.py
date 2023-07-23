from django.core.paginator import Paginator
from django.shortcuts import render
from drevo.models import QuizResult, FriendsInviteTerm, Message
from drevo.models.feed_messages import FeedMessage
from users.models import User, MenuSections
from users.views import access_sections


def show_quiz_result(request,id):
    if request.method == 'GET':
        user = User.objects.filter(id=id).first()
        context = {}
        if user is not None:
            if user == request.user:
                context['sections'] = access_sections(user)
                context['activity'] = [i for i in context['sections'] if i.startswith('Мои') or
                                       i.startswith('Моя')]
                context['link'] = 'users:myprofile'
                invite_count = FriendsInviteTerm.objects.filter(recipient=request.user.id).count()
                context['invite_count'] = invite_count if invite_count else 0
                context['new_knowledge_feed'] = FeedMessage.objects.filter(recipient=user, was_read=False).count()
                context['new_messages'] = Message.objects.filter(recipient=user, was_read=False).count()
                context['new'] = int(context['new_knowledge_feed']) + int(
                    context['invite_count'] + int(context['new_messages']))
            else:
                context['sections'] = [i.name for i in user.sections.all()]
                context['activity'] = [i.name for i in user.sections.all() if
                                       i.name.startswith('Мои') or i.name.startswith('Моя')]
                context['link'] = 'public_human'
                context['id'] = id
            context['pub_user'] = user
            all_results = QuizResult.objects.filter(user=user)
            if quiz_for_search := request.GET.get('quiz_for_search'):
                all_results = all_results.filter(quiz__name__icontains=quiz_for_search)
                context['filter'] = 1
            all_quizzes_name = all_results.values_list("quiz__name", flat=True).distinct()
            quiz_results = []
            for quizzes in all_quizzes_name:
                questions_and_answers = {}
                all_questions_name = all_results.filter(quiz__name=quizzes).values_list("question__name", flat=True) \
                    .distinct().order_by('-question__order')
                for questions in all_questions_name:
                    questions_and_answers[questions] = all_results.filter(question__name=questions, quiz__name=quizzes) \
                        .values_list("answer__name", "answer__related__tr__name").order_by('-answer__order')
                date = str(all_results.filter(quiz__name=quizzes).values_list("date_time__day", "date_time__month",
                                                                              "date_time__year").first()).rstrip(')'). \
                    lstrip('(').replace(' ', '')
                for_link = all_results.filter(quiz__name=quizzes).values_list("quiz__pk", flat=True).first()
                quiz_results.append((f'{quizzes} {date.replace(",", ".")} {str(for_link)}',questions_and_answers))
            context['quiz_result'] = quiz_results
            page_number = int(request.GET.get('page')) if request.GET.get('page') else 1
            paginator = Paginator(quiz_results, 5)
            context['page_obj'] = paginator.get_page(page_number)
            return render(request, 'drevo/show_quiz_result.html', context)