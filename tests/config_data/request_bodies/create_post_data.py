VALID_POST_DATA = {
    "userId": 1,
    "title": "My Test Post",
    "body": "This is the body of my test post"
}

POST_WITHOUT_TITLE = {
    "userId": 1,
    "body": "Missing title field"
}

POST_WITH_EXTRA_FIELDS = {
    "userId": 1,
    "title": "Extra fields",
    "body": "Testing",
    "extraField": "should be ignored"
}