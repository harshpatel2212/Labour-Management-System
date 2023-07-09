from django.template import loader
from django.http import HttpResponse
from django.db import connection
from labour_management_system.models import District, Person, Bank_Details, Supervisor


def home(request):
    template = loader.get_template('home.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def district(request):
    template = loader.get_template('district.html')
    flag = False
    if request.method == 'POST':
        dist_id = request.POST['dist_id'],
        dist_name = request.POST['dist_name'],
        dist_code = request.POST['dist_code']

        values = "".join(dist_id) + "," + "".join(dist_code) + \
            ",\'" + "".join(dist_name) + "\'"
        status = True

        if insert('district', values):
            msg = 'Insertion Succesfull!!'
            flag = True
        else:
            msg = 'Insertion Failed!!'
    else:
        status = False
        msg = ""

    context = {
        'status': status,
        'success': flag,
        'msg': msg,
    }
    return HttpResponse(template.render(context, request))


def editDistrict(request):
    template = loader.get_template('editDistrict.html')
    if request.method == 'POST':
        dist_id = request.POST['dist_id'],
        dist_name = request.POST['dist_name'],
        dist_code = request.POST['dist_code']
        status = True
        flag = False
        if delete('district', 'dist_id', "".join(dist_id)):
            values = "".join(dist_id) + "," + "".join(dist_code) + \
                ",\'" + "".join(dist_name) + "\'"
            if insert('district', values):
                msg = 'Edit Successful'
                flag = True
            else:
                msg = 'Edit Failed'
        else:
            msg = 'Edit Failed'

    else:
        status = False
        msg = ""
        flag = False

    context = {
        'status': status,
        'success': flag,
        'msg': msg,
    }
    return HttpResponse(template.render(context, request))


def deleteDistrict(request):
    template = loader.get_template('deleteDistrict.html')
    if request.method == 'POST':
        dist_id = request.POST['dist_id'],
        status = True
        flag = False
        msg = "Delete Failed"
        if delete('district', 'dist_id', "".join(dist_id)):
            msg = "Delete Succesfull"
            flag = True

    else:
        status = False
        flag = False
        msg = ""

    context = {
        'status': status,
        'success': flag,
        'msg': msg,
    }
    return HttpResponse(template.render(context, request))


def insert(table_name, values):
    try:
        insert_query = f'INSERT INTO labourer_db.{table_name} VALUES({values});'
        cursor = connection.cursor()
        cursor.execute(insert_query)
        connection.commit()
        return True
    except Exception as err:
        print(err)
        return False


def edit(table_name, values):
    try:
        insert_query = f'UPDATE INTO labourer_db.{table_name} VALUES({values});'
        cursor = connection.cursor()
        cursor.execute(insert_query)
        connection.commit()
        return True
    except Exception as err:
        print(err)
        return False


def delete(table_name, pk_attr, id):
    try:
        delete_query = f'DELETE FROM labourer_db.{table_name} WHERE {pk_attr} = {id};'
        cursor = connection.cursor()
        cursor.execute(delete_query)
        connection.commit()
        return True
    except Exception as err:
        print(err)
        return False


def showDistrict(request):
    template = loader.get_template('showDistrict.html')
    try:
        showall = District.objects.all()
    except:
        showall = None

    context = {
        'data': showall
    }
    return HttpResponse(template.render(context, request))


def person(request):
    template = loader.get_template('person.html')
    flag = False
    if request.method == 'POST':
        person_id = request.POST['person_id'],
        first_name = request.POST['first_name'],
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        dist_id = request.POST['dist_id']
        birth_date = request.POST['birth_date']
        bank_name = request.POST['bank_name']
        bank_head_branch = request.POST['bank_head_branch']
        account_number = request.POST['account_number']
        Account_holder_name = request.POST['Account_holder_name']

        v_p = "".join(person_id) + ",\'" + "".join(first_name) + \
            "\',\'" + "".join(middle_name) + "\',\'" + "".join(last_name) + \
            "\'," + "".join(dist_id) + ",\'" + "".join(birth_date) + "\'"

        b_p = "".join(person_id) + ",\'" + "".join(bank_name) + \
            "\',\'" + "".join(bank_head_branch) + "\',\'" + "".join(account_number) + \
            "\',\'" + "".join(Account_holder_name) + "\'"

        status = True

        if insert('person', v_p) and insert('\"Bank_details\"', b_p):
            msg = 'Insertion Succesfull!!'
            flag = True
        else:
            msg = 'Insertion Failed!!'
    else:
        status = False
        msg = ""

    context = {
        'status': status,
        'success': flag,
        'msg': msg,
    }
    return HttpResponse(template.render(context, request))


def editPerson(request):
    template = loader.get_template('editPerson.html')
    flag = False
    if request.method == 'POST':
        person_id = request.POST['person_id'],
        first_name = request.POST['first_name'],
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        dist_id = request.POST['dist_id']
        birth_date = request.POST['birth_date']
        bank_name = request.POST['bank_name']
        bank_head_branch = request.POST['bank_head_branch']
        account_number = request.POST['account_number']
        Account_holder_name = request.POST['Account_holder_name']

        status = True
        if delete('\"Bank_details\"', 'person_id', "".join(person_id)) and delete('person', 'person_id', "".join(person_id)):
            v_p = "".join(person_id) + ",\'" + "".join(first_name) + \
                "\',\'" + "".join(middle_name) + "\',\'" + "".join(last_name) + \
                "\'," + "".join(dist_id) + ",\'" + "".join(birth_date) + "\'"

            b_p = "".join(person_id) + ",\'" + "".join(bank_name) + \
                "\',\'" + "".join(bank_head_branch) + "\',\'" + "".join(account_number) + \
                "\',\'" + "".join(Account_holder_name) + "\'"

            if insert('person', v_p) and insert('\"Bank_details\"', b_p):
                msg = 'Edit Successful!!'
                flag = True
            else:
                msg = 'Edit Failed!!'
        else:
            msg = 'Edit Failed'

    else:
        status = False
        msg = ""

    context = {
        'status': status,
        'success': flag,
        'msg': msg,
    }
    return HttpResponse(template.render(context, request))


def deletePerson(request):
    template = loader.get_template('deletePerson.html')
    if request.method == 'POST':
        person_id = request.POST['person_id'],
        status = True
        flag = False
        msg = "Delete Failed"
        if delete('\"Bank_details\"', 'person_id', "".join(person_id)) and delete('person', 'person_id', "".join(person_id)):
            msg = "Delete Succesfull"
            flag = True

    else:
        status = False
        flag = False
        msg = ""

    context = {
        'status': status,
        'success': flag,
        'msg': msg,
    }
    return HttpResponse(template.render(context, request))


def showPerson(request):
    template = loader.get_template('showPerson.html')
    try:
        raw_query = "select * from labourer_db.person NATURAL join labourer_db.\"Bank_details\";"
        cursor = connection.cursor()
        cursor.execute(raw_query)
        headings = [desc[0] for desc in cursor.description]
        alldata = cursor.fetchall()
        status = True
    except:
        status = False
        headings = None
        alldata = None

    context = {
        'status': status,
        'headings': headings,
        'data': alldata
    }
    return HttpResponse(template.render(context, request))


def supervisor(request):
    template = loader.get_template('supervisor.html')
    flag = False
    if request.method == 'POST':
        sup_id = request.POST['sup_id'],
        person_id = request.POST['person_id'],
        salary = request.POST['salary']

        values = "".join(sup_id) + "," + "".join(person_id) + \
            "," + "".join(salary)
        status = True

        if insert('supervisor', values):
            msg = 'Insertion Succesfull!!'
            flag = True
        else:
            msg = 'Insertion Failed!!'
    else:
        status = False
        msg = ""

    context = {
        'status': status,
        'success': flag,
        'msg': msg,
    }
    return HttpResponse(template.render(context, request))


def editSupervisor(request):
    template = loader.get_template('editSupervisor.html')
    flag = False
    if request.method == 'POST':
        sup_id = request.POST['sup_id'],
        person_id = request.POST['person_id'],
        salary = request.POST['salary']

        status = True
        if delete('supervisor', 'sup_id', "".join(sup_id)):
            values = "".join(sup_id) + "," + "".join(person_id) + \
                "," + "".join(salary)

            if insert('supervisor', values):
                msg = 'Edit Succesfull!!'
                flag = True
            else:
                msg = 'Edit Failed!!'
        else:
            msg = 'Edit Failed'

    else:
        status = False
        msg = ""

    context = {
        'status': status,
        'success': flag,
        'msg': msg,
    }
    return HttpResponse(template.render(context, request))


def deleteSupervisor(request):
    template = loader.get_template('deleteSupervisor.html')
    if request.method == 'POST':
        sup_id = request.POST['sup_id'],
        status = True
        flag = False
        msg = "Delete Failed"
        if delete('supervisor', 'sup_id', "".join(sup_id)):
            msg = "Delete Succesfull"
            flag = True

    else:
        status = False
        flag = False
        msg = ""

    context = {
        'status': status,
        'success': flag,
        'msg': msg,
    }
    return HttpResponse(template.render(context, request))


def showSupervisor(request):
    template = loader.get_template('showSupervisor.html')
    try:
        raw_query = "select s.sup_id, first_name, middle_name, last_name, dist_id, birth_date, s.salary from labourer_db.supervisor as s, labourer_db.person as p where s.person_id = p.person_id;"
        cursor = connection.cursor()
        cursor.execute(raw_query)
        headings = [desc[0] for desc in cursor.description]
        alldata = cursor.fetchall()
        status = True
    except:
        status = False
        headings = None
        alldata = None

    context = {
        'status': status,
        'headings': headings,
        'data': alldata
    }
    return HttpResponse(template.render(context, request))


def perform(request):
    template = loader.get_template('perform.html')
    status = False
    success = False
    msg = ""
    headings = None
    alldata = None
    if request.method == 'POST':
        status = True
        query = request.POST['query']
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            headings = [desc[0] for desc in cursor.description]
            alldata = cursor.fetchall()
            success = True
            msg = 'Query Successful'
        except Exception as err:
            msg = err

    context = {
        'status': status,
        'success': success,
        'headings': headings,
        'data': alldata,
        'msg': msg,
    }
    return HttpResponse(template.render(context, request))
