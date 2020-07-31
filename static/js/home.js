
$(".mainNavbar").removeClass("bg-dark")
$(window).scroll(function(){
    var scrollNo = $(window).scrollTop();
    if (scrollNo > 100) {
        $("#searchForm").css('visibility','visible');
        $(".mainNavbar").addClass("bg-dark")
    }
    else if (scrollNo <10) {
        $(".mainNavbar").removeClass("bg-dark")
        $("#searchForm").css('visibility','hidden');

    } else {
        
    }
    // console.log(scrollNo)

});

// $(".card").hover(function(){
//     $(this).css({
        
//     })
// });
// $("#carouselExampleCaptions").hide("slow");