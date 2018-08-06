from cellphonedb.app.app_logger import app_logger
from cellphonedb.app.flask.flask_extensions import cellphonedb_flask


class FlaskLocalQueryLauncher:
    def __getattribute__(self, name):
        method = object.__getattribute__(self, name)
        if hasattr(method, '__call__'):
            app_logger.info('Launching Query {}'.format(name))

        return method

    @staticmethod
    def find_interactions_by_element(element: str) -> None:
        print(cellphonedb_flask.cellphonedb.query.find_interactions_by_element(element).to_csv(index=False))

    @staticmethod
    def get_interaction_gene(columns: str) -> None:
        if columns:
            columns = columns.split(',')

        print(cellphonedb_flask.cellphonedb.query.get_interaction_gene(columns).to_csv(index=False))
