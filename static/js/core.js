$(document).ready(function() {
    $("#form").on('submit', function(e) {
        e.preventDefault();
        var search = $("#search").val();
        $.ajax({
            url: "/query",
            type: "POST",
            dataType: "json",
            data: {
                "search": search
            },
            success: function(e) {
                var data = JSON.parse(JSON.stringify(e));
                switch (data.error) {
                    case 1:
                    case 2:
                        swal("Opps", data.message, "error");
                        break;
                    case 0:
                        swal(data.message, data.title);
                        break;
                }
            },
            error: function(e) {
                swal("Opps", "Somethings went wrong", "error");
            }
        });
    });
});