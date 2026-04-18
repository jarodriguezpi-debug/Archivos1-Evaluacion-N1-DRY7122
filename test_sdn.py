import unittest
import requests

def get_device_data(device_id):
    url = f"https://jsonplaceholder.typicode.com/users/{device_id}"
    response = requests.get(url)
    return response.json()

class TestSDNMonitoring(unittest.TestCase):
    def test_tipo_dato(self):
        data = get_device_data(1)
        self.assertIsInstance(data, dict)

    def test_integridad_atributos(self):
        data = get_device_data(1)
        self.assertIn('username', data)

    def test_valor_esperado(self):
        data = get_device_data(1)
        self.assertEqual(data['id'], 1)

if __name__ == '__main__':
    unittest.main()
