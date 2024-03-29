$(".modal-galery").click(function (e) {
    e.preventDefault();
    let target = $(e.currentTarget);
    if (target.data('url') != '') {
        $("#GalleryModal1 .event-url").removeClass('d-none');
        $("#GalleryModal1 .event-img").addClass('d-none');
        $("#GalleryModal1 .event-url").attr('src', target.data('url'));
    } else {
        $("#GalleryModal1 .event-img").removeClass('d-none');
        $("#GalleryModal1 .event-url").addClass('d-none');
        $("#GalleryModal1 .event-img").attr('src', target.data('img'));
    }
    $("#GalleryModal1 .event-img").attr('src', target.data('img'));
    $("#GalleryModal1 .event-title").text(target.data('title'));
    $("#GalleryModal1 .event-description").text(target.data('description'));
    $("#GalleryModal1 .event-date").text(target.data('date'));
    $("#GalleryModal1 .event-category").text(target.data('category'));
    $("#GalleryModal1").modal('show');
});
$("#GalleryModal1 .close-btn").click(function (e) {
    $("#GalleryModal1").modal('hide');
});

const step = 6;
const year_form = $('#select_anno');
const cat_form = $('#select_category');

filterSelection({a: year_form.val(), c: cat_form.val()}, '', 1, step);

year_form.change(function () {
    console.log($(this).val());
    filterSelection({a: $(this).val(), c: cat_form.val()}, '', 1, step);
});
cat_form.change(function () {
    console.log($(this).val());
    filterSelection({c: $(this).val(), a: year_form.val()}, '', 1, step);
});


function filterSelection(c, search = '', page = 1, step = step) {
    let elements = 0;
    let x, i;
    x = document.getElementsByClassName("event-item");

    for (i = 0; i < x.length; i++) {
        let xi = $(x[i]);
        CardRemoveClass(x[i], "show-event");
        CardAddClass(x[i], "hide-event");

        if ((xi.hasClass(c.a) || (xi.data('date') && xi.data('date').split('-')[0] === c.a)) &&
            (xi.hasClass(c.c) || (xi.data('category') && xi.data('category') === c.c))) {
            elements++;
            if ((elements > ((page - 1) * step)) && (elements <= page * step)) {
                CardAddClass(x[i], "show-event");
            }
        }
    }
    if (!elements) {
        let n = $('#no-event')
        n.removeClass('hide-event');
        n.removeClass('show-event');
    }
    if (page === 1)
        drawPagination(c, search, elements, page, step);
}

function CardAddClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        if (arr1.indexOf(arr2[i]) == -1) {
            element.className += " " + arr2[i];
        }
    }
}

function CardRemoveClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        while (arr1.indexOf(arr2[i]) > -1) {
            arr1.splice(arr1.indexOf(arr2[i]), 1);
        }
    }
    element.className = arr1.join(" ");
}

function drawPagination(c, search, elements, page, step) {
    paginationholder = $('#paginationholder');
    paginationholder.html('');
    paginationholder.html('<ul id="pagination"></ul>');
    total = elements / step;

    if ((elements % step) > 0)
        total += 1;

    if (total > 0)
        $('#pagination').twbsPagination({

            totalPages: total,
            prev: '<i class="fa fa-arrow-left"></i>',
            next: '<i class="fa fa-arrow-right"></i>',
            pageClass: 'page-item',
            anchorClass: 'page-link',
            hideOnlyOnePage: true,
            first: null,
            last: null,
            initiateStartPageClick: false,
            onPageClick: function (event, num) {
                filterSelection(c, search, num, step);
            },
        })
}