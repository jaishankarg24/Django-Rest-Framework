from rest_framework import serializers

class EmployeeSerializers(serializers.Serializer):
	eno = serializers.IntegerField()
	ename = serializers.CharField(max_length=50)
	esalary = serializers.IntegerField()
	eaddress = serializers.CharField(max_length=50)