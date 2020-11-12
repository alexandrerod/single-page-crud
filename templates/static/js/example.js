
//essa função vai carregar o form assim que clicar na tab de criar/editar
$(function () {
    //carrega o formulário
    var loadForm =function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      success: function (data) {
        $("#create-update").html(data.html_form);
      }
    });
  };


    //carrega a tabela assim que clicar na tab da lista
   $(".js-list").click(function () {
        $.ajax({
          url: '/list/',
          type: 'get',
          dataType: 'json',
          success: function (data) {
            $("#list").html(data.html_list);
          }
        });
    });



//salva o formulário.
      var saveForm =function () {
      var form = $(this)
      $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
            $.ajax({
              url: '/create/',
              type: 'get',
              dataType: 'json',
              success: function (data) {
                $("#create-update").html(data.html_form);
              }
            });
        }
        else {
          $("#create-update").html(data.html_form);
        }
      }
    });
    return false;
  };

//create equipamentes
 $(".js-create-update").click(loadForm);
 $("#create-update").on("submit", ".js-create-form", saveForm );

//atualiza

});


