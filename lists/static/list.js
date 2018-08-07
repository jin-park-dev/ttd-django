window.Superlists = {};
window.Superlists.initialize = function () {
    $('input[name="text"]').on('keypress', function () {
        $('.has-error').hide();
    });
};

/*
 There are lots of other, much cleverer ways of dealing with namespaces in JavaScript, but they are all more complicated, and I’m not enough of an expert to be able to steer you around them. If you do want to learn more, search for require.js, which seemed to be the done thing, or at least it was in the last JavaScript femtosecond.
 */