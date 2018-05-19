from django.db import models

class yojna_desc(models.Model):
	desc=models.TextField(blank=True)
	name=models.CharField(max_length=200)
	lower_age=models.IntegerField(default=-1)
	upper_age=models.IntegerField(default=-1)
	salary_min=models.IntegerField(default=-1)
	salary_max=models.IntegerField(default=-1)

	def __str__(self):
		return self.name

class Field(models.Model):
	field_name=models.CharField(max_length=250)

	def __str__(self):
		return self.field_name


class state(models.Model):
	state_name=models.CharField(max_length=50)

	def __str__(self):
		return self.state_name

class problem(models.Model):
	problem_name=models.CharField(max_length=250)
	related_field=models.ForeignKey(Field,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.problem_name)

class yojna_state(models.Model):
	yojna_id=models.ForeignKey(yojna_desc,on_delete=models.CASCADE)
	state_id=models.ForeignKey(state,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.yojna_id)

class yojna_problem(models.Model):
	yojna_id=models.ForeignKey(yojna_desc,on_delete=models.CASCADE)
	problem_id=models.ForeignKey(problem,on_delete=models.CASCADE)


	def __str__(self):
		return str(self.yojna_id)





