import unittest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from main import app
from services.search_service import SearchService
from services.tag_service import TagService
from config.settings import settings


class TestSearchEndpoint(unittest.TestCase):
    """Unit and Integration Tests for the Search Endpoint"""

    def setUp(self):
        self.client = TestClient(app)  # Use `TestClient(app)` correctly here
        self.mock_search_service = MagicMock(SearchService)
        app.dependency_overrides[SearchService] = lambda: self.mock_search_service

    def test_search_unit_valid_query(self):
        """Test /search/ endpoint with valid query (Unit Test)"""
        self.mock_search_service.search.return_value = {
            "took": 7,
            "timed_out": False,
            "_shards": {"total": 1, "successful": 1, "skipped": 0, "failed": 0},
            "hits": {"total": {"value": 0, "relation": "eq"}, "max_score": None, "hits": []},
        }
        # Mock the SearchService response to return the above

        response = self.client.get("/api/search/", params={"field": "title", "value": "test"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("successful", response.json()["_shards"])
        self.assertIn("hits", response.json())

    def test_search_unit_missing_query(self):
        """Test /search/ endpoint with missing parameters (Unit Test)"""
        response = self.client.get("/api/search/")
        self.assertEqual(response.status_code, 422)  # Validation error

    def test_search_integration(self):
        """Test /search/ endpoint (Integration Test)"""
        response = self.client.get("/api/search/", params={"field": "title", "value": "test"})
        self.assertEqual(response.status_code, 200)
        # Add assertions based on real Elasticsearch data if applicable


class TestTagEndpoint(unittest.TestCase):
    """Unit and Integration Tests for the Tag Endpoint"""

    def setUp(self):
        self.client = TestClient(app)  # Use `TestClient(app)` correctly here
        self.mock_tag_service = MagicMock(TagService)
        app.dependency_overrides[TagService] = lambda: self.mock_tag_service

    def test_tag_unit_valid_request(self):
        """Test /tag/ endpoint with valid request (Unit Test)"""
        search_service = SearchService(settings.ELASTIC_HOST, index=settings.TEXTS_INDEX)

        search_service.initialize_data()
        self.mock_tag_service.tag_content.return_value = {"doc_id": "12345", "tag": "important"}

        request_data = {"doc_id": "LyrH3pMBUWdzd634tRpC", "tag": "1"}
        response = self.client.post("/api/tag/", json=request_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Document LyrH3pMBUWdzd634tRpC tagged with 1'})


    def test_tag_integration(self):
        search_service = SearchService(settings.ELASTIC_HOST, index=settings.TEXTS_INDEX)
        search_service.initialize_data()
        """Test /tag/ endpoint (Integration Test)"""
        request_data = {"doc_id": "LyrH3pMBUWdzd634tRpC", "tag": "2"}
        response = self.client.post("/api/tag/", json=request_data)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
