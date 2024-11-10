import unittest

from lib.utils.inspect import FunctionSignature, inspect_class_attrs, inspect_obj_attrs


class TestFunctionSignature(unittest.TestCase):

    def test_smoke(self):
        _ = FunctionSignature(lambda: None)

    def test_simple(self):
        def foo(x, y=42, z='abc'):
            ...

        signature = FunctionSignature(foo)
        self.assertEqual(signature.func_name, 'foo')
        self.assertEqual(signature.args, ['x'])
        self.assertEqual(signature.kwargs, {'y': 42, 'z': 'abc'})
        self.assertEqual(signature.pos_args, signature.args)
        self.assertEqual(signature.all_args, ['x', 'y', 'z'])
        self.assertTrue(signature.module_name.endswith('tests.test_inspect'))
        self.assertEqual(signature.get_arguments_map(1, y=2, z=3), {'x': 1, 'y': 2, 'z': 3})
        self.assertNotEqual(str(signature), '')


class TestInspectClassAttrs(unittest.TestCase):

    def test_smoke(self):
        _ = inspect_class_attrs(type('classname', (), {}))

    def test_simple(self):
        expected = {'A': 1, 'B': 2}
        mycls = type('MyClass', (), expected)
        result = {name: value for name, value in inspect_class_attrs(mycls)}
        self.assertEqual(expected, result)


class TestInspectObjAttrs(unittest.TestCase):

    def test_smoke(self):
        _ = inspect_obj_attrs(type('classname', (), {})())

    def test_simple(self):
        mycls = type('MyClass', (), {})
        obj = mycls()
        obj.x = 10
        obj.y = 'abc'
        result = list(inspect_obj_attrs(obj))
        self.assertCountEqual(result, ['x', 'y'])
