from rest_framework import serializers
from .models import CustomUser, MedicalHistoryDocument

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'role', 'password', 'first_name', 'last_name', 'age', 'gender', 'phone_number', 'medical_history')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username'],
            role=validated_data['role'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            age=validated_data.get('age', None),
            gender=validated_data.get('gender', ''),
            phone_number=validated_data.get('phone_number', ''),
            medical_history=validated_data.get('medical_history', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
class PatientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'age', 'gender', 'phone_number', 'medical_history')
class MedicalHistoryDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistoryDocument
        fields = ['id', 'document', 'uploaded_at']

class PatientUpdateSerializer(serializers.ModelSerializer):
    new_medical_documents = serializers.ListField(
        child=serializers.FileField(allow_empty_file=True, required=False),
        write_only=True,
        required=False
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'age', 'gender', 'phone_number', 'medical_history', 'new_medical_documents']

    def update(self, instance, validated_data):
        new_medical_documents = validated_data.pop('new_medical_documents', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        for document in new_medical_documents:
            MedicalHistoryDocument.objects.create(user=instance, document=document)

        return instance
