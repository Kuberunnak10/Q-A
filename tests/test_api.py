import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Question Tests
def test_create_question_success():
    """Test creating a valid question"""
    response = client.post("/api/v1/questions/", json={"text": "What is FastAPI?"})
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "What is FastAPI?"
    assert "id" in data
    assert "created_at" in data

def test_create_question_empty_text():
    """Test that empty question text is rejected"""
    response = client.post("/api/v1/questions/", json={"text": ""})
    assert response.status_code == 422

def test_get_question_by_id():
    """Test getting a specific question"""
    # Create a question first
    create_response = client.post("/api/v1/questions/", json={"text": "Test question for get"})
    question_id = create_response.json()["id"]
    
    response = client.get(f"/api/v1/questions/{question_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == question_id
    assert data["text"] == "Test question for get"

# Answer Tests
def test_create_answer_success():
    """Test creating a valid answer"""
    # Create a question first
    question_response = client.post("/api/v1/questions/", json={"text": "What is Python?"})
    question_id = question_response.json()["id"]
    
    response = client.post(
        f"/api/v1/questions/{question_id}/answers/",
        json={"text": "Python is a programming language", "user_id": "user123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Python is a programming language"
    assert data["user_id"] == "user123"
    assert data["question_id"] == question_id
    assert "id" in data
    assert "created_at" in data

def test_create_answer_nonexistent_question():
    """Test creating answer for non-existent question"""
    response = client.post(
        "/api/v1/questions/99999/answers/",
        json={"text": "Some answer", "user_id": "user123"}
    )
    assert response.status_code == 404

def test_cascade_delete():
    """Test that deleting question also deletes its answers"""
    # Create question
    question_response = client.post("/api/v1/questions/", json={"text": "Question for cascade test"})
    question_id = question_response.json()["id"]
    
    # Create answer
    answer_response = client.post(
        f"/api/v1/questions/{question_id}/answers/",
        json={"text": "Answer for cascade test", "user_id": "user123"}
    )
    answer_id = answer_response.json()["id"]
    
    # Delete question
    delete_response = client.delete(f"/api/v1/questions/{question_id}")
    assert delete_response.status_code == 200
    
    # Verify answer is also deleted
    answer_check = client.get(f"/api/v1/answers/{answer_id}")
    assert answer_check.status_code == 404