import graphene
from graphene_django import DjangoObjectType
from .models import Portfolio

class PortfolioType(DjangoObjectType):
    class Meta:
        model= Portfolio
        fields=  '__all__'
        
class Query(graphene.ObjectType):
    profile=graphene.List(PortfolioType)
    
    def resolve_profile(root,info):
        return Portfolio.objects.all()
    
schema= graphene.Schema(query=Query)
