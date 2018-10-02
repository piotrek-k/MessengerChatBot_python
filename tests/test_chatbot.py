import pytest

from messenger_chatbot import chatbot


@pytest.fixture
def client():
    # configuration before every test
    client = chatbot.app.test_client()

    yield client


def test_sending_correct_data_returns_200(client):
    rv = client.get('/webhook?hub.verify_token=some random token&hub.challenge=CHALLENGE_ACCEPTED&hub.mode=subscribe')

    assert rv.status_code == 200


def test_sending_bad_token_returns_403(client):
    rv = client.get('/webhook?hub.verify_token=some bad token&hub.challenge=CHALLENGE_ACCEPTED&hub.mode=subscribe')

    assert rv.status_code == 403


# Blow test would use real Facebook API to send response message to user
"""
def test_post_request_should_return_200(client):
    # Below dictionary structure is base on real API call from Facebook
    request_data = {
        'object': 'page',
        'entry': [{
            'id': '[number]',
            'time': 1538421274715,
            'messaging': [
                {
                    'sender': {
                        'id': '[number]'
                    },
                    'recipient': {
                        'id': '[number]'
                    },
                    'timestamp': 1538421274284,
                    'message': {
                        'mid': '[string]',
                        'seq': 855684,
                        'text': '[typed text]'
                    }
                }
            ]
        }]
    }

    rv = client.post('/webhook', data=json.dumps(request_data), follow_redirects=True)

    assert rv.status_code == 200
"""
