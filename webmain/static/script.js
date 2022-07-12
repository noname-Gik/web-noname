// select2-multiple - все disabled отключены для отображения, смотреть css-файл
$(document).ready(function () {
    $('.organization-role-multiple').select2();
    let organization_select = $('#idsorganization');
    let role_select = $('#idsrole');
    let organization_select_m = $('#idmorganization');
    let role_select_m = $('#idmrole');
    // вывод списка организаций
    $.get(`api/get_organization`, function (data) {
        data.result.forEach((i) => {
            organization_select.append(`<option value="${i.id}">${i.name}</option>`)
            organization_select_m.append(`<option value="${i.id}">${i.name}</option>`)
        })
    });
    // вывод списка ролей
    $.get(`api/get_roles`, function (data) {
        data.result.forEach((i) => {
            role_select.append(`<option value="${i.id}">${i.name}</option>`)
            role_select_m.append(`<option value="${i.id}">${i.name}</option>`)
        })
    });
});
