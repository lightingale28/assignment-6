"""Write a Python function student_data () which will print the id of a student (student_id).
If the user passes an argument student_name or student_class the function will print the
student name and class."""
def l(sid, name, class1, i = False, n = False, c = False):
    if i:
        print(sid)
    if n:
        print(name)
    if c:
        print(class1)

l(22106023, "Yashawi", "CSE DS", i = True)
l(22106023, "Yashawi", "CSE DS", n = True)
l(22106023, "Yashawi", "CSE DS", c = True)