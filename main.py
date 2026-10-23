from pyscript import document

def candidate_checker(e):
    club_members = ["inigo combong", "ayeezha moises", "andrea chua", "danna cu", "melcy benasas"]

    f_name = document.getElementById("first name").value
    l_name = document.getElementById("last name").value
    candidate = f_name + ' ' + l_name
    member_checker = candidate.lower() in club_members

    message = (f'Sorry, {candidate}, your name is not on the list.' ,
               f'Congratulations, {candidate}, you are part of the rainbow catering club.')

    document.getElementById('result').innerHTML = message[member_checker]