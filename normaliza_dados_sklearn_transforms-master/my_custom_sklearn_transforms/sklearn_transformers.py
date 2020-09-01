from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import QuantileTransformer


class NormalizaDaos(BaseEstimator, TransformerMixin):

        def fit(self, X, y=None):
                return self

        def transform(self, X):
                data = X.copy()

	return QuantileTransformer().fit_transform(data[['REPROVACOES_DE', 'REPROVACOES_EM', 'REPROVACOES_MF', 'REPROVACOES_GO','NOTA_DE', 'NOTA_EM', 'NOTA_MF', 'NOTA_GO', 'H_AULA_PRES','FALTAS', 'QUALITY_DE', 'QUALITY_EM','QUALITY_MF', 'QUALITY_GO']])
