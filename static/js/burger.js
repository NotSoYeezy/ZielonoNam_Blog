document.addEventListener('DOMContentLoaded', () => {

    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
  
    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {
  
      // Add a click event on each of them
      $navbarBurgers.forEach( el => {
        el.addEventListener('click', () => {
  
          // Get the target from the "data-target" attribute
          const target = el.dataset.target;
          const $target = document.getElementById(target);
          const main_header = document.getElementById('main_header')

          // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
          el.classList.toggle('is-active');
          if(el.classList.contains('is-active')){
              main_header.setAttribute('style', 'margin-top: 250px;')
          }
          else{
            main_header.setAttribute('style', 'margin-top: none;')
          }
          
          $target.classList.toggle('is-active');
  
        });
      });
    }
  
  });