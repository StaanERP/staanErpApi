import graphene
import itemmaster.schema
import itemmaster.mutations.Item_master_mutations


class Query(itemmaster.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(itemmaster.mutations.Item_master_mutations.Mutation , graphene.ObjectType):
    pass



schema = graphene.Schema(query=Query, mutation=Mutation)
