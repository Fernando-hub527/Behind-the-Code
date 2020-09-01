from sklearn.base import BaseEstimator, TransformerMixin


class QualityAluno(BaseEstimator, TransformerMixin):
        def fit(self, X, y=None):
                return self

        def transform(self, X):
                data = X.copy()
                N = ['NOTA_DE', 'NOTA_EM', 'NOTA_MF', 'NOTA_GO']
                R = ['REPROVACOES_DE', 'REPROVACOES_EM', 'REPROVACOES_MF', 'REPROVACOES_GO']
                Q = ['QUALITY_DE', 'QUALITY_EM', 'QUALITY_MF', 'QUALITY_GO']

                for i in range(4):
                        data[Q[i]] = pd.DataFrame((data[N[i]] - data[R[i]])*2).values

                return data
