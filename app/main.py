from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema

from app.gql.mutation import Mutation
from app.gql.query import Query
from app.routes.user_route import purchase_bluprint

app = Flask(__name__)
# schema = Schema(query=Query, mutation=Mutation)
# app.add_url_rule(
#     '/graphql',
#     view_func=GraphQLView.as_view(
#         'graphql',
#         schema=schema,
#         graphiql=True
#     )
# )
app.register_blueprint(purchase_bluprint, url_prefix="/api/purchase")
if __name__ == '__main__':
    app.run()
