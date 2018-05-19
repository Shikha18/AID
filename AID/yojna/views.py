from django.shortcuts import render
from .models import state,Field,problem,yojna_desc,yojna_problem,problem
from django.http import JsonResponse


def home(request):
	field_obj=Field.objects.all()
	return render(request,'yojna/home.html',{'fields':field_obj})

def field(request,id="1",range="1"):
	states=state.objects.values_list('state_name')
	problems=problem.objects.values_list('problem_name')
	yojna_field_related=problem.objects.filter(related_field=id)
	yojna_display=yojna_problem.objects.filter(problem_id__in=yojna_field_related).order_by('-id')
	loop_time='a'*150
	for yojna in yojna_display:
		print(yojna.yojna_id.name)
	context={
		'states':states,
		'problems':problems,
		'loop_times':loop_time,
		'yojnas':yojna_display
	}
	return render(request,'yojna/field.html',context)

def ajax(request):
	age=request.GET.get("age")
	salary=request.GET.get("salary")
	state=request.GET.get("state")
	problem_rec=request.GET.get("problem")
	yojna_prob_filter=[]
	yojna_age_filter=[]
	final={}
	if age!="Select Age" :
		yojna_age_filter=yojna_desc.objects.filter(lower_age__lte=age,upper_age__gte=age).values_list('id')
	if problem_rec!="Select Your Problem":
		yojna_prob_id=problem.objects.get(problem_name=problem_rec)
	if problem_rec!="Select Your Problem" and age!="Select Age":
		yojna_prob_filter=yojna_problem.objects.filter(problem_id=yojna_prob_id).values_list('yojna_id')
		for k in yojna_prob_filter:
			print(k)
			final[k[0]] = yojna_desc.objects.get(pk=k).values_list()
		return JsonResponse(final)
	if age!="Select Age" and problem_rec=="Select Your Problem":
	    print(yojna_age_filter)
	    for k in yojna_age_filter:
	        final[k[0]]=yojna_desc.objects.values_list().get(pk=k[0])
	    print(final)
	    return JsonResponse(final)
	if problem_rec!="Select Your Problem" and age=="Select Age":
		pass
	return JsonResponse({"Heelo":"hii"})
