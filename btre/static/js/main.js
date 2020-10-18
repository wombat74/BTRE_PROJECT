const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// Jquery added to fadeout the error messages on register and login.html
// After adding this to (btre/static) we must run "python mange.py collectstatic" so that this code moves to the main static folder.
setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);
