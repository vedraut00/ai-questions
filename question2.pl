:- use_module(library(csv)).
:- use_module(library(http/http_server)).
:- use_module(library(http/http_json)).
:- use_module(library(http/http_cors)).

% Dynamic predicates for storing student data
:- dynamic student/4.

% Load CSV data
load_data :-
    csv_read_file("data.csv", Rows, [functor(student), arity(4)]),
    maplist(assert, Rows).

% Rule for scholarship eligibility
eligible_for_scholarship(StudentId) :-
    student(StudentId, _, Attendance, CGPA),
    Attendance >= 75,
    CGPA >= 9.0.

% Rule for exam permission
permitted_for_exam(StudentId) :-
    student(StudentId, _, Attendance, _),
    Attendance >= 75.

% HTTP handlers
:- http_handler('/api/check-eligibility', handle_eligibility, []).

handle_eligibility(Request) :-
    http_read_json_dict(Request, Data),
    StudentId = Data.student_id,
    (eligible_for_scholarship(StudentId) ->
        Scholarship = true
    ;   
        Scholarship = false
    ),
    (permitted_for_exam(StudentId) ->
        ExamPermission = true
    ;   
        ExamPermission = false
    ),
    reply_json_dict(_{
        student_id: StudentId,
        scholarship_eligible: Scholarship,
        exam_permitted: ExamPermission
    }).

% Start server
start_server :-
    http_server(http_dispatch, [port(8000)]).

% Initialize
:- load_data.
:- start_server.
