from django.http import JsonResponse

from webcontainer.models import OrganizationTableMode, RoleTableMode, UserTableMode


def get_organization(request):
    organizations = OrganizationTableMode.objects.filter()
    result = []
    for i in organizations:
        result.append({
            'id': i.id,
            'name': i.name,
        })
    return JsonResponse({'result': result})


def get_roles_all(request):
    roles = RoleTableMode.objects.filter()
    result = []
    for i in roles:
        result.append({
            'id': i.id,
            'name': i.name,
        })
    return JsonResponse({'result': result})


def get_roles(request, ids):
    roles = RoleTableMode.objects.filter(connectiontablemode__organizations_id=ids).distinct()
    result = []
    for i in roles:
        result.append({
            'id': i.id,
            'name': i.name,
        })
    return JsonResponse({'result': result})


def get_users(request):
    users = UserTableMode.objects.filter()
    result = []
    for i in users:
        result.append({
            'id': i.id,
            'fio': f'{i.firstname} {i.mainname} {i.lastname}',
        })
    return JsonResponse({'result': result})
