import graphene
from graphene_django import DjangoObjectType
from .models import UserProfile,Skill,Project

class UserProfileType(DjangoObjectType):
    class Meta:
        model= UserProfile
        fields=  '__all__'
        
class SkillType(DjangoObjectType):
    class Meta:
        model = Skill
        fields = "__all__"


class ProjectType(DjangoObjectType):
    class Meta:
        model= Project
        fields= "__all__"        
        
        
class Query(graphene.ObjectType):
    profile=graphene.Field(UserProfileType, id=graphene.Int())
    # skill=graphene.List(SkillType)
    
    def resolve_profile(root,info,id):
        return UserProfile.objects.get(pk=id)
    
    # def resolve_skill(root,info):
    #     return Skill.objects.all()
    
schema= graphene.Schema(query=Query)
