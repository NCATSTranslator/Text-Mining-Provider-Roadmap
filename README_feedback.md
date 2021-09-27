# Feedback Service API
The Feedback Service is a small API, served from https://feedback-p36smkc6hq-uc.a.run.app/.
Currently this API only exposes one endpoint, /evaluations
This accepts a POST request with an application/json body, and creates a record in the database indicating the evaluation of the assertion. 
The request object can contain the following properties:
* key: The API key used to authenticate the user making the request.
* assertion_id: The alphanumeric ID of the assertion being evaluated.
* overall_correct: A boolean indicating whether the overall assertion is correct (Optional, default false).
* subject_correct: A boolean indicating whether the subject in the assertion is correct (Optional, default null).
* object_correct: A boolean indicating whether the object in the assertion is correct (Optional, default null).
* predicate_correct: A boolean indicating whether the predicate in the assertion is correct (Optional, default null).

If only the key and assertion ID are provided the created record will only indicate that the assertion as a whole is incorrect, without specifying where in the triple the error exists. If necessary, the optional boolean properties can be provided to give more detailed feedback.
The service will return the follwing information based on the request:
* 200 (OK) with the plain text message "Evaluation saved" if the request succeeded.
* 400 (Bad Request) if the request body is not in JSON format or lacks the mandatory assertion_id property; the response text will clarify which error was found.
* 401 (Unauthorized) with the plain text message "Unidentified user" if the request body does not contain the mandatory key property, or if the key does not correspond to an authorized user.

Example usage:
```
curl --location --request POST 'https://feedback-p36smkc6hq-uc.a.run.app/evaluations' \
--header 'Content-Type: application/json' \
--data '{
    "key": "<api_key>",
    "assertion_id": "<assertion_id>",
    "overall_correct": false,
    "subject_correct": true,
    "object_correct": true,
    "predicate_correct": false
}'
```