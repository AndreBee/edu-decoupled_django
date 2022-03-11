from ariadne import load_schema_from_path, gql, make_executable_schema
from ariadne import ObjectType, MutationType
from ariadne.utils import convert_kwargs_to_snake_case
from pathlib import Path
from user.models import User
from billing.models import Invoice, ItemLine

BASE_DIR = Path(__file__).resolve().parent

schema_file = load_schema_from_path(BASE_DIR / "schema.graphql")
type_defs = gql(schema_file)

query = ObjectType("Query")

# adding a resolver, a callable in charge
# of querying a DB. It is the bridge between
# the public API and the DB.
@query.field("getClients")
def resolve_clients(obj, info):
    return User.objects.all()

@query.field("getClient")
def resolve_client(obj, info, id):
    return User.objects.get(id=id)

mutation = MutationType()

@mutation.field("invoiceCreate")
@convert_kwargs_to_snake_case
def resolve_invoice_create(obj, info, invoice):
    user_id = invoice.pop('user')
    items = invoice.pop('items')

    invoice = Invoice.objects.create(user_id=user_id, **invoice)

    for item in items:
        ItemLine.objects.create(invoice=invoice, **item)
    
    return invoice

schema = make_executable_schema(type_defs, query, mutation)