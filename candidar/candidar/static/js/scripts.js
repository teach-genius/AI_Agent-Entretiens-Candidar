document.addEventListener('contextmenu', function (e) {
    e.preventDefault();
});

// Désactiver le copier-coller
document.addEventListener('copy', function (e) {
    e.preventDefault();
});

document.addEventListener('cut', function (e) {
    e.preventDefault();
});
