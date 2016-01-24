# from django.template import RequestContext, loader
# from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# 视图反映基本的Web开发中的一个常见情况：
# 根据URL中的参数从数据库中获取数据、载入模板文件然后返回渲染后的模板。
# 由于这种情况特别常见，Django提供一种快捷方式，叫做“通用视图”系统。
# 通用视图将常见的模式抽象化，可以使你在编写应用时甚至不需要编写Python代码。

# 一般来说，当编写一个Django应用时，你应该先评估一下通用视图是否可以解决你的问题，
# 你应该在一开始使用它，而不是进行到一半时重构代码。
from django.views import generic

from .models import Question, Choice


# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     # content = RequestContext(request, {
#     #     'latest_question_list': latest_question_list,
#     # })
#     # return HttpResponse(template.render(content))
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)


# get_list_or_404()函数，它的工作方式类似get_object_or_404()
# 差别在于它使用filter()而不是get()。如果列表为空则引发Http404。
# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404('Question does not exist.')
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# 这里使用两个通用视图：ListView 和 DetailView。
# 这两个视图分别抽象“显示一个对象列表”和“显示一个特定类型对象的详细信息页面”这两种概念。
class IndexView(generic.ListView):
    # template_name属性是用来告诉Django使用一个指定的模板名字，而不是自动生成的默认名字。
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    # 每个通用视图需要知道它将作用于哪个模型。 这由model 属性提供。
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoseNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 该在成功处理POST数据后总是返回一个HttpResponseRedirect。
        # 这不是Django的特定技巧； 这是那些优秀网站在开发实践中形成的共识。
        # 在HttpResponseRedirect的构造函数中使用reverse()函数。
        # 这个函数避免了我们在视图函数中硬编码URL
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


