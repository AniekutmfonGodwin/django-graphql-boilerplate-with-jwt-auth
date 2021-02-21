import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations


# from .models import Quizzes, Category, Question, Answer



class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_set = mutations.PasswordSet.Field() # For passwordless registration
    password_change = mutations.PasswordChange.Field()
    update_account = mutations.UpdateAccount.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    send_secondary_email_activation =  mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()
    remove_secondary_email = mutations.RemoveSecondaryEmail.Field()



# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = Category
#         fields = ("id","name")

# class QuizzesType(DjangoObjectType):
#     class Meta:
#         model = Quizzes
#         fields = ("id","title","category","quiz")

# class QuestionType(DjangoObjectType):
#     class Meta:
#         model = Question
#         fields = ("title","quiz")

# class AnswerType(DjangoObjectType):
#     class Meta:
#         model = Answer
#         fields = ("question","answer_text")




class Mutation(AuthMutation, graphene.ObjectType):
    pass





class Query(UserQuery, MeQuery,graphene.ObjectType):
    pass

    # all_questions = graphene.Field(QuestionType, id=graphene.Int())
    # all_answers = graphene.List(AnswerType, id=graphene.Int())

    # def resolve_all_questions(root, info, id):
    #     return Question.objects.get(pk=id)
    # def resolve_all_answers(root, info, id):
    #     return Answer.objects.filter(question=id)



schema = graphene.Schema(query=Query, mutation=Mutation)


