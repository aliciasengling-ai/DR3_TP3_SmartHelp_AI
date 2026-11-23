import unittest
from ferramentas import consultar_planos, diagnosticar_conexao


class TestFerramentas(unittest.TestCase):
    def test_planos(self):
        self.assertIn('99,90', consultar_planos.invoke({}))

    def test_lentidao(self):
        self.assertIn('cabo', diagnosticar_conexao.invoke({'sintoma': 'internet lenta'}))

    def test_queda(self):
        self.assertIn('roteador', diagnosticar_conexao.invoke({'sintoma': 'sem internet'}))


if __name__ == '__main__':
    unittest.main()
