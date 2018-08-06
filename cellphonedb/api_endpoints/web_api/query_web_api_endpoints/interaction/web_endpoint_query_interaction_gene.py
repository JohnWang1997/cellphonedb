from flask import request, Response

from cellphonedb.app.flask import flask_extensions
from cellphonedb.api_endpoints.web_api.web_api_endpoint_base import WebApiEndpointBase


class WebEndpointQueryInteractionGene(WebApiEndpointBase):
    def get(self):
        columns = request.args.get('columns')

        columns = columns.split(',') if columns else None

        genes = flask_extensions.cellphonedb_flask.cellphonedb.query.get_interaction_gene(columns)
        genes = genes.to_json(orient='records')

        response = Response(genes, content_type='application/json')

        return response
