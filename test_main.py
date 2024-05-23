import unittest
from fastapi.testclient import TestClient
from main import app
from api import router as api_router

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_read_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "¡Desafío Musache!"})

    def test_ask_question_endpoint(self):
        data = {"question": "¿Cuál es la respuesta a la vida, el universo y todo lo demás?"}
        response = self.client.post("/ask", json=data)
        self.assertEqual(response.status_code, 200)
        # Asegúrate de agregar más pruebas según el comportamiento esperado de tu aplicación

if __name__ == "__main__":
    unittest.main()
