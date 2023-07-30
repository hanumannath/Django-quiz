# Flow
The flow which I assumed is like this:-
1. user will login and then he will see list of exams which he want to practice. (these APIs will be called from frontend)
2. after selecting the exam he will see a list of sections which he wants to practice.
3. when he will select a section he will see a list of topics he wants to practice.
4. after selecting a topic he will see a list of quizzes available for that particular topic.
5. then he will select the quiz which he wants to practice and there he will see all the questions related to that quiz.
6. whenever a user will answer a question we will save it in the Answer table with user_id,question_id, and option_id
so that if there is a network problem or anything next time he can start from that questions dont need to reanswer all previous questions
and while fetching we can fetch those questions from answer table(this same functionality can be used to show question 
the second time when he will navigate to the quiz after solving)
Didn't have time to implement this answer API just the model I have created(wasted maximum time in that signal thing, that was giving some error)
## API Documentation

The Quiz app has the following APIs:

#user APIs
1. /users/users/login  --for login user
2. /users/users/logout   --for logout user
(here forgot to create register API)

#exam APIs
1. /exams/  ---this API will send a list of all exams
2. /exam/{exam_id}/sections  --this will send all the sections for a particular exam
3. /section/{section_id}/topics   -- this will send all the topics for a particular section
4. /topic/{toipc_id}/quizzes   --this will send all the quizzes for that particular topic
5. /quiz/{quiz_id}/questions   -- this will send all the questions for a particular quiz with options
