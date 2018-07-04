import pandas as pd
from flask import request, Response

from cellphonedb import extensions
from cellphonedb.api_endpoints.endpoint_base import EndpointBase

# curl -i \
#     -F "counts_file=@in/example_data/test_counts.txt;type=text/tab-separated-values" \
#     -F "meta_file=@in/example_data/test_meta.txt;type=text/tab-separated-values" \
#     http://127.0.0.1:5000/api/cell_to_cluster
from utils import utils


class CellToCluster(EndpointBase):
    def post(self):

        counts = utils.read_data_from_content_type(request.files['counts_file'], index_column_first=True)
        meta = utils.read_data_from_content_type(request.files['meta_file'], index_column_first=True)

        if not isinstance(counts, pd.DataFrame):
            self.attach_error(
                {'code': 'parsing_error', 'title': 'Error parsing counts file', 'detail': 'Error parsing counts file'})

        if not isinstance(meta, pd.DataFrame):
            self.attach_error(
                {'code': 'parsing_error', 'title': 'Error parsing meta file', 'detail': 'Error parsing meta file'})

        if not self._errors:
            result_df = extensions.cellphonedb_flask.cellphonedb.query.cells_to_clusters(meta, counts)

            self._attach_csv(result_df.to_csv(), 'cluster_counts.csv')

        self._commit_attachments()

        return Response(self._msg.as_string(), mimetype='multipart/form-data; boundary="%s"' % self._msg.get_boundary())
