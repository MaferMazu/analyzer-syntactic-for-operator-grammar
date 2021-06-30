import unittest

from analyzer import Analyzer

_SUCCESS = 0
_ERROR = 1


class TestAnalyzer(unittest.TestCase):
    def test_creation(self):
        analyzer = Analyzer()
        self.assertTrue(isinstance(analyzer, Analyzer))

    def test_add_rule(self):
        analyzer = Analyzer()
        response = analyzer.add_rule(['E','n'])
        self.assertEqual(response, _SUCCESS)

    def test_add_rule_fail(self):
        analyzer = Analyzer()
        response = analyzer.add_rule(['E', 'E', 'E'])
        self.assertEqual(response, _ERROR)

    def test_add_rule_fail_2(self):
        analyzer = Analyzer()
        response = analyzer.add_rule(['e', 'E', 'E'])
        self.assertEqual(response, _ERROR)

    def test_set_init(self):
        analyzer = Analyzer()
        analyzer.add_rule(['E', 'n'])
        response = analyzer.set_init('E')
        self.assertEqual(response, _SUCCESS)

    def test_set_init_fail(self):
        analyzer = Analyzer()
        analyzer.add_rule(['F', 'n'])
        response = analyzer.set_init('E')
        self.assertEqual(response, _ERROR)

    def test_precedence_base(self):
        analyzer = Analyzer()
        analyzer.add_precedence(['a', '>', 'b'])
        analyzer.build()
        self.assertEqual(analyzer.f['a'], 1)
        self.assertEqual(analyzer.f['b'], 0)

    def test_precedence_with_two(self):
        analyzer = Analyzer()
        analyzer.add_precedence(['a', '>', 'b'])
        analyzer.add_precedence(['b', '>', 'c'])
        analyzer.build()
        self.assertEqual(analyzer.f['a'], 1)
        self.assertEqual(analyzer.f['b'], 1)

    def test_precedence_with_equal(self):
        analyzer1 = Analyzer()
        analyzer1.add_precedence(['(', '=', ')'])
        analyzer1.add_precedence(['n', '>', '('])
        analyzer1.add_precedence(['$', '<', '('])
        analyzer1.build()
        self.assertEqual(analyzer1.f['n'], 1)
        self.assertEqual(analyzer1.f['('], 1)




