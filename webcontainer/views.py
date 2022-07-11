from django.http import JsonResponse

from webcontainer.models import OrganizationTableMode, RoleTableMode, UserTableMode


def get_organization(request):
    datalist = OrganizationTableMode.objects.filter()
    result = []
    for i in datalist:
        result.append({
            'id': i.id,
            'organizations': i.name,
        })
    return JsonResponse({'result': result})


def get_roles(request):
    datalist = RoleTableMode.objects.filter()
    result = []
    for i in datalist:
        result.append({
            'id': i.id,
            'roles': i.name,
        })
    return JsonResponse({'result': result})


def get_users(request):
    datalist = UserTableMode.objects.filter()
    result = []
    for i in datalist:
        result.append({
            'id': i.id,
            'users': f'{i.firstname} {i.mainname} {i.lastname}',
        })
    return JsonResponse({'result': result})
