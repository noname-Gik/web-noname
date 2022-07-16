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
    // очистка выбранных ролей при смене организации
    organization_select.on('select2:select', function (e) {
        role_select.empty();
        role_select.append(`<option></option>`);
    });

    // выборка организация-роли, отключение disabled в css
    organization_select.change(function () {
        let selectedItem = $(this).val();
        if (selectedItem) {
            $.get(`api/get_roles/${selectedItem}`, function (data) {
                data.result.forEach((item) => {
                    role_select.append(`<option value="${item.id}">${item.name}</option>`)
                })
            });
        }
    });
    // вывод списка ролей
    $.get(`api/get_roles_all`, function (data) {
        data.result.forEach((i) => {
            role_select_m.append(`<option value="${i.id}">${i.name}</option>`)
        })
    });
});
// Отправка сообщения с файлом в database
$(".form-message").submit(function (e) {
    e.preventDefault();
    let formData = new FormData(this);
    $.ajax({
        processData: false,
        contentType: false,
        method: 'POST',
        data: formData, // получаем данные формы
        url: this.action,
        success: function (response) {
            alert('Поздравляю, ваше сообщение отправлено в database');
        },
        error: function (response) {
            alert('Внимание!! Что-то пошло не так');
        }
    });
});